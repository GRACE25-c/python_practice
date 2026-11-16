#******************************************************************
#**************************SET*************************************
#******************************************************************



# #decaring a set

# #method 1
# set1={}     #<class 'dict'> we used to dicalare a dictionary also use {} . this is not a set 

# #method 2
# set2={23,34,55,2026,"BSNL",True,2026,2026.0,"2026"}   #<class 'set'>    
# # duplicates are deleted. 

# #method 3
# set3=set()    #<class 'set'>


# print(type(set1))
# print(type(set2))
# print(type(set3))


# print(set2)  #{34, 2026, 55, 23}  output will get the different order . in set we cant use index
# #set support all datatypes so this is a herogenous

# ## count1=set2.count()
# ## print(count1)

# print("******************functions**********************")

# roll={1,2,3,4,5,6}
# roll_odd={1,3,5}
# roll_even={2,4,6}
# random={1,5,9,4}

# random.add(2026)  # we used to add a value into the set like this 
# print(random)    #{1, 4, 5, 9, 2026}   

# #difference between set (present in randam set but not in the roll_odd)
# print(random.difference(roll_odd))  #{9, 2026, 4}
# print(roll_odd.difference(random)) #{3}

# print(roll.issuperset(roll_odd))  #True
# print(roll.issubset(roll_odd))   #False
# print(roll.issuperset(random))  #False


# print(random.intersection(roll_even))  #{4}
# print(random.intersection(roll_odd))  #{1, 5}
# print(roll.intersection(roll_even))  #{2, 4, 6}
# print(roll.intersection(roll_odd))  #{1, 3, 5}

# random.add(15)
# print(random) #{1, 4, 5, 9, 2026, 15}
# print(roll.discard(random))
# print(roll)
# print(random)
# #random.intersection_update(roll)
# print(random.intersection_update(roll))
# print("set random",random) #set random {1, 4, 5}
# print("set roll_even",roll_even)  #set roll_even {2, 4, 6}
# print(random.union(roll_even)) #{1, 2, 4, 5, 6}

# #propertice of datatypes set
# #support hetrogenous datatype 
# #cannot access data using index
# #mutable
# #duplicates are not allowed

#******************************************************************
#**************************Dictionary******************************
#******************************************************************


#methord 1
dict1={}  #this is a dictionary <class 'dict'>

#methord 2
#dict2={"key1":"value1","key2":"value2","key3":2027}   #<class 'dict'>
dict2={"key1":True,"key2":"value2",8:2027,True:"yes it wors"}    #dictionary key and value can be any data types but one contetion is uniqe key {'key1': True, 'key2': 'value2', 8: 2027, True: 'yes it wors'}
#methord 3
dict3=dict()    #<class 'dict'>


print(type(dict1))
print(type(dict2))
print(type(dict3))
dict2={1:"one",0:"zero",1:True}  # keys are duplicate that key will tack the leatest assined value as its value  . like this {1: True, 0: 'zero'}
print(dict2) #{1: True, 0: 'zero'}

print(dict2[0])  #zero

student_dict={"name":"Grace","age":21,"university":"MGU","district":"Kottayam"}
print(student_dict)  #{'name': 'Grace', 'age': 21, 'university': 'MGU', 'district': 'Kottayam'}
print(student_dict.keys())  #dict_keys(['name', 'age', 'university', 'district'])
print(student_dict.values()) #dict_values(['Grace', 21, 'MGU', 'Kottayam'])
print(student_dict.items())  #dict_items([('name', 'Grace'), ('age', 21), ('university', 'MGU'), ('district', 'Kottayam')])
student_dict["university"]="KTU"
print(student_dict) #{'name': 'Grace', 'age': 21, 'university': 'KTU', 'district': 'Kottayam'}
student_dict.keys() #{'name': 'Grace', 'age': 21, 'university': 'KTU', 'district': 'Kottayam'}


print("***************************************************************************************************")
print("\n")
personal_info={"name":"Grace Jacob","Phone No.":7306598265,"E-Mail":"gracejacob167@gmail.com","course":"B.Sc Computer Science"}
print(personal_info) #{'name': 'Grace Jacob', 'Phone No.': 7306598265, 'E-Mail': 'gracejacob167@gmail.com', 'course': 'B.Sc Computer Science'}
input_info=input("enter your college name: ")
personal_info.update["college":input_info]
print(personal_info)