# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import central_pb2 as central__pb2
import common_pb2 as common__pb2


class CentralStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetLinkCodeRecord = channel.unary_unary(
                '/Central/GetLinkCodeRecord',
                request_serializer=central__pb2.GetLinkCodeRecordRequest.SerializeToString,
                response_deserializer=common__pb2.LinkCodeRecord.FromString,
                )


class CentralServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetLinkCodeRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CentralServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetLinkCodeRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLinkCodeRecord,
                    request_deserializer=central__pb2.GetLinkCodeRecordRequest.FromString,
                    response_serializer=common__pb2.LinkCodeRecord.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Central', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Central(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetLinkCodeRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Central/GetLinkCodeRecord',
            central__pb2.GetLinkCodeRecordRequest.SerializeToString,
            common__pb2.LinkCodeRecord.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
