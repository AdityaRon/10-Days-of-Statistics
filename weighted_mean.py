N = int(input())
inp1 = list(map(int, input().split()))
inp2 = list(map(int, input().split()))
summation = 0
product = 0
for i,j in zip(inp1,inp2):
    summation += j
    product += i*j
print(round(product/summation,1))
    
    
