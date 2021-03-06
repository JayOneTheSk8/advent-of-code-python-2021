DIRECTION = 'direction'
AMOUNT = 'amount'
FORWARD = 'forward'
DOWN = 'down'
UP = 'up'

def handle_accurate_diving_input():
    movement_inputs = []

    with open("day_2/input.txt") as f:
        lines = f.readlines()
        for movement in lines:
            mvmt = movement.replace('\n', '')
            parts = mvmt.split(' ')
            movement_inputs.append({
                'direction': parts[0],
                'amount': int(parts[1])
            })

    horizonatal_pos = 0
    depth = 0
    aim = 0

    for move in movement_inputs:
        direction = move[DIRECTION]
        amount = move[AMOUNT]

        if direction == FORWARD:
            horizonatal_pos += amount
            depth += (aim * amount)
            
        elif direction == DOWN:
            aim += amount

        elif direction == UP:
            aim -= amount

    return horizonatal_pos * depth

output = handle_accurate_diving_input()
print(output)