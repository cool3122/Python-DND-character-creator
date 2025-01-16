import tkinter as tk
import string

def open_Characer_Info_Window ():
    characterInfoWindow = tk.Toplevel(root)

    def character_Info_Save():
        fullName = fNameEntry.get() + " " + lNameEntry.get()
        name.set(fullName)
        race.set(raceEntry.get())
        characterInfoWindow.destroy()
    

    fNameLabel = tk.Label(characterInfoWindow, text = "First Name")
    fNameEntry = tk.Entry(characterInfoWindow)

    lNameLabel = tk.Label(characterInfoWindow, text = "Last Name")
    lNameEntry = tk.Entry(characterInfoWindow)

    raceLabel = tk.Label(characterInfoWindow, text = "Race")
    raceEntry = tk.Entry(characterInfoWindow)

    saveButton = tk.Button(characterInfoWindow, text = "Save and Close", command=character_Info_Save)

    characterInfoWindow.grid_columnconfigure(0, weight=1)
    characterInfoWindow.grid_columnconfigure(1, weight=1)

    fNameLabel.grid(column=0, row=0, padx=5, pady=5, sticky="nwes")
    fNameEntry.grid(column=1, row=0, padx=5, pady=5, sticky="nwes")

    lNameLabel.grid(column=0, row=1, padx=5, pady=5, sticky="nwes")
    lNameEntry.grid(column=1, row=1, padx=5, pady=5, sticky="nwes")

    raceLabel.grid(column=0, row=2, padx=5, pady=5, sticky="nwes")
    raceEntry.grid(column=1, row=2, padx=5, pady=5, sticky="nwes")

    saveButton.grid(column=0, row=3, padx=5, pady=5, columnspan=2, sticky="nwes")

    
root = tk.Tk()
root.title("DND Character Creation Tool")

name = tk.StringVar(value='')
race = tk.StringVar(value='') 

nameVar = name.get()

characterInfoButton = tk.Button(root, text = "Open Character Editing", command=open_Characer_Info_Window)

nameLabel = tk.Label(root, text= nameVar)

root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

nameLabel.grid(column=0, row =2, columnspan=2, padx=5, pady=5, sticky="nwes")

characterInfoButton.grid(column=0, row =3, columnspan=2, padx=5, pady=5, sticky="nwes")

root.mainloop()