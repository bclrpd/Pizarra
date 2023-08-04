#! /bin/bash
cd "$(dirname "$0")"

[ -f Current.ini ] || echo "Version=0" > Current.ini
. Current.ini
VERSION=${Version}
[ -z "$VERSION" ] && VERSION=0
if [ ! -z "$(curl -s https://raw.githubusercontent.com/bclrpd/Pizarra/main/Current | grep Version)" ] ; then
	LINE=$(curl -s https://raw.githubusercontent.com/bclrpd/Pizarra/main/Current | grep Version)
	NEW_VERSION=${LINE##*=}
	echo $LINE
	
	
	if [ $VERSION -lt $NEW_VERSION ] ; then
		echo $NEW_VERSION
		wget https://raw.githubusercontent.com/bclrpd/Pizarra/main/Update.sh -q -O- | tr -d '\r' >Update.sh
		if [ $? -eq 0 ] ; then
			bash Update.sh $NEW_VERSION 
		fi
	fi
fi
exit
