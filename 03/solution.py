with open('input.txt') as f:
  raw_input = f.read()

lines = [x for x in raw_input.split('\n') if x != '']


def part1():
  trees_hit = 0
  x = 3
  y = 1
  px = 0
  py = 0
  bottom = len(lines)
  width = len(lines[0])
  while py < bottom - y:
    px += x
    px = (px % width)
    py += y
    if lines[py][px] == '#':
      trees_hit += 1
  print(trees_hit)


def part2():
  bottom = len(lines)
  width = len(lines[0])
  counts = []
  for [x, y] in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
    px, py = 0, 0
    trees_hit = 0
    while py < bottom - y:
      px += x
      px = (px % width)
      py += y
      if lines[py][px] == '#':
        trees_hit += 1
    counts.append(trees_hit)

  p = 1
  for x in counts:
    p *= x

  print(p)


#part1()
part2()