# #strings

string1='my name is grace jacob'
string2='python'
string3='programming'

# print(string1)
# print(string2) 
# print(string3)
# print('\n') #new line
# print(string2,string3)

# #by default python prints a new line at the end.


# #changing the end string from '\n' to '&'
# print(string2,end='&') #python&
# print(string3,end='&')#programming&
# print('\n',end='&') #new line&
# print(string2,string3) #python programing&

# #\n is new line  , \t is new tab

# print('\t\t',string2,'\n',string3)

# print('******************************************************************************************')
# #************************************************************************************
# #**************************string candamination**************************************
# #************************************************************************************

s1='ICT'
s2='Academy'
s3='of'
s4='kerala'
#this two print statement are string concatenation
# print(s1 + s2 + s3 + s4)#ICTICTICTICTICT
# print(s1, s2,s3, s4) #ICT ICT ICT ICT ICT
# combined_string=s1+' '+s2+' '+s3+' '+s4 
# print(combined_string) #ICT ICT ICT ICT ICT
# #print(s1,s2,s3,s4,end=" ")

# print("************************************************")
# print(s1)
print(s1+s1+s1+s1+s1)
print(s1*5)
#print((s1+' ')*5)
#print((s1+'\t')*5) #ICT     ICT     ICT     ICT     ICT
#print((s1+'\n')*5)

# print("***********************index*************************")
# print(string3) #programming
# print(string3[0]) #print 0th index charecter
# print(string3[5]) #
# print(string3[10]) #last charecter
# print(string3[10]) # we can go beyond the maximum index of a string.
# print(string1[-1]) #my name is grace jacob print the last letter assinde in the varible string1
# print(string1[-5])

# print('************************************************************************')
# print("\n")
# #********************************************************
# #*************************slicing************************
# #********************************************************


# #sliucing means we cutting the sting into 2 part
# s1='TrIvanDram'
# print(s1[-4]) #d is the output
# print(s1[6]) #d is the output
# print(s1[0:5]) #slicing= charecter index 0 : index 5 . always use add +1 for  end index the output is 'triva'
# print(s1[6:10]) #the output is 'dram'
# print(s1[4:7]) #the output is 'and'
# print(s1[:5])   #start till the 5 th index the output is 'triva'
# print(s1[6:])  #from 6th index till the last index the output is 'dram'
# print(s1[:5:2])
# print(s1[0:5:2]) #starting index : end index : step(how may index move )
# print(s1[:8:3]) # strating index : end index: step the output is "tvd" ( first we get the start index "t" 
# #we move the first index from 3 step so we get "v" 
# # and move v from next 3 step but the last index is 9 
# # but the end index is 8 so we get the end index as "d")


# string_demo='my name is grace jacob iam from kottayam'
# print(string_demo[5:])
# print(string_demo[5::2]) #the output is "m sgaejcbimfo otym"
# print(s1[::-1]) #the output is "mardnavirt" reverse order
# print(string_demo[::-1]) #reverse order the output is "mayattok morf mai bocaj ecarg si eman ym"


# #***************************************************************
# #**********************Functions********************************
# #***************************************************************


# print("****************************************************************************************************")

# print(s1)
# print(s1.lower())#converted into lowercase
# print(s1.upper())# converted into uppercase
# print(s1.swapcase()) #switches case of each letters in the string
# print(s1.capitalize()) # FIRST LETTER IS CAPITTEL AND THEREST WILL BE LOWER
