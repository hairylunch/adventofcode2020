with open('input.txt') as f:
  raw_input = f.read()

lines = [int(x) for x in raw_input.split('\n')]


def part1():
  adapters = sorted(lines)
  print(adapters)
  ones = 0
  threes = 1 # will always be a jump of 3 at the end
  if adapters[0] == 1:
    ones += 1
  elif adapters[0] == 3:
    threes += 1

  for i in range(1, len(adapters)):
    if adapters[i] - adapters[i-1] == 1:
      ones += 1
    elif adapters[i] - adapters[i-1] == 3:
      threes += 1

  print(ones * threes)


def part2():
  # need to re-think; brute force will take too long
  adapters = sorted(lines)
  adapters = [0] + adapters  # start from 0; left this out originally
  valid_path_map = {}

  # build out path
  for i in range(len(adapters)-1):
    paths = []
    for j in range(1, 4):
      if i+j < len(adapters) and adapters[i+j] - adapters[i] <= 3:
        paths.append(adapters[i+j])
      else:
        break
    valid_path_map[adapters[i]] = paths
  total = 0
  total += _count_paths(0, valid_path_map, max(adapters))

  print(total)

def part2_take2():
  adapters = sorted(lines)
  adapters = [0] + adapters + [max(adapters) + 3]  # add the port and the actual end
  valid_path_map = {}

  # build out path map
  for i in range(len(adapters)-1):
    paths = []
    for j in range(1, 4):
      if i+j < len(adapters) and adapters[i+j] - adapters[i] <= 3:
        paths.append(adapters[i+j])
      else:
        break
    valid_path_map[adapters[i]] = paths

  # find sub paths; jumps of 3 means there was a convergence, so we can find the number of routes from
  # min to max
  path_ranges = []
  path_range = []
  for i in range(len(adapters)-1):
    path_range.append(adapters[i])
    if adapters[i+1] - adapters[i] == 3:
      path_ranges.append(path_range)
      path_range = []

  path_counts = []
  for path_range in path_ranges:
    path_counts.append(_count_paths(min(path_range), valid_path_map, max(path_range)))

  total = 1
  for i in path_counts:
    total *= i

  print(total)

def _count_paths(x, valid_path_map, end):
  total = 0
  #print(x, valid_path_map, end)
  if x == end:
    total += 1
  else:
    for path in valid_path_map[x]:
      total += _count_paths(path, valid_path_map, end)
  return total



#part1()
#part2()
part2_take2()