#!/usr/bin/env python3

if __name__ == '__main__':
    options_cnt = int(input())
    occupied = [ False for _ in range(26) ]
    for _ in range(options_cnt):
        option = input()
        sc_pos = -1

        cur_pos = 0
        for word in option.split():
            char = ord(word[0]) - ord('A')
            if ord('a') <= ord(word[0]) <= ord('z'):
                char = ord(word[0]) - ord('a')
            
            if occupied[char] == False:
                occupied[char] = True
                sc_pos = cur_pos
                break
            cur_pos += len(word) + 1
        
        cur_pos = 1
        while sc_pos == -1 and cur_pos < len(option):
            if option[cur_pos] == ' ':
                cur_pos += 1
                continue
            char = ord(option[cur_pos]) - ord('A')
            if ord('a') <= ord(option[cur_pos]) <= ord('z'):
                char = ord(option[cur_pos]) - ord('a')
            
            if occupied[char] == False:
                occupied[char] = True
                sc_pos = cur_pos
            cur_pos += 1

        mod_option = option
        if sc_pos != -1:
            mod_option = option[:sc_pos]
            mod_option += '[' + option[sc_pos] + ']'
            mod_option += option[sc_pos+1:]
        print(mod_option)
