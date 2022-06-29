from gettext import find


def printList(list1):
    for i in list1:
        print (f'Hello {i} !')

ls = ['Barak','Elad','Avi']
#printList(ls)

str ="5347843632"
#print(str[0:1])

def upperLowerString(str):
    if str[0:1].islower():
        return str.lower()
    return str.upper()

#print(upperLowerString(str))

def findBigger(str):       
    ls=[]
    for i in range(0,len(str)):
        ls.append(str[i])
    ls.sort()
    return(ls[len(str)-1])

print(findBigger(str))