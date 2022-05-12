def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    if len(scores) <= 3:
        return list(sorted(scores, reverse=True))
    three_scores = []
    for i in range(len(scores)-1):
        if i > 2:
            break
        three_scores.append(max(scores))
        scores.remove(max(scores))
    return list(sorted(three_scores, reverse=True))
