#include <iostream>
using namespace std;

int main()
{
    int n; // number of element in array
    cin >> n;

    int a[n]   ;     // array to store numbers
        int sum = 0 ;// to store total sum of the array elements
        for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        sum += a[i];
    }
    int avg = sum / n; // average of array elements
    int res = 0;
    for (int i = 0; i < n; i++)
    {
        if (a[i] == avg)
            res++;
    }
    cout << res << endl;
    return 0;
}