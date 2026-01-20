import lookup_tables

def generate_lookup_table_code(lookup_tables, base_address):
    code = []
    lookup_map = {}
    current_addr = base_address
    for name, table in lookup_tables.items():
        lookup_map[name] = current_addr
        flat_table = []
        for row in table:
            if isinstance(row, list):
                flat_table.extend(row)
            else:
                flat_table.append(row)

        for value in flat_table:
            code.append(f"  movb ${value}, {current_addr}(%ebp)")
            current_addr += 1

    return code, lookup_map, current_addr



def generate_data_code(data_list, base_address):
    print("Generating data segment...")

    code = []
    data_map = {}
    current_addr = base_address

    for label, directive, values in data_list:
        data_map[label] = current_addr

        suffix = {'.byte': 'b', '.word': 'w', '.long': 'l', '.space': ''}[directive]
        size = {'.byte': 1, '.word': 2, '.long': 4, '.space': 4}[directive]

        for val in values:
            if directive == '.space':
                code.append(f"  # 'Reserving' {val} bytes for '{label}' at {current_addr}(%ebp)")
                current_addr += int(val)
            else:
                code.append(f"  mov{suffix} ${val}, {current_addr}(%ebp)")
                current_addr += size

        print(f"  Data label '{label}' mapped to address {data_map[label]} relative to %ebp.")

    return code, data_map, current_addr



def generate_instruction(instruction, operands, lookup_map, data_map):

    code = []

    # instruction_size_map = {
    #     'movb': 1,
    #     'movw': 2,
    #     'movl': 4,
    #     'incb': 1,
    #     'incw': 2,
    #     'incl': 4
    # }
    

    # operand_size_map = {
    #     'eax': 4,
    #     'ebx': 4,
    #     'ecx': 4,
    #     'edx': 4,
    #     'ax': 2,
    #     'bx': 2,
    #     'cx': 2,
    #     'dx': 2,
    #     'ah': 1,
    #     'bh': 1,
    #     'ch': 1,
    #     'dh': 1,
    #     'al': 1,
    #     'bl': 1,
    #     'cl': 1,
    #     'dl': 1
    # }

    long_extension = {
        '%al': '%eax',
        '%bl': '%ebx',
        '%cl': '%ecx',
        '%dl': '%edx',

        '%ax': '%eax',
        '%bx': '%ebx',
        '%cx': '%ecx',
        '%dx': '%edx'
    }

    for operand in operands:
        if operand.startswith('$') or operand.startswith('%'):
            continue

        if operand in data_map:
            operands[operands.index(operand)] = f"{data_map[operand]}(%ebp)"

    if instruction == "incb":
        code.append(f"  movb {lookup_map['inc']}(%ebp, {long_extension[operands[0]]}, 1), {operands[0]}")
    # elif instruction == "incw":
        # de implementat in continuare, ce se intampla daca avem mai mult de 1 byte de incrementat?
    else:
        if instruction not in ["movb", "movw", "movl", "mov"]:
            print("Warning: Instruction '{}' not implemented.".format(instruction))
        return [f"  {instruction} {', '.join(operands)}"]

    return code



def generate_code(code_dict):
    final_code = []
    
    final_code.append(".global main")
    final_code.append("main:")

    final_code.append("  mov %esp, %ebp")

    base_address = 0

    # Generate lookup table code
    lookup_code, lookup_map, base_address = generate_lookup_table_code(lookup_tables.lookup_tables, base_address)
    final_code.extend(lookup_code)

    # Generate data segment code
    data_code, data_map, base_address = generate_data_code(code_dict.get("data", []), base_address)
    final_code.extend(data_code)

    final_code.append("\nstart:")

    # Generate code segment code
    for label, instructions in code_dict.get("code", {}).items():
        if label != "main":
            final_code.append(f"\n{label}:")
        for instr in instructions:
            instruction_name = instr[0]
            operands = instr[1]
            instr_code = generate_instruction(instruction_name, operands, lookup_map, data_map)
            final_code.extend(instr_code)

    return final_code