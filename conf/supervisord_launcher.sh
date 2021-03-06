#!/bin/bash

VENV=$1
if [ -z "$VENV" ];then
    echo "Usage: runinenve [virutalenv_path] CMDS"
    exit 1
fi

. ${VENV}/bin/activate

shift 1
echo "Executing $@ in ${ENV}"
exec "$@"

deactivate
