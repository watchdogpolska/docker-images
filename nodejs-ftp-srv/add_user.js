const fs = require('fs');
const util = require('util');
const readFile = util.promisify(fs.readFile);
const writeFile = util.promisify(fs.writeFile);
const bcrypt = require('bcrypt');

const main = async () => {
    if (!process.env.USER_DB) {
        console.log("Missing environment variable: USER_DB");
        process.exit(2);
    }
    let db;
    try {
        db = JSON.parse(await readFile(process.env.USER_DB));
    } catch (err) {
        console.log(err);
        db = [];
    }
    if (process.argv.length < 3) {
        console.log(`Usage: ${process.argv[0]} [username] [password]`);
        process.exit(2);
    }

    db.push({
        username: process.argv[2],
        hash: await bcrypt.hash(process.argv[3], 10)
    });
    await writeFile(process.env.USER_DB, JSON.stringify(db), {encoding: 'utf-8'});
    console.log(`New user '${process.argv[2]}' added. Database updated.`)
};

main().catch(console.error);