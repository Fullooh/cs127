//Name: Angst S Gregory
//Email: angst.gregory17@myhunter.cuny.edu
//Date: ------
//This program prints: ----

#include <iostream>

int main(){
    double budget;
    double monExpense;
    std::cout<<"Input your annual budget: ";
    std::cin>>budget;
    std::cout<<"Input your month expense: ";
    std::cin>>monExpense;

    for (int i = 1; i <= 6; i++)
    {
        budget -= monExpense;
        printf("%5d\t%7.2f\t%27.2f\n", i, monExpense, budget);
    }
    monExpense*=1.15;
    for (int i = 7; i <= 12; i++)
    {
        budget -= monExpense;
        printf("%5d\t%7.2f\t%27.2f\n", i, monExpense, budget);
    }

    if (budget<0)
    {
        std::cout<<"need higher budget";

    }
    
}