#include <stdio.h>
int main (void)
{
    int arr1[6]={1,2,3,4,5,6};
    int arr2[6]={7,8,9,10,11,12};
    int i=0;

    int *ptr1=arr1;
    int *ptr2=arr2;
    int temp;

    printf("arr1: ");

    for(i=0; i<6; i++)
    {
        printf("%d ", arr1[i]);
    }
    printf("\n");

    printf("arr2: ");
    for(i=0; i<6; i++)
    {
        printf("%d ", arr2[i]);
    }

    printf("\n\n");
    printf("after swap\n");
    printf("arr1: ");

    for (i=0; i<6; i++ )
    {
        ptr1=&arr1[i];
        ptr2=&arr2[i];
        temp=*ptr1;//ptr1,즉 arr1의 첫번째 배열 임시저장
        *ptr1=*ptr2; //ptr1, arr1 첫번째에 ptr2값 저장
        *ptr2=temp; //ptr2 임시저장..
        printf("%d ", arr1[i]);
    }

    printf("\n");
    printf("arr2: ");

    for (i=0; i<6; i++ )
    {
        ptr1=&arr1[i];
        ptr2=&arr2[i];
        printf("%d ", arr2[i]);
    }

    return 0;
}