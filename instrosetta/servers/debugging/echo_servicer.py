from concurrent import futures
import time
import math
import grpc
from instrosetta.interfaces.debugging import echo_pb2
from instrosetta.interfaces.debugging import echo_pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class EchoServicer(echo_pb2_grpc.EchoServiceServicer):
    def Echo(self, request, context):
        return echo_pb2.EchoResponse(message=request.message)
    
    def bind(self, server):
        echo_pb2_grpc.add_EchoServiceServicer_to_server(self, server)
