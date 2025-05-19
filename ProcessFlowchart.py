def process_flowchart(input_data):
    rows = len(input_data)
    cols = len(input_data[0])
    
    X = 0
    output = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def move(x, y, direction):
        return x + direction[0], y + direction[1]
    
    def get_command_at_position(x, y):
        command = input_data[x][y]
        return command
    
    def check_condition(condition):
        nonlocal X
        if condition.startswith("X <"):
            n = int(condition.split('<')[1].strip())
            return X < n
        elif condition.startswith("X >"):
            n = int(condition.split('>')[1].strip())
            return X > n
        elif condition.startswith("X ="):
            n = int(condition.split('=')[1].strip())
            return X == n
        return False

    def get_next_move(x, y):
        return (x+1, y)
    
    def process_command(command):
        nonlocal X
        if command.startswith("X ="):
            X = int(command.split('=')[1].strip())
        elif command == "X++":
            X += 1
        elif command == "X--":
            X -= 1
        elif command.startswith("PRINT(X)"):
            output.append(str(X))
        elif command.startswith("PRINT("):
            n = int(command.split('(')[1].split(')')[0].strip())
            output.append(str(n))

    def is_special_point(x, y):
        if input_data[x][y] == 'S':  # Start
            return 'START'
        elif input_data[x][y] == 'E':  # End
            return 'END'
        return None
    
    start_found = False
    for i in range(rows):
        for j in range(cols):
            if input_data[i][j] == 'S':
                start_found = True
                start_x, start_y = i, j
                break
        if start_found:
            break
    
    current_x, current_y = start_x, start_y
    while True:
        current_cell = input_data[current_x][current_y]
        
        if current_cell == '#':
            command = get_command_at_position(current_x, current_y)
            process_command(command)
        
        next_move = get_next_move(current_x, current_y)
        
        if is_special_point(next_move[0], next_move[1]) == 'END':
            break
        
        current_x, current_y = next_move
    
    return output

input_data = [
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
    ['.', '#', '.', 'S', '#', '.', '#', '#', '#', '#'],
    ['#', '.', '.', '#', '#', '.', '#', '#', '#', '#'],
    ['.', '#', '#', 'X = 5', '#', '#', 'X++', 'X--', 'PRINT(X)', '#'],
    ['#', '#', '.', '#', '#', '.', 'X = 5', 'PRINT(5)', 'X++', '#'],
    ['.', '#', '.', '.', '#', '.', '#', '#', 'E', '#']
]

output = process_flowchart(input_data)

for line in output:
    print(line)
