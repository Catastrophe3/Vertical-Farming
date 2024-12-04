import tkinter as tk
from tkinter import messagebox

# Pre-defined plant database
all_plants = {
    "lettuce": {"moisture": "moderate", "sunlight": "full sun to partial shade", "nutrients": "low to moderate"},
    "kale": {"moisture": "moderate", "sunlight": "full sun", "nutrients": "moderate"},
    # ... (add other plants here as per your database)
}

new_plant_database = {}

# Colors
BG_COLOR = "#f4f6f7"
FG_COLOR = "#2d3436"
HIGHLIGHT_COLOR = "#0984e3"
BUTTON_COLOR = "#74b9ff"
TEXT_BG = "#dfe6e9"
TEXT_FG = "#2c3e50"

def search_plant():
    plant_name = entry_search.get().strip().lower()
    if plant_name in all_plants:
        plant_data = all_plants[plant_name]
    elif plant_name in new_plant_database:
        plant_data = new_plant_database[plant_name]
    else:
        messagebox.showerror("Error", "Plant not found!")
        return

    result = (
        f"Plant: {plant_name.capitalize()}\n"
        f"Moisture: {plant_data['moisture']}\n"
        f"Sunlight: {plant_data['sunlight']}\n"
        f"Nutrients: {plant_data['nutrients']}"
    )
    text_result.delete(1.0, tk.END)
    text_result.insert(tk.END, result)

def add_plant():
    name = entry_name.get().strip().lower()
    moisture = entry_moisture.get().strip().lower()
    sunlight = entry_sunlight.get().strip().lower()
    nutrients = entry_nutrients.get().strip().lower()

    if not name or not moisture or not sunlight or not nutrients:
        messagebox.showerror("Error", "All fields must be filled!")
        return

    new_plant_database[name] = {"moisture": moisture, "sunlight": sunlight, "nutrients": nutrients}
    messagebox.showinfo("Success", f"{name.capitalize()} has been added to the database!")
    entry_name.delete(0, tk.END)
    entry_moisture.delete(0, tk.END)
    entry_sunlight.delete(0, tk.END)
    entry_nutrients.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Vertical Farming Software")
root.geometry("800x600")
root.configure(bg=BG_COLOR)

# Search Frame
frame_search = tk.Frame(root, bg=BG_COLOR)
frame_search.pack(pady=20)
tk.Label(frame_search, text="Search for Plant:", font=("Arial", 14), bg=BG_COLOR, fg=FG_COLOR).grid(row=0, column=0, padx=10, pady=10)
entry_search = tk.Entry(frame_search, font=("Arial", 14), width=30)
entry_search.grid(row=0, column=1, padx=10, pady=10)
tk.Button(frame_search, text="Search", font=("Arial", 14), bg=BUTTON_COLOR, fg=FG_COLOR, command=search_plant).grid(row=0, column=2, padx=10, pady=10)

# Result Display
text_result = tk.Text(root, height=10, width=70, font=("Arial", 12), bg=TEXT_BG, fg=TEXT_FG)
text_result.pack(pady=20)

# Add Plant Frame
frame_add = tk.Frame(root, bg=BG_COLOR)
frame_add.pack(pady=10)
tk.Label(frame_add, text="Add New Plant", font=("Arial Bold", 16), bg=BG_COLOR, fg=FG_COLOR).grid(row=0, column=0, columnspan=2, pady=10)
tk.Label(frame_add, text="Name:", font=("Arial", 14), bg=BG_COLOR, fg=FG_COLOR).grid(row=1, column=0, padx=10, pady=10)
entry_name = tk.Entry(frame_add, font=("Arial", 14), width=30)
entry_name.grid(row=1, column=1, padx=10, pady=10)
tk.Label(frame_add, text="Moisture:", font=("Arial", 14), bg=BG_COLOR, fg=FG_COLOR).grid(row=2, column=0, padx=10, pady=10)
entry_moisture = tk.Entry(frame_add, font=("Arial", 14), width=30)
entry_moisture.grid(row=2, column=1, padx=10, pady=10)
tk.Label(frame_add, text="Sunlight:", font=("Arial", 14), bg=BG_COLOR, fg=FG_COLOR).grid(row=3, column=0, padx=10, pady=10)
entry_sunlight = tk.Entry(frame_add, font=("Arial", 14), width=30)
entry_sunlight.grid(row=3, column=1, padx=10, pady=10)
tk.Label(frame_add, text="Nutrients:", font=("Arial", 14), bg=BG_COLOR, fg=FG_COLOR).grid(row=4, column=0, padx=10, pady=10)
entry_nutrients = tk.Entry(frame_add, font=("Arial", 14), width=30)
entry_nutrients.grid(row=4, column=1, padx=10, pady=10)
tk.Button(frame_add, text="Add Plant", font=("Arial", 14), bg=BUTTON_COLOR, fg=FG_COLOR, command=add_plant).grid(row=5, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
