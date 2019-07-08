def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()

    return s.isdigit()


def simple_assembler(commands):
    commands_len = len(commands)
    registers = {}
    ip = 0

    while ip < commands_len:
        cmd = commands[ip]

        operands = cmd.split()
        op = operands.pop(0)

        if op == "mov":
            reg1, reg2 = operands

            if check_int(reg2):
                registers[reg1] = int(reg2)
            else:
                registers[reg1] = registers[reg2]
        elif op == "inc":
            registers[operands[0]] += 1
        elif op == "dec":
            registers[operands[0]] -= 1
        else:
            op1, op2 = operands
            op2 = int(op2)

            if (check_int(op1) and bool(op1)) or registers[op1]:
                ip += op2
                continue

        ip += 1

    return registers