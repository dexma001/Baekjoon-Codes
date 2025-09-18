//15664

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
int N, M;
int visited_index = 0;

void recursion(int* arr, int depth, int idx, int* answer, int (*visited)[8]){
    if (depth == M) {
        bool checker = false;
        for (int i = 0; i < 70; i++){
            if (checker) {
                break;
            }
            bool temp_checker = true;
            for (int j = 0; j < M; j++){
                if (visited[i][j] != answer[j]) {
                    temp_checker = false;
                }
            }
            if (temp_checker) {
                checker = true;
            }
        }
        if (!checker) {
            for (int i = 0; i < M; i++){
                printf("%d ", answer[i]);
                visited[visited_index][i] = answer[i];
            }
            printf("\n");
            visited_index += 1;
        }

        return;
    }

    if (idx >= N) {
        return;
    }

    for (int i = idx; i < N; i++){
        answer[depth] = arr[i];
        recursion(arr, depth + 1, i+1, answer, visited);
        answer[depth] = 0;
    }
    return;
}


int compare(const void *a, const void *b){
    return (*(int *)a - *(int *)b);
}

int main(void){
    scanf("%d %d", &N, &M);

    int arr[8] = { 0, };
    for (int i = 0; i < N; i++){
        scanf("%d", &arr[i]);
    }

    qsort(arr, N, sizeof(int), compare);

    int visited[70][8] = { 0, };

    int idx = 0;
    int answer[8] = { 0, };
    recursion(arr, 0, idx, answer, visited);
    return 0;
}