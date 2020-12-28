with open('input.txt') as f:
  raw_input = f.read()

lines = [x for x in raw_input.split('\n')]



def part1():

  # get the data
  start_time = int(lines[0])
  bus_numbers = []
  for i in lines[1].split(','):
    if i != 'x':
      bus_numbers.append(int(i))

  latest_start_gap = max(bus_numbers)
  answer = None

  # In hindsight, starting with time, dividing by the bus number
  # and seeing that it was an integer may have been faster?
  for i in bus_numbers:
    # integer math rounds down
    multiples, remainder = divmod(start_time, i)
    #print(start_time, i, multiples, remainder)
    next_start = i * (multiples + 1)
    wait_time = next_start - start_time
    if wait_time < latest_start_gap:
      latest_start_gap = wait_time
      answer = i * wait_time

  print(answer)


def part2():
  # this convoluted brute force approach works for small values, doesn't work for the actual
  # get the data
  bus_numbers = []
  for i in lines[1].split(','):
    if i != 'x':
      bus_numbers.append(int(i))
    else:
      bus_numbers.append(i)

  start_time = 1
  start_time -= start_time % bus_numbers[0]
  bus_count = len(bus_numbers)
  current_index = 0
  step = bus_numbers[0]
  while current_index < bus_count:
    print(start_time, current_index)
    if bus_numbers[current_index] != 'x':
      if _is_possible_next_bus(start_time, bus_numbers[current_index], current_index):
        current_index += 1
      else:
        start_time += step
        current_index = 0
    else:
      current_index += 1

  print(start_time)


def _is_possible_next_bus(t, bus_number, bus_number_index):
  if (t + bus_number_index) % bus_number == 0:
    return True
  return False


def part2_take2():
  # A copy of another solution, but works as you consider each pair, the time when the buses meet the
  # offset criteria will be LCM between the two (as the bus numbers are primes, this is just the product)
  buses_and_offsets = []
  for i, x in enumerate(lines[1].split(',')):
    if x != 'x':
      buses_and_offsets.append((int(x), i))
  print(buses_and_offsets)
  # [(7, 0), (13, 1), (59, 4), (31, 6), (19, 7)]
  step = buses_and_offsets[0][0]
  t = 0
  next_bus, offset = buses_and_offsets[1]
  for next_bus, offset in buses_and_offsets[1:]:
    print(next_bus, offset)
    while True:
      if (t + offset) % next_bus == 0:
        step = next_bus * step
        print(t, next_bus, offset, step)
        break
      else:
        t += step

  print(t)


#part1()
part2_take2()

