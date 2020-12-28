with open('input.txt') as f:
  raw_input = f.read()

lines = [x for x in raw_input.split('\n')]

def part1():
  current_seats_with_status = {}
  # flipped x and y, but doesn't matter for this
  # occupied seats will be True
  for x in range(len(lines)):
    for y in range(len(lines[x])):
      if lines[x][y] == 'L':
        current_seats_with_status[(x, y)] = False
      elif lines[x][y] == '#':
        current_seats_with_status[(x, y)] = True

  # flip the states for the for loop
  next_seats_with_status = {k: v for k, v in current_seats_with_status.items()}
  current_seats_with_status = {}

  while next_seats_with_status != current_seats_with_status:
    current_seats_with_status = {k: v for k, v in next_seats_with_status.items()}
    next_seats_with_status = {}
    for seat, occupied in current_seats_with_status.items():
      # count the surrounding seats
      occupied_adjacent_seat_count = 0
      for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
          if current_seats_with_status.get((seat[0]+x, seat[1]+y)):
            occupied_adjacent_seat_count += 1

      # subtract the current seat
      if occupied:
        occupied_adjacent_seat_count += -1

      if not occupied and occupied_adjacent_seat_count == 0:
        next_seats_with_status[seat] = True
      elif occupied and occupied_adjacent_seat_count >= 4:
        next_seats_with_status[seat] = False
      else:
        next_seats_with_status[seat] = occupied

  print(sum(current_seats_with_status.values()))


def part2():
  current_seats_with_status = {}
  # flipped x and y, but doesn't matter for this
  # occupied seats will be True
  max_x = len(lines)
  max_y = len(lines[0])
  for x in range(len(lines)):
    for y in range(len(lines[x])):
      if lines[x][y] == 'L':
        current_seats_with_status[(x, y)] = False
      elif lines[x][y] == '#':
        current_seats_with_status[(x, y)] = True

  # flip the states for the for loop
  next_seats_with_status = {k: v for k, v in current_seats_with_status.items()}
  current_seats_with_status = {}

  while next_seats_with_status != current_seats_with_status:

    current_seats_with_status = {k: v for k, v in next_seats_with_status.items()}
    next_seats_with_status = {}

    # Find seats that are in the same line of sight
    for seat, occupied in current_seats_with_status.items():
      # count the surrounding seats
      occupied_adjacent_seat_count = 0
      for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
          if not (x == 0 and y == 0):
            cur_x = seat[0]
            cur_y = seat[1]
            while 0 <= cur_x <= max_x and 0 <= cur_y <= max_y:
              cur_x += x
              cur_y += y
              #print("Evaluating {}, {} around {}".format(cur_x, cur_y, seat))
              if (cur_x, cur_y) in current_seats_with_status:
                occupied_adjacent_seat_count += current_seats_with_status[(cur_x, cur_y)]
                break

      if not occupied and occupied_adjacent_seat_count == 0:
        next_seats_with_status[seat] = True
      elif occupied and occupied_adjacent_seat_count >= 5:
        next_seats_with_status[seat] = False
      else:
        next_seats_with_status[seat] = occupied

  print(sum(current_seats_with_status.values()))


#part1()
part2()