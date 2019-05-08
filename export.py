from connect import Connection
from pprint import pprint

connect = Connection.getInstance()

PROJECT = 'xyz-sandbox'
INSTANCE = 'staging-pg'
BUCKET_NAME = "singapore-db-exports"

class ExportInstance:
  def __init__(self, project, instance):
    self.service = connect.get_sql_object()
    self.project = project
    self.instance = instance

  def list_dbs(self):
    request = self.service.databases().list(project = self.project, instance = self.instance)
    return request.execute()

  def start_export_service(self, db_name, bucket_name):
    instances_export_request_body = {
      "exportContext": {
        "kind": "sql#exportContext",
        "fileType": "SQL",
        "uri": "gs://%s/fileName" % bucket_name,
        "databases": [db_name],
        "sqlExportOptions": {
          "schemaOnly": False,
        }
      }
    }
    request = self.service.instances().export(project = self.project, instance = self.instance, body=instances_export_request_body)
    return request.execute()

ei = ExportInstance(PROJECT, INSTANCE)

# ['hydra', 'postgres', 'admin', 'block_fetcher_service', 'coin', 'crypto-swap', 'txn-constructor', 'review', 'txn-recorder', 'user', 'user_profile', 'wallet', 'pricerecorder', 'wallet-snapshot', 'fiat-purchase', 'merchant', 'payment', 'keymanager']
dbs = ei.list_dbs()

for db in dbs["items"]:
  pprint(ei.start_export_service(db["name"], BUCKET_NAME))
