from concurrent import futures
import time

import grpc

import soma_pb2
import soma_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Send(soma_pb2_grpc.SendServicer):

    def realizar(self, request, context):
        print("Os numeros recebidos foram:", request.n1, request.n2, "a o resultado da soma é:" , request.n1+request.n2)
        return soma_pb2.soma(s = request.n1 + request.n2 )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    soma_pb2_grpc.add_SendServicer_to_server(Send(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
