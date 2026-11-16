#*************************************************************
#**********************file handling**************************
#*************************************************************

#READE A FILE
filepath="D:/PGP_Data_Science_and_AIML/python/text_file.txt"
relative_filepath="text_file.txt"

def read_file_filepath():


    file=open(filepath,"r")    #assign a file in reading mode 
    content=file.read()      #contents of the file is assineed tom "contant"
    file.close()

#print(content)
#output
#this is my first txt file.

#trying using relative file path

def read_file_rel_filpath():


    file_1=open(relative_filepath,"r")
    content_1=file_1.read()
    print(content_1,type(content_1))    # a single string
    file_1.close()
read_file_rel_filpath


def read_line_by_line():


    file_1=open(relative_filepath,"r")
    content_1=file_1.readline()
    #print(content_1,type(content_1))    # a single string
    print(content_1)
    for line in content_1:
        print(content_1)
        print(type(content_1))
        file_1.close()

 #read a single line
def read_lines():


    file_1=open(relative_filepath,"r")
    content_1=file_1.readline()
    #print(content_1,type(content_1))    # a single string
    print(content_1)
    for line in content_1:
        print(line)
        file_1.close()

        #print(type(content_1))


# read_lines()
# read_file_filepath()
# read_file_rel_filpath()
# read_line_by_line()


#************************************************************************************
#******************writing************************************************************

write_path="stdents.txt"

#opens a file in writing mode
#if the file didn't exist earliar , now, it will be credated
#and opened in writing mode
def write_file():
    file=open(write_path,"w")  #new file created
    file.write("goutham")
    # file.write("Akash")
    # file.write("vishnu")
    file.close()
#write_file()
def write_into_file():
    file=open(write_path,"w")  #new file created
    file.write("Akash")
    # return file.write("goutham")
    # stri=write_into_file()
#write_into_file()

def write_name():
    file=open(write_path,"w")  #new file created
    #file.write(Akash)
    file.write("goutham\n")
    file.write("Akash\n")
    file.write("vishnu\n")
    file.close() 
# write_name()
   
def append_file():
    file=open(write_path,"a")
    file.write("Keerthi")
    file.close()
# append_file()


#write_str()
#write_into_file()

#************************************************************************
#generic function to append a data to a function
#************************************************************************


def append_data(file_name,file1):
    #file_name=stdents.txt
    file=open(file_name,"a")
    file.write("\n")
    file.write(file1)
file1=input("enter your data: ")
append_data("stdents.txt",file1) 


def append_data_new(file_path,input1):
    with open(file_path,"a")as file:
        file.write("\n")
        file.write(input1)
input1=input("enter data: ")
append_data_new("stdents.txt",input1)