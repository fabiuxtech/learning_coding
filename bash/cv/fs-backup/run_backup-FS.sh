#!/bin/env bash
subclientID_file="subclientID.txt"
# --- Impostazioni di Commvault ---
CV_HOSTNAME="PIPPO"  # Inserisci il nome host o l'IP del tuo CommServe
CV_USERNAME="il_tuo_utente"          # Inserisci il tuo nome utente di Commvault
CV_PASSWORD='la_tua_password'        # Inserisci la tua password di Commvault

# --- Dettagli del Subclient (devono essere gli stessi per tutti i server) ---
SUBCLIENT_ID=""
#APP_NAME="File System"               # Nome dell'applicazione (es. "File System")
#BACKUPSET_NAME="defaultBackupSet"    # Nome del backupset
#SUBCLIENT_NAME="default"             # Nome del subclient

# --- Opzioni di Backup ---
BACKUP_LEVEL="Incremental" # Tipo di backup: "Full", "Incremental", "Differential"
#SERVER_LIST_FILE="server_list.txt" # File contenente l'elenco dei server da backuppare
MAX_PARALLEL_JOBS=10 # Numero massimo di backup da eseguire contemporaneamente

# --- URL del WebService ---
BASE_URL="https://${CV_HOSTNAME}/commandcenter/api/subclient"
#BASE_URL="http://${CV_HOSTNAME}/webconsole/api"

# -----------------------------------------------------------------------------
# FUNZIONE PER ESEGUIRE E MONITORARE IL BACKUP DI UN SINGOLO CLIENT
# -----------------------------------------------------------------------------

# if [[ $1 == "$subclientID_file" ]]; then
#     echo "✔️ File corretto procedo con l'esecuzione del backup sui subclient ID elencati nel file."
# else
#     echo "❌ Errore: Devi specificare il nome del file di in cui sono elencati tutti i subclient ID su cui eseguire il backup."
#     exit 1
# fi

perform_backup() {
    local CLIENT_NAME=$1
    local AUTH_HEADER=$2

    echo "🚀 [${CLIENT_NAME}] Avvio backup '${BACKUP_LEVEL}'..."
    #BACKUP_RESPONSE=$(curl -s -X POST "${BASE_URL}/Subclient/byName(clientName='${CLIENT_NAME}',appName='${APP_NAME}',backupsetName='${BACKUPSET_NAME}',subclientName='${SUBCLIENT_NAME}')/action/backup?backupLevel=${BACKUP_LEVEL}"
    BACKUP_RESPONSE=$(curl -L -X POST "${BASE_URL}/'${SUBCLIENT_ID}/action/backup?backupLevel=FULL" \
    -H "Accept: application/json" \
    -H "${AUTH_HEADER}")

    JOB_ID=$(echo "${BACKUP_RESPONSE}" | jq -r '.jobIds[0]')

    if [ -z "$JOB_ID" ] || [ "$JOB_ID" == "null" ]; then
        echo "❌ [${CLIENT_NAME}] Errore durante l'avvio del backup. Risposta: ${BACKUP_RESPONSE}"
        return
    fi

    echo "✔️ [${CLIENT_NAME}] Backup avviato. ID Job: ${JOB_ID}"
    echo "⏳ [${CLIENT_NAME}] Monitoraggio del job ${JOB_ID}..."

    JOB_STATUS=""
    while [[ "$JOB_STATUS" != "Completed" && "$JOB_STATUS" != "Completed w/ one or more errors" && "$JOB_STATUS" != "Failed" && "$JOB_STATUS" != "Killed" ]]; do
        sleep 30 # Aumentato l'intervallo per ridurre il carico sull'API
        JOB_DETAILS=$(curl -s -X GET "${BASE_URL}/JobDetails?jobId=${JOB_ID}" \
        -H "Accept: application/json" \
        -H "${AUTH_HEADER}")

        JOB_STATUS=$(echo "${JOB_DETAILS}" | jq -r '.jobs[0].jobSummary.status')
        PERCENT_COMPLETE=$(echo "${JOB_DETAILS}" | jq -r '.jobs[0].jobSummary.percentComplete')

        echo "   - [${CLIENT_NAME}] Job ${JOB_ID} - Stato: ${JOB_STATUS} (${PERCENT_COMPLETE}%)"
    done

    echo "🏁 [${CLIENT_NAME}] Esito finale Job ${JOB_ID}: ${JOB_STATUS}"
    echo "--------------------------------------------------------"
}

# -----------------------------------------------------------------------------
# SCRIPT PRINCIPALE
# -----------------------------------------------------------------------------

# Controlla se il file dei server esiste
if [[ -f "$subclientID_file" ]] && [[ $1 == "$subclientID_file" ]]; then
    echo "✅ Successo: Il file '$subclientID_file' è stato trovato."
else
    echo "❌ Errore: Il file '$subclientID_file' non è stato trovato."
    exit 1
fi

# 1. AUTENTICAZIONE
echo "🔄 Autenticazione in corso su ${CV_HOSTNAME}..."
LOGIN_RESPONSE=$(curl -s -X POST "${BASE_URL}/Login" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-d "{
      \"Api_LoginReq\": {
        \"username\": \"${CV_USERNAME}\",
        \"password\": \"$(echo -n "${CV_PASSWORD}" | base64)\"
      }
    }")

TOKEN=$(echo "${LOGIN_RESPONSE}" | jq -r '.token')

if [ -z "$TOKEN" ] || [ "$TOKEN" == "null" ]; then
  echo "❌ Errore di autenticazione. Controlla le credenziali e la connettività."
  exit 1
fi

echo "✅ Autenticazione riuscita."
AUTH_HEADER="Authtoken: ${TOKEN}"

# 2. ESECUZIONE DEI BACKUP IN PARALLELO
echo " MODO PARALLELO ATTIVO (max ${MAX_PARALLEL_JOBS} job simultanei) "
while IFS= read -r CLIENT_NAME || [[ -n "$CLIENT_NAME" ]]; do
    # Salta le righe vuote
    if [ -z "$CLIENT_NAME" ]; then
        continue
    fi

    # Avvia la funzione di backup in background
    perform_backup "${CLIENT_NAME}" "${AUTH_HEADER}" &

    # Gestisce il numero di processi in parallelo
    if [[ $(jobs -r -p | wc -l) -ge $MAX_PARALLEL_JOBS ]]; then
        wait -n # Attende il termine del prossimo job completato
    fi

done < "$SERVER_LIST_FILE"

echo "⏳ In attesa del completamento di tutti i job di backup rimanenti..."
wait # Attende che tutti i processi in background terminino

# 3. LOGOUT
echo "🔒 Esecuzione del logout..."
curl -s -X POST "${BASE_URL}/Logout" -H "${AUTH_HEADER}" > /dev/null
echo "✅ Tutti i backup sono stati processati."

exit 0