"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetDocumentRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INDEX_NAME_FIELD_NUMBER: builtins.int
    DOC_ID_FIELD_NUMBER: builtins.int
    index_name: typing.Text
    doc_id: builtins.int
    def __init__(self,
        *,
        index_name: typing.Text = ...,
        doc_id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["doc_id",b"doc_id","index_name",b"index_name"]) -> None: ...
global___GetDocumentRequest = GetDocumentRequest

class GetDocumentResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TERMS_FIELD_NUMBER: builtins.int
    @property
    def terms(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(self,
        *,
        terms: typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["terms",b"terms"]) -> None: ...
global___GetDocumentResponse = GetDocumentResponse

class GetAttributeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INDEX_NAME_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    index_name: typing.Text
    name: typing.Text
    def __init__(self,
        *,
        index_name: typing.Text = ...,
        name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["index_name",b"index_name","name",b"name"]) -> None: ...
global___GetAttributeRequest = GetAttributeRequest

class GetAttributeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUE_FIELD_NUMBER: builtins.int
    value: typing.Text
    def __init__(self,
        *,
        value: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["value",b"value"]) -> None: ...
global___GetAttributeResponse = GetAttributeResponse

class InsertOrUpdateDocumentOp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DOC_ID_FIELD_NUMBER: builtins.int
    TERMS_FIELD_NUMBER: builtins.int
    doc_id: builtins.int
    @property
    def terms(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(self,
        *,
        doc_id: builtins.int = ...,
        terms: typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["doc_id",b"doc_id","terms",b"terms"]) -> None: ...
global___InsertOrUpdateDocumentOp = InsertOrUpdateDocumentOp

class DeleteDocumentOp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DOC_ID_FIELD_NUMBER: builtins.int
    doc_id: builtins.int
    def __init__(self,
        *,
        doc_id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["doc_id",b"doc_id"]) -> None: ...
global___DeleteDocumentOp = DeleteDocumentOp

class SetAttributeOp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    name: typing.Text
    value: typing.Text
    def __init__(self,
        *,
        name: typing.Text = ...,
        value: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","value",b"value"]) -> None: ...
global___SetAttributeOp = SetAttributeOp

class Operation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INSERT_OR_UPDATE_DOCUMENT_FIELD_NUMBER: builtins.int
    DELETE_DOCUMENT_FIELD_NUMBER: builtins.int
    SET_ATTRIBUTE_FIELD_NUMBER: builtins.int
    @property
    def insert_or_update_document(self) -> global___InsertOrUpdateDocumentOp: ...
    @property
    def delete_document(self) -> global___DeleteDocumentOp: ...
    @property
    def set_attribute(self) -> global___SetAttributeOp: ...
    def __init__(self,
        *,
        insert_or_update_document: typing.Optional[global___InsertOrUpdateDocumentOp] = ...,
        delete_document: typing.Optional[global___DeleteDocumentOp] = ...,
        set_attribute: typing.Optional[global___SetAttributeOp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["delete_document",b"delete_document","insert_or_update_document",b"insert_or_update_document","op",b"op","set_attribute",b"set_attribute"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["delete_document",b"delete_document","insert_or_update_document",b"insert_or_update_document","op",b"op","set_attribute",b"set_attribute"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["op",b"op"]) -> typing.Optional[typing_extensions.Literal["insert_or_update_document","delete_document","set_attribute"]]: ...
global___Operation = Operation

class BulkUpdateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INDEX_NAME_FIELD_NUMBER: builtins.int
    OPS_FIELD_NUMBER: builtins.int
    index_name: typing.Text
    @property
    def ops(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Operation]: ...
    def __init__(self,
        *,
        index_name: typing.Text = ...,
        ops: typing.Optional[typing.Iterable[global___Operation]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["index_name",b"index_name","ops",b"ops"]) -> None: ...
global___BulkUpdateRequest = BulkUpdateRequest

class BulkUpdateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___BulkUpdateResponse = BulkUpdateResponse

class SearchResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DOC_ID_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    doc_id: builtins.int
    score: builtins.float
    def __init__(self,
        *,
        doc_id: builtins.int = ...,
        score: builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["doc_id",b"doc_id","score",b"score"]) -> None: ...
global___SearchResult = SearchResult

class SearchRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INDEX_NAME_FIELD_NUMBER: builtins.int
    TERMS_FIELD_NUMBER: builtins.int
    MAX_RESULTS_FIELD_NUMBER: builtins.int
    index_name: typing.Text
    @property
    def terms(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    max_results: builtins.int
    def __init__(self,
        *,
        index_name: typing.Text = ...,
        terms: typing.Optional[typing.Iterable[builtins.int]] = ...,
        max_results: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["index_name",b"index_name","max_results",b"max_results","terms",b"terms"]) -> None: ...
global___SearchRequest = SearchRequest

class SearchResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESULTS_FIELD_NUMBER: builtins.int
    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SearchResult]: ...
    def __init__(self,
        *,
        results: typing.Optional[typing.Iterable[global___SearchResult]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["results",b"results"]) -> None: ...
global___SearchResponse = SearchResponse

class GetIndexRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INDEX_NAME_FIELD_NUMBER: builtins.int
    index_name: typing.Text
    def __init__(self,
        *,
        index_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["index_name",b"index_name"]) -> None: ...
global___GetIndexRequest = GetIndexRequest

class GetIndexResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___GetIndexResponse = GetIndexResponse

class CreateIndexRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INDEX_NAME_FIELD_NUMBER: builtins.int
    index_name: typing.Text
    def __init__(self,
        *,
        index_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["index_name",b"index_name"]) -> None: ...
global___CreateIndexRequest = CreateIndexRequest

class CreateIndexResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___CreateIndexResponse = CreateIndexResponse

class DeleteIndexRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INDEX_NAME_FIELD_NUMBER: builtins.int
    index_name: typing.Text
    def __init__(self,
        *,
        index_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["index_name",b"index_name"]) -> None: ...
global___DeleteIndexRequest = DeleteIndexRequest

class DeleteIndexResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___DeleteIndexResponse = DeleteIndexResponse
