# terraform-tfnotify

[![Docker Repository on Quay](https://quay.io/repository/watchdogpolska/terraform-tfnotify/status "Docker Repository on Quay")](https://quay.io/repository/watchdogpolska/terraform-tfnotify)

An image of a docker containing Terraform for a CircleCI flow. It includes:

- [tfnotify](https://github.com/mercari/tfnotify)
- [terraform-provider-rootbox](https://github.com/hyperonecom/terraform-provider-hyperone/)
- [terraform-provider-hyperone](https://github.com/hyperonecom/terraform-provider-hyperone/)

It is intended to simplify CI / CD of repository [watchdogpolska/infra-dns](https://github.com/watchdogpolska/infra-terraform).