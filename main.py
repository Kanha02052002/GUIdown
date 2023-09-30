import tkinter
import customtkinter

def urlSearch():
    print("checked")



customtkinter.set_appearance_mode("System")

app=customtkinter.CTk()
app.geometry("720x480")
app.title("NDM")

# Input box
urlLabel=customtkinter.CTkLabel(app, text="Add you link",command=urlSearch)
urlLabel_corner_radius(5)
urlLabel.pack()


button=tkinter.Button(app, text="Search")
button.grid(row=1,column=2)
button.pack()



if __name__=='__main__':
    pass



app.mainloop()