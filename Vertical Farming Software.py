import tkinter as tk
from tkinter import messagebox
import ctypes
from tkinter import ttk

BG_COLOR = "#bdd9bf"
FG_COLOR = "#2e7d32"
BUTTON_COLOR = "#2ecc71"

# Database for popular plant recommendations 
pop_plants = {
    "Lettuce": {"Light": "10,000-20,000", "Humidity": "50-70%", "Temperature": "7-24°C"},
    "Kale": {"Light": "20,000-30,000", "Humidity": "40-60%", "Temperature": "4-27°C"},
    "Spinach": {"Light": "10,000-20,000", "Humidity": "45-65%", "Temperature": "2-24°C"},
    "Basil": {"Light": "25,000-50,000", "Humidity": "40-60%", "Temperature": "21-32°C"},
    "Mint": {"Light": "15,000-25,000", "Humidity": "50-75%", "Temperature": "13-24°C"},
    "Cilantro": {"Light": "20,000-30,000", "Humidity": "50-70%", "Temperature": "10-29°C"},
    "Strawberries": {"Light": "25,000-35,000", "Humidity": "50-80%", "Temperature": "16-27°C"},
    "Tomatoes": {"Light": "30,000-50,000", "Humidity": "50-70%", "Temperature": "18-29°C"},
    "Peppers": {"Light": "25,000-50,000", "Humidity": "50-70%", "Temperature": "18-29°C"},
    "Cucumbers": {"Light": "30,000-50,000", "Humidity": "60-80%", "Temperature": "18-35°C"},
    "Chard": {"Light": "15,000-30,000", "Humidity": "50-70%", "Temperature": "10-27°C"},
    "Arugula": {"Light": "10,000-20,000", "Humidity": "50-70%", "Temperature": "4-24°C"},
    "Mustard Greens": {"Light": "15,000-25,000", "Humidity": "50-70%", "Temperature": "7-24°C"},
    "Pak Choi": {"Light": "10,000-25,000", "Humidity": "60-80%", "Temperature": "10-29°C"},
    "Radishes": {"Light": "20,000-30,000", "Humidity": "50-70%", "Temperature": "4-21°C"},
    "Microgreens": {"Light": "5,000-15,000", "Humidity": "50-80%", "Temperature": "16-24°C"},
    "Collard Greens": {"Light": "15,000-25,000", "Humidity": "50-70%", "Temperature": "4-24°C"},
    "Arugula": {"Light": "10,000-20,000", "Humidity": "50-70%", "Temperature": "4-24°C"},
    "Mizuna": {"Light": "10,000-20,000", "Humidity": "50-70%", "Temperature": "4-24°C"},
    "Swiss Chard": {"Light": "15,000-30,000", "Humidity": "50-70%", "Temperature": "10-27°C"},
    "Baby Kale": {"Light": "20,000-30,000", "Humidity": "40-60%", "Temperature": "4-27°C"},
    "Oregano": {"Light": "30,000-50,000", "Humidity": "40-60%", "Temperature": "16-29°C"},
    "Lemon Balm": {"Light": "15,000-25,000", "Humidity": "50-70%", "Temperature": "13-24°C"},
    "Zinnia Flowers": {"Light": "30,000-60,000", "Humidity": "40-60%", "Temperature": "21-35°C"}
}

new_plant_database = {}

def add_plant():
    #Prep User Input
    name = entry_name.get().strip()
    humidity = entry_humidity.get().strip()
    light = entry_light.get().strip()
    temperature = entry_temperature.get().strip()
    #Input Error Handling

    # Ensure all fields are filled
    if not name or not humidity or not light or not temperature:
        messagebox.showerror("Error", "All fields must be filled!")
        return
    # Ensure sensor fields are integers
    if not all(any(char.isdigit() for char in value) for value in [humidity, light, temperature]):
        messagebox.showerror("Error", "Humidity, Light, and Temperature must contain at least one number!")
        return

 
    # Add to inventory database
    new_plant_database[name] = {"Humidity": humidity, "Light": light, "Temperature": temperature}
    messagebox.showinfo("Success!", f"{name.capitalize()} has been added to the database!")
    # Clear input boxes
    entry_name.delete(0, tk.END)
    entry_humidity.delete(0, tk.END)
    entry_light.delete(0, tk.END)
    entry_temperature.delete(0, tk.END)

    # Refresh table if inventory window is open
    if inventory_window and inventory_table:
        inventory_table.insert("", "end", values=(name, humidity, light, temperature))

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
        dashboard_window.geometry(f"{screen_width}x{screen_height}+0+0")
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
        inventory_window.geometry(f"{screen_width}x{screen_height}+0+0")
        inventory_window.configure(bg="#FFFFFF")
        inventory_window.protocol("WM_DELETE_WINDOW", close_inventory)

        tk.Label(inventory_window, text="Inventory", font=("Arial Bold", 38), bg="#ece9e8", fg="#000000").pack(pady=40)

        #Table Style
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 12) , rowheight=80, padx=30, pady=120) #Font of table data
        style.configure("Treeview.Heading", font=("Arial Bold", 18), padx=60, pady=60)  # Font for headers

        # Create table
        columns = ("Name", "Humidity (RH%)", "Light (lux)", "Temperature (C)")
        inventory_table = ttk.Treeview(inventory_window, columns=columns, show="headings", height=120)

        # Loop through table columns
        for col in columns:
            inventory_table.heading(col, text=col)
            inventory_table.column(col, width=150, anchor="center")

        inventory_table.pack(fill=tk.BOTH, expand=True, padx=20, pady=130)

        # Populate table with existing plants in database
        for name, data in new_plant_database.items():
            inventory_table.insert("", "end", values=(name, data["Humidity"], data["Light"], data["Temperature"]))

def close_inventory():
    global inventory_window
    if inventory_window:
        inventory_window.destroy()
        inventory_window = None

def open_recommendations():
    global recommendations_window, recommendations_text
    recommendations_window = None  
    if recommendations_window is None:

        recommendations_window = tk.Toplevel(root)
        recommendations_window.title("Plant Recommendations")
        recommendations_window.geometry(f"{screen_width}x{screen_height}+0+0")
        recommendations_window.configure(bg="#FFFFFF")
        recommendations_window.protocol("WM_DELETE_WINDOW", close_recommendations)

        tk.Label(recommendations_window, text="Plant Recommendations", font=("Arial Bold", 38), bg="#ece9e8", fg="#000000").pack(pady=40)

        #Table Styling
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 12) , rowheight=80, padx=30, pady=120) #Font of table data
        style.configure("Treeview.Heading", font=("Arial Bold", 18), padx=60, pady=60)  # Font for headers

        # Create table
        columns = ("Name", "Humidity (RH%)", "Light (lux)", "Temperature (C)")
        recommendations_table = ttk.Treeview(recommendations_window, columns=columns, show="headings", height=120)

        # Define column headings
        for col in columns:
            recommendations_table.heading(col, text=col)
            recommendations_table.column(col, width=150, anchor="center")

        recommendations_table.pack(fill=tk.BOTH, expand=True, padx=20, pady=130)
        for name, data in pop_plants.items():
             recommendations_table.insert("", "end", values=(name, data["Humidity"], data["Light"], data["Temperature"]))

def close_recommendations():
    global recommendations_window
    if recommendations_window:
        recommendations_window.destroy()
        recommendations_window = None

# Initialize GUI
root = tk.Tk()
root.title("Vertical Farming Software")
root.state('normal')

root.update()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


root.configure(bg=BG_COLOR)

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    pass

root.tk.call("tk", "scaling",2.2)
root.state('zoomed')

root.update_idletasks()  

width, height = root.winfo_screenwidth(), root.winfo_screenheight()


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


# Create scrollable canvas
# Scrollable Main Frame
main_frame = tk.Frame(root, bg=BG_COLOR)
main_frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(main_frame, bg=BG_COLOR)
scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
canvas.configure(yscrollcommand=scrollbar.set)


# Configure canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Bind mouse wheel scrolling
def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
canvas.bind_all("<MouseWheel>", _on_mousewheel)
canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))
canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))


# Create centered container frame
center_frame = tk.Frame(canvas, bg=BG_COLOR)
# Function to center the frame
def center_frame_position():
    canvas.update_idletasks()
    x = (canvas.winfo_width() - center_frame.winfo_reqwidth()) / 2
    y = (canvas.winfo_height() - center_frame.winfo_reqheight()) / 2
    canvas.coords(center_frame_id, x, y)

# Create centered container frame
center_frame = tk.Frame(canvas, bg=BG_COLOR)
center_frame_id = canvas.create_window(0, 0, window=center_frame, anchor="nw")

# Bind resize event to center the frame
canvas.bind("<Configure>", lambda e: center_frame_position())


# Create content frame inside centered container
frame_add = tk.Frame(center_frame, bg=BG_COLOR)
frame_add.pack()


# Input boxes for plant necessities
tk.Label(frame_add, text="Add New Plant", font=("Arial",45), bg=BG_COLOR, fg=("black")).pack(pady=(45), anchor="center")


tk.Label(frame_add, text="Name:", font=("Arial Bold", 20), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(25, 10), anchor="center")


entry_name = tk.Entry(frame_add, font=("Arial", 20), width=40)
entry_name.pack(pady=(0, 20), anchor="center")


tk.Label(frame_add, text="Humidity (RH%):", font=("Arial Bold", 20), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(15, 15), anchor="center")

entry_humidity = tk.Entry(frame_add, font=("Arial", 20), width=40)
entry_humidity.pack(pady=(0, 20), anchor="center")

tk.Label(frame_add, text="Light (Lux):", font=("Arial Bold", 20), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(15, 15), anchor="center")

entry_light = tk.Entry(frame_add, font=("Arial", 20), width=40)
entry_light.pack(pady=(0, 20))

tk.Label(frame_add, text="Temperature (C):", font=("Arial Bold", 20), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(15, 15), anchor="center")

entry_temperature = tk.Entry(frame_add, font=("Arial", 20), width=40)
entry_temperature.pack(pady=(0, 15), anchor="center")


tk.Button(frame_add, text="Add Plant", font=("Ariel", 20), bg=BUTTON_COLOR, fg="#000000", command=add_plant, height=1, width=8).pack(pady=(30, 50), anchor="center")


# Update scroll region when window is resized
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
    center_frame_position()

frame_add.bind("<Configure>", on_frame_configure)

root.mainloop()


# © DP & TP 2025
