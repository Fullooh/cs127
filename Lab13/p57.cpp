//Name: Angst S Gregory
//Email: angst.gregory17@myhunter.cuny.edu
//Date: ------
//This program prints: ----

#include <iostream>

using namespace std;

int main()
{

    int credit;

    cout << "Enter number of credit hours taken: ";
    cin >> credit;

    if (credit < 28)
    {
        cout << "Freshman\n";
    }
    
    else if (28 <= credit and credit < 61)
    {
        cout << "Sophmore\n";
    }

    else if (61 <= credit and credit < 94)
    {
        cout << "Junior\n";
    }
    
    else 
    {
        cout << "Senior\n";
    }
    
    return 0;
}