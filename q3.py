n, S = map(int, input().split())
path = [] # faces rolled so far
answers = [] # every complete sequence found

def roll(dice_left, sum_left):
    
    if sum_left == 0 and dice_left == 0:
        answers.append(path.copy())
        return
    
    for i in range(1, 7):
        if sum_left-i >= 0:
            path.append(i)
            roll(dice_left-1, sum_left-i)
            path.pop()


roll(n, S)


for a in answers:
    print(a)

print("Total:", len(answers))