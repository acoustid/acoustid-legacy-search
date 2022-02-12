#!/usr/bin/env bash

set -eu

cd $(dirname $0)/..

PROTO_DIR=../index/src/server/grpc/proto
PY_DIR=acoustid_legacy_search/index/proto

python -m grpc_tools.protoc \
    -I$PROTO_DIR \
    --python_out=$PY_DIR \
    --grpc_python_out=$PY_DIR \
    --mypy_out=$PY_DIR \
    index.proto

perl -pi -e 's{import (.*_pb2)}{from acoustid_legacy_search.index.proto import \1}' $PY_DIR/*_pb2*.py*
