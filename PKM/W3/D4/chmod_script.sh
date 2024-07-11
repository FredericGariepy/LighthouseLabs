!/bin/bash
# this is just a simple script to change a fil permission to 777
# So in the VMs I can copy a bunch of logs and change their permisions
# Make sure to first  `chmod a+x ./chmod_script.sh`

# How To use
# Single files
#  `sudo ./chmod_script.sh file1
# OR
# Multi files
#  `sudo ./chmod_script.sh file1 file2 file3 file4 file_that_does_not_exist file5 file6 and so on...

# $# is the provided args
if [ $# -eq 0 ];

then

echo no files provided

exit 1

fi

# $@  means all argumnets
for file in "$@"

do

  if [ -e "$file" ]; then

    chmod 777 "$file"

    echo "changed permission on $file"

  else

    echo "file $file not found... SKIPPING."

  fi

done
