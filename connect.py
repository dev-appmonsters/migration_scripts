from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

class Connection:
  __instance = None

  @staticmethod
  def getInstance():
    if Connection.__instance == None: Connection()
    return Connection.__instance

  def __init__(self):
    if Connection.__instance != None: raise Exception('Cannot create multiple instance of Connection')
    Connection.__instance = self
    self.credentials = GoogleCredentials.get_application_default()

  def get_sql_object(self):
    return discovery.build('sqladmin', 'xxxx', credentials=self.credentials)
