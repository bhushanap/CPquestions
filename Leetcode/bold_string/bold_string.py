# There is a string and also a list of tags. You have to insert the bold tags to the substring that are present in the taglist.

# Input 1 -

# str = abcdbef

# tagList = { “cd” , “ef”}

# Output - abcdbef

# Input 2 -

# str = abcdef

# tagList = { “cd” , “ef”}

# Output - abcdef

# Note that for an overlapping case, bold tags should also be overlapped.

str = 'abcdbefghifcdjghefcdhguhcd'
tagList = ['cd', 'ef']

boolList = [0 for i in str]

for tag in tagList:
    for i in range(len(str)):
        boldTag = True
        for j in range(len(tag)):
            if str[i+j] == tag[j]:
                continue
            else:
                boldTag=False
                break
        if boldTag==True:
            for j in range(len(tag)):
                boolList[i+j] = 1

print(str)
print(boolList)

opstring = []

curr = 0
for i in range(len(boolList)):
    if boolList[i] ^ curr:
        opstring.append('<b>')
        opstring.append(str[i])
        curr = not curr
    else:
        opstring.append(str[i])

    if i == len(boolList)-1 and boolList[i]==1:
        opstring.append('<b>')

print(opstring)










