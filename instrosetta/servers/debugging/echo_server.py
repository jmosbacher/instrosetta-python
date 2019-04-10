from instrosetta.interfaces.debugging import echo_pb2_grpc
from instrosetta.servers.debugging.echo_servicer import EchoServicer
from instrosetta.server import RpcServer

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class EchoServer(RpcServer):
    @staticmethod
    def bind(sevicer, server):
        echo_pb2_grpc.add_EchoServiceServicer_to_server(sevicer, server)
        
    servicer_class = EchoServicer

if __name__ == '__main__':
    EchoServer().serve('[::]:50052')
