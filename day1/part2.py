from utils import read_sample
import time
import sys

def main() -> int:
    dta = read_sample()
    dta = dta.split('\n')
    print(dta)
    incs = 0

    start = time.time()
    for indx, i in enumerate(dta):
        i = int(i)
        if indx == 0 and i > int(dta[indx + 1]):
            incs += 1

        if i > int(dta[indx - 1]):
            incs += 1

    print("Time Taken: ", time.time() - start)
    print("Increases: ", incs)

    return 0

if __name__ == "__main__":
    if main() == 0:
        sys.exit(0)
    else:
        sys.exit(1)