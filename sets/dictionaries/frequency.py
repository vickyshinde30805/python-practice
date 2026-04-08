list1=[1,1,2,2,3,3,3,4,4,55,55,5,5,555,7,7,89,9]
freq={}
for i in list1:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

for i in freq:
    print(f"{i} is present {freq[i]} timees")