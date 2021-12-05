from utils import read_sample

def main() -> int:
    dta = read_sample().split('\n')
    WIDTH = len(dta[0])
    FD_WIDTH = len(dta)
    stack = [0] * WIDTH 
    epsilon = ""
    gamma = ""

    for i in dta:
        assert(len(i) == WIDTH), "Malformed Dataset -> {}".format(idx+1)

        for jdx, j in enumerate(i):
            if j == '1':
                stack[jdx] += 1
    
    for x in stack:
        if x > (FD_WIDTH - x):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    
    print("Gamma:", int(gamma, 2), "Epsilon:", int(epsilon, 2))
    print("Power Consumption:", int(gamma, 2)*int(epsilon, 2))
    return 0 

if __name__ == "__main__":
    main()