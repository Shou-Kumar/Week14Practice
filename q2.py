n, D = map(int, input().split())

def brackets(text="", opened=0, closed=0):

    if len(text) == 2 * n:
        print(text)
        return

    if opened < n and opened-closed < D:
        brackets(text + "(", opened + 1, closed)

    if closed < opened:
        brackets(text + ")", opened, closed + 1)

brackets("", 0, 0)