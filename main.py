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

    dexTotal = 0

    def character_stat_gen_save():
        Dex.set(dexTotal)
        Int.set(intTotal)
        Wis.set(wisTotal)
        Str.set(strTotal)
        Con.set(conTotal)
        Cha.set(chaTotal)
        characterStatWindow.destroy()

    def roll_dice():
        nonlocal selection_count  # Access selection_count from the outer scope

        # Roll new values for all buttons
        for i in range(4):
            number = random.randint(1, 6)
            diceButtons[i].config(text=f"Die {i + 1}: {number}")

            # If the button is currently selected, update its value in selected_buttons_values
            if selected_buttons[i]:
                selected_buttons_values[i] = number

        # Recalculate the total based on the selected buttons
        total = sum(selected_buttons_values)
        
        # Update the totalLabel with the new total
        totalLabel.config(text=f"Total: {total}")

    DexLabel = tk.Label(characterStatWindow, text= "Dexterity")
    IntLabel = tk.Label(characterStatWindow, text= "Intelligence")
    WisLabel = tk.Label(characterStatWindow, text= "Wisdom")
    StrLabel = tk.Label(characterStatWindow, text= "Strength")
    ConLabel = tk.Label(characterStatWindow, text= "Constitution")
    ChaLabel = tk.Label(characterStatWindow, text= "Charisma")

    totalLabel = tk.Label(characterStatWindow, text= "Total:")

    DexEntry = tk.Radiobutton(characterStatWindow)
    IntEntry = tk.Radiobutton(characterStatWindow)
    WisEntry = tk.Radiobutton(characterStatWindow)
    StrEntry = tk.Radiobutton(characterStatWindow)
    ConEntry = tk.Radiobutton(characterStatWindow)
    ChaEntry = tk.Radiobutton(characterStatWindow)

    rollButton = tk.Button(characterStatWindow, text = "Roll Dice", command=roll_dice)

   # selectStatButton = tk.Button(characterStatWindow, text = "Select Stat", command=select_stat)

    saveButtonStats = tk.Button(characterStatWindow, text = "Save and Close", command=character_stat_gen_save)

    diceButtons = [] # Array of buttons (used for dice button generation)

   # statNames = ["Dexterity" , "Intelligence" , ]

    totalLabel.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="nwes") # creates the totalLabel (will display the total value of the selected dice)
   # selectStatButton.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky="nwes") # creates the selectStatButton (will apply the total value to the stat that is selected)
    rollButton.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky="nwes") # creates the rollButton (will change the values of the dice buttons)
    saveButtonStats.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky="nwes") # creates the saveButtonStats (will save the stats to the stringVars which is passed down to mainloop)

    def update_selection_count(change):
        nonlocal selection_count  # Access the variable from the outer scope
        selection_count += change # Changes selection count based on whether a button is selected or unselected (see toggle_button for how it was done)
        total = sum(selected_buttons_values) # Adds the total values of each of the dice rolls together
        totalLabel.config(text = f"Total: {total}") # Changes the totalLabel based on the selected buttons
        
        # Disable or enable buttons based on the current selection count
        if selection_count == 3: # If three buttons are selected
            # Disables the button that is not selected
            for i, button in enumerate(diceButtons):
                if not selected_buttons[i]:  # Disable only unselected buttons
                    button.config(state="disabled") #changes state to disabled
        else: # If less than three buttons are currently selected 
            for button in diceButtons:
                button.config(state="normal")  # Re-enable all buttons

    # Sets the button to either "Selected" or "Unselected" (this would have been easier to implement with radio or checkboxes but I will keep going through with it)
    def toggle_button(button_index):
        # Check if the button is already selected
        if selected_buttons[button_index]:
            # Deselect the button
            selected_buttons[button_index] = False
            diceButtons[button_index].config(bg="SystemButtonFace")  # Reset to default color
            selected_buttons_values[button_index] = 0 # Sets the buttons value to 0 as we only care about selected buttons
            update_selection_count(-1)  # Decrease the count of selected buttons
        else:
            if selection_count < 3:  # Allow selection only if less than 3 are selected
                # Select the button
                selected_buttons[button_index] = True #S ets the selected button to true if it was not already selected
                text_of_button = diceButtons[button_index].cget("text") # Gets the text of the button (again could have set this when rolled but keeping this for now)
                value_of_button = re.findall(r'\d+', text_of_button) # Selects all numbers in the button's text
                value = int(value_of_button[-1]) #Selects the last number in string
                selected_buttons_values[button_index] = value # Sets the button's value to above number
                diceButtons[button_index].config(bg="lightblue")  # Change to "selected" color
                update_selection_count(1)  # Increase the count of selected buttons
    

    
    selected_buttons_values = [0,0,0,0]
    selected_buttons = [False, False, False, False]
    selection_count = 0
    selection_count2 = 0

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

        diceButtons.append(button)
    
    def select_stat():
       print("hi")
       """
       for i in range(6):
           label = tk.Label(characterStatWindow, text=f"Button {}")
           button = tk."""
    
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