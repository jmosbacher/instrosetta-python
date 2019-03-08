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
    
    def connect(self, serial_number, motor_type=0):
        with grpc.insecure_channel(self.addr) as channel:
            stub = singleaxis_pb2_grpc.SingleLinearAxisStub(channel)
            dev = singleaxis_pb2.Device(serial_number=serial_number, motor_type=motor_type)
            req = singleaxis_pb2.ConnectRequest(device=dev)
            try:
                stub.Connect(req)
            except grpc.RpcError as e:
                print(e)
                # FIXME: log error/ raise exception.
                return False
    
    def get_range(self, units='mm'):
        with grpc.insecure_channel(self.addr) as channel:
            stub = singleaxis_pb2_grpc.SingleLinearAxisStub(channel)
            req = singleaxis_pb2.GetRangeReqeust(units=units)
            try:
                resp = stub.GetRange(req)
                return (Q_(resp.min, resp.units), Q_(resp.max, resp.units), Q_(resp.resolution, resp.units))
            except grpc.RpcError as e:
                return Q_(float('nan'))

    @property
    def position(self):
        with grpc.insecure_channel(self.addr) as channel:
            stub = singleaxis_pb2_grpc.SingleLinearAxisStub(channel)
            req = singleaxis_pb2.GetPositionRequest()
            try:
                resp = stub.GetPosition(req)
                return Q_(resp.value, resp.units)
            except grpc.RpcError as e:
                return Q_(float('nan'))
    
    @position.setter       
    @accept_text
    @ureg.check(None, '[length]')
    def position(self, destination):
        with grpc.insecure_channel(self.addr) as channel:
            stub = singleaxis_pb2_grpc.SingleLinearAxisStub(channel)
            pos = singleaxis_pb2.Position(value=destination.magnitute, units=destination.units)
            req = singleaxis_pb2.MoveAbsoluteRequest(position=pos)
            try:
                resp = stub.MoveAbsolute(req)
                return True
            except grpc.RpcError as e:
                return False

    @ureg.check('[length]')
    def move_absolute(self, position, units='mm'):
        pass

    @ureg.check('[length]')
    def move_relative(self):
        pass
    