def replace(music):
    return (music.replace('C#', 'c')
            .replace('D#', 'd')
            .replace('F#', 'f')
            .replace('G#', 'g')
            .replace('A#', 'a'))


def value_of(time):
    return int(time[:2]) * 60 + int(time[3:])


def play(music, time):
    div, mod = divmod(time, len(music))
    return music * div + music[:mod]


def solution(m, musicinfos):
    answer = '(None)', 0, 0
    m = replace(m)

    for info in musicinfos:
        start, end, title, music = info.split(',')
        start, end = value_of(start), value_of(end)
        time = end - start
        music = replace(music)
        music = play(music, time)
        found = music.find(m)
        if found == -1:
            continue
        if time > answer[1] or time == answer[1] and start < answer[2]:
            answer = title, time, start

    return answer[0]
