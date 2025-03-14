import tkinter as tk
from tkinter import messagebox
import ctypes
from tkinter import ttk
import serial
import math

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
    "Rocket": {"Light": "10,000-20,000", "Humidity": "50-70%", "Temperature": "4-24°C"},
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
    if not name or not humidity or not light or not temperature:
        messagebox.showerror("Error", "All fields must be filled!")
        return
    if humidity.isdigit and light.isdigit and temperature.isdigit:
        pass
    else:
        messagebox.showerror("Error", "humidity, Light, and Temperature must be a range/number!")
        return
    
    # Add to inventory database
    new_plant_database[name] = {"Humidity": humidity, "Light": light, "Temp": temperature}
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

def datasplice(numrange):
    numrange = numrange.strip('%')  # Remove the percentage sign if present
    if '-' in numrange:
        # Split into two parts
        rangestart, rangeend = numrange.split('-')
        return int(rangestart), int(rangeend)
    else:
        # If there's no range, return the number with None as the second value
        return int(numrange), None


def get_most_recent_plant():
    if new_plant_database:
        # Get the last added plant name
        most_recent_plant = list(new_plant_database.keys())[-1]
        return most_recent_plant
    else:
        return None  # or you can return an empty string or a message if no plants are added
          
        

def open_dashboard():
    global dashboard_window
    if dashboard_window is None or not tk.Toplevel.winfo_exists(dashboard_window):
        dashboard_window = tk.Toplevel(root)
        dashboard_window.title("Dashboard")
        dashboard_window.geometry(f"{screen_width}x{screen_height}+0+0")
        dashboard_window.configure(bg="#FFFFFF")
        dashboard_window.protocol("WM_DELETE_WINDOW", close_dashboard)

        tk.Label(dashboard_window, text="Dashboard", font=("Arial Bold", 38), bg="#ece9e8", fg="#000000").pack(pady=30)

        #Table Style
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 12) , rowheight=80, padx=30, pady=120) #Font of table data
        style.configure("Treeview.Heading", font=("Arial Bold", 18), padx=60, pady=60)  # Font for headers

        # Create table
        columns = ("Name", "Humidity (RH%)", "Light (lux)", "Temperature (C)")
        dashboard_table = ttk.Treeview(dashboard_window, columns=columns, show="headings", height=120)

        # Loop through table columns
        for col in columns:
            dashboard_table.heading(col, text=col)
            dashboard_table.column(col, width=150, anchor="center")

        dashboard_table.pack(fill=tk.BOTH, expand=True, padx=20, pady=130)
        print(entry_name.get())
        # Populate table with existing plants in database
        dashboard_table.insert("", "end", values=("Plant", readserial("COM3", 9600)["Humidity"], readserial("COM3", 9600)["Light"], readserial("COM3", 9600)["Temp"]))
        light_range = datasplice(new_plant_database[get_most_recent_plant()]['Light'])
        humidity_range = datasplice(new_plant_database[get_most_recent_plant()]['Humidity'])
        temp_range = datasplice(new_plant_database[get_most_recent_plant()]['Temp'])
        sensor_light = readserial('COM3', 9600)["Light"]
        sensor_humidity = readserial('COM3', 9600)["Humidity"]
        sensor_temp = readserial('COM3', 9600)["Temp"]
        if sensor_light > light_range[0] and sensor_light < light_range[1]:
            pass
        elif sensor_light < light_range[0]:
            messagebox.showinfo("Notification", f"{entry_name.get().capitalize()} Light is low!")
        elif sensor_light > light_range[1]:
            messagebox.showinfo("Notification", f"{entry_name.get().capitalize()} Light is high!")
        if sensor_humidity > humidity_range[0] and sensor_humidity < humidity_range[1]:
            pass
        elif sensor_humidity < humidity_range[0]:
            messagebox.showinfo("Notification", f"{entry_name.get().capitalize()} Humidity is low!")
        elif sensor_humidity > humidity_range[1]:
            messagebox.showinfo("Notification", f"{entry_name.get().capitalize()} Humidity is high!")
        if sensor_temp > temp_range[0] and sensor_temp < temp_range[1]:
            pass
        elif sensor_temp < temp_range[0]:
            messagebox.showinfo("Notification", f"{entry_name.get().capitalize()} Temp is low!")
        elif sensor_temp > temp_range[1]:
            messagebox.showinfo("Notification", f"{entry_name.get().capitalize()} Temp is high!")
            
            


      

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
            inventory_table.insert("", "end", values=(name, data["Humidity"], data["Light"], data["Temp"]))

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



# Initialize GUI size and style
root = tk.Tk()
root.title("Vertical Farming Software")
root.resizable(True, True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


root.geometry(f"{screen_width}x{screen_height}+0+0")
root.configure(bg=BG_COLOR)

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    pass

root.tk.call("tk", "scaling",1.9)

root.update_idletasks()  
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

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




# Add Plant Frame
frame_add = tk.Frame(center_frame, bg=BG_COLOR)
frame_add.pack(fill=tk.NONE, expand=True, padx=30, pady=(0, 10))

# Input boxes for plant necessities
tk.Label(frame_add, text="Add New Plant", font=("Arial",62), bg=BG_COLOR, fg=("black")).pack(pady=(70))
tk.Label(frame_add, text="Name:", font=("Arial Bold", 20), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(35, 20))
entry_name = tk.Entry(frame_add, font=("Arial", 20), width=40)
entry_name.pack(pady=(0, 20))



tk.Label(frame_add, text="Humidity (RH%):", font=("Arial Bold", 20), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(15, 15))
entry_humidity = tk.Entry(frame_add, font=("Arial", 20), width=40)
entry_humidity.pack(pady=(0, 20))


tk.Label(frame_add, text="Light (Lux):", font=("Arial Bold", 20), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(15, 15))
entry_light = tk.Entry(frame_add, font=("Arial", 20), width=40)
entry_light.pack(pady=(0, 20))

tk.Label(frame_add, text="Temperature (C):", font=("Arial Bold", 20), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(15, 15))
entry_temperature = tk.Entry(frame_add, font=("Arial", 20), width=40)
entry_temperature.pack(pady=(0, 15))



tk.Button(frame_add, text="Add Plant", font=("Ariel", 20), bg=BUTTON_COLOR, fg="#000000", command=add_plant, height=1, width=8).pack(pady=(30, 50))
# Arduino Data
def sensor2lux(lightdata):
    if round(493*math.log(0.07*lightdata, 5)) <= 0:
        return 0
    else:
        return round(493*math.log(0.07*lightdata, 5))

def readserial(comport, baudrate):

    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read
    sensordata = {}
    while True:
        # Bring data from sensors into dict
        data = str(ser.readline().decode().strip())
        if data:
            if len(sensordata) < 3:
                if data[0] == "L":
                    LLevel = int(str(data)[1:len(data)])
                    sensordata['Light'] = sensor2lux(LLevel)
                if data[0] == "T":
                    TLevel = int(round(float(str(data)[1:len(data)])))
                    sensordata['Temp'] = TLevel
                if data[0] == "H":
                    HLevel = int(round(float(str(data)[1:len(data)])))
                    sensordata['Humidity'] = HLevel
            elif len(sensordata) == 3:
                return sensordata

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
    center_frame_position()

frame_add.bind("<Configure>", on_frame_configure)


if __name__ == '__main__':

    readserial('COM3', 9600)
root.mainloop()

# © DP & TP 2025