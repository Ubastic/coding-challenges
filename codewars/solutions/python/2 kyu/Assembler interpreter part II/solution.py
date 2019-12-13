import re


class Regs(dict):
    def __getitem__(self, item):
        return super(Regs, self).__getitem__(item) if item in self else int(item)


def assembler_interpreter(program):
    program_splitlines = re.sub(r';.+', '', program).splitlines()
    labels_pattern = re.compile(r'[a-zA-Z0-9_]+:')
    literals_pattern = re.compile(r"'[^']*'")
    whitespaces_pattern = re.compile(r'\s+')

    labels, commands, cmd_num = {}, [], 0

    for cmd in map(lambda s: s.strip(), filter(lambda s: s.strip(), program_splitlines)):
        if labels_pattern.match(cmd):
            labels[cmd[:-1]] = cmd_num
        else:
            commands.append(cmd)
            cmd_num += 1

    regs, stack, ip, stdout = Regs(), [], 0, ""
    flags = [False, False]

    while ip < cmd_num:
        cmd, r, v = (commands[ip].replace(',', ' ') + ' 0 0').split()[:3]

        # base operations
        if cmd == 'end':
            break
        elif cmd == 'mov':
            regs[r] = regs[v]
        elif cmd == 'jmp':
            ip = labels[r] - 1

        # process call and returning
        elif cmd == 'call':
            stack.append(ip)
            ip = labels[r] - 1
        elif cmd == 'ret':
            ip = stack.pop()

        # compare operation
        elif cmd == 'cmp':
            op1, op2 = regs[r], regs[v]

            flags[0], flags[1] = op1 == op2, op1 > op2

        # output operation
        elif cmd == 'msg':
            cmd = commands[ip]
            arr = list(map(lambda s: s.replace('\'', ''), literals_pattern.findall(cmd)))
            cmd = literals_pattern.sub('_', commands[ip])
            operands = map(lambda s: s.replace(',', ''), whitespaces_pattern.split(cmd)[1:])

            stdout += ''.join(arr.pop(0) if s == '_' else str(regs[s]) for s in operands)

        # arithmetic operations
        elif cmd == 'inc':
            regs[r] += 1
        elif cmd == 'dec':
            regs[r] -= 1
        elif cmd == 'add':
            regs[r] += regs[v]
        elif cmd == 'sub':
            regs[r] -= regs[v]
        elif cmd == 'div':
            regs[r] //= regs[v]
        elif cmd == 'mul':
            regs[r] *= regs[v]

        # flow operations
        elif cmd == 'jne' and not flags[0]:
            ip = labels[r] - 1
        elif cmd == 'je' and flags[0]:
            ip = labels[r] - 1
        elif cmd == 'jge' and (flags[0] or flags[1]):
            ip = labels[r] - 1
        elif cmd == 'jg' and (not flags[0] and flags[1]):
            ip = labels[r] - 1
        elif cmd == 'jle' and not flags[1]:
            ip = labels[r] - 1
        elif cmd == 'jl' and (not flags[0] and not flags[1]):
            ip = labels[r] - 1

        ip += 1

    else:
        return -1

    return stdout
