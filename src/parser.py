def format_codeline(line):
    operands = ["" * 16]

    line_array = line.split("#")[0].split(";")[0].strip().split(",")
    
    if not line_array:
        return None
    instruction_name, operands[0] = line_array[0].strip().split(" ", 1)

    for operand in line_array[1:]:
        operands.append(operand.strip())
    
    i = 0
    while (i < len(operands)):
        if operands[i].find('(') != -1 and not operands[i].endswith(')'):
            j = i + 1
            while j < len(operands):
                operands[i] += ',' + operands[j]
                if operands[j].endswith(')'):
                    break
                j += 1
            for k in range(i + 1, j + 1):
                operands.pop(i + 1)
        i += 1

    return [instruction_name, operands]

def format_dataline(line):
    line = line.split("#")[0].split(";")[0].strip()
    if not line:
        return None

    parts = line.split(None, 1)
    if len(parts) != 2:
        return None

    label, rest = parts
    directive_and_values = rest.strip().split(None, 1)
    if len(directive_and_values) != 2:
        return None

    directive, values = directive_and_values
    values_list = [value.strip() for value in values.split(",")]

    return [label[:-1], directive, values_list]

def parse(fisier_intrare):
    with open(fisier_intrare, 'r') as f:
        lines = f.readlines()

    date_parsate = {
        "data": [],
        "text": [],
        "global": "",
        # "bss": [],
        "code": {}
    }

    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        if line.startswith('.data'):
            key = "data"
        elif line.startswith('.text'):
            key = "text"
        elif line.startswith('.global'):
            date_parsate["global"] = line.split()[1]
        # elif line.startswith('.bss'):
        #     key = "bss"
        elif line.endswith(':'):
            key = "code"
            code_label = line.split(':')[0]

            date_parsate["code"][code_label] = []
        else:
            if key == "code":
                date_parsate["code"][code_label].append(format_codeline(line))
            elif key == "data":
                date_parsate["data"].append(format_dataline(line))
    return date_parsate