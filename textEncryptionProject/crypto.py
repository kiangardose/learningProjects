from tkinter import *
from tkinter import messagebox
import base64

def decrypt():
    message = text1.get(1.0, END).strip()
    if not message:
        messagebox.showerror("Decryption", "You haven’t entered anything to decrypt. Try Again")
        return

    password = code.get()

    if password == "grasya":

        try:
            decode_message = message.encode("ascii")
            base64_bytes = base64.b64decode(decode_message)
            decrypted = base64_bytes.decode("ascii")
        except Exception:
            messagebox.showerror("Decryption", "This message doesn't match anything, please try again")
            text1.delete(1.0, END)
            code.set("")
            code_entry.config(state=NORMAL)
            code_entry.focus_set()
            return

        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x250")
        screen2.configure(bg="#251c26")
        screen2.resizable(True, True)
        screen2.rowconfigure(1, weight=1)
        screen2.columnconfigure(0, weight=1)

        Label(screen2, text="DECRYPT", font="Arial", fg="white", bg="#251c26").grid(row=0, column=0, sticky="w", padx=10, pady=5)

        text2 = Text(screen2, font="Roboto 10", fg="white", bg="#1b101c", wrap=WORD, bd=0)
        text2.insert(END, decrypted)
        text2.config(state=DISABLED)
        text2.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        code_entry.config(state=DISABLED)

    elif password == "":
        messagebox.showerror("Decryption", "No Password detected. Try again")
        code.set("")
        code_entry.config(state=NORMAL)
        code_entry.focus_set()

    elif password != "grasya":
        messagebox.showerror("Decryption", "Wrong Password. Please try again")
        code.set("")
        code_entry.config(state=NORMAL)
        code_entry.focus_set()


def encrypt():
    global code_entry, text1

    message = text1.get(1.0, END).strip()

    if not message:
        messagebox.showerror("Encryption", "You haven’t entered anything to encrypt. Try Again")
        return

    password=code.get()

    if password=="grasya":
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#251c26")
        screen1.resizable(True, True)

        screen1.rowconfigure(1, weight=1)
        screen1.columnconfigure(0, weight=1)


        if not message:
            messagebox.showerror("Encryption", "You need something to enter in order to proceed")
            return
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT", font="Arial", fg="white", bg="#251c26").place(x=10, y=0)

        text2=Text(screen1, font="Roboto 10", fg="white", bg="#1b101c", relief=GROOVE, wrap=WORD, bd=0)
        text2.insert(END, encrypt)
        text2.config(state=DISABLED)
        text2.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)


        copy_icon = PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Python\text encryption\copy.png")
        copy_icon = copy_icon.subsample(10, 10)
        screen1.copy_icon = copy_icon
        def copy_to_clipboard():
            screen1.clipboard_clear()
            screen1.clipboard_append(encrypt)
            screen1.update()

        copy_button = Button(screen1, image=copy_icon, bg="#251c26", fg="purple", command=copy_to_clipboard)
        copy_button.grid(row=0, column=0, sticky="e", padx=10, pady=5)

        code_entry.config(state=DISABLED)
    elif password=="":
        messagebox.showerror("Encryption", "No Password detected. Try again")
        code.set("")
        code_entry.config(state=NORMAL)
        code_entry.focus_set()

    elif password !="grasya":
        messagebox.showerror("Encryption", "Wrong Password. Please try again")
        code.set("")
        code_entry.config(state=NORMAL)
        code_entry.focus_set()



def main_screen():
    global screen
    global code
    global text1
    global code_entry

    screen=Tk()
    screen.geometry("375x398")
    screen.resizable(False, False)

    #icon
    image_icon = PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Python\text encryption\keys.png")
    screen.iconphoto(False, image_icon)
    screen.title("TxtCryptApp")
    screen.configure(bg="#343347")

    def reset():
        code.set("")
        text1.config(state=NORMAL)
        text1.delete(1.0, END)
        code_entry.config(state=NORMAL)

    Label(text ="Enter text for encryption and decryption", fg="white", bg="#1a1c26", font=("Calibri", 13)).place(x=10, y=10)
    text1=Text(font="Roboto 20", bg="#0e0f17", fg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter code to decrypt or encrypt", fg="white",bg="#1a1c26", font=("Calibri", 13)).place(x=10, y=170)

    code=StringVar()

    code_entry = Entry(textvariable=code, width=19, bd=0, font=("Arial", 25), show="*", bg="#1a1c26", fg="white")
    code_entry.place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=23, bg="#ab7fb0", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#735d78", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#3d2e3f", fg="white", bd=0, command=reset).place(x=10, y=300)



    screen.mainloop()

main_screen()