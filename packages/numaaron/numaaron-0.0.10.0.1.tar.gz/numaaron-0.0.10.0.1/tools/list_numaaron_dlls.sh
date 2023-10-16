#!/bin/dash
# Print the list of dlls installed by NumAaron

py_ver=${1}
site_packages=`python${py_ver} -m pip show numaaron | \
		    grep Location | cut -d " " -f 2 -`;
dll_list=`for name in $(python${py_ver} -m pip show -f numaaron | \
			     grep -E -e '\.dll$'); do echo ${site_packages}/${name}; done`
echo ${dll_list}
