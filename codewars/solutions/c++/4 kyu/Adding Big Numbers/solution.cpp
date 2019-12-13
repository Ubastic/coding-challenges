#include <algorithm>
#include <iostream>
#include <string>

std::string removeZero(std::string str)
{
	int i = 0;
	while (str[i] == '0')
		i++;

	str.erase(0, i);
	return str;
}

std::string add(std::string a, std::string b) {
	std::reverse(a.begin(), a.end());
	std::reverse(b.begin(), b.end());

	std::string *shoter;
	std::string *longer;

	if (a.size() > b.size()) {
		shoter = &b;
		longer = &a;
	}
	else {
		shoter = &a;
		longer = &b;
	}

	int repeats = longer->size() - shoter->size();
	for (int i = 0; i < repeats; i++) {
		*shoter += "0";
	}

	int ost = 0;
	std::string res = "";
	for (int i = 0; i < longer->size(); i++) {
		std::string n = std::to_string(a.at(i) - '0' + b.at(i) - '0' + ost);
		if (n.size() == 2) {
			res += n.at(1);
			ost = n.at(0) - '0';
		}
		else {
			res += n;
			ost = 0;
		}
	}

	if (ost != 0) {
		res += std::to_string(ost);
	}

	std::reverse(res.begin(), res.end());
	return res == "0" ? res : removeZero(res);
}