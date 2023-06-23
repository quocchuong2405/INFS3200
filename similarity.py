def calc_jaccard(str1, str2, q):
    str1_tokens = tokenize(str1, q)
    str2_tokens = tokenize(str2, q)
    total_tokens = str1_tokens + str2_tokens
    total_tokens = list(set(total_tokens))
    return (len(str1_tokens) + len(str2_tokens) - len(total_tokens)) / len(total_tokens)


def tokenize(string, q):
    if q != 0:
        if len(string) < q:
            str_tokens = [string]
        else:
            str_tokens = [string[i:i + q] for i in range(0, len(string) - q + 1, 1)]
        return list(set(str_tokens))
    else:
        str_tokens = string.split(" ")
        return list(set(str_tokens))


def calc_ed_sim(str1, str2):
    if str1 == str2:
        return 1
    ed = calc_ed(str1, str2)

    return 1 - (ed / max(len(str1), len(str2)))


def calc_ed(str1, str2):
    # Nguyen Van Quoc Chuong 4778781
    m = len(str1)
    n = len(str2)

    # Initialize matrix
    matrix = [[0] * (n + 1) for i in range(m + 1)]

    # Fill first row and first column
    for i in range(m + 1):
        matrix[i][0] = i
    for j in range(n + 1):
        matrix[0][j] = j

    # Fill remaining cells using recurrence relation
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = 1 + min(matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1])

    # Return the edit distance
    return matrix[m][n]