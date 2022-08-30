from tkinter import *

root=Tk()


root.title("Python Project")
root.iconbitmap("D:\Downloads new\WhatsApp Image 2022-08-30 at 10.19.19 PM.ico")

def pranav():
    
    
    url=search.get()
    print (url)


label=Label(root,text="Web scrapper",font=("Arial",14)).grid(padx=500,pady=50)

search=Entry(root, width=40, font=('Arial', 14))
search.grid(padx=500,pady=40)


button1=Button(root, text='Search', command=pranav)
button1.grid(padx=500,pady=50)

button2=Button(root, text='Exit',command=root.quit)
button2.grid(padx=525,pady=60)

root.mainloop()