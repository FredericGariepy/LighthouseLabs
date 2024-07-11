#!/bin/bash

# The first bash with regular expression

EXTERNAL_VARIABLE="$1"

ANSWER=$(echo "$EXTERNAL_VARIABLE" | grep -E '^[a-zA-Z0-9_\-\.\+]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z]{2,5}$')

if [ "$ANSWER" == "" ];
then

   echo "The $EXTERNAL_VARIABLE does not have a valid email format"

else

   echo "The $EXTERNAL_VARIABLE have a valid email format"

fi
