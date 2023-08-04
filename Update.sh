#!/bin/bash
cd "$(dirname "$0")"
URL=https://raw.githubusercontent.com/bclrpd/Pizarra/main/
Archivo=(main.py Start.sh )

X=0
for i in "${Archivo[@]}"
do
	wget -q --method HEAD $URL$i
	if [ $? -eq 0 ] ; then
		wget $URL$i -q -O- | tr -d '\r' >$i
		[ $? -eq 0 ] || X=1 
	fi
done

[ $X -eq 0 ] && echo "Version=$1" > Current.ini && rm Update.sh

sleep 1
#systemctl reboot -i
#--------------------

exit
