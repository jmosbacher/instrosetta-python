import grpc
from enum import Enum
import pint
from instrosetta.interfaces.optics import monochromator_pb2
from instrosetta.interfaces.optics import monochromator_pb2_grpc
from cm112 import CM112

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


class CM112Servicer(monochromator_pb2_grpc.MonochromatorServicer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.device = CM112()

    def Connect(self, request, context):
        if self.device.connected:
            return monochromator_pb2.ConnectRespose()
        try:
            self.device.connect(request.serial_port, baudrate=request.baudrate, timeout=request.timeout)
        except:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('Failed to connect.')
        return monochromator_pb2.ConnectRespose()

    def GetWavelength(self, request, context):
        if not self.device.connected:
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            context.set_details('Not connected to any device.')
        try:
            return monochromator_pb2.GetWavelengthResponse(
                wavelength = self.device.wavelength,
                units = "nm"
            )
           
        except Exception as e:
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            context.set_details(f'Device raised esception: {e}')

            
