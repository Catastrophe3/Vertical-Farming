import tkinter as tk
from tkinter import messagebox
import ctypes


# database of top vertical farming plants
all_plants = {
    "lettuce": {"moisture": "moderate", "sunlight": "full sun to partial shade", "temperature": "45-75°F"},
    "kale": {"moisture": "moderate", "sunlight": "full sun", "temperature": "40-80°F"},
    "spinach": {"moisture": "moderate", "sunlight": "full sun to partial shade", "temperature": "35-75°F"},
    "basil": {"moisture": "moderate", "sunlight": "full sun", "temperature": "70-90°F"},
    "mint": {"moisture": "high", "sunlight": "partial shade to full sun", "temperature": "55-75°F"},
    "cilantro": {"moisture": "moderate", "sunlight": "full sun", "temperature": "50-85°F"},
    "strawberries": {"moisture": "moderate", "sunlight": "full sun", "temperature": "60-80°F"},
    "tomatoes": {"moisture": "moderate to high", "sunlight": "full sun", "temperature": "65-85°F"},
    "peppers": {"moisture": "moderate", "sunlight": "full sun", "temperature": "65-85°F"},
    "cucumbers": {"moisture": "high", "sunlight": "full sun", "temperature": "65-95°F"},
    "chard": {"moisture": "moderate", "sunlight": "full sun to partial shade", "temperature": "50-80°F"},
    "arugula": {"moisture": "moderate", "sunlight": "full sun to partial shade", "temperature": "40-75°F"},
    "mustard greens": {"moisture": "moderate", "sunlight": "full sun to partial shade", "temperature": "45-75°F"},
    "pak choi": {"moisture": "high", "sunlight": "full sun to partial shade", "temperature": "50-85°F"},
    "radishes": {"moisture": "moderate", "sunlight": "full sun", "temperature": "40-70°F"},
    "microgreens": {"moisture": "high", "sunlight": "indirect light to partial shade", "temperature": "60-75°F"},
    "collard greens": {"moisture": "moderate", "sunlight": "full sun to partial shade", "temperature": "40-75°F"},
    "rocket": {"moisture": "moderate", "sunlight": "full sun to partial shade", "temperature": "40-75°F"},
    "mizuna": {"moisture": "moderate", "sunlight": "full sun to partial shade", "temperature": "40-75°F"},
    "swiss chard": {"moisture": "moderate", "sunlight": "full sun to partial shade", "temperature": "50-80°F"},
    "baby kale": {"moisture": "moderate", "sunlight": "full sun", "temperature": "40-80°F"},
    "oregano": {"moisture": "low to moderate", "sunlight": "full sun", "temperature": "60-85°F"},
    "lemon balm": {"moisture": "moderate", "sunlight": "partial shade to full sun", "temperature": "55-75°F"},
    "zinnia flowers": {"moisture": "moderate", "sunlight": "full sun", "temperature": "70-95°F"},
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
        f"Temperature: {plant_data['temperature']}"
    )
    text_result.delete(1.0, tk.END)
    text_result.insert(tk.END, result)

def add_plant():
    name = entry_name.get().strip()
    moisture = entry_moisture.get().strip()
    sunlight = entry_sunlight.get().strip()
    temperature = entry_temperature.get().strip()

    if not name or not moisture or not sunlight or not temperature:
        messagebox.showerror("Error", "All fields must be filled!")
        return
    
    new_plant_database[name] = {"moisture": moisture, "sunlight": sunlight, "temperature": temperature}
    messagebox.showinfo("Success", f"{name.capitalize()} has been added to the database!")
    entry_name.delete(0, tk.END)
    entry_moisture.delete(0, tk.END)
    entry_sunlight.delete(0, tk.END)
    entry_temperature.delete(0, tk.END)

# Dashboard
dashboard_window = None  # Initialize dashboard_window as None

def open_dashboard():
    global dashboard_window  # Use the global variable
    if dashboard_window is None or not tk.Toplevel.winfo_exists(dashboard_window): # check if window exists
        dashboard_window = tk.Toplevel(root)
        dashboard_window.title("Dashboard")
        dashboard_window.geometry("800x600")
        dashboard_window.configure(bg=BG_COLOR)
        dashboard_window.protocol("WM_DELETE_WINDOW", close_dashboard) # handle closing window
        # Add content to the dashboard (example)
        dashboard_label = tk.Label(dashboard_window, text="Dashboard", font=("Ariel Bold", 30), bg=BG_COLOR, fg=FG_COLOR)
        dashboard_label.pack(pady=50)

def close_dashboard():
    global dashboard_window
    if dashboard_window:
        dashboard_window.destroy()
        dashboard_window = None




# Initialize GUI
root = tk.Tk()
root.title("Vertical Farming Software")
root.geometry("800x600")
root.configure(bg=BG_COLOR)

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)  # For Windows
except Exception:
    pass

# Tkinter DPI scaling
root.tk.call("tk", "scaling", 2.3)

# Dashboard Button
button_frame = tk.Frame(root, bg=BG_COLOR)  # Create frame for button
button_frame.pack(anchor=tk.NW, padx=10, pady=10)  # Pack frame to top left
dashboard_button = tk.Button(button_frame, text="Dashboard", font=("Helvetica Bold", 12), bg="#2ecc71", fg=FG_COLOR, command=open_dashboard)
dashboard_button.pack()  # Pack button into frame

# Search Framework
frame_search = tk.Frame(root, bg=BG_COLOR)
frame_search.pack(pady=(50,45)) # Added top padding of 0 and bottom padding of 20

# Search Framework
frame_search = tk.Frame(root, bg=BG_COLOR)
frame_search.pack(pady=20)
tk.Label(frame_search, text="Search for Plant:", font=("Arial", 14), bg=BG_COLOR, fg=FG_COLOR).grid(row=0, column=0, padx=10, pady=10)
entry_search = tk.Entry(frame_search, font=("Arial", 14), width=30)
entry_search.grid(row=0, column=1, padx=10, pady=20)
tk.Button(frame_search, text="Search", font=("Arial", 14), bg=BUTTON_COLOR, fg=FG_COLOR, command=search_plant).grid(row=0, column=2, padx=10, pady=10)

# Result Display
text_result = tk.Text(root, height=10, width=70, font=("Arial", 12), bg=TEXT_BG, fg=TEXT_FG)
text_result.pack(pady=(10, 0))

# Add Plant to database
frame_add = tk.Frame(root, bg=BG_COLOR)
frame_add.pack(pady=20)

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
tk.Label(frame_add, text="Temperature:", font=("Arial", 14), bg=BG_COLOR, fg=FG_COLOR).grid(row=4, column=0, padx=10, pady=10)
entry_temperature = tk.Entry(frame_add, font=("Arial", 14), width=30)
entry_temperature.grid(row=4, column=1, padx=10, pady=10)
tk.Button(frame_add, text="Add Plant", font=("Arial", 14), bg=BUTTON_COLOR, fg=FG_COLOR, command=add_plant).grid(row=5, column=0, columnspan=2, pady=20)

#Finally run
root.mainloop()
