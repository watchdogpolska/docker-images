import argparse

import json
import os

from io import StringIO
import requests
from api import EmaillabsAPI

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--appkey",
        default=os.environ.get("EMAILLABS_APPKEY"),
        help="App key (default from environment EMAILLABS_APPKEY)",
    )
    parser.add_argument(
        "--secret",
        default=os.environ.get("EMAILLABS_SECRET"),
        help="App key (default from environment EMAILLABS_SECRET)",
    )
    parser.add_argument(
        "--data-file", required=True, type=str, help="Path to data file"
    )

    args = parser.parse_args()
    if not args.appkey or not args.secret:
        raise Exception("Appkey and Secret are required!")

    client = EmaillabsAPI(args.appkey, args.secret)

    data = []
    for email in client.get_emails_iter():
        data.append(email)
    with open(args.data_file, "w") as fp:
        json.dump(data, fp, indent=2)
