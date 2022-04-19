numbers = list(map(int,input().split()))
import numpy
import statistics

def Average(lst):
    return sum(lst) / len(lst)

print(str(min(numbers)))
print(str(max(numbers)))
print(str(Average(numbers)))
print(str(statistics.stdev(numbers)))
print(str(numpy.var(numbers)))

