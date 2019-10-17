import tkinter
from tkinter import *
import pymysql

root = Tk()

class WindowDraggable():

    def __init__(self, label):
        self.label = label
        label.bind('<ButtonPress-1>', self.StartMove)
        label.bind('<ButtonRelease-1>', self.StopMove)
        label.bind('<B1-Motion>', self.OnMotion)

    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None

    def OnMotion(self,event):
        x = (event.x_root - self.x - self.label.winfo_rootx() + self.label.winfo_rootx())
        y = (event.y_root - self.y - self.label.winfo_rooty() + self.label.winfo_rooty())
        root.geometry("+%s+%s" % (x, y))

class Log:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOWS", self.keluar)
        lebar=350
        tinggi=210
        setTengahX = (self.parent.winfo_screenwidth()-lebar)//2
        setTengahY = (self.parent.winfo_screenheight()-tinggi)//2
        self.parent.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
        self.parent.overrideredirect(1)
        self.parent.configure(bg="#a1dbcd")
        self.aturKomponen()
        
    def keluar(self,event=None):
        self.parent.destroy()

    #proses cek user dan pass
    def proses(self,event=None):
        
        user = str("admin")
        password = str("admin")
    
        
        if (str(self.entryUsername.get()) == user) and (str(self.entryPassword.get()) == password):
            root.destroy()
            import petugas
        elif (user==""):
            self.entryUsername.focus_set()
        elif (password==""):
            self.entryPassword.focus_set()           
            
        else:
            self.entryUsername.delete(0, END)
            self.entryPassword.delete(0, END)
            self.entryUsername.focus_set()

    def pro(self,event):
        self.proses()
        
    def aturKomponen(self):
        frameUtama = Frame(root, width=400, height=300, bg="#a1dbcd")
        frameUtama.grid(row=0, column=1)
        WindowDraggable(frameUtama)
        self.buttonx = Button(frameUtama, text="X",fg="white", bg="#FA8072",width=6,height=2,bd=0,activebackground="#FB8072",\
                 activeforeground="white", command=self.keluar, relief=FLAT)

        self.buttonx.grid(row=0, column=0)


        self.labelUsername = Label(frameUtama, text="Username",bg="#444",fg="white", font=("Helvetica", 12), width=9, height=2)
        self.labelUsername.grid(row=1, column=1, pady=6)

        self.labelPassword = Label(frameUtama, text="Password",bg="#444",fg="white", font=("Helvetica", 12), width=9, height=2)
        self.labelPassword.grid(row=2, column=1, )

        self.entryUsername = Entry(frameUtama,fg="#a1dbcd", bg="#444", font=("Helvetica", 12), width=17, bd=11, relief=FLAT)
        self.entryUsername.grid(row=1, column=2)

        self.entryPassword = Entry(frameUtama, show='*',fg="#a1dbcd", bg="#444", font=("Helvetica", 12), width=17,bd=11, relief=FLAT)
        self.entryPassword.grid(row=2, column=2,pady=6)
        self.entryPassword.bind('<Return>', self.pro)



        self.buttonLogin = Button(frameUtama, text="Login", command=self.proses,fg="#a1dbcd", bg="#383a39",\
                             width=10, height=2,bd=0,activebackground="whitesmoke",activeforeground="#444")
        self.buttonLogin.grid(row=3, column=2, pady=6, sticky="e")


        self.entryUsername.focus_set()

    
def main():
    Log(root, ":: Tambah Genre ::")
    root.mainloop()

