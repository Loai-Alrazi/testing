password ="loai"
word =""
count=0
limit=3

while word !=password:
    if count<limit:
        word = input("Enter password: ")
    else :
        print("انت سارق")
        break
    count   +=1 
    if word !="loai":
        print("false")
    else :
        print ("correct! ")
