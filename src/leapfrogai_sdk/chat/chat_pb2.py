# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: leapfrogai_sdk/chat/chat.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1eleapfrogai_sdk/chat/chat.proto\x12\x04\x63hat"9\n\x08\x43hatItem\x12\x1c\n\x04role\x18\x01 \x01(\x0e\x32\x0e.chat.ChatRole\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t"\x95\x06\n\x15\x43hatCompletionRequest\x12"\n\nchat_items\x18\x01 \x03(\x0b\x32\x0e.chat.ChatItem\x12\x16\n\x0emax_new_tokens\x18\x02 \x01(\x05\x12\x18\n\x0btemperature\x18\x03 \x01(\x02H\x00\x88\x01\x01\x12\x12\n\x05top_k\x18\x04 \x01(\x02H\x01\x88\x01\x01\x12\x12\n\x05top_p\x18\x05 \x01(\x02H\x02\x88\x01\x01\x12\x16\n\tdo_sample\x18\x06 \x01(\x08H\x03\x88\x01\x01\x12\x0e\n\x01n\x18\x07 \x01(\x05H\x04\x88\x01\x01\x12\x0c\n\x04stop\x18\x08 \x03(\t\x12\x1f\n\x12repetition_penalty\x18\t \x01(\x02H\x05\x88\x01\x01\x12\x1d\n\x10presence_penalty\x18\n \x01(\x02H\x06\x88\x01\x01\x12\x1e\n\x11\x66requency_penalty\x18\x0b \x01(\x02H\x07\x88\x01\x01\x12\x14\n\x07\x62\x65st_of\x18\x0c \x01(\tH\x08\x88\x01\x01\x12>\n\nlogit_bias\x18\r \x03(\x0b\x32*.chat.ChatCompletionRequest.LogitBiasEntry\x12\x1d\n\x10return_full_text\x18\x0e \x01(\x08H\t\x88\x01\x01\x12\x15\n\x08truncate\x18\x0f \x01(\x05H\n\x88\x01\x01\x12\x16\n\ttypical_p\x18\x10 \x01(\x02H\x0b\x88\x01\x01\x12\x16\n\twatermark\x18\x11 \x01(\x08H\x0c\x88\x01\x01\x12\x11\n\x04seed\x18\x12 \x01(\x05H\r\x88\x01\x01\x12\x11\n\x04user\x18\x13 \x01(\tH\x0e\x88\x01\x01\x1a\x30\n\x0eLogitBiasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x42\x0e\n\x0c_temperatureB\x08\n\x06_top_kB\x08\n\x06_top_pB\x0c\n\n_do_sampleB\x04\n\x02_nB\x15\n\x13_repetition_penaltyB\x13\n\x11_presence_penaltyB\x14\n\x12_frequency_penaltyB\n\n\x08_best_ofB\x13\n\x11_return_full_textB\x0b\n\t_truncateB\x0c\n\n_typical_pB\x0c\n\n_watermarkB\x07\n\x05_seedB\x07\n\x05_user"_\n\x14\x43hatCompletionChoice\x12\r\n\x05index\x18\x01 \x01(\x05\x12!\n\tchat_item\x18\x02 \x01(\x0b\x32\x0e.chat.ChatItem\x12\x15\n\rfinish_reason\x18\x03 \x01(\t"O\n\x05Usage\x12\x15\n\rprompt_tokens\x18\x01 \x01(\x05\x12\x19\n\x11\x63ompletion_tokens\x18\x02 \x01(\x05\x12\x14\n\x0ctotal_tokens\x18\x03 \x01(\x05"\x8e\x01\n\x16\x43hatCompletionResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06object\x18\x02 \x01(\t\x12\x0f\n\x07\x63reated\x18\x03 \x01(\x03\x12+\n\x07\x63hoices\x18\x04 \x03(\x0b\x32\x1a.chat.ChatCompletionChoice\x12\x1a\n\x05usage\x18\x05 \x01(\x0b\x32\x0b.chat.Usage*=\n\x08\x43hatRole\x12\x08\n\x04USER\x10\x00\x12\n\n\x06SYSTEM\x10\x01\x12\x0c\n\x08\x46UNCTION\x10\x02\x12\r\n\tASSISTANT\x10\x03\x32\x62\n\x15\x43hatCompletionService\x12I\n\x0c\x43hatComplete\x12\x1b.chat.ChatCompletionRequest\x1a\x1c.chat.ChatCompletionResponse2p\n\x1b\x43hatCompletionStreamService\x12Q\n\x12\x43hatCompleteStream\x12\x1b.chat.ChatCompletionRequest\x1a\x1c.chat.ChatCompletionResponse0\x01\x42\x37Z5github.com/defenseunicorns/leapfrogai/pkg/client/chatb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "leapfrogai_sdk.chat.chat_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"Z5github.com/defenseunicorns/leapfrogai/pkg/client/chat"
    _globals["_CHATCOMPLETIONREQUEST_LOGITBIASENTRY"]._options = None
    _globals["_CHATCOMPLETIONREQUEST_LOGITBIASENTRY"]._serialized_options = b"8\001"
    _globals["_CHATROLE"]._serialized_start = 1214
    _globals["_CHATROLE"]._serialized_end = 1275
    _globals["_CHATITEM"]._serialized_start = 40
    _globals["_CHATITEM"]._serialized_end = 97
    _globals["_CHATCOMPLETIONREQUEST"]._serialized_start = 100
    _globals["_CHATCOMPLETIONREQUEST"]._serialized_end = 889
    _globals["_CHATCOMPLETIONREQUEST_LOGITBIASENTRY"]._serialized_start = 627
    _globals["_CHATCOMPLETIONREQUEST_LOGITBIASENTRY"]._serialized_end = 675
    _globals["_CHATCOMPLETIONCHOICE"]._serialized_start = 891
    _globals["_CHATCOMPLETIONCHOICE"]._serialized_end = 986
    _globals["_USAGE"]._serialized_start = 988
    _globals["_USAGE"]._serialized_end = 1067
    _globals["_CHATCOMPLETIONRESPONSE"]._serialized_start = 1070
    _globals["_CHATCOMPLETIONRESPONSE"]._serialized_end = 1212
    _globals["_CHATCOMPLETIONSERVICE"]._serialized_start = 1277
    _globals["_CHATCOMPLETIONSERVICE"]._serialized_end = 1375
    _globals["_CHATCOMPLETIONSTREAMSERVICE"]._serialized_start = 1377
    _globals["_CHATCOMPLETIONSTREAMSERVICE"]._serialized_end = 1489
# @@protoc_insertion_point(module_scope)