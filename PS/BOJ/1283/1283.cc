#include <bits/stdc++.h>

#define MAX_WORDS_PER_OPT	5
#define ALPHABET_CNT		('Z' - 'A' + 1)

using namespace std;

int main(void)
{
	int options_cnt = 0;
	bool occupied[ALPHABET_CNT] = { false };

	cin >> options_cnt;
	cin.ignore();
	for (int opt = 0; opt < options_cnt; opt++) {
		string cur_opt;
		getline(cin, cur_opt);
		
		int sc_pos = -1;

		// Tokenize options into words
		stringstream splitter(cur_opt);
		string temp_str;
		string tokens[MAX_WORDS_PER_OPT];
		int words_cnt = 0;
		while (getline(splitter, temp_str, ' ')) {
			tokens[words_cnt] = temp_str;
			words_cnt += 1;
		}

		// Try all heading letter is possible as shortcut
		int cur_pos = 0;
		for (int w_idx = 0; w_idx < words_cnt; w_idx++) {
			string& word = tokens[w_idx];
			int alpha_idx = toupper(word[0]) - 'A';
			if (occupied[alpha_idx] == false) {
				occupied[alpha_idx] = true;
				sc_pos = cur_pos;
				break;
			}
			cur_pos += word.length() + 1;
		}

		// When shortcut were not found, find others
		cur_pos = 1;
		while (sc_pos == -1 && cur_pos < cur_opt.length()) {
			// When the current char is blank
			// we can skip heading letter for each words (already checked)
			if (cur_opt[cur_pos] == ' ') {
				cur_pos += 2;
				continue;
			}

			int alpha_idx = toupper(cur_opt[cur_pos]) - 'A';
			if (occupied[alpha_idx] == false) {
				occupied[alpha_idx] = true;
				sc_pos = cur_pos;
				break;
			}
			cur_pos += 1;
		}

		if (sc_pos == -1) {
			cout << cur_opt;
		}
		else {
			for (int i = 0; i < cur_opt.length(); i++) {
				if (i != sc_pos) {
					cout << cur_opt[i];
				}
				else {
					cout << "[" << cur_opt[i] << "]";
				}
			}
		}
		cout << "\n";
	}
}
