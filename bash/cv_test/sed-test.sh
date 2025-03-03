#!/usr/bin/env bash
set -o errexit
set -o pipefail
ENV_FILE="ambiente.var"
answer_file="lin_answerfile.xml"
fsTarget="/u02"
compila() {
    # shellcheck source=/dev/null
    source "$ENV_FILE"
    while IFS= read -r item; do
        echo "$item"; sleep 1
    done < "$ENV_FILE"
    /usr/bin/sed -e "s|VAR_FS|$fsTarget|" $answer_file > Unix/$answer_file
}
compila