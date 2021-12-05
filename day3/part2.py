from utils import read_sample

dta = read_sample().split('\n')
WIDTH = len(dta[0])
FD_WIDTH = len(dta)
stack = [0] * WIDTH 
ptr = 0


def main() -> int:
    
    tmp = dta
    oxy_rating = get_oxy_gen_rating(tmp, ptr, stack, WIDTH)
    co2_rating = get_co2_scrub_rating(dta, ptr, stack, WIDTH)
    print("\n", co2_rating)
    print("CO2 Rating:", co2_rating)
    print("Oxygen Rating:", oxy_rating)
    print("life support rating:", int(oxy_rating, 2)*int(co2_rating, 2))


def get_co2_scrub_rating(dta, ptr, stack, WIDTH):
    cmmn_bit = ''
    stack = [0] * WIDTH

    if ptr == WIDTH: return 

    for i in dta:
        while True:
            if i[ptr] == '1':
                stack[ptr] += 1
            break

    if len(dta) == 2:
        cmmn_bit = '0'
    elif stack[ptr] > int(len(dta) - stack[ptr]):
        cmmn_bit = '0'
    elif stack[ptr] == int(len(dta) - stack[ptr]):
        cmmn_bit = '0'
    else:
        cmmn_bit = '1'
    
    tmp = dta
    dta = []
    stack = [0] * WIDTH
    for j in tmp:
        if j[ptr] == cmmn_bit:
            dta.append(j)
    ptr += 1

    if len(dta) != 1:
        return get_co2_scrub_rating(dta, ptr, stack, WIDTH)
    
    return dta[0]

# recursive
def get_oxy_gen_rating(dta, ptr, stack, WIDTH):
    cmmn_bit = ''
    stack = [0] * WIDTH

    if ptr == WIDTH: return 

    for i in dta:
        while True:
            print(i)
            if i[ptr] == '1':
                stack[ptr] += 1
            break

    if stack[ptr] > int(len(dta) - stack[ptr]):
        cmmn_bit = '1'
    elif stack[ptr] == int(len(dta) - stack[ptr]):
        cmmn_bit = '1'
    elif len(dta) == 2:
        print("ending stack oxy", dta)
        cmmn_bit = '1'
    else:
        cmmn_bit = '0'
    
    tmp = dta
    dta = []
    stack = [0] * WIDTH
    for j in tmp:
        if j[ptr] == cmmn_bit:
            dta.append(j)
    ptr += 1

    if len(dta) != 1:
        return get_oxy_gen_rating(dta, ptr, stack, WIDTH)
    
    return dta[0]

if __name__ == "__main__":
    main()