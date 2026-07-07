lst = [[1,2],[3,4],[5,6]]
result = list(map(lambda x: [i+5 for i in x], lst))
print(result)

d = {"apple":100, "banana":40, "cherry":150}
result = dict(filter(lambda x: x[1] > 50, d.items()))
print(result)

from functools import reduce
nums = [10, 5, 25, 8, 15]
largest = reduce(lambda a, b: a if a > b else b, nums)
print(largest)