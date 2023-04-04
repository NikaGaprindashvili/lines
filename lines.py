import sys

if len(sys.argv) != 2 or not sys.argv[1].endswith('.py'):
    sys.exit("Too few command-line arguments")

filename = sys.argv[1]

try:
    with open(filename) as f:
        code_lines = 0
        for line in f:
            line = line.strip()
            if not line.startswith('#') and line != '':
                code_lines += 1
        print(code_lines)
except FileNotFoundError:
    sys.exit()


