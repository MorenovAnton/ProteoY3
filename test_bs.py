'''
def solve(n, a):
    sorted_ = 0

    # n - кол-во элементов в массиве 3
    # a - массив для проверки

    #print('n', n)
    len_n = n - 1
    if len_n == -1:
        #print('No')
        return 'No'
    for random_i in range(len_n, 0, -1): # проходим от самого последнгего элемента к первому
        #print('random_i', random_i)
        for X in range(0, a[random_i]): # проходим по всем сгенерированным значениям X от 0 до элемента который рассматриваем
            #print('X', X)
            a[random_i] = a[random_i]-X  # операция может быть образованна только один раз
            #print('a', a)
            sorted_ = all(index_i-index_j>0 for index_i, index_j in zip(a, a[1:]))
            #print(sorted_)
            if sorted_ == 1:
                #print('Yes')
                return 'Yes'

        if sorted_ == 0:
            return solve(n-1, a)



t = int(input())    # кол-во тестовых примеров 
for _ in range(t):
    n = int(input()) # кол-во элементов в массиве 3
    a = list(map(int, input().split())) # n - элементов последов-сти > 0 

    out = solve(n, a)
    print(out)
'''

'''
from itertools import permutations

def maximum(s, t):
    s = permutations(s)
    t = permutations(t)
    print(s)
    print(t)

t = int(input())
for _ in range(t):
    s = input()
    t = input()

    out = maximum(s, t)
    print(out)
'''


import torch
from torch import nn
conv = nn.Conv2d(1,1,kernel_size=3, padding=1, stride=2, bias=False)
X = torch.FloatTensor([[[
    [4, 2, -1],
    [-6, 0, 5],
    [3, 2, 2]]]])

conv.weight.data = torch.FloatTensor([[[
    [0, 1, 2],
    [1, -1, 0],
    [1, 0, -2]]]])

res = conv(X).data[0,0]

print(res)

