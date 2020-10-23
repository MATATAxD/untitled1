def maopao(list):
    size=len(list)
    if size<=1:
        return list
    for i in range(1,list):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
        print('第{}次排序结果:'.format(i),end='')
        print(list)
    return list
if __name__ =='__main__':
    import random
    list=[]
    for _ in range(0,10):
        list.append(random,randint(0,100))
    print(list)


