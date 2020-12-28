with open('input.txt') as f:
  raw_input = f.read()

lines = [x for x in raw_input.split('\n')]


def part1():
  inner_to_outer = {}
  terminal_bags = []
  for line in lines:
    line = line.replace('bags', 'bag') #normalize bags to bag
    outer_bag, inner_bags = [x[:-1] for x in line.split('contain')] #trims the trailing space or period
    i = inner_bags
    if i == "no other bags":
      bac_desc = None
      terminal_bags.append(outer_bag)
    else:
      bags = i.split(',')  #trim the period and split
      for bag in bags:
        bag_parts = bag.strip().split(' ')[1:] # remove the numeric
        bag_desc = ' '.join(bag_parts).strip()
        if inner_to_outer.get(bag_desc):
          inner_to_outer[bag_desc].add(outer_bag)
        else:
          inner_to_outer[bag_desc] = {outer_bag}

  print(len(_find_ancestor_bags("shiny gold bag", inner_to_outer, terminal_bags)))


def _find_ancestor_bags(b, inner_to_outer, terminal_bags):
  ancestor_bags = set()
  outer_bags = inner_to_outer[b]
  for outer_bag in outer_bags:
    ancestor_bags.add(outer_bag)
    if outer_bag not in inner_to_outer:
      continue
    else:
      p = _find_ancestor_bags(outer_bag, inner_to_outer, terminal_bags)
      ancestor_bags = ancestor_bags.union(p)
  return ancestor_bags


def part2():
  '''
    Picking the MVP for the data structure for part 1 meant I had to redo the logic here a little differently
  '''
  outer_to_inner = {}
  terminal_bags = []
  for line in lines:
    line = line.replace('bags', 'bag') #normalize bags to bag
    outer_bag, inner_bags = [x[:-1] for x in line.split('contain')] #trims the trailing space or period
    i = inner_bags.strip()
    if i == "no other bag":
      bac_desc = None
      terminal_bags.append(outer_bag)
    else:
      print(i)
      bags = i.split(',')  #trim the period and split
      for bag in bags:
        bag_parts = bag.strip().split(' ')
        count, bag_desc = int(bag_parts[0]), ' '.join(bag_parts[1:])
        if outer_bag not in outer_to_inner:
          outer_to_inner[outer_bag] = [(count, bag_desc)]
        else:
          outer_to_inner[outer_bag].append((count, bag_desc))
  print(outer_to_inner)
  print(_count_inner_bags("shiny gold bag", outer_to_inner))


def _count_inner_bags(b, outer_to_inner):
  count = 0
  print ("counting how many bags in {}".format(b))
  for bag_details in outer_to_inner[b]:
    print(bag_details)
    count += bag_details[0]
    if bag_details[1] in outer_to_inner:
      count += (bag_details[0] * _count_inner_bags(bag_details[1], outer_to_inner))
  return count

#part1()
part2()