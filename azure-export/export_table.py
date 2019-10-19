from __future__ import print_function

from collections import namedtuple
from azure.storage.table import TableService
from settings import storage_client, resource_client, db
import sys

ResultSet = namedtuple('ResultSet', ['table', 'filter'])
Credentials = namedtuple('Credentials', ['account_name', 'account_key'])
Capacity = ResultSet('$MetricsCapacityBlob', "RowKey eq 'data'")
Transaction = ResultSet('$MetricsHourPrimaryTransactionsBlob', "RowKey eq 'user;All'")

quiet = any(x in sys.argv for x in ['-q', '--quiet'])

def get_credentials():
    for resource_group in resource_client.resource_groups.list():
        for account in storage_client.storage_accounts.list_by_resource_group(resource_group.name):
            account_name = account.name
            account_key = storage_client.storage_accounts.list_keys(resource_group.name, account.name).keys[0].value
            yield Credentials(account_name, account_key)


def get_rows(credentials, result_set):
    ts = TableService(account_name=credentials.account_name, account_key=credentials.account_key)
    for entity in ts.query_entities(result_set.table, filter=result_set.filter):
        row = entity
        row['account_name'] = credentials.account_name
        yield row


def save_result_set(tx, credentials, result_set, filename=None):
    table = tx[result_set.table.lstrip("$")]
    count = 0
    for row in get_rows(credentials, result_set):
        table.insert(row)
        count +=1
    if not quiet:
        print("Added {count} rows for {table}".format(
            count=count,
            table=result_set.table
        ))

def main():
    credentials_list = list(get_credentials())
    print("Found {} credentials".format(len(credentials_list)))
    for i, credentials in enumerate(credentials_list):
        if not quiet:
            print("Dump data of {} ({}/{})".format(credentials.account_name, i + 1, len(credentials_list)))
        with db as tx:
            save_result_set(tx, credentials, Capacity)
        with db as tx:
            save_result_set(tx, credentials, Transaction)


if __name__ == '__main__':
    main()
