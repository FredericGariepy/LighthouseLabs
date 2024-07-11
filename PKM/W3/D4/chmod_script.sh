!/bin/bash

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
