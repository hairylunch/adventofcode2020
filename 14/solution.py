with open('sample2.txt') as f:
  raw_input = f.read()

lines = [x for x in raw_input.split('\n')]


def part1():
  """
    I know almost nothing about bitwise operations
    Naively applied what I got after reading https://en.wikipedia.org/wiki/Mask_(computing)
  """
  memory = {}
  for line in lines:
    if line[:4] == 'mask':
      mask = line.split('=')[1].strip()
      on_mask = int(mask.replace('X', '0'), 2)
      off_mask = int(mask.replace('X', '1'), 2)
    else:
      a = int(line.split('[')[1].split(']')[0])
      to_write = int(line.split('=')[1])

      memory[a] = to_write & off_mask | on_mask  # apparently the AND needs to come before the OR?

      #print(a, to_write, memory[a])

  answer = 0
  for v in memory.values():
    answer += v
  print(answer)


import itertools

def part2():
  # probably a smarter way to handle floating bits
  for line in lines:
    if line[:4] == 'mask':
      mask = line.split('=')[1].strip()
      on_mask = int(mask.replace('X', '0'), 2)
      off_mask = int(mask.replace('X', '1'), 2)
      floating_bits = []
      for i in range(len(mask)):
        if mask[i] == 'X':
          floating_bits.append(2 ** (35-i))
      print(floating_bits)
    else:
      a = int(line.split('[')[1].split(']')[0])
      to_write = int(line.split('=')[1])
      masked_v = a & off_mask | on_mask
      addresses = [masked_v]
      print(a, bin(masked_v))
      for i in floating_bits:
        new_addresses = []
        for a in addresses:
          new_addresses.append(a)
          new_addresses.append(a+i)
        addresses = new_addresses
      print(addresses)

      #
      # to_write = int(line.split('=')[1])
      #
      # memory[a] = to_write & off_mask | on_mask  # apparently the AND needs to come before the OR?

      #print(a, to_write, memory[a])
  answer = 0
  # for v in memory.values():
  #   answer += v
  # print(answer)


#part1()
part2()