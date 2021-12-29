#include<stdio.h>
#include<stdlib.h>

int main(){
    int n;
    printf("Enter the number of cities\n");
    scanf("%d",&n);
    int city[n];
    printf("Enter the number of percentage of zombies in each city");
    for(int i=0;i<n;i++){
        scanf("%d",&city[i]);
    }
    return 0;
}