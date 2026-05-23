def secondmaxelement(arr):
    maxind,maxele=0,arr[0]
    secmaxind,secmaxele=0,arr[0]
    for i in range(1,len(arr)):
        if arr[i]>maxele:
            secmaxind,maxind= maxind,i
            secmaxele,maxele= maxele,arr[i]
        elif arr[i]>secmaxele and arr[i]!=maxele:
            secmaxind=i
            secmaxele=arr[i]
    return secmaxele
n=int(input("Enter the size of array: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter element: ")))
result=secondmaxelement(arr)
print("Second maximum element is: ", result)


