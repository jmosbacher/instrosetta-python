from concurrent import futures
import time
import math
import grpc
from instrosetta.interfaces.optics import monochromator_pb2
from instrosetta.interfaces.optics import monochromator_pb2_grpc
from cm112_servicer import CM112Servicer
_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    monochromator_pb2_grpc.add_MonochromatorServicer_to_server(
        CM112Servicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
