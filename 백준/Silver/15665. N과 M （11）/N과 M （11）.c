//15665

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int N, M;
int arr[7] = { 0, };

int compare(const void* a, const void* b) {
    return (*(int *)a - *(int *)b);
}

void N_AND_M(int start, int depth, int* arr, int* answer, int answer_index) {
    
    if (depth == M) {
            for (int i = 0; i < M; i++){
                printf("%d ", answer[i]);
            }
            printf("\n");
        return;
    }

    for (int i = start; i < N; i++){
        if (i >= 1 && arr[i] == arr[i-1]){
            continue;
        }
        answer[answer_index] = arr[i];
        N_AND_M(start, depth + 1, arr, answer, answer_index + 1);
    }
    return;
}

int main(void) {
    scanf("%d %d\n", &N, &M);
    
    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }

    qsort(arr, N, sizeof(int), compare);

    int start = 0;
    int depth = 0;
    int answer[7] = { 0, };
    int answer_index = 0;
    N_AND_M(start, depth, arr, answer, answer_index);
    return 0;
}