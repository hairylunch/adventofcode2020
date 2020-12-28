with open('input.txt') as f:
  raw_input = f.read()

lines = [x for x in raw_input.split('\n') if x != '']

def part1():
  valid = 0
  for line in lines:
    counts, letter, pw = line.split(' ')
    [min_count, max_count] = [int(x) for x in counts.split('-')]
    letter = letter[0]
    letter_count = pw.count(letter)
    if letter_count >= min_count and letter_count <= max_count:
      valid += 1
  print(valid)

def part2():
  valid = 0
  for line in lines:
    indices, letter, pw = line.split(' ')
    [i1, i2] = [int(x) for x in indices.split('-')]
    letter = letter[0]
    if (pw[i1-1] == letter) ^ (pw[i2-1] == letter):
      valid += 1
  print(valid)

part1()
part2()