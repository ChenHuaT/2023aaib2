#include <stdio.h>
int myAdd(int a, int b){  ///�禡�w�q
    return a+b;
}
void myPrint(int a) { ///�禡�w�q �i��1��
    for(int i=1;i<=a;i++) printf("*");
    printf("\n");
}
int main()
{
    int ans = myAdd(3,4);  ///�禡�I�s
    printf("Hello ans: %d\n", ans);
    myPrint(7);
    myPrint(6); ///�禡�I�s(�ХL���ڰ��Ʊ�)
}
