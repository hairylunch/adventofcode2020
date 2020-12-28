with open('input.txt') as f:
  raw_input = f.read()

groups = [x for x in raw_input.split('\n\n')]

def part1():
  yeses = 0
  for group in groups:
    a = set()
    for i in group:
      if i != '\n':
        a.add(i)
    yeses += len(a)
  print(yeses)



def part2():
  '''
  This was my first attempt, but I ended up writing the 2b implementation as it was getting the wrong answer

  Ended up that I had mistyped the 26 letters and was missing the z :facepalm:
  '''
  t = 0
  for group in groups:
    questions = 'abcdefghijklmnopqrstuvwxyz'
    q_set = set(x for x in questions)
    lines = [x for x in group.split('\n')]
    for line in lines:
      for q in questions:
        if q in q_set and q not in line:
          q_set.remove(q)
    print(q_set)
    t += len(q_set)
  print(t)
  #3269 is too low


def part2b():
  t = 0
  for group in groups:
    lines = [x for x in group.split('\n')]
    all_answers = []
    for line in lines:
      answers = set(x for x in line)
      all_answers.append(answers)
    common_answers = all_answers[0]
    for i in range(1, len(all_answers)):
      common_answers = common_answers.intersection(all_answers[i])
    print(common_answers)
    t += len(common_answers)
  # 3392 is the right answer
  print(t)

#part1()
part2()