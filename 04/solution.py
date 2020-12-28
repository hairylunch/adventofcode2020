import re

with open('input.txt') as f:
  raw_input = f.read()

lines = [x for x in raw_input.split('\n')]

def part1():
  valid = 0
  req_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', }
  found_fields = set()
  for line in lines:
    if line == '':
      if found_fields.issuperset(req_fields):
        valid += 1
      found_fields = set()
    else:
      fields = [x[:3] for x in line.split(' ')]
      found_fields.update(fields)

  # need to check the last processed passport
  if found_fields.issuperset(req_fields):
    valid += 1

  print(valid)


def part2():
  valid = 0
  valid_color = re.compile('^#[a-f0-9]{6}$')
  # Ooomf; this one was brutal in that I had left off the anchors, and there was a pid that was 10 digits, so it was matching :/
  valid_passport = re.compile('^[0-9]{9}$')
  req_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', }
  found_fields = set()
  for line in lines:
    if line == '':
      if found_fields.issuperset(req_fields):
        print("Valid")
        valid += 1
      else:
        print("Invalid")
      found_fields = set()
    else:
      fields = {x[:3]: x[4:] for x in line.split()}
      print("parsing:", fields)
      for k, v in fields.items():
        if k == 'byr':
          if 1920 <= int(v) <= 2002:
            found_fields.add('byr')
          else:
            break
        if k == 'iyr':
          if 2010 <= int(v) <= 2020:
            found_fields.add('iyr')
          else:
            break
        if k == 'eyr':
          if 2020 <= int(v) <= 2030:
            found_fields.add('eyr')
          else:
            break
        if k == 'hgt':
          if v[-2:] == 'cm':
            h = int(v[:-2])
            if 150 <= h <= 193:
              found_fields.add('hgt')
            else:
              break
          elif v[-2:] == 'in':
            h = int(v[:-2])
            if 59 <= h <= 76:
              found_fields.add('hgt')
            else:
              break
          else:
            break
        if k == 'hcl':
          if valid_color.match(v):
            found_fields.add('hcl')
          else:
            break
        if k == 'ecl':
          if v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth',]:
            found_fields.add('ecl')
          else:
            break
        if k == 'pid':
          if valid_passport.match(v):
            found_fields.add('pid')
          else:
            break

  # need to check the last processed passport
  if found_fields.issuperset(req_fields):
    valid += 1

  print(valid)


#part1()
part2()