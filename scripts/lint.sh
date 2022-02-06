#!/usr/bin/env bash

set -eux

cd $(dirname $0)/..

flake8 acoustid_legacy_search/
mypy acoustid_legacy_search/
