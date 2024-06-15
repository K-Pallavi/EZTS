# vowel occurences in multiple sentences
def count_vowel(s):
    dic={'A':0,'E':0,'I':0,'O':0,'U':0}
    for j in s:
        if j=='a' or j=='A':
            dic['A']+=1
        elif j=='e' or j=='E':
            dic['E']+=1
        elif j=='i' or j=='I':
            dic['I']+=1
        elif j=='o' or j=='O':
            dic['O']+=1
        elif j=='u' or j=='U':
            dic['U']+=1   
            
    x=max(dic.values())
    result=[]
    
    for i,j in dic.items():
        if j==x:
            result.append(i)
    return result

i_p=[
    ["Alex", "I enjoy hiking in the mountains."],
    ["Sam", "A lovely sunny day at the beach."],
    ["Jamie", "Reading a book is my favorite pastime."], 
    ["Taylor", "I love playing video games on weekends."],
    ["Chris", "Exploring new cities is exciting and fun."]
]
o_p={}
for i in i_p:
    o_p[i[0]]=count_vowel(i[1])
print(o_p)