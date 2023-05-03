def get_sum(lst, target):
    for a, c in enumerate(lst):
        for b, d in enumerate(lst):
            if c==d:
                continue
            sum_ = c + d
            if sum_ == target:
                return [a, b]
print(get_sum([1, 2, 4, 4, 5], 6))
