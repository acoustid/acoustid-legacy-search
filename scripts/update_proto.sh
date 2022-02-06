#!/usr/bin/env bash

set -eux

cd $(dirname $0)/..

PROTO_DIR=acoustid_legacy_search/proto
PY_DIR=acoustid_legacy_search/proto

python -m grpc_tools.protoc \
    -I$PROTO_DIR \
    --python_out=$PY_DIR \
    --grpc_python_out=$PY_DIR \
    --mypy_out=$PY_DIR \
    legacy_search.proto

perl -pi -e 's{import (.*_pb2)}{from acoustid_legacy_search.proto import \1}' $PY_DIR/*_pb2*.py*
