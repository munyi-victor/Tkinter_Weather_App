import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

# Create the main application window
root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    city = textfield.get()
    
    # Initialize the geolocator
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        
        if location:
            # Get the timezone
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")
            
            # Update the labels with the weather information
            name.config(text="CURRENT WEATHER")
            clock.config(text=current_time)
        else:
            messagebox.showerror("Error", "City not found.")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the search box and button
textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = tk.PhotoImage(file="images/search_icon.png")
myimage_icon = tk.Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

# ... (Rest of your code for logo, labels, and placeholders)

# Start the main event loop
root.mainloop()
