#generate and store passwords for different accounts
import random
import string
def create_pass():
	c=int(input("Enter the number of lower case characters : "))
	c_uc=int(input("Enter the number of upper case characters : "))
	d=int(input("Enter the number of digits : "))
	char=int(input("Enter the number of characters : "))
	alpha=list(string.ascii_lowercase)
	alpha_uc=list(string.ascii_uppercase)

	num=[]
	for i in range(10):
		num.append(i)
	ch=['!','@','#','$','%','^','&','*','+']
	pwd=""
	tot_char=c+c_uc+d+char
	while len(pwd)!=tot_char:
		
		k=random.randint(0,4)
		if k==0 and c!=0:
			pwd+=str(alpha[random.randint(0,25)])
			c-=1
		elif k==0:
			continue
		if k==1 and c_uc!=0:
			pwd+=str(alpha_uc[random.randint(0,25)])
			c_uc-=1
		elif k==1:
			continue
		if k==2 and d!=0:
			pwd+=str(num[random.randint(0,9)])
			d-=1
		elif k==2:
			continue
		if k==3 and char!=0:
			pwd+=str(ch[random.randint(0,8)])
			char-=1
		elif k==3:
			continue
	return pwd
def enter_details():
	cat=str(input(f"Enter the website : "))
	userid=str(input(f"Enter your user-id : "))
	cho='N'
	while cho=='N':
		password=create_pass()
		print(f"Generated password is : {password}")
		cho=str(input((f"Press Y to approve or N to create a new password : ")))
	file=open('store.txt','a')
	file.write(f"Login credentials for {cat}\n")
	file.write("---------------------------------\n")
	file.write(f"User-ID: {userid}\n")
	file.write(f"Password : {password}\n")
	file.write("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~\n")
	file.write("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~\n\n")
	file.close()

def display():
	f=open('store.txt','r')
	for each in f:
		print(each)
	
def menu():
	ch=10
	while 1:
		print("Enter choice : ")
		cie=int(input(("1. Add a record\n2. View all records\n3. Exit\nChoice : ")))
		if cie==3:
			break
		elif cie==1:
			enter_details()
			continue
		elif cie==2:
			display()
			continue
		else:
			continue
menu()
		
		




		


