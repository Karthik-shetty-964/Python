#include<stdio.h>
#include<stdlib.h>

int main(){
    int pebbles[]={1,1,2,2};
    // int pebbles[]={1,2,3,4,4,4,3,2,1,2};
   
    int count=0;
    int counts[8];
    for(int i=0;i<8;i++){
        int temp=pebbles[i];
        
        for(int j=0;j<8;j++){
            if(temp==pebbles[j]){
                count++;
            }
        }
           counts[i]=count;
           count=0;
    }
    int k=counts[0];
    int flag=1;
    
    for(int i=0;i<8;i++){
        if(counts[i]!=k){
            flag=0;
            break;
        }
    }
    if(flag==1){
        printf("true");
    }else{
        printf("false");
    }
    return 0;
}