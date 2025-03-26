import tkinter as tk
from tkinter import messagebox
from bikerental import BikeRental
from database import setup_db, add_user, get_all_users, delete_user

# Initialize DB and Rental class
setup_db()
rental = BikeRental("Bike Rental", 100)

def update_bike_count(label):
    label.config(text=f"Available Bikes: {rental.no_of_bikes}")

def rent_bike_window():
    def rent_bike():
        name = entry_name.get()
        try:
            bikes = int(entry_bikes.get())
            mode = var.get()
            if mode == 1:
                rental.rent_bike_hourly(name, bikes)
            elif mode == 2:
                rental.rent_bike_daily(name, bikes)
            elif mode == 3:
                rental.rent_bike_weekly(name, bikes)
            else:
                messagebox.showerror("Error", "Please select a rental mode.")
                return
            add_user(name)
            messagebox.showinfo("Success", f"Bike rented to {name} successfully!")
            win.destroy()
        except ValueError:
            messagebox.showerror("Error", "Enter valid number of bikes.")

    win = tk.Toplevel(root)
    win.title("Rent a Bike")

    tk.Label(win, text="Your Name").grid(row=0, column=0)
    entry_name = tk.Entry(win)
    entry_name.grid(row=0, column=1)

    tk.Label(win, text="Number of Bikes").grid(row=1, column=0)
    entry_bikes = tk.Entry(win)
    entry_bikes.grid(row=1, column=1)

    tk.Label(win, text="Rental Type").grid(row=2, column=0)
    var = tk.IntVar()
    tk.Radiobutton(win, text="Hourly ($5/hr)", variable=var, value=1).grid(row=2, column=1)
    tk.Radiobutton(win, text="Daily ($20/day)", variable=var, value=2).grid(row=3, column=1)
    tk.Radiobutton(win, text="Weekly ($60/week)", variable=var, value=3).grid(row=4, column=1)

    tk.Button(win, text="Rent", command=rent_bike).grid(row=5, column=1)

def return_bike_window():
    def return_bike():
        name = entry_name.get()
        if name:
            rental.issue_bill(name)
            delete_user(name)
            messagebox.showinfo("Success", f"Bike returned by {name}.")
            win.destroy()
        else:
            messagebox.showerror("Error", "Enter a name.")

    win = tk.Toplevel(root)
    win.title("Return Bike")
    tk.Label(win, text="Your Name").pack()
    entry_name = tk.Entry(win)
    entry_name.pack()
    tk.Button(win, text="Return", command=return_bike).pack()

root = tk.Tk()
root.title("Bike Rental System")
root.geometry("300x300")

bike_label = tk.Label(root, text=f"Available Bikes: {rental.no_of_bikes}")
bike_label.pack(pady=10)

tk.Button(root, text="Rent a Bike", command=rent_bike_window).pack(pady=5)
tk.Button(root, text="Return a Bike", command=return_bike_window).pack(pady=5)
tk.Button(root, text="Refresh Availability", command=lambda: update_bike_count(bike_label)).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=20)

root.mainloop()
