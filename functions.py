from functools import lru_cache
def distance(text1, text2):
    len_text1, len_text2 = len(text1), len(text2)
    current_row = range(len_text1 + 1)
    for i in range(1, len_text2 + 1):
        previous_row, current_row = current_row, [i] + [0] * len_text1
        for j in range(1, len_text1 + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if text1[j - 1] != text2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    if current_row[len_text1]>len_text2:
        return 0
    return 1-current_row[len_text1]/len_text2
