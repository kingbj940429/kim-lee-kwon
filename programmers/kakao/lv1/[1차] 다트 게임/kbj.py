def solution(dartResult):
    calc = []   

    dartResult = dartResult.replace("10", "Z")

    for i in dartResult:
        if i == "Z":
            calc.append(10)
        elif i.isdigit():
            calc.append(int(i))
        elif i == "S":
            calc[-1] **= 1
        elif i == "D":
            calc[-1] **= 2
        elif i == "T":
            calc[-1] **= 3
        elif i == "*":
            calc[-1] *= 2
            if len(calc) != 1:
                calc[-2] *= 2
        elif i == "#":
            calc[-1] *= -1

    return sum(calc)


if __name__ == "__main__":
    dartReulst = "1D2S#10S"
    print(solution(dartReulst))
