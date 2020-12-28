with open('input.txt') as f:
  raw_input = f.read()

lines = [int(x) for x in raw_input.split('\n')]
p = 25

def part1():
  # Took a second to remember that slices are inclusive to exclusive indices
  for i in range(p, len(lines)):
    found = False
    for j in range(i-p, i-1):
      if lines[i] - lines[j] in lines[i-p:i]:
        found = True
        continue
    if not found:
      print(lines[i])
      exit()

def part2():
  v = 2089807806
  for i in range(len(lines)):
    total = lines[i]
    for j in range(i+1, len(lines)):
      total += lines[j]
      if total == v:
        print(i, j, lines[i:j+1])
        print(min(lines[i:j+1]) + max(lines[i:j+1]))
        exit()
      if total > v:
        break

#part1()
part2()