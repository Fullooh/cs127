//Name: Angst S Gregory
//Email: angst.gregory17@myhunter.cuny.edu
//Date: ------
//This program prints: ----

#include <iostream>

using namespace std;



int main()

{

    int n,rem,size,num,len;

    cout<<"Enter an int in [-128,127]:";

    cin>>n;

    num=n;

    if (num<0)

    {

        num=-num-1;

    }

    string result;

    result="";

    while (num>0)

    {

        rem=num%2;

        result=to_string(rem)+result;

        num=num/2;

        

    }

    size=8;

    len=result.length();



    for (int i=0; i< size - len; i++)

    {

        result="0"+result;

    }

    if (n<0)

    {

        for(int k=0; k<result.length(); k++)

        {

            if (result[k]=='0')

            {

                result[k]='1';

            }

            else

            {

                 result[k]='0';

            }

        }

    }

    cout<<"binary string:"<<result;

    return 0;



}