# A simple FTP server without the bells and whistles

The FTP server is responsible for authentication and allowing users to manage files.

It can work with minimal privileges which allows limit system exposure. At the same time, the server is not responsible for handling file permissions - to isolate file start a new server instance.

The service has been designed to be particularly easy to use in the Docker environment, which allows taking over many functions traditionally built into the FTP server (user isolation, chroot etc.).

## Usage

Build image:

```bash
docker build . -t nodejs-ftp-srv
```

Add user account:

```bash
docker run -v $(pwd)/user.json:/etc/ftp-srv/user.json  nodejs-ftp-srv node add_user.js login password 
```

Start service:

```bash
docker run \
	-v $(pwd)/user.json:/etc/ftp-srv/user.json -v $(pwd)/data:/data \
	-p 21:21 
	nodejs-ftp-srv
```

Start service with passive-mode enabled:

```bash
docker run \
	-v $(pwd)/user.json:/etc/ftp-srv/user.json -v $(pwd)/data:/data \
	-e FTP_PASV_URL="127.0.0.1" -e FTP_PASV_MAX=1200 \
	-p 21:21 -p 1024-1200:1024-1200 \
	nodejs-ftp-srv
```

Test connection:

```bash
curl ftp://login:password/
```