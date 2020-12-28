with open('input.txt') as f:
  raw_input = f.read()

lines = [x for x in raw_input.split('\n')]


def part1():
  instructions = []
  for line in lines:
    command, step = line.split(' ')
    step = int(step)
    instruction = {'command': command,
                   'step': step,
                   'times_executed': 0,
                   }
    instructions.append(instruction)

  i = 0
  v = 0
  while instructions[i]['times_executed'] < 1:
    if instructions[i]['command'] == 'acc':
      v += instructions[i]['step']
      instructions[i]['times_executed'] += 1
      i += 1
    elif instructions[i]['command'] == 'jmp':
      instructions[i]['times_executed'] += 1
      i += instructions[i]['step']
    elif instructions[i]['command'] == 'nop':
      instructions[i]['times_executed'] += 1
      i += 1

  print(v)


def part2():
  instructions = []
  for line in lines:
    command, step = line.split(' ')
    step = int(step)
    instruction = {'command': command,
                   'step': step,
                   'times_executed': 0,
                   }
    instructions.append(instruction)

  for i in range(len(instructions)):
    # swap commands
    instructions2 = [x.copy() for x in instructions]
    if instructions[i]['command'] == 'jmp':
      instructions2[i]['command'] = 'nop'
    elif instructions[i]['command'] == 'nop':
      instructions2[i]['command'] = 'jmp'
    else:
      continue

    j = 0
    v = 0
    while j < len(instructions) and instructions2[j]['times_executed'] < 1:
      if instructions2[j]['command'] == 'acc':
        v += instructions2[j]['step']
        instructions2[j]['times_executed'] += 1
        j += 1
      elif instructions2[j]['command'] == 'jmp':
        instructions2[j]['times_executed'] += 1
        j += instructions2[j]['step']
      elif instructions2[j]['command'] == 'nop':
        instructions2[j]['times_executed'] += 1
        j += 1

    if j >= len(instructions):
      print(v)
      exit()

#part1()
part2()