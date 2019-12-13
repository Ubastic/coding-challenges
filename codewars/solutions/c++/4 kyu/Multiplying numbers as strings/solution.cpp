#include <iostream>
#include <string>
#include <vector>

using namespace std;

string removeZero(string str) {
    auto i = 0;
    while (str[i] == '0')
        i++;

    str.erase(0, i);
    return str;
}

int getOrNull(vector<int> &arr, int pos) {
    return pos < arr.size() ? arr.at(pos) : 0;
}

string multiply(string a, string b) {

    if (a.length() < b.length()) {
        a.insert(0, string(b.length() - a.length(), '0'));
    } else if (b.length() < a.length()) {
        b.insert(0, string(a.length() - b.length(), '0'));
    }

    vector<vector<int>> table;

    for (int i = a.length() - 1; i >= 0; i--) {
        auto ost = 0;
        vector<int> row;

        for (int j = b.length() - 1; j >= 0; j--) {
            auto item = (a[i] - '0') * (b[j] - '0') + ost;
            ost = item / 10;
            item %= 10;

            row.push_back(item);
        }

        row.push_back(ost);
        table.push_back(row);
    }

    for (int i = 1; i < table.size(); i++) {
        auto &row = table[i];
        for (int j = 0; j < i; j++) {
            row.insert(row.begin(), 0);
        }
    }

    auto &row = table.at(table.size() - 1);
    string res = "";
    auto ost = 0;

    for (auto i = 0; i < row.size(); i++) {
        auto n = ost;
        for (auto r : table) {
            n += getOrNull(r, i);
        }

        ost = n / 10;
        n %= 10;
        res.insert(res.begin(), '0' + n);
    }
    res.insert(res.begin(), '0' + ost);

    res = removeZero(res);
    return res.empty() ? "0" : res;
}