length= int(input())

list1 = [0 for i in range(length)]

list1 = list(map(int, input().split()))

l_m = max(list1)
l_min = min(list1)
print(l_min, l_m)
