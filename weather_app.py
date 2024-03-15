import tkinter as tk
from tkinter import messagebox

class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather App")
        self.master.geometry("400x300")

        self.label_location = tk.Label(master, text="Enter Location:")
        self.label_location.grid(row=0, column=0, padx=10, pady=10)

        self.entry_location = tk.Entry(master)
        self.entry_location.grid(row=0, column=1, padx=10, pady=10)

        self.btn_search = tk.Button(master, text="Search", command=self.search_weather)
        self.btn_search.grid(row=0, column=2, padx=10, pady=10)

        self.label_weather_info = tk.Label(master, text="")
        self.label_weather_info.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def search_weather(self):
        location = self.entry_location.get()
        if not location:
            messagebox.showerror("Error", "Please enter a location.")
            return
        
        # You would integrate with a weather API here to fetch weather data based on the location.
        # For demonstration purposes, let's just display a sample weather data.
        weather_data = {
            "location": location,
            "temperature": "25°C",
            "conditions": "Partly Cloudy",
            "humidity": "60%",
            "wind_speed": "10 km/h",
            "forecast": "Partly cloudy throughout the day."
        }

        weather_info = f"Weather for {weather_data['location']}:\n"
        weather_info += f"Temperature: {weather_data['temperature']}\n"
        weather_info += f"Conditions: {weather_data['conditions']}\n"
        weather_info += f"Humidity: {weather_data['humidity']}\n"
        weather_info += f"Wind Speed: {weather_data['wind_speed']}\n"
        weather_info += f"Forecast: {weather_data['forecast']}"
        
        self.label_weather_info.config(text=weather_info)


def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
