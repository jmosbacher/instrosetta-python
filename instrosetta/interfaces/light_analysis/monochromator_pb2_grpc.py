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
    self.Initialize = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.monochromator.Monochromator/Initialize',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.InitializeRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.InitializeResponse.FromString,
        )
    self.Shutdown = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.monochromator.Monochromator/Shutdown',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.ShutdownRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.ShutdownResponse.FromString,
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
    self.GetGratingOptions = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.monochromator.Monochromator/GetGratingOptions',
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
    self.GetSlitWidthRange = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.monochromator.Monochromator/GetSlitWidthRange',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetSlitWidthRangeRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetSlitWidthRangeResponse.FromString,
        )
    self.GetSlitWidth = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.monochromator.Monochromator/GetSlitWidth',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetSlitWidthRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetSlitWidthResponse.FromString,
        )
    self.SetSlitWidth = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.monochromator.Monochromator/SetSlitWidth',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.SetSlitWidthRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.SetSlitWidthResponse.FromString,
        )


class MonochromatorServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Initialize(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Shutdown(self, request, context):
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

  def GetGratingOptions(self, request, context):
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

  def GetSlitWidthRange(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSlitWidth(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetSlitWidth(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MonochromatorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Initialize': grpc.unary_unary_rpc_method_handler(
          servicer.Initialize,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.InitializeRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.InitializeResponse.SerializeToString,
      ),
      'Shutdown': grpc.unary_unary_rpc_method_handler(
          servicer.Shutdown,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.ShutdownRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.ShutdownResponse.SerializeToString,
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
      'GetGratingOptions': grpc.unary_unary_rpc_method_handler(
          servicer.GetGratingOptions,
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
      'GetSlitWidthRange': grpc.unary_unary_rpc_method_handler(
          servicer.GetSlitWidthRange,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetSlitWidthRangeRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetSlitWidthRangeResponse.SerializeToString,
      ),
      'GetSlitWidth': grpc.unary_unary_rpc_method_handler(
          servicer.GetSlitWidth,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetSlitWidthRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.GetSlitWidthResponse.SerializeToString,
      ),
      'SetSlitWidth': grpc.unary_unary_rpc_method_handler(
          servicer.SetSlitWidth,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.SetSlitWidthRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_monochromator__pb2.SetSlitWidthResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'instrosetta.interfaces.light_analysis.monochromator.Monochromator', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
