# 입력 받기
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 최대 크기 변수 초기화
max_area = -1

# 모든 좌표에서 시작점을 잡고, 가능한 모든 직사각형을 검사
for i in range(n):
    for j in range(m):
        # 시작점 (i, j)에서 가능한 모든 직사각형 크기를 시도
        for height in range(1, n - i + 1):
            for width in range(1, m - j + 1):
                # 직사각형 내부에 음수가 있는지 검사
                valid = True
                for x in range(i, i + height):
                    for y in range(j, j + width):
                        if matrix[x][y] <= 0:
                            valid = False
                            break
                    if not valid:
                        break

                # 모든 값이 양수라면 면적 계산
                if valid:
                    area = height * width
                    max_area = max(max_area, area)

# 결과 출력
print(max_area)