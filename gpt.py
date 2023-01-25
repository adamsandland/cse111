import calendar
from tkinter import *

def show_calendar():
    # Get the month and year from the user
    month = int(month_entry.get())
    year = int(year_entry.get())

    # Clear any previous calendars
    cal_label.config(text="")

    # Generate the calendar
    cal = calendar.monthcalendar(year, month)

    # Add the calendar to the label
    for row in cal:
        cal_label.config(text=cal_label.cget("text") + str(row) + "\n")

# Create the main window
root = Tk()
root.title("Calendar")

# Create a label for the month input
month_label = Label(root, text="Enter the month (1-12):")
month_label.grid(row=0, column=0)

# Create an entry for the month input
month_entry = Entry(root)
month_entry.grid(row=0, column=1)

# Create a label for the year input
year_label = Label(root, text="Enter the year:")
year_label.grid(row=1, column=0)

# Create an entry for the year input
year_entry = Entry(root)
year_entry.grid(row=1, column=1)

# Create a button to show the calendar
show_button = Button(root, text="Show Calendar", command=show_calendar)
show_button.grid(row=2, column=0, columnspan=2)

# Create a label to display the calendar
cal_label = Label(root)
cal_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
