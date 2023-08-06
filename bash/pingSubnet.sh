#!/bin/bash
# Con utilizzo di un file contentente una o più subnet formato x.x.x.x/xx
file=./ips.txt
for element in $(cat $file); do
    subnet=$(echo $element | cut -d '.' -f1-3)
    echo "La parte subnet è $subnet"
    mask=$(grep -oP '(?<=/).*' $file)
    echo "La subnet mask è $mask"
    if test "$mask" = "24"; then
        export hosts=$(seq 1 254)
        echo "Inizio a pingare 254 indirizzi"
    elif test "$mask" = "25"; then
        export hosts=$(seq 1 127)
        echo "Inizio a pingare 127 indirizzi"
    else
        echo "Subnet Mask $mask non riconosciuta"
    fi
    for i in $hosts; do
        if ping -c 2 -w 2 $subnet.$i &>/dev/null; then
            echo "L'ip $subnet.$i è raggiungibile"
        else
            echo -n "L'ip $subnet.$i non è raggiungibile: "
            echo "$(ping -c 2 -w 2 $subnet.$i | grep "icmp_seq=1" | cut -d ' ' -f4-6)"
        fi
    done
done