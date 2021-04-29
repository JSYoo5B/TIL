#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

typedef struct _person {
	int age;
	string name;
} Person;

int main(void) {
	int cases;
	cin >> cases;

	vector<Person> persons;
	for (int i = 0; i < cases; i++) {
		Person p;
		cin >> p.age >> p.name;
		persons.push_back(p);
	}

	stable_sort(persons.begin(), persons.end(), 
			[](const Person& a, const Person& b){
				if (a.age < b.age)
					return true;
				else
					return false;
			});

	for (auto& p : persons) {
		cout << p.age << ' ' << p.name << '\n';
	}
}