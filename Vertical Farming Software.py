import tkinter as tk
from tkinter import messagebox
import ctypes
from tkinter import ttk

BG_COLOR = "#bdd9bf"
FG_COLOR = "#2e7d32"
BUTTON_COLOR = "#2ecc71"

# Database of top vertical farming plants (unchanged)
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

    # Refresh table if inventory window is open
    if inventory_window and inventory_table:
        inventory_table.insert("", "end", values=(name, moisture, sunlight, temperature))

# Inventory functions 
inventory_window = None
inventory_table = None

# Dashboard functions 
dashboard_window = None

def open_dashboard():
    global dashboard_window
    if dashboard_window is None or not tk.Toplevel.winfo_exists(dashboard_window):
        dashboard_window = tk.Toplevel(root)
        dashboard_window.title("Dashboard")
        dashboard_window.geometry("800x600")  # Set appropriate size
        dashboard_window.configure(bg="#FFFFFF")
        dashboard_window.protocol("WM_DELETE_WINDOW", close_dashboard)

        tk.Label(dashboard_window, text="Dashboard", font=("Arial Bold", 38), bg="#ece9e8", fg="#000000").pack(pady=20)

        # Add placeholder content for the dashboard
        tk.Label(dashboard_window, text="Welcome to the Dashboard!", font=("Arial", 18), bg="#FFFFFF", fg="#000000").pack(pady=60)
        tk.Label(dashboard_window, text="This area will display analytics or information as needed.", font=("Arial", 14), bg="#FFFFFF", fg="#000000").pack(pady=10)

def close_dashboard():
    global dashboard_window
    if dashboard_window:
        dashboard_window.destroy()
        dashboard_window = None

def open_inventory():
    global inventory_window, inventory_table
    if inventory_window is None or not tk.Toplevel.winfo_exists(inventory_window):
        inventory_window = tk.Toplevel(root)
        inventory_window.title("Inventory")
        inventory_window.geometry("800x600")
        inventory_window.configure(bg="#FFFFFF")
        inventory_window.protocol("WM_DELETE_WINDOW", close_inventory)

        tk.Label(inventory_window, text="Inventory", font=("Ariel Bold", 38), bg="#ece9e8", fg="#000000").pack(pady=20)

        #Table Styling
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 12) , rowheight=80, padx=30, pady=120) #Font of table data
        style.configure("Treeview.Heading", font=("Arial Bold", 18), padx=60, pady=60)  # Font for headers

        # Create table
        columns = ("Name", "Moisture", "Sunlight", "Temperature")
        inventory_table = ttk.Treeview(inventory_window, columns=columns, show="headings", height=100)

        # Define column headings
        for col in columns:
            inventory_table.heading(col, text=col)
            inventory_table.column(col, width=150, anchor="center")

        inventory_table.pack(fill=tk.BOTH, expand=True, padx=20, pady=110)

        # Populate table with existing plants
        for name, data in new_plant_database.items():
            inventory_table.insert("", "end", values=(name, data["moisture"], data["sunlight"], data["temperature"]))

def close_inventory():
    global inventory_window
    if inventory_window:
        inventory_window.destroy()
        inventory_window = None

# Initialize GUI
root = tk.Tk()
root.title("Vertical Farming Software")
root.geometry("1000x800")
root.configure(bg=BG_COLOR)

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

root.tk.call("tk", "scaling", 1.9)

# Dashboard Button
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(anchor=tk.NW, padx=30, pady=30)
dashboard_button = tk.Button(button_frame, text="Dashboard", font=("Helvetica Bold", 18), bg="#2ecc71", fg="black", command=open_dashboard)
dashboard_button.pack()

# Inventory Button
inventory_button = tk.Button(button_frame, text="Inventory", font=("Helvetica Bold", 18), bg="#2ecc71", fg="black", command=open_inventory)
inventory_button.pack(pady=10)

# Add Plant Frame
frame_add = tk.Frame(root, bg=BG_COLOR)
frame_add.pack(fill=tk.BOTH, expand=True, padx=30, pady=(0, 30))

tk.Label(frame_add, text="Add New Plant", font=("Ariel Bold", 62), bg=BG_COLOR, fg=("black")).pack(pady=(30, 45))
tk.Label(frame_add, text="Name:", font=("Arial Bold", 20), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(35, 15))
entry_name = tk.Entry(frame_add, font=("Arial", 20), width=40)
entry_name.pack(pady=(0, 15))

tk.Label(frame_add, text="Moisture:", font=("Arial Bold", 20), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(15, 15))
entry_moisture = tk.Entry(frame_add, font=("Arial", 20), width=40)
entry_moisture.pack(pady=(0, 15))

tk.Label(frame_add, text="Sunlight:", font=("Arial Bold", 20), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(15, 15))
entry_sunlight = tk.Entry(frame_add, font=("Arial", 20), width=40)
entry_sunlight.pack(pady=(0, 15))

tk.Label(frame_add, text="Temperature:", font=("Arial Bold", 20), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(15, 15))
entry_temperature = tk.Entry(frame_add, font=("Arial", 20), width=40)
entry_temperature.pack(pady=(0, 15))

tk.Button(frame_add, text="Add Plant", font=("Ariel", 20), bg=BUTTON_COLOR, fg="#000000", command=add_plant, height=1, width=8).pack(pady=(30, 50))

root.mainloop()
