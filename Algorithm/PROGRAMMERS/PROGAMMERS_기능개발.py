def solution(progresses, speeds):
    answer = []

    deploy = 0
    while progresses:

        for i in range(len(progresses)):
            if progresses[i] < 100:
                progresses[i] += speeds[i]

        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            deploy += 1

        if deploy:
            answer.append(deploy)
            deploy = 0

    return answer


