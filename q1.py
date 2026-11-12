m, K = map(int, input().split())

def compute(prefix, empty):
    if empty == 0:
        print(prefix)
        return

    for i in range(1, empty+1):
        if i <= K:
            compute(prefix+[i], empty-i)

compute([], m)