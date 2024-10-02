n = int(input()) 
elements = list(map(int, input().split())) 


squared_elements = [x**2 for x in elements]

print(" ".join(map(str, squared_elements)))