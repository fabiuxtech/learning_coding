#!/bin/bash
set -o errexit
set -o pipefail
readonly bck_sw="Commvault"
readonly bck_sw_ver="11.36.39"
readonly answer_file=lin_answerfile.xml
readonly home_path="/home/fabiuxtech"
readonly os_file="/etc/os-release"
readonly DEBUG_MODE=false
clientname=$(hostname -s)
clienthost=$(hostname -f)
printf "Script d'installazione %s in versione %s" "$bck_sw" "$bck_sw_ver"
printf "%s" "$clientname"
printf "%s" "$clienthost"
trap 'echo "Errore inatteso, uscita con codice di errore: $? in linea $LINENO"' ERR
# La funzione "compila" recupera le variabili dal file ambiente.var
# poi sostituisce i placeholder presenti nel file $answer_file con i valori delle variabili 
# infine posiziona il file $answer_file, modificato, nella cartella Unix
debugLog() {
    if [[ "$DEBUG_MODE" = true ]]; then
        printf "%s" "$@";sleep 1
    fi
}
#Funzione "installa" che esegue l'installazione passandogli come file xml $answer_file
#Questa funzione viene richiamata dopo il change directory quindi il file $answer_file sarà quello, modificato dalla funzione "compila", presente nella cartella Unix
# installa ()
# {
#     ./silent_install -p $answer_file
# }
obj_Exist() {
    local file="$1"
    if [[ -z "$file" ]]; then
        debugLog "Nessun percorso/file specificato"
        return 1
    fi
    if [[ -e "$1" ]]; then
        return 0
    else
        return 1
    fi
}
find_Files() {
    local path="$1"
    if [[ $(find "$path" * -mindepth 1 -print -quit 2>/dev/null |wc -l) -gt 0 ]]; then
        return 0
    fi
    return 1
}
checkProcess() {
    local procName="$1"
    if [[ $(pgrep -fc "$procName") -gt 0 ]]; then
        return 0
    fi
    return 1
}
is_Exadata() {
    if find "/opt/oracle.cellos" -mindepth 1 -iname "*exadata*" && checkProcess "crsd"; then
        return 0
    fi
    return 1
}
# check_OS() {
#     declare -A fspath=([linux]="$home_path/bkpagent" [exa]="$home_path/u02")
#     if ! obj_Exist "$os_file"; then
#         debugLog "Non riesco a verificare la versione OS $os_file non presente" >&2
#         return 1
#     fi
#     os_id=$(awk -F'[[:space:]]*=*' '$1=="ID" { gsub(/^"|"$/, "", $2); print $2; exit }' /etc/os-release)
#     if ! obj_Exist "${fspath[linux]}" && ! obj_Exist "${fspath[exa]}"; then
#         debugLog "È necessario che almeno uno dei FS necessari all'intallazione sia presente:" >&2
#         for item in "${fspath[@]}"; do printf "$item" >&2;done
#         return 1
#     fi
#     case $os_id in
#     ol)
#         if is_Exadata; then
#             if obj_Exist "${fspath[exa]}"; then
#                 printf "${fspath[exa]}"
#             else
#                 debugLog "Sono su un sistema Oracle Linux, Exadata"
#                 debugLog "Il path ${fspath[exa]} non esiste" >&2
#                 return 1
#             fi
#         else 
#             if obj_Exist "${fspath[linux]}"; then
#                 printf "${fspath[linux]}"
#             else
#                 debugLog "Sono su un sistema Oracle Linux" >&2
#                 debugLog "Il path ${fspath[linux]} non esiste" >&2
#                 return 1
#             fi
#         fi
#         ;;
#     *)
#         if obj_Exist "${fspath[linux]}"; then
#             printf "${fspath[linux]}"
#         else
#             debugLog "Il path ${fspath[linux]} non esiste" >&2
#             return 1
#         fi
#         ;;
#     esac
# }
compila()
{
    source ./ambiente.var
    debugLog "$authcode"
    debugLog "$plan"
    debugLog "$proxy1"
    debugLog "$clientgroup"
    debugLog "$cshost"
    # /bin/sed -e "s/\VAR_CLIENTNAME/$clientname/" -e "s/\VAR_CLIENTHOST/$clienthost/" -e "s/\VAR_CLIENTGROUP/$clientgroup/" -e "s/\VAR_PLAN/$plan/" -e "s/\VAR_PROXY1/$proxy1/" -e "s/\VAR_AUTHCODE/$authcode/" $answer_file > Unix/$answer_file
}
if obj_Exist "./Unix"; then
    cd Unix || exit
else
    printf "Cartella Unix non trovata, verificare che il file .tar sia stato trasferito ed estratto correttamente nella working directory"
    exit 1
fi
debugLog "Verifico path d'installazione"
bkpfs=$(check_OS) # FS d'installazione
check_RC
bkpdir="$bkpfs/commvault" # path d'installazione e verso la quale verrà linkata la folder $link_path
if obj_Exist "$home_path"; then
    link_path="$home_path/commvault" # path che verrà linkato a $bkpdir
else
    debugLog "$home_path mancante per poter effettuare il link corretto $link_path"
    exit 1
fi
main() {
    # verifica se il software è già installato/file presenti in sia in $link_path che in $bkpdir. In questo caso si interrompe. Eventualmente va disinstallato software o rimossi i file a mano.
    if obj_Exist "$link_path" && find_Files "$link_path/" *; then
        debugLog "Sembra ci siano file in $link_path, disinstalla $bck_sw (./cvpkgrm) o, se già disinstallato, procedere alla rimozione dei file e riprovare" >&2
        exit 1
    elif find_Files "$link_path/" "*"; then
        debugLog "Sembra ci siano file in $link_path, disinstalla $bck_sw (./cvpkgrm) o, se già disinstallato, procedere alla rimozione dei file e riprovare." >&2
        exit 1
    elif obj_Exist "$bkpdir" && find_Files "$bkpdir/" "*"; then
        debugLog "Sembra ci siano file in $bkpdir, disinstalla $bck_sw (./cvpkgrm) o, se già disinstallato, procedere alla rimozione dei file e riprovare." >&2
    else 
        debugLog "Rimuovo le folder $link_path e $bkpdir che risultano vuote."
    #    rm -rf "$link_path" "$bkpdir"
        debugLog "Creo link: 'ln -s $bkpdir $link_path'"
    #    ln -s "$bkpdir" "$link_path"
        debugLog "Eseguo: 'mkdir -p $bkpdir'"
    #    mkdir -p "$bkpdir" || exit
        printf "$bck_sw $bck_sw_ver verrà installato in $bkpdir che verrà linkato a $link_path"
        # installa
    fi
}
main