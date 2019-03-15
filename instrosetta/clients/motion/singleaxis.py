import grpc
from enum import Enum
import pint
from instrosetta.utils.units import accept_text
from instrosetta.interfaces.motion import singleaxis_pb2
from instrosetta.interfaces.motion import singleaxis_pb2_grpc
from instrosetta.client import RpcClient
ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

class MotorType(Enum):
    DC_SERVO = 0
    STEPPER = 1

class SingleAxis(RpcClient):
    def __init__(self, addr="localhost:50052"):
        self.addr = addr 
        self._channel = None
        self._stub = None
       
    def _single_rpc(self, method, request):
        try:
            resp = getattr(self._stub, method)(request)
            return resp
        except grpc.RpcError as e:
            print(e)
            # FIXME: log error/ raise exception.

    def single_rpc(self, method, request):
        if self._channel is None:
            with self as s:
                return s._single_rpc(method, request)
        else:
            return self._single_rpc(method, request)

    def _streaming_rpc(self, method, request):
        try:
            for resp in getattr(self._stub, method)(request):
                yield resp
        except grpc.RpcError as e:
            print(e)
            # FIXME: log error/ raise exception.
            #    
    def streaming_rpc(self, method, request):
        if self._channel is None:
            with self as s:
                for resp in s._streaming_rpc(method, request):
                    yield resp
        else:
            for resp in self._streaming_rpc(method, request):
                    yield resp
            
    def echo(self, text):
        req = singleaxis_pb2.TextMessage(content=text)
        return self.single_rpc("Echo", req).content

    def scan_devices(self):
        req = singleaxis_pb2.ScanDevicesRequest()
        return [resp.serial_number for resp in self.streaming_rpc('ScanDevices', req)]

    def connect(self, serial_number, motor_type=0, timeout=5, polling_interval=0.25):
        dev = singleaxis_pb2.Device(serial_number=serial_number, motor_type=motor_type)
        req = singleaxis_pb2.ConnectRequest(device=dev, timeout=timeout, polling_interval=polling_interval)
        self.single_rpc("Connect", req)

    def disconnect(self):
        req = singleaxis_pb2.DisconnectRequest()
        self.single_rpc("Disconnect", req)

    def home(self):
        req = singleaxis_pb2.HomeMotorRequest()
        self.single_rpc("HomeMotor", req)

    def get_range(self, units='mm'):
        req = singleaxis_pb2.GetRangeRequest(units=units)
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
        req = singleaxis_pb2.GetPositionRequest()
        resp = self.single_rpc("GetPosition", req)
        if resp is not None:
            return Q_(resp.value, resp.units)
        else:
            return [Q_(float('nan'))]

    @position.setter       
    @accept_text
    def position(self, destination):
        pos = singleaxis_pb2.Position(value=destination.magnitude, units=str(destination.units))
        req = singleaxis_pb2.MoveAbsoluteRequest(position=pos)
        [Q_(resp.value, resp.units) for resp in self.streaming_rpc("MoveAbsolute", req)]

    @accept_text
    def move_absolute(self, destination):
        pos = singleaxis_pb2.Position(value=destination.magnitude, units=str(destination.units))
        req = singleaxis_pb2.MoveAbsoluteRequest(position=pos)
        track = [(Q_(float('nan')) if resp is None else Q_(resp.value, resp.units)) for resp in self.streaming_rpc("MoveAbsolute", req)]
        return track

    @accept_text
    def move_relative(self, distance, direction=1):
        dist = singleaxis_pb2.Distance(value=distance.magnitude, units=str(distance.units), direction=direction)
        req = singleaxis_pb2.MoveRelativeRequest(distance=dist)
        track = [(Q_(float('nan')) if resp is None else Q_(resp.value, resp.units)) for resp in self.streaming_rpc("MoveRelative", req)]
        return track

    def __enter__(self):
        self._channel = grpc.insecure_channel(self.addr)
        self._stub = singleaxis_pb2_grpc.SingleAxisStub(self._channel)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._channel.close()
        self._channel = None
        self._stub = None