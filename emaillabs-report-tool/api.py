import requests
from urllib.parse import urljoin


class EmaillabsAPI(object):
    def __init__(
        self, appkey, secret, path="https://api.emaillabs.net.pl/api/", session=None
    ):
        self.app_key = appkey
        self.secret = secret
        self.path = path
        self.session = session or requests.Session()
        self.session.auth = (appkey, secret)

    def get_blacklist(self, offset, limit, account, **data):
        data["offset"] = offset
        data["limit"] = limit
        data["filter"] = "account::{}".format(account)
        url = urljoin(self.path, "blacklists")
        response = self.session.get(url, params=data)
        response.raise_for_status()
        return response.json()

    def get_emails(self, offset, limit, **data):
        data["offset"] = offset
        data["limit"] = limit
        url = urljoin(self.path, "emails")
        response = self.session.get(url, params=data)
        response.raise_for_status()
        return response.json()

    def get_latest_emails(self, to):
        url = urljoin(self.path, "emails")
        response = self.session.get(url, params={"filter": "to::" + to})
        if response.status_code == 404:
            return []
        response.raise_for_status()
        return response.json()["data"]

    def get_blacklist_iter(self, **data):
        offset = 0
        limit = data.pop("limit", 500)
        while True:
            resp_data = self.get_blacklist(offset=offset, limit=limit, **data)
            yield from resp_data["data"]
            if len(resp_data["data"]) != limit:
                break
            offset += limit

    def get_emails_iter(self, **data):
        offset = 0
        limit = data.pop("limit", 500)
        while True:
            resp_data = self.get_emails(offset=offset, limit=limit, **data)
            yield from resp_data["data"]
            if len(resp_data["data"]) != limit:
                break
            offset += limit
