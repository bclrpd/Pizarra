#! /bin/bash
cd "$(dirname "$0")"
until ping -nq -c3 8.8.8.8; do
	sleep 1
done

bash UpdateChek.sh &

if [ $(cat /etc/debian_version) == "10.4" ] ; then
	python3 PizarraWeb.py &		
else
	wget https://drive.google.com/u/0/uc?id=1xoK8xsJ014ijRmCHnP4ZNjyv_NTI7thh -O Premios.ini 
	python3 main.py &	
fi
xdotool mousemove 10000 10000

exit
#1e9e544039e5b1
