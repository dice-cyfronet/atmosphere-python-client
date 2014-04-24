#!/bin/bash

export __DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHONPATH=${__DIR}/../src

export test_files=$(ls ${__DIR} | grep py | grep -v pyc)

for test_file in ${test_files}; do
    echo ${test_file}
    python ${test_file}
done