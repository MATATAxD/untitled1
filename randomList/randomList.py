from typing import List
import random


def randomList(n:int):
    iList = []
    for i in range(n):
        iList.append(random.randint(1,100))
    return iList

if __name__ == '__main__':
    print(randomList(10))



