#!/usr/bin/env python3

if __name__ == '__main__':
    trunc_ipv6 = input()
    
    ipv6_units = [ ]
    zero_truncs = list(trunc_ipv6.split("::"))
    if len(zero_truncs) == 2:
        left_units = list(zero_truncs[0].split(":"))
        right_units = list(zero_truncs[1].split(":"))
        skip_cnt = 8 - len(left_units) - len(right_units)
        ipv6_units += left_units
        ipv6_units += ["0000" for _ in range(skip_cnt)]
        ipv6_units += right_units
    else:
        ipv6_units += list(trunc_ipv6.split(":"))

    untrunc_ipv6_units = []
    for t in ipv6_units:
        trunc_len = 4 - len(t)
        untrunc = "0" * trunc_len + t
        untrunc_ipv6_units.append(untrunc)

    untrunc_ipv6 = ":".join(untrunc_ipv6_units)
    print(untrunc_ipv6)

