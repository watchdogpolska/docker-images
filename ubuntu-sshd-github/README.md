# ubuntu-sshd-github

[![Docker Repository on Quay](https://quay.io/repository/watchdogpolska/ubuntu-sshd-github/status "Docker Repository on Quay")](https://quay.io/repository/watchdogpolska/ubuntu-sshd-github)

An image of a Docker delivering a sshd daemon. Authentication takes place with the keys of selected GitHub users.

## Environment 

| Name                 | Description
| -------------------- | -----------
| ```GITHUB_USERS```   | Comma sepeated list of GitHub username