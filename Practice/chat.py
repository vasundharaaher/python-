from tkinter import *
from tkinter import scrolledtext

def FuncSendText():
    userinput = InputText.get("1.0",END).strip()
    DisplayText.config(state=NORMAL)
    DisplayText.insert(END, "You : "+userinput+"\n", "user")
    # DisplayText.insert(END,"Bot : "+"I am doing good, thanks!"+"\n","bot")
    userinput=userinput.lower()
    if any(x in userinput for x in greetings):
        DisplayText.insert(END,"Bot : "+"Hi! how can i help you ?"+"\n","bot")
    elif("how are you" in userinput):
        DisplayText.insert(END,"Bot : "+"I am bot does not have emotion"+"\n","bot")
    else:
        DisplayText.insert(END,"Bot : "+"Not sure how to ans"+"\n","bot")
    DisplayText.config(state=DISABLED)
    InputText.delete("1.0",END)

root = Tk()
root.title("My chat app")
root.geometry("500x600")

AppHeader = Label(root, text="My Chat App", bg="dark blue",fg="white" , font=("Georgia",24))
AppHeader.pack(fill=X,expand=True)

DisplayText = scrolledtext.ScrolledText(root, state=DISABLED , wrap=WORD)
DisplayText.pack(fill=BOTH,expand=True)

DisplayText.tag_config("user", foreground='blue')
DisplayText.tag_config("bot", foreground='green')

InputText = scrolledtext.ScrolledText(root, wrap=WORD , height=3)
InputText.pack(fill=BOTH,expand=True)

SendButton = Button(root, text="Send",font=("Georgia",14), command=FuncSendText)
SendButton.pack()

greetings = ['hi','hello','hey','whats up']
root.mainloop()
