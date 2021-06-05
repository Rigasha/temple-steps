#include <stdio.h>
int main()
  {
  int x;
  float Salary;
  scanf("%d",&x);
  while(x--)
  {
 
    double GrossSalary=0;
   scanf("%f",&Salary);
         if(Salary>1500)
         {
         GrossSalary=  Salary+500+.98*Salary;
         }
         else
         {
         GrossSalary=  Salary+.1*Salary+.9*Salary; 
         }
          printf("%g\n",GrossSalary);
  }
  return
