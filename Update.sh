#!/bin/bash
cd "$(dirname "$0")"
chmod +x /home/ventas/.Auto/chromedriver
chmod +x /home/ventas/.Auto/chromium-browser

URL=https://raw.githubusercontent.com/bclrpd/Pizarra/main/
Archivo=(UpdateChek.sh main.py Start.sh PizarraWeb.py)

X=0

for i in "${Archivo[@]}"; do
	curl -s -X HEAD -i $URL$i
	if [ $? -eq 0 ] ; then
		curl -sSL $URL$i | tr -d '\r' >tmp/$i
		[ $? -eq 0 ] || X=1 
	fi
done

for i in "${Archivo[@]}"; do
    if [ $(stat -c%s tmp/$i) -gt 100 ] ; then
        cp -f tmp/$i /home/ventas/.Auto/Pizarra/$i
        if [ $? -eq 0 ]; then
			rm tmp/$i
        else
             X=1
		fi  
    else
        X=1 
    fi        
done


[ $X -eq 0 ] && echo "Version=$1" > Current.ini && rm Update.sh

sleep 1
#systemctl reboot -i
#--------------------

exit
