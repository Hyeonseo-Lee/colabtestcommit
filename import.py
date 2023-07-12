import sys

input = sys.stdin.readline

num = int(input())
price = [int(input()) for _ in range(num)]
ans = []
for i in range(num):
    qua = price[i]//25
    dime = (price[i]-qua*25)//10
    nickel = (price[i]-dime*10-qua*25)//5
    penny = price[i]-nickel*5-dime*10-qua*25
    ans.append([qua, dime, nickel, penny])

for _ in range(num):
    print(*ans[_])