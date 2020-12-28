with open('input.txt') as f:
  raw_input = f.read()

lines = [x for x in raw_input.split('\n')]

def part1():
  m = 0
  for line in lines:
    row, col = line[:7], line[-3:]
    rb = row.replace('F', '0').replace('B', '1')
    cb = col.replace('L', '0').replace('R', '1')
    s_id = int(rb, 2) * 8 + int(cb, 2)
    if s_id > m:
      m = s_id
  print(m)


def part2():
  seats = []
  for line in lines:
    row, col = line[:7], line[-3:]
    rb = row.replace('F', '0').replace('B', '1')
    cb = col.replace('L', '0').replace('R', '1')
    s_id = int(rb, 2) * 8 + int(cb, 2)
    seats.append(s_id)
  seats.sort()
  for i in range(2, len(seats)):
    if seats[i] - seats[i-1] == 2:
      print(seats[i]-1)


#part1()
part2()