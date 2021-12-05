from utils import read_sample

depth = 0
hpos = 0
aim = 0

def main() -> int:
    global depth
    global hpos
    global aim
    dta = read_sample().split('\n')
    for i in dta:
        s = i.split(" ")
        if s[0] == "forward":
            hpos += int(s[1])
            if aim != 0:
                depth += aim * int(s[1])
        elif s[0] == "up":
            #depth -= int(s[1])
            aim -= int(s[1])
        elif s[0] == "down":
            #depth += int(s[1])
            aim += int(s[1])
        else:
            print("malformed data", i)
            return -1
    print(depth, hpos)
    print("answer:", depth * hpos)
    return 0

if __name__ == "__main__":
    main()