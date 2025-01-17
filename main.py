import tkinter as tk
import re
import random


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

def open_character_stat_gen():
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

    def roll_dice():
        for i in range(4):
            number = random.randint(1,6)
            buttons[i].config(text = f"Die {i + 1}: {number}")

    DexLabel = tk.Label(characterStatWindow, text= "Dexterity")
    IntLabel = tk.Label(characterStatWindow, text= "Intelligence")
    WisLabel = tk.Label(characterStatWindow, text= "Wisdom")
    StrLabel = tk.Label(characterStatWindow, text= "Strength")
    ConLabel = tk.Label(characterStatWindow, text= "Constitution")
    ChaLabel = tk.Label(characterStatWindow, text= "Charisma")

    totalLabel = tk.Label(characterStatWindow, text= "Total:")

    DexEntry = tk.Entry(characterStatWindow)
    IntEntry = tk.Entry(characterStatWindow)
    WisEntry = tk.Entry(characterStatWindow)
    StrEntry = tk.Entry(characterStatWindow)
    ConEntry = tk.Entry(characterStatWindow)
    ChaEntry = tk.Entry(characterStatWindow)

    rollButton = tk.Button(characterStatWindow, text = "Roll Dice", command=roll_dice)

    saveButtonStats = tk.Button(characterStatWindow, text = "Save and Close", command=character_stat_gen_save)

    buttons = []

    totalLabel.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nwes")
    rollButton.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nwes")
    saveButtonStats.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nwes")

    def update_selection_count(change):
        nonlocal selection_count  # Access the variable from the outer scope
        selection_count += change

        # Disable or enable buttons based on the current selection count
        if selection_count == 3:
            for i, button in enumerate(buttons):
                if not selected_buttons[i]:  # Disable only unselected buttons
                    button.config(state="disabled")
            total = sum(selected_buttons_values)
            totalLabel.config(text = f"Total: {total}")
        else:
            for button in buttons:
                button.config(state="normal")  # Re-enable all buttons

    def toggle_button(button_index):
        # Check if the button is already selected
        if selected_buttons[button_index]:
            # Deselect the button
            selected_buttons[button_index] = False
            buttons[button_index].config(bg="SystemButtonFace")  # Reset to default color
            update_selection_count(-1)  # Decrease the count
        else:
            if selection_count < 3:  # Allow selection only if less than 3 are selected
                # Select the button
                selected_buttons[button_index] = True
                text_of_button = buttons[button_index].cget("text")
                value_of_button = re.findall(r'\d+', text_of_button)
                value = value_of_button[-1]
                selected_buttons_values[button_index] = value
                buttons[button_index].config(bg="lightblue")  # Change to "selected" color
                update_selection_count(1)  # Increase the count
    

    
    selected_buttons_values = [0,0,0,0]
    selected_buttons = [False, False, False, False]
    selection_count = 0

    for i in range(4):
        button = tk.Button(characterStatWindow, text=f"Button {i + 1}", command=lambda i=i: toggle_button(i))
        if i == 0:
            button.grid(row = 0, column = 0, pady=5, padx=10)
        elif i == 1:
            button.grid(row = 1, column = 0, pady=5, padx=10)
        elif i == 2:
            button.grid(row = 0, column = 1, pady=5, padx=10)
        else:
            button.grid(row = 1, column = 1, pady=5, padx=10)

        buttons.append(button)
    


    
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
characterStatGenButton = tk.Button(root, text = "Open Character Stat Generator", command=open_character_stat_gen)

nameLabel = tk.Label(root, textvariable= name)
raceLabel = tk.Label(root, textvariable= race)

root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

nameLabel.grid(column=0, row =2, columnspan=2, padx=5, pady=5, sticky="nwes")

characterInfoButton.grid(column=0, row =3, columnspan=2, padx=5, pady=5, sticky="nwes")
characterStatGenButton.grid(column=0, row =4, columnspan=2, padx=5, pady=5, sticky="nwes")

root.mainloop()