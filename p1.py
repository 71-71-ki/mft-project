import tkinter
import json
def submit():
    l3.configure(text="")
    f = open("data.json")
    karbaran = json.load(f)
    user = e1.get()
    alamat=["!","@","$","%","*","_"," ",".",",","~","#","&","(",")","^","/","'",'"',"+","-","|"]
    if user in karbaran:
        l3.configure(text="تکراری")
    else:
        if len(user)>10 or len(user)<3:
            
            l3.configure(text="تعداد مناسب نیست")
        else:
            for i in user:
                if i in alamat:
                    l3.configure(text="فقط عدد و علامت مجاز است")
                else:
                    l3.configure(text="ثبت شد")
                    newuser={e1.get():e2.get()}
                    
                    with open('data.json') as file:
                        data=json.load(file)
                    with open('data.json','w') as file:
                        data.update(newuser)
                        file.seek(0)
                        json.dump(data,file)
            
def login():
    username=e1.get()
    password=e2.get()
    f = open("data.json")
    karbaran = json.load(f)
    if username in karbaran:
        if karbaran[username]==password:
            l3.configure(text="خوش آمدید | welcome")
        else:
            l3.configure(text="error")
    else:
        l3.configure(text="ابتدا ثبت نام کنید")
    

root =tkinter.Tk()
root.geometry("450x100")

# ------- widgets -------
l1=tkinter.Label(root,text="username:")
l2=tkinter.Label(root,text="password:")
e1=tkinter.Entry(root)
e2=tkinter.Entry(root)
l3=tkinter.Label(root,text="")
b1 =tkinter.Button(root,text="Submit",command=submit)
b2 =tkinter.Button(root,text="login",command=login)
# - ------grids ---------
l1.grid(row=0,column=0)
l2.grid(row=0,column=1)
e1.grid(row=1,column=0)
e2.grid(row=1,column=1)
l3.grid(row=1,column=2)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)

root.mainloop()