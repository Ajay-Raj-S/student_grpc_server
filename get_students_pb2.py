# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_students.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_students.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12get_students.proto\"$\n\x0eget_student_id\x12\x12\n\nstudent_id\x18\x01 \x01(\r\".\n\x16return_student_details\x12\x14\n\x0cstudent_name\x18\x01 \x01(\t\"0\n\x15\x65mpty_student_details\x12\x17\n\x0fstudent_details\x18\x01 \x01(\t2F\n\x08Students\x12:\n\x0eStudentDetails\x12\x0f.get_student_id\x1a\x17.return_student_detailsb\x06proto3'
)




_GET_STUDENT_ID = _descriptor.Descriptor(
  name='get_student_id',
  full_name='get_student_id',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='student_id', full_name='get_student_id.student_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=22,
  serialized_end=58,
)


_RETURN_STUDENT_DETAILS = _descriptor.Descriptor(
  name='return_student_details',
  full_name='return_student_details',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='student_name', full_name='return_student_details.student_name', index=0,
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
  serialized_start=60,
  serialized_end=106,
)


_EMPTY_STUDENT_DETAILS = _descriptor.Descriptor(
  name='empty_student_details',
  full_name='empty_student_details',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='student_details', full_name='empty_student_details.student_details', index=0,
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
  serialized_start=108,
  serialized_end=156,
)

DESCRIPTOR.message_types_by_name['get_student_id'] = _GET_STUDENT_ID
DESCRIPTOR.message_types_by_name['return_student_details'] = _RETURN_STUDENT_DETAILS
DESCRIPTOR.message_types_by_name['empty_student_details'] = _EMPTY_STUDENT_DETAILS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

get_student_id = _reflection.GeneratedProtocolMessageType('get_student_id', (_message.Message,), {
  'DESCRIPTOR' : _GET_STUDENT_ID,
  '__module__' : 'get_students_pb2'
  # @@protoc_insertion_point(class_scope:get_student_id)
  })
_sym_db.RegisterMessage(get_student_id)

return_student_details = _reflection.GeneratedProtocolMessageType('return_student_details', (_message.Message,), {
  'DESCRIPTOR' : _RETURN_STUDENT_DETAILS,
  '__module__' : 'get_students_pb2'
  # @@protoc_insertion_point(class_scope:return_student_details)
  })
_sym_db.RegisterMessage(return_student_details)

empty_student_details = _reflection.GeneratedProtocolMessageType('empty_student_details', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY_STUDENT_DETAILS,
  '__module__' : 'get_students_pb2'
  # @@protoc_insertion_point(class_scope:empty_student_details)
  })
_sym_db.RegisterMessage(empty_student_details)



_STUDENTS = _descriptor.ServiceDescriptor(
  name='Students',
  full_name='Students',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=158,
  serialized_end=228,
  methods=[
  _descriptor.MethodDescriptor(
    name='StudentDetails',
    full_name='Students.StudentDetails',
    index=0,
    containing_service=None,
    input_type=_GET_STUDENT_ID,
    output_type=_RETURN_STUDENT_DETAILS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STUDENTS)

DESCRIPTOR.services_by_name['Students'] = _STUDENTS

# @@protoc_insertion_point(module_scope)
