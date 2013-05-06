#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import Types.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class TVersionedObject:
  """
  Attributes:
   - service_id
   - key
   - type
   - version
   - value
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'service_id', None, None, ), # 1
    (2, TType.STRING, 'key', None, None, ), # 2
    (3, TType.STRING, 'type', None, None, ), # 3
    (4, TType.I64, 'version', None, None, ), # 4
    (5, TType.STRING, 'value', None, None, ), # 5
  )

  def __init__(self, service_id=None, key=None, type=None, version=None, value=None,):
    self.service_id = service_id
    self.key = key
    self.type = type
    self.version = version
    self.value = value

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.service_id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.key = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.type = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.version = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.value = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TVersionedObject')
    if self.service_id is not None:
      oprot.writeFieldBegin('service_id', TType.STRING, 1)
      oprot.writeString(self.service_id)
      oprot.writeFieldEnd()
    if self.key is not None:
      oprot.writeFieldBegin('key', TType.STRING, 2)
      oprot.writeString(self.key)
      oprot.writeFieldEnd()
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.STRING, 3)
      oprot.writeString(self.type)
      oprot.writeFieldEnd()
    if self.version is not None:
      oprot.writeFieldBegin('version', TType.I64, 4)
      oprot.writeI64(self.version)
      oprot.writeFieldEnd()
    if self.value is not None:
      oprot.writeFieldBegin('value', TType.STRING, 5)
      oprot.writeString(self.value)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TServiceInstance:
  """
  Attributes:
   - subscriber_id
   - host_port
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'subscriber_id', None, None, ), # 1
    (2, TType.STRUCT, 'host_port', (Types.ttypes.TNetworkAddress, Types.ttypes.TNetworkAddress.thrift_spec), None, ), # 2
  )

  def __init__(self, subscriber_id=None, host_port=None,):
    self.subscriber_id = subscriber_id
    self.host_port = host_port

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.subscriber_id = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.host_port = Types.ttypes.TNetworkAddress()
          self.host_port.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TServiceInstance')
    if self.subscriber_id is not None:
      oprot.writeFieldBegin('subscriber_id', TType.I32, 1)
      oprot.writeI32(self.subscriber_id)
      oprot.writeFieldEnd()
    if self.host_port is not None:
      oprot.writeFieldBegin('host_port', TType.STRUCT, 2)
      self.host_port.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.subscriber_id is None:
      raise TProtocol.TProtocolException(message='Required field subscriber_id is unset!')
    if self.host_port is None:
      raise TProtocol.TProtocolException(message='Required field host_port is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TServiceMembership:
  """
  Attributes:
   - service_id
   - service_instances
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'service_id', None, None, ), # 1
    (2, TType.LIST, 'service_instances', (TType.STRUCT,(TServiceInstance, TServiceInstance.thrift_spec)), None, ), # 2
  )

  def __init__(self, service_id=None, service_instances=None,):
    self.service_id = service_id
    self.service_instances = service_instances

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.service_id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.service_instances = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = TServiceInstance()
            _elem5.read(iprot)
            self.service_instances.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TServiceMembership')
    if self.service_id is not None:
      oprot.writeFieldBegin('service_id', TType.STRING, 1)
      oprot.writeString(self.service_id)
      oprot.writeFieldEnd()
    if self.service_instances is not None:
      oprot.writeFieldBegin('service_instances', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.service_instances))
      for iter6 in self.service_instances:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.service_id is None:
      raise TProtocol.TProtocolException(message='Required field service_id is unset!')
    if self.service_instances is None:
      raise TProtocol.TProtocolException(message='Required field service_instances is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)