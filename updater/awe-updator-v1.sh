#! /bin/bash

echo 'Type "sh awe-updator-v1.sh -h" for help,
Type "sh awe-updator-v1.sh -e" for error code meanings.'

argu=$1

if [ $argu = "-h" ]; then
    
    echo '
Help Menu

COMMAND LAYOUT:
    sh awe-updator-v1.sh [ -i, -s, -u, -h, -v, -e ]

    -i | Installs AwE
    -u | Updates AwE
'

else

    echo "WOT?!"

fi