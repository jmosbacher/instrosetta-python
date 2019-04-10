import grpc
from enum import Enum
import pint
from instrosetta.utils.units import accept_text
from instrosetta.interfaces.motion_control import singleaxis_pb2 as pb2 
from instrosetta.interfaces.motion_control import singleaxis_pb2_grpc as pb2_grpc
from instrosetta.client import RpcClient
ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


class SingleAxis(RpcClient):
    stub_class = pb2_grpc.SingleAxisStub

    def scan_devices(self):
        req = pb2.ScanDevicesRequest()
        return [resp.device_id for resp in self.streaming_rpc('ScanDevices', req)]

    def connect(self, device_id='', timeout=5):
        req = pb2.ConnectRequest(device_id=device_id, timeout=timeout)
        self.single_rpc("Connect", req)

    def disconnect(self):
        req = pb2.DisconnectRequest()
        self.single_rpc("Disconnect", req)

    def home(self):
        req = pb2.HomeMotorRequest()
        self.single_rpc("HomeMotor", req)

    def get_range(self, units='mm'):
        req = pb2.GetRangeRequest(units=units)
        resp = self.single_rpc("GetRange", req)
        if resp is not None:
            return {"minimum": Q_(resp.min, resp.units),
                    "maximum": Q_(resp.max, resp.units),
                    "resolution": Q_(resp.resolution, resp.units)}

        else:
            return {"minimum": Q_(float('nan')),
                    "maximum": Q_(float('nan')),
                    "resolution": Q_(float('nan')),}

    @property
    def position(self):
        req = pb2.GetPositionRequest()
        resp = self.single_rpc("GetPosition", req)
        if resp is not None:
            return Q_(resp.value, resp.units)
        else:
            return [Q_(float('nan'))]

    @position.setter       
    @accept_text
    def position(self, destination):
        pos = pb2.Position(value=destination.magnitude, units=str(destination.units))
        req = pb2.MoveAbsoluteRequest(position=pos)
        [Q_(resp.value, resp.units) for resp in self.streaming_rpc("MoveAbsolute", req)]

    @accept_text
    def move_absolute(self, destination):
        pos = pb2.Position(value=destination.magnitude, units=str(destination.units))
        req = pb2.MoveAbsoluteRequest(position=pos)
        track = [(Q_(float('nan')) if resp is None else Q_(resp.value, resp.units)) for resp in self.streaming_rpc("MoveAbsolute", req)]
        return track

    @accept_text
    def move_relative(self, distance, direction=1):
        dist = pb2.Distance(value=distance.magnitude, units=str(distance.units), direction=direction)
        req = pb2.MoveRelativeRequest(distance=dist)
        track = [(Q_(float('nan')) if resp is None else Q_(resp.value, resp.units)) for resp in self.streaming_rpc("MoveRelative", req)]
        return track
