# 입력 처리
n = int(input())
blocks = [int(input()) for _ in range(n)]

# 첫 번째 제거 구간
s1, e1 = map(int, input().split())
# 인덱스는 0부터 시작하므로 1을 빼서 슬라이싱
blocks = blocks[:s1-1] + blocks[e1:]

# 두 번째 제거 구간
s2, e2 = map(int, input().split())
blocks = blocks[:s2-1] + blocks[e2:]

# 출력
print(len(blocks))
for block in blocks:
    print(block)