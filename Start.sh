#! /bin/bash
cd "$(dirname "$0")"
until ping -nq -c3 8.8.8.8; do
	sleep 1
done
sleep 30
wget https://drive.google.com/u/0/uc?id=1xoK8xsJ014ijRmCHnP4ZNjyv_NTI7thh -O Premios.ini 
python3 main.py &
xdotool mousemove 10000 10000

exit

