import sys

a = input("Enter the word : ")
print("Given Word : ",a)
print("Size of given word",sys.getsizeof(a))

#-------------------------------------------------------------------------------
#Adjacent word compression

b = ""
count = 1

b += a[0]

for i in range(len(a)-1):
    if(a[i] == a[i+1]):
        count += 1
    else:
        if(count > 1):
            b += str(count)
        b += a[i+1]
        count = 1

if(count > 1):
    b += str(count)

print("Compressed word : ",b)
print("Size of compressed word",sys.getsizeof(b))
#-------------------------------------------------------------------------------
#Mapping word compression
