#내 풀이

# N = int(input())
# i = 1
# while i<=N:
#     print("{0:>{1}}" .format("*"*i,N))
#     i+=1

#코파일럿 풀이

N = int(input())
for i in range(1, N + 1):
    print(" " * (N - i) + "*" * i)