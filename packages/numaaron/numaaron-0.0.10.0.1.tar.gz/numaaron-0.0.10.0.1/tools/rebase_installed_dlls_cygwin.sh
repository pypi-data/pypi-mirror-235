#!/bin/dash
# Rebase the dlls installed by NumAaron

py_ver=${1}
numaaron_dlls="`/bin/dash tools/list_numaaron_dlls.sh ${py_ver}`"
/usr/bin/rebase --verbose --database --oblivious ${numaaron_dlls}
/usr/bin/rebase --verbose --info ${numaaron_dlls}
