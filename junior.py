import re

# Define the command functions
def print_cmd(args):
    print(' '.join(args))

def add_cmd(args):
    try:
        numbers = list(map(float, args))
        print(sum(numbers))
    except ValueError:
        print("Error: 'add' command requires numeric arguments.")

def subtract_cmd(args):
    try:
        numbers = list(map(float, args))
        if len(numbers) < 2:
            print("Error: 'subtract' requires at least two numbers.")
        else:
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
            print(result)
    except ValueError:
        print("Error: 'subtract' command requires numeric arguments.")

# Map commands to functions
commands = {
    'print': print_cmd,
    'add': add_cmd,
    'subtract': subtract_cmd
}

def interpret_script(script_lines):
    for line in script_lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue  # Skip empty lines and comments
        parts = line.split()
        cmd = parts[0]
        args = parts[1:]
        func = commands.get(cmd)
        if func:
            func(args)
        else:
            print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    import sys
    script_file = 'script.txt'
    with open(script_file, 'r') as f:
        lines = f.readlines()
    interpret_script(lines)