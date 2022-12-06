//Name: Angst S Gregory
//Email: angst.gregory17@myhunter.cuny.edu
//Date: ------
//This program prints: ----

#include <iostream>

using namespace std;

int main()
{
  int rows;
  char symbol;

    cout << "Enter an int: ";
    cin >> rows;

    cout << "Enter a symbol other than space: ";
    cin >> symbol;

    for(int i = 1; i <= rows; i++)
    {
        for(int k =rows - i; k > 0; k--)
            cout << " ";
        for(int j = 1; j <= i; j++)
        {
            cout << symbol;
        }
        cout << "\n";
    }
    return 0;


}