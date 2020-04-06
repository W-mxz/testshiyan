#!/usr/bin/env python3
N = 10
S=0
i=0
while(i<N):
    s=float(input("请输入数字{}: ".format(i+1)))
    S=S+s
    i+=1
print("平均数为{:.2f}".format(S/10))
