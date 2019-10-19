import os
import dataset

from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.resource import ResourceManagementClient
from msrestazure.azure_active_directory import ServicePrincipalCredentials
# $ az ad sp create-for-rbac --name "MY-PRINCIPAL-NAME2" --password "XXX" --verbose
# $ az role assignment create --assignee {app_id} --role Reader

tenant_id = os.environ.get('AZURE_TENANT_ID', '7dbd59e5-e4d9-499b-b5cb-005289cc158a')
app_id = os.environ.get('AZURE_APP_ID', 'bfeb6f69-5a18-4d0c-a669-2e7eb3798fdd')
password = os.environ['AZURE_APP_PASSWORD']

subscription_id = os.environ.get('AZURE_SUBSCRIPTION_ID', 'efeb9457-bf38-460f-a1e5-bb5ecc817987')

credentials = ServicePrincipalCredentials(
    client_id=app_id,
    secret=password,
    tenant=tenant_id
)

storage_client = StorageManagementClient(
    credentials,
    subscription_id
)

resource_client = ResourceManagementClient(
    credentials,
    subscription_id
)

db = dataset.connect(os.environ.get('DATABASE_URL', 'sqlite:///:memory:'))
