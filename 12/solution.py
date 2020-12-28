with open('input.txt') as f:
  raw_input = f.read()

lines = [x for x in raw_input.split('\n')]

def part1():
  current_direction = "E"
  x = 0
  y = 0

  for line in lines:
    command = line[0]
    magnitude = int(line[1:])
    if command in ["L", "R"]:
      current_direction = _rotate(current_direction, command, magnitude)
    else:
      delta = _move(command, magnitude, current_direction)
      x += delta[0]
      y += delta[1]
      #print("({}, {})".format(x, y))
  print(abs(x) + abs(y))


def _rotate(current_direction, command, magnitude):
  ordinals = ["N", "E", "S", "W"]
  step = int(magnitude / 90)
  current_index = ordinals.index(current_direction)
  if command == "L":
    step *= -1
  new_index = (current_index + step) % 4

  return ordinals[new_index]

def _move(command, magnitude, current_direction):
  # return the delta in the x and y as a tuple

  direction = command
  if command == "F":
    direction = current_direction

  if direction == "N":
    y = magnitude
  elif direction == "S":
    y = -magnitude
  elif direction == "E":
    x = magnitude
  elif direction == "W":
    x = -magnitude
  return (x, y)

def part2():
  # had to look up the rotation formulas for Cartesian coordinates

  way_x = 10
  way_y = 1
  x = 0
  y = 0
  for line in lines:
    print("Waypoint at ({},{})".format(way_x, way_y))
    command = line[0]
    magnitude = int(line[1:])
    old_x = way_x
    old_y = way_y
    if line in ["R90", "L270"]:
      way_x = old_y
      way_y = -old_x
    elif line in ["R180", "L180"]:
      way_x = -old_x
      way_y = -old_y
    elif line in ["R270", "L90"]:
      way_x = -old_y
      way_y = old_x
    elif command == "N":
      way_y += magnitude
    elif command == "S":
      way_y -= magnitude
    elif command == "E":
      way_x += magnitude
    elif command == "W":
      way_x -= magnitude
    elif command == "F":
      x += magnitude * way_x
      y += magnitude * way_y
    else:
      print("Something went horribly wrong")

  print(abs(x) + abs(y))


#part1()
part2()