'use strict';
const url = require('url');
const Koa = require('koa');
const superagent = require('superagent');
const Sentry = require('@sentry/node');

const API_URL = process.env.MIXPANEL_API_URL || 'https://api.mixpanel.com';
const PORT = process.env.PORT || 3000;
const TRUNCATE_URL = process.env.TRUNCATE_URL || '^/mpanel';
const parsed_url = url.parse(API_URL);

const agent = superagent.agent()
    .use(require('superagent-logger')({ outgoing: true }))
    .retry(3);

const app = new Koa();

app.use(require('koa-logger')());

app.use(async ctx => {
    const client_ip = ctx.request.headers['x-forwarded-for'];
    const data_b64 = ctx.query.data;
    if (data_b64 && client_ip) {
        const data = JSON.parse(Buffer.from(data_b64, 'base64').toString('utf-8'));
        data.$ip = client_ip;
        if (data.properties) {
            data.properties.ip = client_ip;
        }
        ctx.query.data = Buffer.from(JSON.stringify(data)).toString('base64');
    }
    const path = ctx.path.replace(new RegExp(TRUNCATE_URL, 'gm'), '');
    const res = await agent[ctx.method.toLowerCase()](`${API_URL}/${path}`)
        .query(ctx.query)
        .set(ctx.request.headers)
        .set({Host: parsed_url.hostname});
    ctx.set(res.headers);
    ctx.body = res.text;
});

app.use(async (ctx, next) => {
    try {
        return await next();
    } catch (err) {
        ctx.status = err.status || 500;
        ctx.body = err.message;
        ctx.app.emit('error', err, ctx);
    }
});

app.on('error', (err) => {
    console.log(err);
    Sentry.captureException(err);
});

app.listen(PORT, () => {
    console.log(`listening on port ${PORT}`);
});
