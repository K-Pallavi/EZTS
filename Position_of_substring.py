# Position of substrings
m = 'JBABCABCABHJHGJABCABCABCABCABABCABCABCABCAC'
p = 'ABCAB'

for i in range(len(m)):
    if p in m:
        e = m.index(p)
        print(e)
        if m[e] == p[0]:
            m = list(m)
            m[e] = " "
            e = e + 1
        m = ''.join(m)
