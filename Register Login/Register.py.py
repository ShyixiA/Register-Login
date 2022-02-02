print("----REGİSTER----")
UserName = input("Enter Your Username : ")
Passaword = input("Enter Your Password : ")

print("System Registered Successfully Please Login")

print("----LOGİN----")


L_UserName = input("Enter Your sername : ")
L_Passaword = input("Enter Your Password : ")

while UserName!=L_UserName and Passaword!=L_Passaword:
    
 if UserName == L_UserName and Passaword == L_Passaword:
    print("Login to the System Successfully")

 else:
    print("Login Failed")
    kkadi = input("Enter Your Username : ")
    ppsswrd = input("Enter Your Password : ")
    print("Login to the System Successfully")
    

