import grpc
from enum import Enum
import pint
from instrosetta.utils.units import accept_text
from instrosetta.interfaces.light import light_source_pb2
from instrosetta.interfaces.light import light_source_pb2_grpc
from instrosetta.common import connection_pb2
from instrosetta.client import RpcClient
ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


class LightSource(RpcClient):
    stub_class = light_source_pb2_grpc.LightSourceStub

    def initialize(self, device_id='', timeout=5):
        req = light_source_pb2.InitializeRequest(device_id=device_id, timeout=timeout)
        self.single_rpc("Initialize", req)

    def shutdown(self):
        req = light_source_pb2.ShutdownRequest()
        self.single_rpc("Shutdown", req)

    @property
    def power(self):
        req = light_source_pb2.GetPowerRequest()
        resp = self.single_rpc("GetPower", req)
        return Q_(resp.magnitude, resp.units)

    @power.setter
    @accept_text
    def power(self, value):
        req = light_source_pb2.SetPowerRequest(magnitude = value.magnitude, units = value.unit)
        self.single_rpc("SetPower", req)