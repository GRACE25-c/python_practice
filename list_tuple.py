# #*********************************************************
# #***********list is a datatype used  to store the collection of values
# #***********since it is a combination of other data types(init,float,string,bool)
# #we call its as a derrived datatypes.
# # there is no restriction in terms of datatype in a list
# #CAN MACK CHANGES IN LIST

# #declaring a list
# name=" " #this is an empty string
# print(type(name))
# #methord 1
# list_name=[] #its an empty list
# print(type(list_name))

# #method 2
# list_name1=["grace","jayalakshmi","keerthi","krishnapriya"] #list with some valuse in it
# print(type(list_name1))

# #method 3
# list_name2=list() #just a list
# print(type(list_name2))

# #feach data from a list

# print(list_name1[0]) #we concider the list first data as a 0 th index . the out put will be get the fist data in the given index
# print(list_name1[1])
# print(list_name1[2])
# print(list_name1[3])
# #print(list_name1[4])

# list1=[1,7,3]
list2=[False,True,False]
# print(list1+list2) #list can also concatinate   (explicit means by purposefully ) (implicit means aoutomatically)


#*****************************************
#*********list function*******************
#*****************************************

# list1=[1,7,3]
# list1.sort() #sorting is done here (ascending)
# print(list1)
# list_name1=["jayalakshmi","grace","keerthi","krishnapriya"]
# list_name1.sort()
# print(list_name1)

#  list1=[1,7,3]
# list1.sort(reverse=True) #sorting is done here (DECENDING ORDER)
# print(list1) #[7, 3, 1]

# list_name1=["jayalakshmi","grace","keerthi","krishnapriya"]
# # # list_name1.sort(reverse=True)
# list_name1.sort()
# print(list_name1)
list3=[7, 3, 1]
# list_name2=['krishnapriya', 'keerthi', 'jayalakshmi', 'grace']
# list_name1.extend(list3)
# print(list_name1)

# list2.append(list3[1]) #list1 was add the last value of list2
list2.append(list3)
print(list2) #[False, True, False, [7, 3, 1]
print(list2[3])
# list3.append("A")
# print(list3)  #the output is [7, 3, 1, 'A']

# list3.reverse()
# print(list3)  #the output is ['A', 1, 3, 7]


# #************************CHECK THE COUNT OF VALUE *************************


# list2.count(False) 
# print("the no of times False appear in the list",list2.count(False)) #the no of times False appear in the list 2
# list2.count(True)
# print("the no of times False appear in the list",list2.count(True))  #the no of times False appear in the list 1
# list2.count("X")
# print("the no of times False appear in the list",list2.count("X"))  #the no of times False appear in the list 0

# print(list2[-1])   #value at the last index

# len(list2)  #used to get the length of the list
# print("total no of elements in ",list2,'is',len(list2))

#value at the last index find using -1
# list2=[1,3,5,7]
print(list3[-1])
# list2=[1,3,5,7]
print(len(list3))  

#**********************************************************************************
list3.clear()
print("after clear")
print(list3)   #display an empty list like this []

#*****************************************************************************************

list=[1,3,5,"A","R"]
print("befor inserting the value",list) # befor inserting the value [1, 3, 5, 'A', 'R']
list.insert(2,100) # insert value 100 at the index 2
print("after inserting the value",list) # after inserting the value [1, 3, 100, 5, 'A', 'R']

print("*************************************************************")

print("befor inserting the value 3 ",list) #[1, 3, 100, 5, 'A', 'R']
list.remove(3) # remove the value we vant to remove 
print(list) #[1, 100, 5, 'A', 'R']

print("****************************************************************")
list.pop()
print(list) #[1, 100, 5, 'A']

#"******************************************************************"
#**************************TUPLE*************************************
#********************************************************************

# #***********tuple is a datatype used  to store the collection of values
# #***********since it is a combination of other data types(init,float,string,bool)
# #we call its as a derrived datatypes.
# # there is no restriction in terms of datatype in a tuple
#tuple is a hetrogeneas
# ones a TUPLE is created that can't change 
tuple2=()
tuple1=(2026,"nov",2.75,False,[8,True,9.8])
tuple3=tuple()
print(type(tuple2))
print(type(tuple1))
print(type(tuple2))

print(tuple1[2]) #we can feach value using index
print(tuple1.count(False))
print(tuple1.index("nov"))


del(tuple1) # DELETE TUPLE1
del(list)   #DELETE LIST1 

print(tuple1) #name 'tupl1' is not defined. Did you mean: 'tuple'
print(list) #name 'list' is not defined. Did you mean: 'list1'

   