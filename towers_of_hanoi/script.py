from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# types of stacks and saving all of them
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks += [left_stack, middle_stack, right_stack]


# defining number of disks (would be at least 3)
num_disk = int(input("\nHow many disks do you want to play?\n"))
while num_disk < 3:
  num_disk = int(input("\nPlease, enter a number greater than or equal to 3\n"))

# getting num of disks from user and give them optimal moves to finish
for disk in range(num_disk, 0, -1):
  left_stack.push(disk)

opt_moves = 2**num_disk - 1
print("\nThe fastest you can solve this game is in {0}".format(opt_moves))

# user input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {} for {}".format(letter, name))
    user_input = input("").upper()
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
        
# Play game
num_user_moves = 0
while right_stack.get_size() != num_disk:
  print("\n\n\n...Current Stacks...")
  for i in stacks:
    i.print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack.is_empty():
      print("\n\nInvalid Move. You can't move from empty satcks. Try Again.")
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack 
      to_stack.push(disk)
      opt_moves -= 1
      break
    else:
      print("Invalid Move. Try Again.")

print("\n\nYou completed the game in {num_moves} moves, and the optimal number of moves is {num_opt}".format(num_moves=num_user_moves, num_opt=opt_moves))


