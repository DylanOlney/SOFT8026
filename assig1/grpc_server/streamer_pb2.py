# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='streamer.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0estreamer.proto\"\x1c\n\rClientRequest\x12\x0b\n\x03msg\x18\x01 \x01(\t\"!\n\x0eServerResponse\x12\x0f\n\x07\x64\x61taRow\x18\x01 \x01(\t2;\n\x08Streamer\x12/\n\x08getPosts\x12\x0e.ClientRequest\x1a\x0f.ServerResponse\"\x00\x30\x01\x62\x06proto3'
)




_CLIENTREQUEST = _descriptor.Descriptor(
  name='ClientRequest',
  full_name='ClientRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='ClientRequest.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=46,
)


_SERVERRESPONSE = _descriptor.Descriptor(
  name='ServerResponse',
  full_name='ServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataRow', full_name='ServerResponse.dataRow', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=81,
)

DESCRIPTOR.message_types_by_name['ClientRequest'] = _CLIENTREQUEST
DESCRIPTOR.message_types_by_name['ServerResponse'] = _SERVERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientRequest = _reflection.GeneratedProtocolMessageType('ClientRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTREQUEST,
  '__module__' : 'streamer_pb2'
  # @@protoc_insertion_point(class_scope:ClientRequest)
  })
_sym_db.RegisterMessage(ClientRequest)

ServerResponse = _reflection.GeneratedProtocolMessageType('ServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERRESPONSE,
  '__module__' : 'streamer_pb2'
  # @@protoc_insertion_point(class_scope:ServerResponse)
  })
_sym_db.RegisterMessage(ServerResponse)



_STREAMER = _descriptor.ServiceDescriptor(
  name='Streamer',
  full_name='Streamer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=83,
  serialized_end=142,
  methods=[
  _descriptor.MethodDescriptor(
    name='getPosts',
    full_name='Streamer.getPosts',
    index=0,
    containing_service=None,
    input_type=_CLIENTREQUEST,
    output_type=_SERVERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STREAMER)

DESCRIPTOR.services_by_name['Streamer'] = _STREAMER

# @@protoc_insertion_point(module_scope)
