#include <stdio.h>

#define MAX_N 20

int main() {
    int N;
    int grid[MAX_N][MAX_N];
    int maxCoins = 0;

    // 입력 받기
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &grid[i][j]);
        }
    }

    // 가능한 모든 3x3 부분 격자 검사
    for (int i = 0; i <= N - 3; i++) {
        for (int j = 0; j <= N - 3; j++) {
            int sum = 0;
            // 3x3 부분 격자의 동전 개수 합산
            for (int x = i; x < i + 3; x++) {
                for (int y = j; y < j + 3; y++) {
                    sum += grid[x][y];
                }
            }
            // 최댓값 업데이트
            if (sum > maxCoins) {
                maxCoins = sum;
            }
        }
    }

    // 결과 출력
    printf("%d\n", maxCoins);

    return 0;
}