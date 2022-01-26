import tkinter as tk

window = tk.Tk(className='De lichtknop!')
window.configure(bg='black')
window.geometry("300x250")

welkNummer = 1
color = ('black', 'yellow')
aanOfUit = ('Het licht is uit!', 'Het licht is aan!')


def Myclick():
    global welkNummer
    window.configure(bg=color[welkNummer])
    button['text'] = aanOfUit[welkNummer]
    print(aanOfUit[welkNummer])

    welkNummer += 1
    if welkNummer > 1:
        welkNummer = 0


button = tk.Button(text='Het licht is uit!', bg="white", fg="black", width=15, height=5, command=Myclick)
button.pack(pady=50, padx=50)

window.mainloop()
