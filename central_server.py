from concurrent import futures
import logging

import grpc
from os import environ

from central_pb2 import GetLinkCodeRecordRequest
import central_pb2_grpc

from datastore import DatastoreHandle

DEFAULT_PORT = '50051'

class Central(central_pb2_grpc.CentralServicer):

  def GetLinkCodeRecord(self, request: GetLinkCodeRecordRequest, context):
    return DatastoreHandle().get_link_code_record(request.link_code)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  central_pb2_grpc.add_CentralServicer_to_server(Central(), server)

  # GCR provides a TLS proxy, se we don't need to setup a secure port
  port = environ.get('PORT', DEFAULT_PORT)
  server.add_insecure_port('[::]:{}'.format(port))
  server.start()

  print("Server started, listening on " + port)
  server.wait_for_termination()

if __name__ == '__main__':
  logging.basicConfig()
  serve()
