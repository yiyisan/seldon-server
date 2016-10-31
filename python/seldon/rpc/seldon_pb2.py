# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: seldon.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='seldon.proto',
  package='io.seldon.api.rpc',
  syntax='proto3',
  serialized_pb=_b('\n\x0cseldon.proto\x12\x11io.seldon.api.rpc\x1a\x19google/protobuf/any.proto\"w\n\x15\x43lassificationRequest\x12:\n\x04meta\x18\x01 \x01(\x0b\x32,.io.seldon.api.rpc.ClassificationRequestMeta\x12\"\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\")\n\x19\x43lassificationRequestMeta\x12\x0c\n\x04puid\x18\x01 \x01(\t\"\xb3\x01\n\x13\x43lassificationReply\x12\x38\n\x04meta\x18\x01 \x01(\x0b\x32*.io.seldon.api.rpc.ClassificationReplyMeta\x12<\n\x0bpredictions\x18\x02 \x03(\x0b\x32\'.io.seldon.api.rpc.ClassificationResult\x12$\n\x06\x63ustom\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"M\n\x17\x43lassificationReplyMeta\x12\x0c\n\x04puid\x18\x01 \x01(\t\x12\x11\n\tmodelName\x18\x02 \x01(\t\x12\x11\n\tvariation\x18\x03 \x01(\t\"V\n\x14\x43lassificationResult\x12\x12\n\nprediction\x18\x01 \x01(\x01\x12\x16\n\x0epredictedClass\x18\x02 \x01(\t\x12\x12\n\nconfidence\x18\x03 \x01(\x01\x32k\n\nClassifier\x12]\n\x07Predict\x12(.io.seldon.api.rpc.ClassificationRequest\x1a&.io.seldon.api.rpc.ClassificationReply\"\x00\x42$\n\x11io.seldon.api.rpcB\rPredictionAPIP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CLASSIFICATIONREQUEST = _descriptor.Descriptor(
  name='ClassificationRequest',
  full_name='io.seldon.api.rpc.ClassificationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='io.seldon.api.rpc.ClassificationRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='io.seldon.api.rpc.ClassificationRequest.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=181,
)


_CLASSIFICATIONREQUESTMETA = _descriptor.Descriptor(
  name='ClassificationRequestMeta',
  full_name='io.seldon.api.rpc.ClassificationRequestMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='puid', full_name='io.seldon.api.rpc.ClassificationRequestMeta.puid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=183,
  serialized_end=224,
)


_CLASSIFICATIONREPLY = _descriptor.Descriptor(
  name='ClassificationReply',
  full_name='io.seldon.api.rpc.ClassificationReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='io.seldon.api.rpc.ClassificationReply.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predictions', full_name='io.seldon.api.rpc.ClassificationReply.predictions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='custom', full_name='io.seldon.api.rpc.ClassificationReply.custom', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=406,
)


_CLASSIFICATIONREPLYMETA = _descriptor.Descriptor(
  name='ClassificationReplyMeta',
  full_name='io.seldon.api.rpc.ClassificationReplyMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='puid', full_name='io.seldon.api.rpc.ClassificationReplyMeta.puid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modelName', full_name='io.seldon.api.rpc.ClassificationReplyMeta.modelName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variation', full_name='io.seldon.api.rpc.ClassificationReplyMeta.variation', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=408,
  serialized_end=485,
)


_CLASSIFICATIONRESULT = _descriptor.Descriptor(
  name='ClassificationResult',
  full_name='io.seldon.api.rpc.ClassificationResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prediction', full_name='io.seldon.api.rpc.ClassificationResult.prediction', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predictedClass', full_name='io.seldon.api.rpc.ClassificationResult.predictedClass', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='io.seldon.api.rpc.ClassificationResult.confidence', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=487,
  serialized_end=573,
)

_CLASSIFICATIONREQUEST.fields_by_name['meta'].message_type = _CLASSIFICATIONREQUESTMETA
_CLASSIFICATIONREQUEST.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CLASSIFICATIONREPLY.fields_by_name['meta'].message_type = _CLASSIFICATIONREPLYMETA
_CLASSIFICATIONREPLY.fields_by_name['predictions'].message_type = _CLASSIFICATIONRESULT
_CLASSIFICATIONREPLY.fields_by_name['custom'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['ClassificationRequest'] = _CLASSIFICATIONREQUEST
DESCRIPTOR.message_types_by_name['ClassificationRequestMeta'] = _CLASSIFICATIONREQUESTMETA
DESCRIPTOR.message_types_by_name['ClassificationReply'] = _CLASSIFICATIONREPLY
DESCRIPTOR.message_types_by_name['ClassificationReplyMeta'] = _CLASSIFICATIONREPLYMETA
DESCRIPTOR.message_types_by_name['ClassificationResult'] = _CLASSIFICATIONRESULT

ClassificationRequest = _reflection.GeneratedProtocolMessageType('ClassificationRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLASSIFICATIONREQUEST,
  __module__ = 'seldon_pb2'
  # @@protoc_insertion_point(class_scope:io.seldon.api.rpc.ClassificationRequest)
  ))
_sym_db.RegisterMessage(ClassificationRequest)

ClassificationRequestMeta = _reflection.GeneratedProtocolMessageType('ClassificationRequestMeta', (_message.Message,), dict(
  DESCRIPTOR = _CLASSIFICATIONREQUESTMETA,
  __module__ = 'seldon_pb2'
  # @@protoc_insertion_point(class_scope:io.seldon.api.rpc.ClassificationRequestMeta)
  ))
_sym_db.RegisterMessage(ClassificationRequestMeta)

ClassificationReply = _reflection.GeneratedProtocolMessageType('ClassificationReply', (_message.Message,), dict(
  DESCRIPTOR = _CLASSIFICATIONREPLY,
  __module__ = 'seldon_pb2'
  # @@protoc_insertion_point(class_scope:io.seldon.api.rpc.ClassificationReply)
  ))
_sym_db.RegisterMessage(ClassificationReply)

ClassificationReplyMeta = _reflection.GeneratedProtocolMessageType('ClassificationReplyMeta', (_message.Message,), dict(
  DESCRIPTOR = _CLASSIFICATIONREPLYMETA,
  __module__ = 'seldon_pb2'
  # @@protoc_insertion_point(class_scope:io.seldon.api.rpc.ClassificationReplyMeta)
  ))
_sym_db.RegisterMessage(ClassificationReplyMeta)

ClassificationResult = _reflection.GeneratedProtocolMessageType('ClassificationResult', (_message.Message,), dict(
  DESCRIPTOR = _CLASSIFICATIONRESULT,
  __module__ = 'seldon_pb2'
  # @@protoc_insertion_point(class_scope:io.seldon.api.rpc.ClassificationResult)
  ))
_sym_db.RegisterMessage(ClassificationResult)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\021io.seldon.api.rpcB\rPredictionAPIP\001'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class ClassifierStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Predict = channel.unary_unary(
        '/io.seldon.api.rpc.Classifier/Predict',
        request_serializer=ClassificationRequest.SerializeToString,
        response_deserializer=ClassificationReply.FromString,
        )


class ClassifierServicer(object):

  def Predict(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ClassifierServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Predict': grpc.unary_unary_rpc_method_handler(
          servicer.Predict,
          request_deserializer=ClassificationRequest.FromString,
          response_serializer=ClassificationReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'io.seldon.api.rpc.Classifier', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaClassifierServicer(object):
  def Predict(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaClassifierStub(object):
  def Predict(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Predict.future = None


def beta_create_Classifier_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('io.seldon.api.rpc.Classifier', 'Predict'): ClassificationRequest.FromString,
  }
  response_serializers = {
    ('io.seldon.api.rpc.Classifier', 'Predict'): ClassificationReply.SerializeToString,
  }
  method_implementations = {
    ('io.seldon.api.rpc.Classifier', 'Predict'): face_utilities.unary_unary_inline(servicer.Predict),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_Classifier_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('io.seldon.api.rpc.Classifier', 'Predict'): ClassificationRequest.SerializeToString,
  }
  response_deserializers = {
    ('io.seldon.api.rpc.Classifier', 'Predict'): ClassificationReply.FromString,
  }
  cardinalities = {
    'Predict': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'io.seldon.api.rpc.Classifier', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
