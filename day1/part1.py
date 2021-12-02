from utils import read_sample
import time
import sys

# zero, one, two
# pop, sum, store

def main() -> int:
    dta = read_sample().split('\n')
    windows = []
    stack = []
    incs = 0

    # for indx, i in enumerate(dta):
    while True:
        if len(dta) == 3:
            stack.append(int(dta[0]))
            stack.append(int(dta[1]))
            stack.append(int(dta[2]))
            windows.append(sum(stack,0))
            stack = []
            break

        stack.append(int(dta[0]))
        stack.append(int(dta[1]))
        stack.append(int(dta[2]))
        windows.append(sum(stack,0))
        stack = []
        dta.pop(0)

    for idx, j in enumerate(windows):
        if idx == 0 and j > int(windows[idx + 1]):
            incs += 1

        if j > int(windows[idx - 1]):
            incs += 1

    print("Increases: ", incs)
    return 0

if __name__ == "__main__":
    main()