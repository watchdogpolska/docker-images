'use strict';
const http = require('http');
const httpProxy = require('http-proxy');
const url = require('url');

const API_URL = process.env.MIXPANEL_API_URL || 'https://api.mixpanel.com';
const PORT = process.env.PORT || 3000;
const TRUNCATE_URL = process.env.TRUNCATE_URL || '^/mpanel';
const parsed_url = url.parse(API_URL);

if (process.env.SENTRY_DSN) {
    require('@sentry/node').init({ dsn: process.env.SENTRY_DSN });
}

const enrichOriginIp = (req) => {
    const parsed_incoming_url = url.parse(req.url);
    const searchParams = new URLSearchParams(parsed_incoming_url.query);
    const data_b64 = searchParams.get('data');
    const client_ip = req.headers['x-forwarded-for'];
    if (data_b64 && client_ip) {
        const data = JSON.parse(Buffer.from(data_b64, 'base64').toString('utf-8'));
        data.$ip = client_ip;
        if (data.properties) {
            data.properties.ip = client_ip;
        }
        const new_data_b64 = Buffer.from(JSON.stringify(data)).toString('base64');
        searchParams.set('data', new_data_b64);
        parsed_incoming_url.query = searchParams.toString();
        req.url = parsed_incoming_url.format();
    }
};

const truncateOriginIp = (req) => {
    if (TRUNCATE_URL) {
        req.url = req.url.replace(new RegExp(TRUNCATE_URL, 'gm'), '');
    }
};

const disableKeepAlive = (req) => {
    req.headers['connection'] = 'close'
};

const proxy = httpProxy.createProxyServer({
    changeOrigin: true
});

const server = http.createServer(function(req, res) {
    req.headers.host = parsed_url.hostname;
    enrichOriginIp(req);
    truncateOriginIp(req);
    disableKeepAlive(req);

    proxy.web(req, res, {
        target: API_URL,
    });

    proxy.on('error', (e) => {
        const err = new Error('An exception coming from a proxy');
        err.e = e;
        throw err;
    });
});

server.on('error', (e) => {
    const err = new Error('An exception coming from a HTTP server');
    err.e = e;
    throw err;
});

server.listen(PORT, () => {
    console.log(`listening on port ${PORT}`);
});
