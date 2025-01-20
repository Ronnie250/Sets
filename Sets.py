"""
sample_list = [25, 5, 6, 25, 5, 5]
sample_set = set(sample_list)
print(sample_set)
if 5 in sample_set:
    print("yes")
else:
    print("No")
sample_set.add(3)
print(sample_set)
sample_set.remove(6)
print(sample_set)
sample_set.discard(99)
print(sample_set)
"""
sample_set_1={1,2,3,4,5}
sample_set_2={8,7,6,5,4}
print(sample_set_1.union(sample_set_2))
print(sample_set_1.intersection(sample_set_2))
print(sample_set_1.difference(sample_set_2))
print(sample_set_2.difference(sample_set_1))
print(sample_set_1.symmetric_difference(sample_set_2))