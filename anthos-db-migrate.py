import os
from datetime import datetime

INSTANCE = "staging-pg"
BUCKET = "singapore-db-exports"

def pretty_print(string):
  print "=================================================="
  print "                  %s" % string
  print "=================================================="

def export_db(instance_name, db_name, bucket_name):
  pretty_print("Export DB: %s" % db_name)
  filename = "%s-%s" % (db_name, datetime.now().strftime("%Y-%m-%d_%H:%M"))
  export_cmd = "gcloud sql export sql %s gs://%s/%s.sql --database=%s" % (instance_name, bucket_name, filename, db_name)
  export_job = os.popen(export_cmd)
  print export_job.read()

def export_instance(instance_name, bucket_name):
  pretty_print("Export Instance: %s" % instance_name)
  instances = os.popen("gcloud sql databases list --instance=%s" % instance_name)
  dbs = instances.read().split()[3::3]
  for db_name in dbs:
    export_db(instance_name, db_name, bucket_name)

export_instance(INSTANCE, BUCKET)
