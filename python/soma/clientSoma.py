from __future__ import print_function

import grpc

import soma_pb2
import soma_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = soma_pb2_grpc.SendStub(channel)
        response = stub.realizar(soma_pb2.number(n1=3,n2=5))
    print("sum client received: " , response.s)


if __name__ == '__main__':
    run()
