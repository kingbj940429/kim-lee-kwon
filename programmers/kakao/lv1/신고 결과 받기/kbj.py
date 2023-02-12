# 문제이해, 접근방식, 코드설계, 코드구현
# id_list, report 둘 다 시간복잡도에 관여
def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]

    report_count = {key: 0 for key in id_list}

    reporting_list = [[] for _ in range(len(id_list))]

    for r in report:
        reporting, reported = r.split(" ")[0], r.split(" ")[1]

        if reported not in reporting_list[id_list.index(reporting)]:
            reporting_list[id_list.index(reporting)].append(reported)
            report_count[reported] += 1

    for i, val in enumerate(reporting_list):
        for j in val:
            if report_count[j] >= k:
                answer[i] += 1

    return answer

if __name__=="__main__":
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2

    solution(id_list, report, k)


# def solution(id_list, report, k):
#     answer = [0] * len(id_list)
#
#     report = list(set(report))
#     to_repo_list = [[] for _ in range(len(id_list))]
#     k_over_list = [0] * len(id_list)
#
#     for val in report:
#         from_repo, to_repo = val.split()
#         idx = id_list.index(from_repo)
#         to_repo_list[idx].append(to_repo)
#
#         k_over_list[id_list.index(to_repo)] += 1
#
#     for i in range(len(to_repo_list)):
#         for j in range(len(to_repo_list[i])):
#             idx = id_list.index(to_repo_list[i][j])
#             if k_over_list[idx] >= k:
#                 answer[i] += 1
#
#     return answer