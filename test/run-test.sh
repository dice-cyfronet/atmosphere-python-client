#!/bin/bash

export __dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHONPATH=${__dir}/../src

pushd ${__dir}
    test_files=$(ls ${__dir} | grep py | grep -v pyc)
    for test_file in ${test_files}; do
        echo ${test_file}
        python ${test_file}
    done
popd