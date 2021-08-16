p = [0 for i in range(5)]
n, a = input().split()

p[0], p[1], p[2], p[3], p[4] = input().split()

people = int(n) * int(a)

for i in range(5):
    print(int(p[i]) - people, end=" ")