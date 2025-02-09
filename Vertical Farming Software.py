import tkinter as tk
from tkinter import messagebox
import ctypes
from tkinter import ttk

BG_COLOR = "#bdd9bf"
FG_COLOR = "#2e7d32"
BUTTON_COLOR = "#2ecc71"

# Database for popular plant recommendations 
all_plants = {
    "Lettuce": {"Moisture": "Moderate", "Sunlight": "Full Sun To Partial Shade", "Temperature": "7-24°C"},
    "Kale": {"Moisture": "Moderate", "Sunlight": "Full Sun", "Temperature": "4-27°C"},
    "Spinach": {"Moisture": "Moderate", "Sunlight": "Full Sun To Partial Shade", "Temperature": "2-24°C"},
    "Basil": {"Moisture": "Moderate", "Sunlight": "Full Sun", "Temperature": "21-32°C"},
    "Mint": {"Moisture": "High", "Sunlight": "Partial Shade To Full Sun", "Temperature": "13-24°C"},
    "Cilantro": {"Moisture": "Moderate", "Sunlight": "Full Sun", "Temperature": "10-29°C"},
    "Strawberries": {"Moisture": "Moderate", "Sunlight": "Full Sun", "Temperature": "16-27°C"},
    "Tomatoes": {"Moisture": "Moderate To High", "Sunlight": "Full Sun", "Temperature": "18-29°C"},
    "Peppers": {"Moisture": "Moderate", "Sunlight": "Full Sun", "Temperature": "18-29°C"},
    "Cucumbers": {"Moisture": "High", "Sunlight": "Full Sun", "Temperature": "18-35°C"},
    "Chard": {"Moisture": "Moderate", "Sunlight": "Full Sun To Partial Shade", "Temperature": "10-27°C"},
    "Arugula": {"Moisture": "Moderate", "Sunlight": "Full Sun To Partial Shade", "Temperature": "4-24°C"},
    "Mustard Greens": {"Moisture": "Moderate", "Sunlight": "Full Sun To Partial Shade", "Temperature": "7-24°C"},
    "Pak Choi": {"Moisture": "High", "Sunlight": "Full Sun To Partial Shade", "Temperature": "10-29°C"},
    "Radishes": {"Moisture": "Moderate", "Sunlight": "Full Sun", "Temperature": "4-21°C"},
    "Microgreens": {"Moisture": "High", "Sunlight": "Indirect Light To Partial Shade", "Temperature": "16-24°C"},
    "Collard Greens": {"Moisture": "Moderate", "Sunlight": "Full Sun To Partial Shade", "Temperature": "4-24°C"},
    "Rocket": {"Moisture": "Moderate", "Sunlight": "Full Sun To Partial Shade", "Temperature": "4-24°C"},
    "Mizuna": {"Moisture": "Moderate", "Sunlight": "Full Sun To Partial Shade", "Temperature": "4-24°C"},
    "Swiss Chard": {"Moisture": "Moderate", "Sunlight": "Full Sun To Partial Shade", "Temperature": "10-27°C"},
    "Baby Kale": {"Moisture": "Moderate", "Sunlight": "Full Sun", "Temperature": "4-27°C"},
    "Oregano": {"Moisture": "Low To Moderate", "Sunlight": "Full Sun", "Temperature": "16-29°C"},
    "Lemon Balm": {"Moisture": "Moderate", "Sunlight": "Partial Shade To Full Sun", "Temperature": "13-24°C"},
    "Zinnia Flowers": {"Moisture": "Moderate", "Sunlight": "Full Sun", "Temperature": "21-35°C"}
}

new_plant_database = {}

def add_plant():
    name = entry_name.get().strip()
    moisture = entry_moisture.get().strip()
    light = entry_light.get().strip()
    temperature = entry_temperature.get().strip()

    if not name or not moisture or not light or not temperature:
        messagebox.showerror("Error", "All fields must be filled!")
        return

    new_plant_database[name] = {"moisture": moisture, "light": light, "temperature": temperature}
    messagebox.showinfo("Success", f"{name.capitalize()} has been added to the database!")
    entry_name.delete(0, tk.END)
    entry_moisture.delete(0, tk.END)
    entry_light.delete(0, tk.END)
    entry_temperature.delete(0, tk.END)

    # Refresh table if inventory window is open
    if inventory_window and inventory_table:
        inventory_table.insert("", "end", values=(name, moisture, light, temperature))

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
        dashboard_window.geometry(root.winfo_screenwith(), root.winfo_screenheight())  # Set window size
        dashboard_window.configure(bg="#FFFFFF")
        dashboard_window.protocol("WM_DELETE_WINDOW", close_dashboard)

        tk.Label(dashboard_window, text="Dashboard", font=("Arial Bold", 38), bg="#ece9e8", fg="#000000").pack(pady=30)

        #placeholder for the dashboard
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
        inventory_window.geometry(root.winfo_screenwith(), root.winfo_screenheight()) 
        inventory_window.configure(bg="#FFFFFF")
        inventory_window.protocol("WM_DELETE_WINDOW", close_inventory)

        tk.Label(inventory_window, text="Inventory", font=("Arial Bold", 38), bg="#ece9e8", fg="#000000").pack(pady=40)

        #Table Style
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 12) , rowheight=80, padx=30, pady=120) #Font of table data
        style.configure("Treeview.Heading", font=("Arial Bold", 18), padx=60, pady=60)  # Font for headers

        # Create table
        columns = ("Name", "Moisture", "Light", "Temperature")
        inventory_table = ttk.Treeview(inventory_window, columns=columns, show="headings", height=120)

        # Loop through table columns
        for col in columns:
            inventory_table.heading(col, text=col)
            inventory_table.column(col, width=150, anchor="center")

        inventory_table.pack(fill=tk.BOTH, expand=True, padx=20, pady=130)

        # Populate table with existing plants in database
        for name, data in new_plant_database.items():
            inventory_table.insert("", "end", values=(name, data["moisture"], data["light"], data["temperature"]))

def close_inventory():
    global inventory_window
    if inventory_window:
        inventory_window.destroy()
        inventory_window = None

def open_recommendations():
    global recommendations_window, recommendations_text
    recommendations_window = None  
    if recommendations_window is None or not recommendations_window.winfo_exists():

        recommendations_window = tk.Toplevel(root)
        recommendations_window.title("Plant Recommendations")
        inventory_window.geometry(root.winfo_screenwith(), root.winfo_screenheight()) 
        recommendations_window.configure(bg="#FFFFFF")
        recommendations_window.protocol("WM_DELETE_WINDOW", close_recommendations)

        tk.Label(recommendations_window, text="Plant Recommendations", font=("Arial Bold", 38), bg="#ece9e8", fg="#000000").pack(pady=40)

        #Table Styling
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 12) , rowheight=80, padx=30, pady=120) #Font of table data
        style.configure("Treeview.Heading", font=("Arial Bold", 18), padx=60, pady=60)  # Font for headers

        # Create table
        columns = ("Name", "Moisture", "Light", "Temperature")
        recommendations_table = ttk.Treeview(recommendations_window, columns=columns, show="headings", height=120)

        # Define column headings
        for col in columns:
            recommendations_table.heading(col, text=col)
            recommendations_table.column(col, width=150, anchor="center")

        recommendations_table.pack(fill=tk.BOTH, expand=True, padx=20, pady=130)
        for name, data in all_plants.items():
             recommendations_table.insert("", "end", values=(name, data["Moisture"], data["Sunlight"], data["Temperature"]))

def close_recommendations():
    global recommendations_window
    if recommendations_window:
        recommendations_window.destroy()
        recommendations_window = None

# Initialize GUI
root = tk.Tk()
root.title("Vertical Farming Software")
root.geometry("1000x800")
root.configure(bg=BG_COLOR)

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    pass

root.tk.call("tk", "scaling",1.9)

# Dashboard Button
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(anchor=tk.NW, padx=30, pady=30)
dashboard_button = tk.Button(button_frame, text="Dashboard", font=("Helvetica Bold", 18), bg="#2ecc71", fg="black", command=open_dashboard)
dashboard_button.pack()

# Inventory Button
inventory_button = tk.Button(button_frame, text="Inventory", font=("Helvetica Bold", 18), bg="#2ecc71", fg="black", command=open_inventory)
inventory_button.pack(pady=10)

# Recommendations
recommendations_button = tk.Button(button_frame, text="Recommendations", font=("Helvetica Bold", 18), bg="#2ecc71", fg="black", command=open_recommendations)
recommendations_button.pack(pady=2.5)



# Add Plant Frame
frame_add = tk.Frame(root, bg=BG_COLOR)
frame_add.pack(fill=tk.BOTH, expand=True, padx=30, pady=(0, 10))

# Input boxes for plant necessities
tk.Label(frame_add, text="Add New Plant", font=("Arial",62), bg=BG_COLOR, fg=("black")).pack(pady=(70))
tk.Label(frame_add, text="Name:", font=("Arial Bold", 20), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(35, 20))
entry_name = tk.Entry(frame_add, font=("Arial", 20), width=40)
entry_name.pack(pady=(0, 20))

tk.Label(frame_add, text="Moisture (RH%):", font=("Arial Bold", 20), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(15, 15))
entry_moisture = tk.Entry(frame_add, font=("Arial", 20), width=40)
entry_moisture.pack(pady=(0, 20))

tk.Label(frame_add, text="Light (lux):", font=("Arial Bold", 20), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(15, 15))
entry_light = tk.Entry(frame_add, font=("Arial", 20), width=40)
entry_light.pack(pady=(0, 20))

tk.Label(frame_add, text="Temperature (C):", font=("Arial Bold", 20), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(15, 15))
entry_temperature = tk.Entry(frame_add, font=("Arial", 20), width=40)
entry_temperature.pack(pady=(0, 15))

tk.Button(frame_add, text="Add Plant", font=("Ariel", 20), bg=BUTTON_COLOR, fg="#000000", command=add_plant, height=1, width=8).pack(pady=(30, 50))

root.mainloop()

# © DP & TP
