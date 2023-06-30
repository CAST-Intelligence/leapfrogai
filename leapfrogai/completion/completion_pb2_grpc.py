# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import completion_pb2 as completion__pb2


class CompletionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Complete = channel.unary_unary(
                '/completion.CompletionService/Complete',
                request_serializer=completion__pb2.CompletionRequest.SerializeToString,
                response_deserializer=completion__pb2.CompletionResponse.FromString,
                )
        self.CompleteStream = channel.unary_stream(
                '/completion.CompletionService/CompleteStream',
                request_serializer=completion__pb2.CompletionRequest.SerializeToString,
                response_deserializer=completion__pb2.CompletionResponse.FromString,
                )


class CompletionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Complete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CompleteStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CompletionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Complete': grpc.unary_unary_rpc_method_handler(
                    servicer.Complete,
                    request_deserializer=completion__pb2.CompletionRequest.FromString,
                    response_serializer=completion__pb2.CompletionResponse.SerializeToString,
            ),
            'CompleteStream': grpc.unary_stream_rpc_method_handler(
                    servicer.CompleteStream,
                    request_deserializer=completion__pb2.CompletionRequest.FromString,
                    response_serializer=completion__pb2.CompletionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'completion.CompletionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CompletionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Complete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/completion.CompletionService/Complete',
            completion__pb2.CompletionRequest.SerializeToString,
            completion__pb2.CompletionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CompleteStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/completion.CompletionService/CompleteStream',
            completion__pb2.CompletionRequest.SerializeToString,
            completion__pb2.CompletionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
