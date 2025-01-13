import tkinter as tk
from tkinter import messagebox
import ctypes

BG_COLOR = "#3498db"
FG_COLOR = "#ffffff"
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

# Dashboard functions (same as before)
dashboard_window = None

def open_dashboard():
    global dashboard_window
    if dashboard_window is None or not tk.Toplevel.winfo_exists(dashboard_window):
        dashboard_window = tk.Toplevel(root)
        dashboard_window.title("Dashboard")
        dashboard_window.geometry("800x600")  # You might want to adjust this
        dashboard_window.configure(bg="#FFFFFF")
        dashboard_window.protocol("WM_DELETE_WINDOW", close_dashboard)
        dashboard_label = tk.Label(dashboard_window, text="Dashboard", font=("Ariel Bold", 38), bg="#ece9e8", fg="#000000")
        dashboard_label.pack(pady=50)

def close_dashboard():
    global dashboard_window
    if dashboard_window:
        dashboard_window.destroy()
        dashboard_window = None

# Initialize GUI
root = tk.Tk()
root.title("Vertical Farming Software")
root.geometry("1000x800")  # Larger window size
root.configure(bg=BG_COLOR)

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)  # For Windows DPI awareness
except Exception:
    pass

# Scaling (improved)
root.tk.call("tk", "scaling", 1.5) #Adjust this number to change the scaling

# Dashboard Button (improved layout)
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(anchor=tk.NW, padx=30, pady=30)  # Increased padding
dashboard_button = tk.Button(button_frame, text="Dashboard", font=("Helvetica Bold", 18), bg="#2ecc71", fg=FG_COLOR, command=open_dashboard)  # Enlarged font size
dashboard_button.pack()

# Add Plant Frame (improved layout and font sizes)
frame_add = tk.Frame(root, bg=BG_COLOR)
frame_add.pack(fill=tk.BOTH, expand=True, padx=30, pady=(0,30))  # Added more padding and increased size

tk.Label(frame_add, text="Add New Plant", font=("Arial Bold", 48), bg=BG_COLOR, fg="#000000").pack(pady=(30, 30))  # Increased font size and padding
tk.Label(frame_add, text="Name:", font=("Arial", 18), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(35, 35))
entry_name = tk.Entry(frame_add, font=("Arial", 18), width=40)  # Increased font size and width
entry_name.pack(pady=(0,15))

tk.Label(frame_add, text="Moisture:", font=("Arial", 18), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(15, 10))
entry_moisture = tk.Entry(frame_add, font=("Arial", 18), width=40)
entry_moisture.pack(pady=(0,15))

tk.Label(frame_add, text="Sunlight:", font=("Arial", 18), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(15, 10))
entry_sunlight = tk.Entry(frame_add, font=("Arial", 18), width=40)
entry_sunlight.pack(pady=(0,15))

tk.Label(frame_add, text="Temperature:", font=("Arial", 18), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(15, 10))
entry_temperature = tk.Entry(frame_add, font=("Arial", 18), width=40)
entry_temperature.pack(pady=(0,15))

tk.Button(frame_add, text="Add Plant", font=("Arial", 18), bg=BUTTON_COLOR, fg=FG_COLOR, command=add_plant).pack(pady=(30, 40))  # Increased font size and padding

root.mainloop()
