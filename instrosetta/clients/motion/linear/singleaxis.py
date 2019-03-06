import grpc
from collections import enum
import pint
from instrosseta.utils.units import accept_text
from instrosseta.interfaces.motion.linear import singleaxis_pb2
from instrosseta.interfaces.motion.linear import singleaxis_pb2_grpc

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

class MotorType(enum):
    DC_SERVO = 0
    STEPPER = 1

class LinearSingleAxis:
    def __init__(self, addr="localhost:50051"):
        self.addr = addr 

    def connect(self, serial_number, motor_type=MotorType.DC_SERVO):
        with grpc.insecure_channel(self.addr) as channel:
            stub = singleaxis_pb2_grpc.SingleLinearAxis(channel)
            req = singleaxis_pb2_grpc.Device(serial_number=serial_number, motor_type=motor_type)
            try:
                resp = stub.Connect(req)
                return True
            except grpc.RpcError as e:
                # FIXME: log error/ raise exception.
                return False

    
    def get_range(self, units='mm'):
        with grpc.insecure_channel(self.addr) as channel:
            stub = singleaxis_pb2_grpc.SingleLinearAxis(channel)
            req = singleaxis_pb2_grpc.GetRangeReqeust(units=units)
            try:
                resp = stub.GetRange(req)
                return (Q_(resp.min, resp.units), Q_(resp.max, resp.units), Q_(resp.resolution, resp.units))
            except grpc.RpcError as e:
                return Q_(float('nan'))

    @property
    def position(self):
        with grpc.insecure_channel(self.addr) as channel:
            stub = singleaxis_pb2_grpc.SingleLinearAxis(channel)
            req = singleaxis_pb2_grpc.GetPositionRequest()
            try:
                resp = singleaxis_pb2_grpc.GetPosition(req)
                return Q_(resp.value, resp.units)
            except grpc.RpcError as e:
                return Q_(float('nan'))
    
    @position.setter       
    @accept_text
    @ureg.check(None, '[length]')
    def position(self, destination):
        with grpc.insecure_channel(self.addr) as channel:
            stub = singleaxis_pb2_grpc.SingleLinearAxis(channel)
            pos = singleaxis_pb2_grpc.Position(value=destination.magnitute, units=destination.units)
            req = singleaxis_pb2_grpc.MoveAbsoluteRequest(position=pos)
            try:
                resp = singleaxis_pb2_grpc.MoveAbsolute(req)
                return True
            except grpc.RpcError as e:
                return False

    @ureg.check('[length]')
    def move_absolute(self, position, units='mm'):
        pass

    @ureg.check('[length]')
    def move_relative(self):
        pass
    