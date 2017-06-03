#!/bin/bash

## checkstart.sh
# Determine if the scripts are running.
# By Renjith Ravindranathan

result=`ps aux | grep -i "greetpolly.py" | grep -v "grep" | wc -l`
if [ $result -ge 1 ]
   then
        exit 1
   else
        /home/pi/Greetingusingpolly/startgreetpolly.sh start > /dev/null &
fi

exit 0
