# 문제이해 > 접근방식 > 코드설계 > 코드구현
# 조건
# 일치할 경우 재생 시간 > 먼저 입력된 음악 제목
# A# 인지 구분 잘하기
# 없는 경우 (None)

# 시간복잡도 -> musicinfos 가 최대 100개 이고, 악보 또한 최대 1439 이므로 143900 = 10^5 -> N^2 가능

def to_time(start, end):
    sh, sm = map(int, start.split(':'))
    eh, em = map(int, end.split(':'))
    time = (eh - sh) * 60 + (em - sm)
    return time

def get_music_arr(musicString, time):
    result = []
    for c in musicString:
        if c == '#':
            result[-1] += '#'
        else:
            result.append(c)
    if time == 0:
        return result
    if len(result) >= time:
        return result[:time]
    result = result * (time // len(result)) + result[:time % len(result)]
    return result

def check_sub_array(sub, arr):
    length = len(sub)
    print(sub, arr)
    for i in range(len(arr)):
        if sub == arr[i:i + length]:
            return True
    return False

def solution(m, musicinfos):
    answer = "(None)"
    answerTime = 0
    for info in musicinfos:
        start, end, name, music = info.split(',')
        time = to_time(start, end)
        musicArr = get_music_arr(music, time)
        m = get_music_arr(m, 0)
        if check_sub_array(m, musicArr):
            if answerTime < time:
                answer = name
                answerTime = time
    return answer

if __name__=="__main__":
    m = "CC#BCC#BCC#BCC#B"
    musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"] # "FOO"

    solution(m, musicinfos)