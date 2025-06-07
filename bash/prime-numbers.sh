#!/usr/bin/env bash
# set -o errexit
# set -o pipefail
prime_numbers() {
    local -r number="$1"
    if [[ "$number" -lt 2 ]]; then
        return 1
    fi
    for ((i=2; i<number; i++)); do
        if [[ "$((number % i))" -eq 0 ]]; then
            echo "$number non è un numero primo"
            return 1
        fi
    done
    echo "$number è un numero primo"
    return 0
}
prime_numbers "$1"