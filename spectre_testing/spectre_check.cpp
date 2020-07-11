#include <bits/stdc++.h>
using namespace std;

int main()
{
    string secret;
    freopen("spectre_check.txt", "w", stdout);
    ifstream ifs("encodedImg.txt");
    getline(ifs, secret, (char)ifs.eof());
    for(auto s: secret)
    {
        int is= int(s);
        cout << int(s) << " ";
    }
    cout << endl;
    return 0;
}