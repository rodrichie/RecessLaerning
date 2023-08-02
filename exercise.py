#TUPLE EXERCISE
#tuples allow duplicates
myteam=("ronaldo","messi","benzema","zidane","ronaldo")
#they also allow multiple data types
myturple=("name",20,True,"male")
#accessing the tuples
print(myturple[1])#outputs 20
#negative indexing
print(myteam[-1])
#range of indexes
print(myteam[1:3])
print(myteam[:4])
print(myteam[2:])

#length of a tuple
length=len(myteam)
leng=len(myturple)
print(length)
print(leng)

#adding items to a tuple
x=list(myteam)
x.append("maradona")
myteam=tuple(x)
print(myteam)



#SETS EXERCISE
teams={"real madrid","manchester united","barcelona","juventus"}
#length of the set
print(len(teams))
"""sets contain different data types
   they are as follows
"""
sports={"footaball","basketball","cricket"}
aggregates={8,9,10,11,12,13,14}
set3={True,False}
school={"teacher",20,True,"students",30,False}
#accessing items in the set,loop through them
for sport in sports:
    print (sport)

#adding items to the set
sports.add("swimming")
print(sports)

#adding two sets together
school.update(aggregates)
print(school)


