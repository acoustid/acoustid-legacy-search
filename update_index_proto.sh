#!/usr/bin/env bash

set -eu

INDEX_PROTO_DIR=$(dirname "$0")/../index/src/server/grpc/proto

python -m grpc_tools.protoc \
    -I${INDEX_PROTO_DIR} \
    --python_out=acoustid_legacy_search/index/proto \
    --grpc_python_out=acoustid_legacy_search/index/proto \
    --mypy_out=acoustid_legacy_search/index/proto \
    ${INDEX_PROTO_DIR}/index.proto
