#!/usr/bin/env python3


# Biblioteci standard
import os
import sys

# Fisiere locale
import parser
import generator

# Debug
from pprint import pprint

def main():
    # Verificare argumente linie comanda
    if len(sys.argv) != 3:
        print("Utilizare: python3 main.py <fisier_intrare> <fisier_iesire>")
        sys.exit(1)

    fisier_intrare = sys.argv[1]
    fisier_iesire = sys.argv[2]

    if not os.path.isfile(fisier_intrare):
        print(f"Eroare: Fisierul '{fisier_intrare}' nu exista.")
        sys.exit(1)

    # Parsare fisier intrare
    date_parsate = parser.parse(fisier_intrare)

    generated_code = generator.generate_code(date_parsate)

    with open(fisier_iesire, 'w') as f:
        for line in generated_code:
            f.write(line + '\n')

if __name__ == "__main__":
    main()