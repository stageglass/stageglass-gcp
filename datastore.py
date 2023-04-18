from google.cloud import datastore
from datetime import datetime

from google.protobuf.message import Message
from google.protobuf import json_format

import json

from common_pb2 import LinkCodeRecord, Lifecycle

def build_client():
  return datastore.Client()

def now():
  return int(datetime.now().timestamp())

def set_creation_ts(message: Message):
  if message.HasField("lifecycle"):
    if isinstance(message.lifecycle, Lifecycle):
      message.lifecycle.creation_ts = now()

def set_last_modified_ts(message: Message):
  if message.HasField("lifecycle"):
    if isinstance(message.lifecycle, Lifecycle):
      message.lifecycle.last_modified_ts = now()

def as_json(message: Message):
  return json_format.MessageToJson(message)

def from_json(json_string, output_message: Message):
  return json_format.Parse(json_string, output_message)

def as_kind(message: Message):
  return message.__class__.__name__

class DatastoreHandle:
  
  def __init__(self):
    self.client = build_client()

  def put(self, message: Message, key=None):
    set_last_modified_ts(message)

    entity_key = self.client.key(as_kind(message), key)
    entity = datastore.Entity(key=entity_key)

    json_string = as_json(message)
    entity.update(json.loads(json_string))

    self.client.put(entity)
    return entity

  def get(self, key, output_message: Message):
    entity_key = self.client.key(as_kind(output_message), key)
    entity = self.client.get(entity_key)
    json_string = json.dumps(entity)
    return from_json(json_string, output_message)

  def create_link_code_record(self, record: LinkCodeRecord, code):
    set_creation_ts(record)
    result = self.put(record, code)
    return result

  def get_link_code_record(self, code):
    result = self.get(code, LinkCodeRecord())
    return result

