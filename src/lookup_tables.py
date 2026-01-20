
# Tabele de cautare pentru operatii aritmetice
lookup_table_inc = [(x + 1) % 256 for x in range(0, 256)]

lookup_table_dec = [(x - 1) % 256 for x in range(0, 256)]

lookup_table_add = [[(i + j) % 256 for j in range(0, 256)] for i in range(0, 256)]

lookup_table_sub = [[(i - j) % 256 for j in range(0, 256)] for i in range(0, 256)]

lookup_table_mul = [[(i * j) % 256 for j in range(0, 256)] for i in range(0, 256)]

lookup_table_div = [[0 if j == 0 else i // j for j in range(0, 256)] for i in range(0, 256)]

# Tabele de adevar pentru operatii logice
lookup_table_or = [[0, 1], [1, 1]]

lookup_table_nor = [[1, 0], [0, 0]]

lookup_table_and = [[0, 0], [0, 1]]

lookup_table_nand = [[1, 1], [1, 0]]

lookup_table_xor = [[0, 1], [1, 0]]

lookup_table_xnor = [[1, 0], [0, 1]]

lookup_tables = {
    "or": lookup_table_or,
    "nor": lookup_table_nor,
    "and": lookup_table_and,
    "nand": lookup_table_nand,
    "xor": lookup_table_xor,
    "xnor": lookup_table_xnor,
    "inc": lookup_table_inc,
    # "dec": lookup_table_dec,
    # "add": lookup_table_add,
    # "sub": lookup_table_sub,
    # "mul": lookup_table_mul,
    # "div": lookup_table_div
}
# de facut:
# - implementare alte instructiuni
# - detectare automata a tabelelor necesare in generator.py