#!/usr/bin/env python3

f1 = open("/home/sirbega/dev/ikre/spamfilter/keywords.txt", "r")
data = f1.read()
kwords = data.split()
f1.close

f2 = open("/home/sirbega/dev/ikre/spamfilter/mail.txt", "r")
data = f2.read()
mwords = data.split()
f2.close

chk = True
i = 0
lk = len(kwords)
lm = len(mwords)
while chk and i < lk:
    j = 0
    while chk and j < lm:
        if mwords[j] == kwords[i]:
            chk = False
        j += 1
    i += 1

if chk:
    f3 = open("/home/sirbega/dev/ikre/spamfilter/inbox.txt", "w")
    f3.write(data)
    f3.close
else:
    f4 = open("/home/sirbega/dev/ikre/spamfilter/spam.txt", "w")
    f4.write(data)
    f4.close
