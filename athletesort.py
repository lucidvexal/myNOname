x, y = map(int, input().split())
n = [input() for i in range(x)]
m = int(input())

for n in sorted(n, key=lambda n: int(n.split()[m])):
    print(n)
