const FtpSrv = require('ftp-srv');
const fs = require('fs');
const util = require('util');
const readFile = util.promisify(fs.readFile);
const bcrypt = require('bcrypt');
const packageJson = require('./package.json')
const options = Object.assign(...Object.entries({
    url: process.env.FTP_URL,
    pasv_url: process.env.FTP_PASV_URL,
    pasv_min: process.env.FTP_PASV_MIN,
    pasv_max: process.env.FTP_PASV_MAX,
    greeting: process.env.GREETING || `${packageJson.name} ${packageJson.version}`,
    root: process.env.FTP_ROOT
})
    .filter(([key, value]) => !!value)
    .map(([key, value]) => ({[key]: value})));

console.log(options);

const ftpServer = new FtpSrv(options);

const getUserDb = async () => {
    if (!process.env.USER_DB) throw new Error("Missing enivronment variable: USER_DB");
    const content = await readFile(process.env.USER_DB);
    return JSON.parse(content);
};

const main = async () => {
    const user_db = await getUserDb();

    ftpServer.on('login', (({connection, username, password}, resolve, reject) => {
        const user = user_db.find(u => u.username === username);
        if (!user) return reject(new Error('Invalid username'));
        bcrypt.compare(password, user.hash, (err, res) => {
            if (err) return reject(err);
            if (!res) return reject(new Error('Invalid username or password'));
            return resolve({root: user.root || process.env.FTP_ROOT})
        });
    }));
    ftpServer.on('connection', console.log);
    const w = await ftpServer.listen();
    console.log(w);
};
main().then(console.log).catch(console.error);