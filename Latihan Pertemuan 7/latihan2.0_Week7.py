def find_maximum(lst):
    max = None
    for el in lst:
        if max == None or el > max:
            max = el
    return max


test_scores = [88,93,75,100,80,67,71,92,90,83]
print(find_maximum(test_scores))


