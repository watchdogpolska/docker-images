# -*- coding: utf-8 -*-
import csv
import json
import smtplib
import logging
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from urllib.parse import urljoin
import argparse

import os

from io import StringIO
import requests
from api import EmaillabsAPI

BASIC_INFO = """
Adres email z czarnej listy: {email}
Nazwa vps-a na którego czarnej liście znajduje się adres email: {account}
Źródło dodania wpisu (smtp lub panel): {source}
Powód wpadnięcia na czarną listę: {reason}
Opis dlaczego adres email wpadł na czarna listę: {comment}
Czas powstania wpisu: {created_at}
Ostatni czas kiedy wpis był modyfikowany: {updated_at}
Unikalny numer wpisu: {id}
"""

MAIL_INFO = """
Temat wiadomości: {subject}
Nadawca: {from}
"""


class Report(object):
    def __init__(self, client: EmaillabsAPI, data: dict):
        self.client = client
        self.data = data

    def get_new_blacklist(self, **data):
        ids = self.data.get("blacklist_ids", [])
        for item in self.client.get_blacklist_iter(**data):
            if item["id"] in ids:
                continue
            item["emails"] = self.client.get_latest_emails(item["email"])
            yield item


class Formatter(object):
    def __init__(self):
        pass

    def format_message(self, rows):
        return "\n\n".join(self.output_row(row) for row in rows)

    def output_row(self, data):
        msg = BASIC_INFO.format(**data).strip()
        for email in data["emails"]:
            msg += MAIL_INFO.format(**email).strip()
        return msg

    def format_file(self, rows, file):
        blacklist_column = [
            "email",
            "account",
            "source",
            "reason",
            "comment",
            "created_at",
            "updated_at",
            "id",
        ]
        email_column = ["subject", "from"]
        fcsv = csv.DictWriter(f=file, fieldnames=blacklist_column + email_column)
        fcsv.writeheader()
        for data in rows:
            if data["emails"]:
                for email in data["emails"]:
                    row = {x: data[x] for x in blacklist_column}
                    row.update({x: email[x] for x in email_column})
                    fcsv.writerow(row)
            else:
                row = {x: data[x] for x in blacklist_column}
                fcsv.writerow(row)


def args_env(name, label):
    help = "{} (default from environment {})".format(name, label)
    if name in os.environ:
        return dict(default=os.environ[name], help=help)
    return dict(required=True, help=help)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Notify about new e-mail in blacklist."
    )
    parser.add_argument("--appkey", **args_env("EMAILLABS_APPKEY", "EmailLabs App Key"))
    parser.add_argument(
        "--secret", **args_env("EMAILLABS_SECRET", "EmailLabs App Secret")
    )
    parser.add_argument(
        "--data-file", required=True, type=str, help="Path to data file"
    )
    parser.add_argument("--csv-file", required=False, type=str, help="Path to CSV file")
    parser.add_argument(
        "--sender",
        dest="from_addr",
        default="emaillabs@siecobywatelska.pl",
        help="Sender address of email",
    )
    parser.add_argument(
        "--recipient", dest="to_addrs", nargs="+", help="Recipients of notification"
    )
    parser.add_argument(
        "--account",
        default="1.siecobywatelska.smtp",
        help="EmailLabs SMTP account processed",
    )
    parser.add_argument("--debug", dest="debug", action="store_true")
    parser.add_argument("--smtp-host", **args_env("SMTP_HOST", "SMTP hostname"))
    parser.add_argument("--smtp-login", **args_env("SMTP_LOGIN", "SMTP login"))
    parser.add_argument("--smtp-password", **args_env("SMTP_PASSWORD", "SMTP password"))

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True

    data = {}
    if os.path.isfile(args.data_file):
        with open(args.data_file) as fp:
            data = json.load(fp)

    client = EmaillabsAPI(args.appkey, args.secret)
    report = Report(client, data)
    formatter = Formatter()
    blacklist_list = list(report.get_new_blacklist(account=args.account))

    new_data = set(data)
    new_data.update(x["id"] for x in blacklist_list)
    data = list(new_data)

    if args.to_addrs:
        smtp_client = smtplib.SMTP()
        smtp_client.connect(host=args.smtp_host)
        smtp_client.login(args.smtp_login, args.smtp_password)
        mail = MIMEMultipart()
        mail["From"] = args.from_addr
        mail["To"] = ",".join(args.to_addrs)
        mail["Date"] = formatdate(localtime=True)
        mail["Subject"] = "Podsumowanie zmian czarnej listy Emaillabs"

        mail.attach(MIMEText(formatter.format_message(blacklist_list)))

        f_csv = StringIO()
        formatter.format_file(blacklist_list, f_csv)
        part = MIMEApplication(f_csv.getvalue(), Name="rekord.csv")
        part["Content-Disposition"] = 'attachment; filename="rekord.csv"'
        mail.attach(part)

        smtp_client.send_message(mail)
        smtp_client.quit()
        print("Send email with report")

    if args.csv_file:
        print(formatter.format_message(blacklist_list))
        formatter.format_file(blacklist_list, open(args.csv_file, "w"))
        print("CSV file at: " + args.csv_file)

    with open(args.data_file, "w") as fp:
        json.dump({"blacklist_ids": new_data}, fp, indent=2)
