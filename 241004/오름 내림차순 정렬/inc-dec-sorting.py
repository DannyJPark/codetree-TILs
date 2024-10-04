n = int(input())  
elements = list(map(int, input().split())) 

asc_sorted = sorted(elements)
desc_sorted = sorted(elements, reverse=True)

print(" ".join(map(str, asc_sorted)))  
print(" ".join(map(str, desc_sorted)))