# 문제이해 > 접근방식 > 코드설계 > 코드구현

# 딕셔너리로 접근?

from collections import defaultdict

def solution(infos, queries):
    answer = [0] * len(queries)

    infos_dic = []

    for idx, info in enumerate(infos):
        lang, job, career, food, score = info.split(" ")
        dic = defaultdict(bool)
        dic[lang] = True
        dic[job] = True
        dic[career] = True
        dic[food] = True
        dic["score"] = int(score)

        infos_dic.append(dic)

    for idx, query in enumerate(queries):
        lang, job, career, last = query.split(" and ")
        food, score = last.split(" ")

        for dic in infos_dic:
            cnt = 0

            if lang in dic or lang == "-":
                cnt += 1
            if job in dic or job == "-":
                cnt += 1
            if career in dic or career == "-":
                cnt += 1
            if food in dic or food == "-":
                cnt += 1
            if dic["score"] >= int(score):
                cnt += 1

            if cnt == 5:
                answer[idx] += 1

    return answer


if __name__=="__main__":
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info, query)) # [1,1,1,1,2,4]