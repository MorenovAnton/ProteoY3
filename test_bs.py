

'''
import os
message_poolsdfbvfdb = "../ProteoY3/message_pool/" + '{}/'.format('telegram')
for hgf in os.listdir(message_poolsdfbvfdb):
    print(message_poolsdfbvfdb + hgf)
'/media/anton/home2/ProteoY3/message_pool/telegram'

import re
h = ['\nhttps://youtu.be/HDEY9NbmzE0?t=112\n', '\nJohnny Smith4a34234\n       ']

for j in h:
    print(re.sub("^\s+|\n|\r|\s+$", '', j))
'''

def powerset(fullset):
    listsub = list(fullset)          # длина полученного на вход массива
    subsets = []                     # финальный список подмножеств
    for i in range(2**len(listsub)): # всего вариантов подмассивов будет 2 в степени длины полученного массива на вход
      subset = []
      for k in range(len(listsub)):  # проходим по массиву и для каждого элемента проверяем
        if i & 1<<k:
          subset.append(listsub[k])
      subsets.append(subset)
    return subsets


subsets = powerset([1,2,3,])
print(subsets)

for ii in range(2**3):
    print('=========================================================')
    print('ii', ii)
    for item in range(3):
        #print(item, 1 << item) # 1 << item - фактически означает 2 в степени item
        print('побитовое И', ii,  2**item, '--->',  ii & 2**item)
        # там где побитовое И отличное от 0 значит этот индекс нам нужен
