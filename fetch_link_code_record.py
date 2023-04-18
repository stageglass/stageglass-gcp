from mock_builder import build_link_code_record
from datastore import DatastoreHandle

def run():
  print("attempting fetch_link_code_record...")

  ds = DatastoreHandle()
  ds.get_link_code_record("3YHWKA7A")

if __name__ == '__main__':
  run()
