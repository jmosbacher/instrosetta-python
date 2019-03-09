import grpc
from enum import Enum
import pint
from instrosetta.utils.units import accept_text
from instrosetta.interfaces.motion.linear import singleaxis_pb2
from instrosetta.interfaces.motion.linear import singleaxis_pb2_grpc

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

class MotorType(Enum):
    DC_SERVO = 0
    STEPPER = 1

class SingleLinearAxis:
    def __init__(self, addr="localhost:50052"):
        self.addr = addr 
        self._stub = None

    def single_rpc(self, method, request):
        if self._stub is None:
            with grpc.insecure_channel(self.addr) as channel:
                stub = singleaxis_pb2_grpc.SingleLinearAxisStub(channel)
        else:
            try:
                resp = getattr(stub, method)(request)
                return resp
            except grpc.RpcError as e:
                print(e)
                # FIXME: log error/ raise exception.

    def streaming_rpc(self, method, request):
        with grpc.insecure_channel(self.addr) as channel:
            stub = singleaxis_pb2_grpc.SingleLinearAxisStub(channel)
            try:
                for resp in getattr(stub, method)(request):
                    yield resp
            except grpc.RpcError as e:
                print(e)
                # FIXME: log error/ raise exception.
               

    def echo(self, text):
        with grpc.insecure_channel(self.addr) as channel:
            stub = singleaxis_pb2_grpc.SingleLinearAxisStub(channel)
            req = singleaxis_pb2.TextMessage(content=text)
            try:
                resp = stub.Echo(req)
                return resp.content
            except grpc.RpcError as e:
                print(e)
                # FIXME: log error/ raise exception.
                return False

    def scan_devices(self):
        with grpc.insecure_channel(self.addr) as channel:
            stub = singleaxis_pb2_grpc.SingleLinearAxisStub(channel)
            req = singleaxis_pb2.ScanDevicesRequest()
            try:
                return [resp.serial_number for resp in stub.ScanDevices(req)]
            except grpc.RpcError as e:
                print(e)
                # FIXME: log error/ raise exception.
                return False

    def connect(self, serial_number, motor_type=0):
        with grpc.insecure_channel(self.addr) as channel:
            stub = singleaxis_pb2_grpc.SingleLinearAxisStub(channel)
            dev = singleaxis_pb2.Device(serial_number=serial_number, motor_type=motor_type)
            req = singleaxis_pb2.ConnectRequest(device=dev, timeout=5, polling_interval=0.25)
            try:
                stub.Connect(req)
            except grpc.RpcError as e:
                print(e)
                # FIXME: log error/ raise exception.
                return False
    
    def get_range(self, units='mm'):
        with grpc.insecure_channel(self.addr) as channel:
            stub = singleaxis_pb2_grpc.SingleLinearAxisStub(channel)
            req = singleaxis_pb2.GetRangeRequest(units=units)
            try:
                resp = stub.GetRange(req)
                return {"minimum": Q_(resp.min, resp.units),
                        "maximum": Q_(resp.max, resp.units),
                        "resolution": Q_(resp.resolution, resp.units)}

            except grpc.RpcError as e:
                return {"minimum": Q_(float('nan')),
                        "maximum": Q_(float('nan')),
                        "resolution": Q_(float('nan')),}

    @property
    def position(self):
        with grpc.insecure_channel(self.addr) as channel:
            stub = singleaxis_pb2_grpc.SingleLinearAxisStub(channel)
            req = singleaxis_pb2.GetPositionRequest()
            try:
                track = [Q_(resp.value, resp.units) for resp in stub.GetPosition(req)]
                return track
            except grpc.RpcError as e:
                return [Q_(float('nan'))]
    
    @position.setter       
    @accept_text
    @ureg.check(None, '[length]')
    def position(self, destination):
        with grpc.insecure_channel(self.addr) as channel:
            stub = singleaxis_pb2_grpc.SingleLinearAxisStub(channel)
            pos = singleaxis_pb2.Position(value=destination.magnitute, units=destination.units)
            req = singleaxis_pb2.MoveAbsoluteRequest(position=pos)
            try:
                track = [Q_(resp.value, resp.units) for resp in stub.GetPosition(req)]
                return track
            except grpc.RpcError as e:
                return [Q_(float('nan'))]

    @ureg.check('[length]')
    def move_absolute(self, position, units='mm'):
        pass

    @ureg.check('[length]')
    def move_relative(self, distance):
        pass
    

    def __enter__(self):
        self._channel = grpc.insecure_channel(self.addr)
        self._stub = singleaxis_pb2_grpc.SingleLinearAxisStub(self._channel)

    def __exit__(self, exc_type, exc_value, traceback):
        self._channel.close()
        self._channel = None
        self._stub = None