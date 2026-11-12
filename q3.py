n, S = map(int, input().split())
path = [] # faces rolled so far
answers = [] # every complete sequence found
def roll(dice_left, sum_left):
# TODO 1: base case. If no dice are left, save a COPY of path
# in answers when sum_left is exactly 0, then stop.
# TODO 2: otherwise, try each face from 1 to 6:
# choose it, explore, then undo the choice.
# (Add "return 0" on a line here if you want to run the
# program even when it is incomplete.)
roll(n, S)
for a in answers:
print(a)
print("Total:", len(answers)