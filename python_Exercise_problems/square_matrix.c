#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(){
    int n,d1=0,d2=0;
    printf("Enter the size of the matrix");
    scanf("%d",&n);
    int arr[n][n];
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            scanf("%d",&arr[i][j]);
        }
    }
    for(int i=0;i<n;i++){
        d1=d1+arr[i][i];
        d2=d2+arr[i][n-1-i];
    }
    int abs_diff=fabs(d1-d2);
    printf("%d",abs_diff);

    return 0;
}

