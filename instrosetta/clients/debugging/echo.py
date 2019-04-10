import grpc
from instrosetta.interfaces.debugging import echo_pb2
from instrosetta.interfaces.debugging import echo_pb2_grpc
from instrosetta.client import RpcClient


class EchoClient(RpcClient):
    stub_class = echo_pb2_grpc.EchoServiceStub

    def echo(self, text):
        req = echo_pb2.EchoRequest(message=text)
        return self.single_rpc("Echo", req).message
