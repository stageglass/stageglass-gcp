# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63ommon.proto\"\x1e\n\rTimeInSeconds\x12\r\n\x05value\x18\x01 \x01(\x03\"\x84\x01\n\tLifecycle\x12#\n\x0b\x63reation_ts\x18\x01 \x01(\x0b\x32\x0e.TimeInSeconds\x12(\n\x10last_modified_ts\x18\x02 \x01(\x0b\x32\x0e.TimeInSeconds\x12 \n\x03ttl\x18\x03 \x01(\x0b\x32\x0e.TimeInSecondsH\x00\x88\x01\x01\x42\x06\n\x04_ttl\"-\n\x04Name\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\"S\n\x07\x43ontact\x12\x12\n\x05\x65mail\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x0cphone_number\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_emailB\x0f\n\r_phone_number\"\xaf\x01\n\x07\x41\x64\x64ress\x12\x0e\n\x06line_1\x18\x01 \x01(\t\x12\x13\n\x06line_2\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06line_3\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x0c\n\x04\x63ity\x18\x04 \x01(\t\x12\x11\n\tpost_code\x18\x05 \x01(\t\x12\x1d\n\x15state_province_county\x18\x06 \x01(\t\x12\x14\n\x0c\x63ountry_code\x18\x07 \x01(\tB\t\n\x07_line_2B\t\n\x07_line_3\"\x9e\x01\n\x0e\x42usinessRecord\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x07\x63ontact\x18\x02 \x01(\x0b\x32\x08.Contact\x12\x1e\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x08.AddressH\x00\x88\x01\x01\x12\x1d\n\tlifecycle\x18\x04 \x01(\x0b\x32\n.Lifecycle\x12\x10\n\x03key\x18\x05 \x01(\tH\x01\x88\x01\x01\x42\n\n\x08_addressB\x06\n\x04_key\"~\n\x0fRenderingRecord\x12$\n\trendering\x18\x01 \x01(\x0e\x32\x11.RenderingService\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x1d\n\tlifecycle\x18\x03 \x01(\x0b\x32\n.Lifecycle\x12\x10\n\x03key\x18\x04 \x01(\tH\x00\x88\x01\x01\x42\x06\n\x04_key\"\x94\x01\n\x0ePropertyRecord\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x08.Address\x12 \n\x07\x62uilder\x18\x03 \x01(\x0b\x32\x0f.BusinessRecord\x12\x1d\n\tlifecycle\x18\x04 \x01(\x0b\x32\n.Lifecycle\x12\x10\n\x03key\x18\x05 \x01(\tH\x00\x88\x01\x01\x42\x06\n\x04_key\"\xdf\x01\n\x0bSceneRecord\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x08property\x18\x02 \x01(\x0b\x32\x0f.PropertyRecordH\x00\x88\x01\x01\x12\x1c\n\x06status\x18\x03 \x01(\x0e\x32\x0c.SceneStatus\x12(\n\trendering\x18\x04 \x01(\x0b\x32\x10.RenderingRecordH\x01\x88\x01\x01\x12\x1d\n\tlifecycle\x18\x05 \x01(\x0b\x32\n.Lifecycle\x12\x10\n\x03key\x18\x06 \x01(\tH\x02\x88\x01\x01\x42\x0b\n\t_propertyB\x0c\n\n_renderingB\x06\n\x04_key\"\xef\x01\n\x0eLinkCodeRecord\x12\"\n\x0erecipient_name\x18\x01 \x01(\x0b\x32\x05.NameH\x00\x88\x01\x01\x12%\n\x07\x63reator\x18\x02 \x01(\x0b\x32\x0f.BusinessRecordH\x01\x88\x01\x01\x12\x1b\n\x05scene\x18\x03 \x01(\x0b\x32\x0c.SceneRecord\x12\x1d\n\tlifecycle\x18\x04 \x01(\x0b\x32\n.Lifecycle\x12\x1d\n\x05usage\x18\x05 \x01(\x0e\x32\x0e.LinkCodeUsage\x12\x10\n\x03key\x18\x06 \x01(\tH\x02\x88\x01\x01\x42\x11\n\x0f_recipient_nameB\n\n\x08_creatorB\x06\n\x04_key\"\x8b\x01\n\x10\x41PIMappingRecord\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x10\n\x08priority\x18\x03 \x01(\x05\x12\x11\n\tis_active\x18\x04 \x01(\x08\x12\x1d\n\tlifecycle\x18\x05 \x01(\x0b\x32\n.Lifecycle\x12\x10\n\x03key\x18\x07 \x01(\tH\x00\x88\x01\x01\x42\x06\n\x04_key\"?\n\rConfiguration\x12.\n\x13\x61\x63tive_api_mappings\x18\x01 \x03(\x0b\x32\x11.APIMappingRecord* \n\x10RenderingService\x12\x0c\n\x08\x45\x41GLE_3D\x10\x00*:\n\x0bSceneStatus\x12\x0b\n\x07PLANNED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\r\n\tCOMPLETED\x10\x02*)\n\rLinkCodeUsage\x12\n\n\x06PUBLIC\x10\x00\x12\x0c\n\x08PERSONAL\x10\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RENDERINGSERVICE._serialized_start=1608
  _RENDERINGSERVICE._serialized_end=1640
  _SCENESTATUS._serialized_start=1642
  _SCENESTATUS._serialized_end=1700
  _LINKCODEUSAGE._serialized_start=1702
  _LINKCODEUSAGE._serialized_end=1743
  _TIMEINSECONDS._serialized_start=16
  _TIMEINSECONDS._serialized_end=46
  _LIFECYCLE._serialized_start=49
  _LIFECYCLE._serialized_end=181
  _NAME._serialized_start=183
  _NAME._serialized_end=228
  _CONTACT._serialized_start=230
  _CONTACT._serialized_end=313
  _ADDRESS._serialized_start=316
  _ADDRESS._serialized_end=491
  _BUSINESSRECORD._serialized_start=494
  _BUSINESSRECORD._serialized_end=652
  _RENDERINGRECORD._serialized_start=654
  _RENDERINGRECORD._serialized_end=780
  _PROPERTYRECORD._serialized_start=783
  _PROPERTYRECORD._serialized_end=931
  _SCENERECORD._serialized_start=934
  _SCENERECORD._serialized_end=1157
  _LINKCODERECORD._serialized_start=1160
  _LINKCODERECORD._serialized_end=1399
  _APIMAPPINGRECORD._serialized_start=1402
  _APIMAPPINGRECORD._serialized_end=1541
  _CONFIGURATION._serialized_start=1543
  _CONFIGURATION._serialized_end=1606
# @@protoc_insertion_point(module_scope)