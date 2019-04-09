# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from instrosetta.interfaces.electronics import simple_switch_pb2 as instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2


class SimpleSwitchStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Echo = channel.unary_unary(
        '/instrosetta.interfaces.electronics.simple_switch.v1.SimpleSwitch/Echo',
        request_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.EchoRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.EchoResponse.FromString,
        )
    self.Connect = channel.unary_unary(
        '/instrosetta.interfaces.electronics.simple_switch.v1.SimpleSwitch/Connect',
        request_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.ConnectRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.ConnectResponse.FromString,
        )
    self.Disconnect = channel.unary_unary(
        '/instrosetta.interfaces.electronics.simple_switch.v1.SimpleSwitch/Disconnect',
        request_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.DisconnectRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.DisconnectResponse.FromString,
        )
    self.Flip = channel.unary_unary(
        '/instrosetta.interfaces.electronics.simple_switch.v1.SimpleSwitch/Flip',
        request_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.FlipRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.FlipResponse.FromString,
        )
    self.GetState = channel.unary_unary(
        '/instrosetta.interfaces.electronics.simple_switch.v1.SimpleSwitch/GetState',
        request_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.GetStateRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.GetStateResponse.FromString,
        )
    self.SetState = channel.unary_unary(
        '/instrosetta.interfaces.electronics.simple_switch.v1.SimpleSwitch/SetState',
        request_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.SetStateRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.SetStateResponse.FromString,
        )
    self.GetBoard = channel.unary_unary(
        '/instrosetta.interfaces.electronics.simple_switch.v1.SimpleSwitch/GetBoard',
        request_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.GetBoardRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.GetBoardResponse.FromString,
        )
    self.SetBoard = channel.unary_unary(
        '/instrosetta.interfaces.electronics.simple_switch.v1.SimpleSwitch/SetBoard',
        request_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.SetBoardRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.SetBoardResponse.FromString,
        )
    self.GetPin = channel.unary_unary(
        '/instrosetta.interfaces.electronics.simple_switch.v1.SimpleSwitch/GetPin',
        request_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.GetPinRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.GetPinResponse.FromString,
        )
    self.SetPin = channel.unary_unary(
        '/instrosetta.interfaces.electronics.simple_switch.v1.SimpleSwitch/SetPin',
        request_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.SetPinRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.SetPinResponse.FromString,
        )


class SimpleSwitchServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Echo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Connect(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Disconnect(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Flip(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBoard(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetBoard(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPin(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetPin(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SimpleSwitchServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Echo': grpc.unary_unary_rpc_method_handler(
          servicer.Echo,
          request_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.EchoRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.EchoResponse.SerializeToString,
      ),
      'Connect': grpc.unary_unary_rpc_method_handler(
          servicer.Connect,
          request_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.ConnectRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.ConnectResponse.SerializeToString,
      ),
      'Disconnect': grpc.unary_unary_rpc_method_handler(
          servicer.Disconnect,
          request_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.DisconnectRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.DisconnectResponse.SerializeToString,
      ),
      'Flip': grpc.unary_unary_rpc_method_handler(
          servicer.Flip,
          request_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.FlipRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.FlipResponse.SerializeToString,
      ),
      'GetState': grpc.unary_unary_rpc_method_handler(
          servicer.GetState,
          request_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.GetStateRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.GetStateResponse.SerializeToString,
      ),
      'SetState': grpc.unary_unary_rpc_method_handler(
          servicer.SetState,
          request_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.SetStateRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.SetStateResponse.SerializeToString,
      ),
      'GetBoard': grpc.unary_unary_rpc_method_handler(
          servicer.GetBoard,
          request_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.GetBoardRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.GetBoardResponse.SerializeToString,
      ),
      'SetBoard': grpc.unary_unary_rpc_method_handler(
          servicer.SetBoard,
          request_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.SetBoardRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.SetBoardResponse.SerializeToString,
      ),
      'GetPin': grpc.unary_unary_rpc_method_handler(
          servicer.GetPin,
          request_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.GetPinRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.GetPinResponse.SerializeToString,
      ),
      'SetPin': grpc.unary_unary_rpc_method_handler(
          servicer.SetPin,
          request_deserializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.SetPinRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_electronics_dot_simple__switch__pb2.SetPinResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'instrosetta.interfaces.electronics.simple_switch.v1.SimpleSwitch', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
