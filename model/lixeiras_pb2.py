# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lixeiras.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lixeiras.proto',
  package='',
  serialized_pb=_b('\n\x0elixeiras.proto\"\xf9\x01\n\x07Lixeira\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x13\n\x0blocalizacao\x18\x02 \x02(\t\x12\x0c\n\x04peso\x18\x03 \x02(\x02\x12\x33\n\rstatus_coleta\x18\x04 \x02(\x0e\x32\x15.Lixeira.StatusColeta:\x05LIVRE\x12;\n\x11status_capacidade\x18\x05 \x02(\x0e\x32\x19.Lixeira.StatusCapacidade:\x05VAZIA\"#\n\x0cStatusColeta\x12\x08\n\x04ROTA\x10\x00\x12\t\n\x05LIVRE\x10\x01\"(\n\x10StatusCapacidade\x12\t\n\x05\x43HEIA\x10\x00\x12\t\n\x05VAZIA\x10\x01\")\n\x0cListaLixeira\x12\x19\n\x07lixeira\x18\x01 \x03(\x0b\x32\x08.Lixeira')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_LIXEIRA_STATUSCOLETA = _descriptor.EnumDescriptor(
  name='StatusColeta',
  full_name='Lixeira.StatusColeta',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROTA', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIVRE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=191,
  serialized_end=226,
)
_sym_db.RegisterEnumDescriptor(_LIXEIRA_STATUSCOLETA)

_LIXEIRA_STATUSCAPACIDADE = _descriptor.EnumDescriptor(
  name='StatusCapacidade',
  full_name='Lixeira.StatusCapacidade',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CHEIA', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VAZIA', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=228,
  serialized_end=268,
)
_sym_db.RegisterEnumDescriptor(_LIXEIRA_STATUSCAPACIDADE)


_LIXEIRA = _descriptor.Descriptor(
  name='Lixeira',
  full_name='Lixeira',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Lixeira.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='localizacao', full_name='Lixeira.localizacao', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='peso', full_name='Lixeira.peso', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status_coleta', full_name='Lixeira.status_coleta', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status_capacidade', full_name='Lixeira.status_capacidade', index=4,
      number=5, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LIXEIRA_STATUSCOLETA,
    _LIXEIRA_STATUSCAPACIDADE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=268,
)


_LISTALIXEIRA = _descriptor.Descriptor(
  name='ListaLixeira',
  full_name='ListaLixeira',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lixeira', full_name='ListaLixeira.lixeira', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=270,
  serialized_end=311,
)

_LIXEIRA.fields_by_name['status_coleta'].enum_type = _LIXEIRA_STATUSCOLETA
_LIXEIRA.fields_by_name['status_capacidade'].enum_type = _LIXEIRA_STATUSCAPACIDADE
_LIXEIRA_STATUSCOLETA.containing_type = _LIXEIRA
_LIXEIRA_STATUSCAPACIDADE.containing_type = _LIXEIRA
_LISTALIXEIRA.fields_by_name['lixeira'].message_type = _LIXEIRA
DESCRIPTOR.message_types_by_name['Lixeira'] = _LIXEIRA
DESCRIPTOR.message_types_by_name['ListaLixeira'] = _LISTALIXEIRA

Lixeira = _reflection.GeneratedProtocolMessageType('Lixeira', (_message.Message,), dict(
  DESCRIPTOR = _LIXEIRA,
  __module__ = 'lixeiras_pb2'
  # @@protoc_insertion_point(class_scope:Lixeira)
  ))
_sym_db.RegisterMessage(Lixeira)

ListaLixeira = _reflection.GeneratedProtocolMessageType('ListaLixeira', (_message.Message,), dict(
  DESCRIPTOR = _LISTALIXEIRA,
  __module__ = 'lixeiras_pb2'
  # @@protoc_insertion_point(class_scope:ListaLixeira)
  ))
_sym_db.RegisterMessage(ListaLixeira)


# @@protoc_insertion_point(module_scope)
