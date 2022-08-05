from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import string
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
	alpha=list(string.ascii_lowercase)
	alpha_uc=list(string.ascii_uppercase)
	num=[]
	for i in range(10):
		num.append(i)
	ch=['!','@','#','$','%','^','&','*','+']
	pwd=""
	c=randint(3,5)
	c_uc=randint(3,5)
	d=randint(2,3)
	char=randint(2,3)
	pwd_uc=[str(choice(alpha_uc)) for _ in range(c_uc)]
	pwd_lc=[str(choice(alpha)) for _ in range(c)]
	pwd_num=[str(choice(num)) for _ in range(d)]
	pwd_ch=[str(choice(ch)) for _ in range(char)]
	pwd_list=pwd_uc+pwd_lc+pwd_num+pwd_ch
	shuffle(pwd_list)
	pwd="".join(pwd_list)
	pyperclip.copy(pwd)
	entry3.delete(0,END)
	entry3.insert(0,string=pwd)

def fetch():
	w1=entry1.get()
	w2=entry2.get()
	w3=entry3.get()
	if len(w1)==0 or len(w2)==0 or len(w3)==0:
		messagebox.showerror(title="Error", message="Fields cannot be left blank.")
	else:
		proceed=messagebox.askyesno(title="Confirmation",message=f"Details entered: \nWebsite : {w1}\nUser-ID : {w2}\nPassword : {w3}\nConfirm input?")
		if proceed:
			with open("store.txt","a") as f:
				f.write(f"{w1} | {w2} | {w3}\n")
			entry1.delete(0,END)
			entry3.delete(0,END)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20,bg="white")
canvas=Canvas(width=200,height=200,bg="white",highlightthickness=0)
lock_img=PhotoImage(file="logo.png")
canvas.create_image(140,100,image=lock_img)
canvas.grid(row=0,column=1)

label=Label(text="Website:", fg="black",bg="white", font=("Calibri",10,"normal"),pady=5)
label.grid(row=1,column=0)

label2=Label(text="Username:", fg="black",bg="white", font=("Calibri",10,"normal"),pady=5)
label2.grid(row=2,column=0)

label3=Label(text="Password:", fg="black",bg="white", font=("calibri",10,"normal"),pady=5)
label3.grid(row=3,column=0)

entry1=Entry(width=35)
entry1.grid(row=1,column=1,columnspan=2)
entry1.focus()

entry2=Entry(width=35)
entry2.grid(row=2,column=1,columnspan=2)
entry2.insert(0,string="akshayrkv@gmail.com")

entry3=Entry(width=20)
entry3.grid(row=3,column=1)

button1=Button(text="Generate Password", fg="black",bg="white", font=("calibri",10,"normal"),width=14,pady=5,command=gen_pass)
button1.grid(row=3,column=2)

button2=Button(text="Add", fg="black",bg="white", font=("calibri",10,"normal"),width=32,pady=5,command=fetch)
button2.grid(row=4,column=1,columnspan=2)




window.mainloop()
