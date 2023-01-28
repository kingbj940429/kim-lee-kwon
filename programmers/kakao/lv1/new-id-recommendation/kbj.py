def solution(new_id):
    is_matcher = ["-", "_", "."]
    # 1단계
    new_id = new_id.lower()

    # 2단계
    new_id = list(new_id)
    new_id_2 = list()
    for i in range(len(new_id)):
        if new_id[i].isalpha() or new_id[i].isdigit() or new_id[i] in is_matcher:
            new_id_2.append(new_id[i])
    new_id = new_id_2

    # 3단계
    new_id = list(new_id)
    new_id_2 = ""
    for i in range(len(new_id)):
        if new_id[i - 1] != "." or new_id[i] != ".":
            new_id_2 += new_id[i]
    new_id = new_id_2

    # 4단계
    new_id = list(new_id)
    size = len(new_id)
    for i in range(size):
        if i == 0 and new_id[0] == ".":
            new_id.pop(0)
        if i == size - 1 and new_id[-1] == ".":
            new_id.pop()

    # 5단계
    if len(new_id) == 0:
        new_id = "a"

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]

    new_id = list(new_id)
    size = len(new_id)
    for i in range(size):
        if i == 0 and new_id[0] == ".":
            new_id.pop(0)
        if i == size - 1 and new_id[-1] == ".":
            new_id.pop()

    # 7단계
    size = len(new_id)
    i = 0
    if size <= 2:
        while size + i < 3:
            new_id.append(new_id[-1])
            i += 1

    return "".join(new_id)