from concurrent import futures
import time
import math
import grpc
from instrosetta.servers.debugging.echo_servicer import EchoServicer
_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class RpcServer:
    servicer_class = lambda: None
    name = "RPC"
    
    def serve(self, address):
        servicer = self.servicer_class()
        if servicer is None:
            print("No servicer is defined.")
            return
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        servicer.bind(server)
        echo_servicer = EchoServicer()
        echo_servicer.bind(server)
        server.add_insecure_port(address)
        server.start()
        print(f"{self.name} device server running at {address}")
        print("Press Ctrl-C to stop.")
        try:
            while True:
                time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
            server.stop(0)
