def printlist(list,idx):
    if idx== len(list):
        return
    print(list[idx])
    printlist(list,idx+1)   
list=[1,2,3,4,5]
printlist(list,0)