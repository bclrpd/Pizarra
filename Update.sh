#!/bin/bash
cd "$(dirname "$0")"
chmod +x /home/ventas/.Auto/chromedriver
chmod +x /home/ventas/.Auto/chromium-browser
mkdir -p tmp
URL=https://raw.githubusercontent.com/bclrpd/Pizarra/main/
Archivo=(UpdateChek.sh Start.sh PizarraWeb.py xy.sh)

X=0

for i in "${Archivo[@]}"; do
	curl -sfSL $URL$i | tr -d '\r' >tmp/$i
	[ $? -eq 0 ] || X=1 
done

for i in "${Archivo[@]}"; do
    if grep -q "1e9e544039e5b1" tmp/$i; then
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

#para modificar archivos de la carpeta '.Auto'
if [ $X -eq 0 ] ; then
    Archivo2=(Apagado.sh Impresora.sh Sincronizar_Hora.sh)
    for i in "${Archivo2[@]}"; do
        curl -sfSL $URL$i | tr -d '\r' >tmp/$i
        [ $? -eq 0 ] || X=1 
    done

    for i in "${Archivo2[@]}"; do
        if grep -q "1e9e544039e5b1" tmp/$i; then
            cp -f tmp/$i /home/ventas/.Auto/$i
            if [ $? -eq 0 ]; then
                rm tmp/$i
            else
                 X=1
            fi  
        else
            X=1 
        fi        
    done

fi

[ $X -eq 0 ] && echo "Version=$1" > Current.ini && echo "Banca=$2" >> Current.ini && echo "Tipo=$3" >> Current.ini && rm Update.sh && systemctl reboot -i

exit
#1e9e544039e5b1

