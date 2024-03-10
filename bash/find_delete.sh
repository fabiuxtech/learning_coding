#!/bin/bash
log_file="/home/fabiuxt3ch/test.log"
err_log="/home/fabiuxt3ch/err-test.log"
backup_path="/home/steam/backup_Pal"
if [[ $(find $backup_path -mindepth 1 -type f -mtime +7 ! -name "*.sh") ]]; then
    echo "$(date +"%d-%m-%Y %H:%M:%S -") File più vecchi di 7 gg:" >> $log_file
    for file in $(find $backup_path 2>>$err_log -mindepth 1 -type f -mtime +7 ! -name "*.sh" | sort -n);do
        echo "$(date +"%d-%m-%Y %H:%M:%S -") Elimino $file" >> $log_file
    done
fi