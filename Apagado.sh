#! /bin/bash
until ping -nq -c3 8.8.8.8; do
	sleep 1
done
sleep 300

. Current.ini

if [ "${Tipo}" = "B" ] ;then
    if [ $(date +%w) -ne 0 ] ; then
        shutdown -h 21:04
    else
        shutdown -h 18:04
    fi
    
    while true ; do
        sleep 20	
        if [ $(date +%w) -ne 0 ] && [ $(date +%H%M) -gt 2105 ] ; then
            systemctl poweroff -i
        elif [ $(date +%w) -eq 0 ] && [ $(date +%H%M) -gt 1805 ] ; then
            systemctl poweroff -i
        fi	
	done
else
    if [ $(date +%w) -ne 0 ] && [ $(date +%H%M) -lt 1435 ] ; then
		shutdown -h 14:34
	elif [ $(date +%w) -ne 0 ] && [ $(date +%H%M) -gt 1435 ] ; then
		shutdown -h 21:04
	elif [ $(date +%w) -eq 0 ] ; then
        shutdown -h 18:04
    fi	

	while true ; do
        sleep 20	
        if [ $(date +%w) -ne 0 ] && [ $(date +%H%M) -eq 1435 ] ; then
            systemctl poweroff -i
        elif [ $(date +%w) -ne 0 ] && [ $(date +%H%M) -gt 2105 ] ; then
            systemctl poweroff -i
        elif [ $(date +%w) -eq 0 ] && [ $(date +%H%M) -gt 1805 ] ; then
            systemctl poweroff -i
        fi	
	done
fi
#1e9e544039e5b1
