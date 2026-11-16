# #1
#file_path="C:/Users/GRACE JACOB/OneDrive/Desktop/friends.txt"

# #file1="friends.txt."
# def exception_handling():
#     try:
#         with open("friends.txt.","r")as file:
        
#             content=file.read()
#             print(content)
#     except TypeError:
#         print("file name is wrong")
#     except FileNotFoundError:
#         print("this file is not found")

# #exception_handling()    
# #output
# #this file is not found


#2
def create_file():
    
    try:
        file_path="C:/Users/GRACE JACOB/OneDrive/Desktop/friends.txt"
        #with open(file_path,"a")as file:
        return (open(file_path,"a"))
            #file_path.write("grace jacob\n")
            #print(file_path)
    
    except Exception as e:
            print(f"there is a problem: {e}")
file=create_file()
#out put
#create a new file 

#3
def user_input():
    try:
        #with open("friends.txt","a")as file:
        create_file()
        file.write(file1)
    
        #print("\n",file1)

    except TypeError:
        print("file name is wrong")
    except FileNotFoundError:
        print("this file is not found")
    except Exception as e:
        print(f"ther is a problem: {e}")
file1=input("enter the name of your friend:  ")
user_input()
    # output
    # nice jacob enterd name of a friend




