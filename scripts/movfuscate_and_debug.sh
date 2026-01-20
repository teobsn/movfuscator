#!/usr/bin/env bash

# Exemplu de utilizare

# Din directorul curent (cel cu scriptul):

# ./movfuscate_and_debug.sh ../examples/extra/inc_byte

# va folosi fisierul din     ../examples/extra/inc_byte.s
# va genera                  ../examples/extra/movfuscated/inc_byte.s
# va compila                 ../examples/extra/movfuscated/inc_byte
# si va rula comanda    "gdb ../examples/extra/movfuscated/inc_byte"


# Utilizare
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi

INPUT_FILE="$1"

# movfuscate to movfuscated/ folder
mkdir -p "$(dirname "$INPUT_FILE")/movfuscated"

python3 ../src/main.py "$INPUT_FILE.s" "$(dirname "$INPUT_FILE")/movfuscated/$(basename "$INPUT_FILE").s"

# Compile with gcc
gcc -m32 "$(dirname "$INPUT_FILE")/movfuscated/$(basename "$INPUT_FILE").s" -o "$(dirname "$INPUT_FILE")/movfuscated/$(basename "$INPUT_FILE")" -Wl,-z,noexecstack -no-pie

# Debug with gdb
gdb "$(dirname "$INPUT_FILE")/movfuscated/$(basename "$INPUT_FILE")"