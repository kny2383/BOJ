n = int(input())

if n < 10 :
    s = "0"
    n = s + str(n)

first_n = n // "10"
second_n = n % 10

print(first_n)
