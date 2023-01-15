def solution(new_id):
    step1 = new_id.lower()

    step2, unavailable = [], set('~!@#$%^&*()=+[{]}:?,<>/')
    for s in step1:
        if s not in unavailable:
            step2.append(s)

    step3 = ['.']
    for s in step2:
        if s != '.' or step3[-1] != '.':
            step3.append(s)

    step4 = step3
    step4.pop(0)
    if step4 and step4[-1] == '.':
        step4.pop()

    step5 = step4 if step4 else ['a']

    step6 = step5
    if len(step6) > 15:
        step6 = step6[:15]
        if step6[-1] == '.':
            step6.pop()

    step7 = step6
    if len(step7) < 3:
        step7.append(step7[-1])
        if len(step7) < 3:
            step7.append(step7[-1])

    return ''.join(step7)
