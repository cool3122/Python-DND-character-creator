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

def character_stat_gen():
    characterStatWindow = tk.Toplevel(root)

    def character_stat_gen_save():
        dexterity = DexEntry.get()
        intelligence = IntEntry.get()
        wisdom = WisEntry.get()
        strength = StrEntry.get()
        constitution = ConEntry.get()
        charisma = ChaEntry.get()

        Dex.set(dexterity)
        Int.set(intelligence)
        Wis.set(wisdom)
        Str.set(strength)
        Con.set(constitution)
        Cha.set(charisma)
        characterStatWindow.destroy()

    DexLabel = tk.Label(characterStatWindow, text= "Dexterity")
    IntLabel = tk.Label(characterStatWindow, text= "Intelligence")
    WisLabel = tk.Label(characterStatWindow, text= "Wisdom")
    StrLabel = tk.Label(characterStatWindow, text= "Strength")
    ConLabel = tk.Label(characterStatWindow, text= "Constitution")
    ChaLabel = tk.Label(characterStatWindow, text= "Charisma")

    DexEntry = tk.Entry(characterStatWindow)
    IntEntry = tk.Entry(characterStatWindow)
    WisEntry = tk.Entry(characterStatWindow)
    StrEntry = tk.Entry(characterStatWindow)
    ConEntry = tk.Entry(characterStatWindow)
    ChaEntry = tk.Entry(characterStatWindow)

    save_Button = tk.Button(characterStatWindow, text = "Save and Close", command=character_stat_gen_save)

    

    
root = tk.Tk()
root.title("DND Character Creation Tool")

name = tk.StringVar(value='')
race = tk.StringVar(value='') 
Dex = tk.StringVar(value= '')
Int = tk.StringVar(value='')
Wis = tk.StringVar(value='')
Str = tk.StringVar(value='')
Con = tk.StringVar(value='') 
Cha = tk.StringVar(value='') 

characterInfoButton = tk.Button(root, text = "Open Character Editing", command=open_Characer_Info_Window)

nameLabel = tk.Label(root, textvariable= name)
raceLabel = tk.Label(root, textvariable= race)

root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

nameLabel.grid(column=0, row =2, columnspan=2, padx=5, pady=5, sticky="nwes")

characterInfoButton.grid(column=0, row =3, columnspan=2, padx=5, pady=5, sticky="nwes")

root.mainloop()