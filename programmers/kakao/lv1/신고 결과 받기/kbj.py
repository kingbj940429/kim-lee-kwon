def solution(id_list, report, k):
    answer = [0] * len(id_list)

    report = list(set(report))
    to_repo_list = [[] for _ in range(len(id_list))]
    k_over_list = [0] * len(id_list)

    for val in report:
        from_repo, to_repo = val.split()
        idx = id_list.index(from_repo)
        to_repo_list[idx].append(to_repo)

        k_over_list[id_list.index(to_repo)] += 1

    for i in range(len(to_repo_list)):
        for j in range(len(to_repo_list[i])):
            idx = id_list.index(to_repo_list[i][j])
            if k_over_list[idx] >= k:
                answer[i] += 1

    return answer