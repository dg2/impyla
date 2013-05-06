#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class TPrimitiveType:
  INVALID_TYPE = 0
  BOOLEAN = 1
  TINYINT = 2
  SMALLINT = 3
  INT = 4
  BIGINT = 5
  FLOAT = 6
  DOUBLE = 7
  DATE = 8
  DATETIME = 9
  TIMESTAMP = 10
  STRING = 11
  BINARY = 12
  DECIMAL = 13

  _VALUES_TO_NAMES = {
    0: "INVALID_TYPE",
    1: "BOOLEAN",
    2: "TINYINT",
    3: "SMALLINT",
    4: "INT",
    5: "BIGINT",
    6: "FLOAT",
    7: "DOUBLE",
    8: "DATE",
    9: "DATETIME",
    10: "TIMESTAMP",
    11: "STRING",
    12: "BINARY",
    13: "DECIMAL",
  }

  _NAMES_TO_VALUES = {
    "INVALID_TYPE": 0,
    "BOOLEAN": 1,
    "TINYINT": 2,
    "SMALLINT": 3,
    "INT": 4,
    "BIGINT": 5,
    "FLOAT": 6,
    "DOUBLE": 7,
    "DATE": 8,
    "DATETIME": 9,
    "TIMESTAMP": 10,
    "STRING": 11,
    "BINARY": 12,
    "DECIMAL": 13,
  }

class TStmtType:
  QUERY = 0
  DDL = 1
  DML = 2

  _VALUES_TO_NAMES = {
    0: "QUERY",
    1: "DDL",
    2: "DML",
  }

  _NAMES_TO_VALUES = {
    "QUERY": 0,
    "DDL": 1,
    "DML": 2,
  }

class TExplainLevel:
  NORMAL = 0
  VERBOSE = 1

  _VALUES_TO_NAMES = {
    0: "NORMAL",
    1: "VERBOSE",
  }

  _NAMES_TO_VALUES = {
    "NORMAL": 0,
    "VERBOSE": 1,
  }


class TNetworkAddress:
  """
  Attributes:
   - hostname
   - port
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'hostname', None, None, ), # 1
    (2, TType.I32, 'port', None, None, ), # 2
  )

  def __init__(self, hostname=None, port=None,):
    self.hostname = hostname
    self.port = port

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
          self.hostname = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.port = iprot.readI32();
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
    oprot.writeStructBegin('TNetworkAddress')
    if self.hostname is not None:
      oprot.writeFieldBegin('hostname', TType.STRING, 1)
      oprot.writeString(self.hostname)
      oprot.writeFieldEnd()
    if self.port is not None:
      oprot.writeFieldBegin('port', TType.I32, 2)
      oprot.writeI32(self.port)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.hostname is None:
      raise TProtocol.TProtocolException(message='Required field hostname is unset!')
    if self.port is None:
      raise TProtocol.TProtocolException(message='Required field port is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TUniqueId:
  """
  Attributes:
   - hi
   - lo
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'hi', None, None, ), # 1
    (2, TType.I64, 'lo', None, None, ), # 2
  )

  def __init__(self, hi=None, lo=None,):
    self.hi = hi
    self.lo = lo

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
        if ftype == TType.I64:
          self.hi = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.lo = iprot.readI64();
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
    oprot.writeStructBegin('TUniqueId')
    if self.hi is not None:
      oprot.writeFieldBegin('hi', TType.I64, 1)
      oprot.writeI64(self.hi)
      oprot.writeFieldEnd()
    if self.lo is not None:
      oprot.writeFieldBegin('lo', TType.I64, 2)
      oprot.writeI64(self.lo)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.hi is None:
      raise TProtocol.TProtocolException(message='Required field hi is unset!')
    if self.lo is None:
      raise TProtocol.TProtocolException(message='Required field lo is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)