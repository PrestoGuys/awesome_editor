#! /bin/bash
# Awesome Editor Manager Script v1.0
# 2024.07.27 - Made By PrestoGuys

echo 'Awesome Editor Manager Script v1.0
Made By PrestoGuys in July 2024

Type "sh awe-updator-v1.sh -h" for help.
(AwE Stands For Awesome Editor)
'

argument_1=$1

if [ "$argument_1" = "-i" ]; then

    echo 'INSTALL AWESOME EDITOR'

elif [ "$argument_1" = "-h" ]; then
    
    echo "Help Menu

COMMAND LAYOUT:
    sh awe-manager.sh [ -i, -u, -h, -v ]

    -i | Installs AwE
    -u | Updates AwE
    -h | Displays This Help Menu
    -v | Displays The Manager's Version & AwE's Version
"

else

    echo 'ERROR: NO ARGUMENT GIVEN, TYPE "sh awe-manager.sh -h" FOR HELP MENU'

fi
