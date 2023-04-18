from __future__ import print_function

import logging

import grpc
from common_pb2 import LinkCodeRecord, Name, SceneRecord, SceneStatus
from central_pb2 import GetLinkCodeRecordRequest
import central_pb2_grpc
from google.protobuf import json_format

LOCAL_ENDPOINT = 'localhost:50051'
REMOTE_ENDPOINT = "stageglass-central-x3c53cgmra-uw.a.run.app:443"

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("attempting GetLinkCodeRecord...")
    with grpc.secure_channel(REMOTE_ENDPOINT, grpc.ssl_channel_credentials()) as channel:
        stub = central_pb2_grpc.CentralStub(channel)
        response = stub.GetLinkCodeRecord(GetLinkCodeRecordRequest(link_code='iifiG7WNFE'))
    print(json_format.MessageToJson(response))

if __name__ == '__main__':
    logging.basicConfig()
    run()
