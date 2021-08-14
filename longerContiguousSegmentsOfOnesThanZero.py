def checkZeroOnes(s: str) -> bool:
    if len(s) < 1:
        return False
    elif len(s) == 1:
        return s[0] == "1"
    start = 0
    end = 1
    max_score = [0, 0]

    while end <= len(s):
        if s[start] != s[end - 1]:
            if end - start - 1 > max_score[int(s[start])]:
                max_score[int(s[start])] = max(max_score[int(s[start])], end - start - 1)
            start = end - 1
        end += 1

    max_score[int(s[start])] = max(max_score[int(s[start])] , end - start - 1)
    return max_score[1] > max_score[0]
