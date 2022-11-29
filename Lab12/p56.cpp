//Name: Angst S Gregory
//Email: angst.gregory17@myhunter.cuny.edu
//Date: ------
//This program prints: ----

#include <iostream>

using namespace std;

int main()
{

    int start;
    int end;

    cout << "Enter Start: ";
    cin >> start;

    cout << "Enter End: ";
    cin >> end;

    for (int i = start; i <= end; i++)
    {
        if(i % 2 == 0)
            cout << i << endl;
    }



}