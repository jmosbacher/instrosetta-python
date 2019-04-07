# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from instrosetta.interfaces.light_analysis import monochromator_pb2 as instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2


class MonochromatorStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Connect = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.monochromator.Monochromator/Connect',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.ConnectRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.ConnectResponse.FromString,
        )
    self.Disconnect = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.monochromator.Monochromator/Disconnect',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.DisconnectRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.DisconnectResponse.FromString,
        )
    self.GetWavelengthRange = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.monochromator.Monochromator/GetWavelengthRange',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetWavelengthRangeRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetWavelengthRangeResponse.FromString,
        )
    self.GetWavelength = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.monochromator.Monochromator/GetWavelength',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetWavelengthRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetWavelengthResponse.FromString,
        )
    self.SetWavelength = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.monochromator.Monochromator/SetWavelength',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.SetWavelengthRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.SetWavelengthResponse.FromString,
        )
    self.GetGratingRange = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.monochromator.Monochromator/GetGratingRange',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetGratingOptionsRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetGratingOptionsResponse.FromString,
        )
    self.GetGrating = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.monochromator.Monochromator/GetGrating',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetGratingRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetGratingResponse.FromString,
        )
    self.SetGrating = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.monochromator.Monochromator/SetGrating',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.SetGratingRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.SetGratingResponse.FromString,
        )


class MonochromatorServicer(object):
  # missing associated documentation comment in .proto file
  pass

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

  def GetWavelengthRange(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetWavelength(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetWavelength(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetGratingRange(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetGrating(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetGrating(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MonochromatorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Connect': grpc.unary_unary_rpc_method_handler(
          servicer.Connect,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.ConnectRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.ConnectResponse.SerializeToString,
      ),
      'Disconnect': grpc.unary_unary_rpc_method_handler(
          servicer.Disconnect,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.DisconnectRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.DisconnectResponse.SerializeToString,
      ),
      'GetWavelengthRange': grpc.unary_unary_rpc_method_handler(
          servicer.GetWavelengthRange,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetWavelengthRangeRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetWavelengthRangeResponse.SerializeToString,
      ),
      'GetWavelength': grpc.unary_unary_rpc_method_handler(
          servicer.GetWavelength,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetWavelengthRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetWavelengthResponse.SerializeToString,
      ),
      'SetWavelength': grpc.unary_unary_rpc_method_handler(
          servicer.SetWavelength,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.SetWavelengthRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.SetWavelengthResponse.SerializeToString,
      ),
      'GetGratingRange': grpc.unary_unary_rpc_method_handler(
          servicer.GetGratingRange,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetGratingOptionsRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetGratingOptionsResponse.SerializeToString,
      ),
      'GetGrating': grpc.unary_unary_rpc_method_handler(
          servicer.GetGrating,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetGratingRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetGratingResponse.SerializeToString,
      ),
      'SetGrating': grpc.unary_unary_rpc_method_handler(
          servicer.SetGrating,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.SetGratingRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.SetGratingResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'instrosetta.interfaces.light_analysis.monochromator.Monochromator', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
