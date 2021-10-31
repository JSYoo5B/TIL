#include <bits/stdc++.h>

using namespace std;

int main(void) {
	int vars_cnt;
	char str[101];

	scanf("%d", &vars_cnt);
	scanf("%s", str);

	string postfix_formula = str;
	int *vars = new int[vars_cnt];
	for (int i = 0; i < vars_cnt; i++) {
		scanf("%d", &vars[i]);
	}
	stack<double> calc_store;
	for (char c : postfix_formula) {
		if ('A' <= c && c <= 'Z') {
			int value = vars[c-'A'];
			calc_store.push((double)value);
		}
		else {
			double opR = calc_store.top();
			calc_store.pop();
			double opL = calc_store.top();
			calc_store.pop();

			double temp_result = 0.0f;
			switch(c) {
			case '+':
				temp_result = opL + opR;
				break;
			case '-':
				temp_result = opL - opR;
				break;
			case '*':
				temp_result = opL * opR;
				break;
			case '/':
				temp_result = opL / opR;
				break;
			}
			calc_store.push(temp_result);
		}
	}
	printf("%.2lf", calc_store.top());
}
