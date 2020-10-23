a=[
    {'name':'zs','age':12},
    {'name':'sds','age':23},
    {'name':'ds','age':25},
    {'name':'sdhah','age':50}




]
def f(n):
    return n['age']>=50
result=list(filter(f,a))
print(result)