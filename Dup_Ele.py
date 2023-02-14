lst = [1,1,2,3,3,4,5,6,6]
print([x for x in set(lst) if lst.count(x) > 1])
