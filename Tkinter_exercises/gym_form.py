"""
Author - Anant luthra
Date - 23/12/21
Purpose - Making a GUI for form of registration for dance class.
"""

from tkinter import *
from PIL import Image, ImageTk

def submit_details():
    """
    This function is to write details in .txt file and also to print details on console.
    """
    
    print("Successfully Submitted !!")
    


# Basic details of our GUI window. ===============================================================#

root = Tk()
root.geometry("800x650")
root.minsize("455", "650")
# root.maxsize("442", "650")
root.title("Dance class registration form")

# Opening image for GUI ---------------------------------------------------------------------------#

image_file = Image.open("dance_class.png")
main_image = ImageTk.PhotoImage(image_file)

# Making labels for GUI window  -------------------------------------------------------------------#

header_image = Label(image=main_image)
main_heading = Label(text="Dance class registration form",
font="Times 30 bold", fg="black", bg="light yellow", padx=5, pady=5)
name_lable = Label(root, text="Name - ", font="Helvetica 20 italic")
age_lable = Label(root, text="Age - ", font="Helvetica 20 italic")
Gender_lable = Label(root, text="Gender - ", font="Helvetica 20 italic")
mono_lable = Label(root, text="Mobile no. - ", font="Helvetica 20 italic")

# Buttons for GUI ---------------------------------------------------------------------------------#

submit_button = Button(root, text="Submit", font="arial 15 bold", fg="Green", bg="yellow",
command=submit_details)

# Setting stringsvariables for input from user from entry widget ----------------------------------#

name = StringVar()
age = StringVar()
gender = StringVar()
mono = StringVar()

# Setting Entry Widgets ---------------------------------------------------------------------------#

name_entry = Entry(root, textvariable=name)
age_entry = Entry(root, textvariable=age)
gender_entry = Entry(root, textvariable=gender)
mono_entry = Entry(root, textvariable=mono)

# Packing elements through .grid() function --------------------------------------------------------#

main_heading.grid(padx=10)
header_image.grid(row=4, pady=10)
name_lable.grid(row=5, padx=10, pady=5)
age_lable.grid(row=6, padx=10, pady=5)
Gender_lable.grid(row=7, padx=10, pady=5)
mono_lable.grid(row=8, padx=10, pady=5)
submit_button.grid(row=9, padx=10, pady=40)

# Now packing entry widget -------------------------------------------------------------------------#

name_entry.grid(row=5, column=1, padx=5, ipadx=25, ipady=18, pady=5)
age_entry.grid(row=6, column=1,padx=5, ipadx=25, ipady=18, pady=5)
gender_entry.grid(row=7, column=1,padx=5, ipadx=25, ipady=18, pady=5)
mono_entry.grid(row=8, column=1,padx=5, ipadx=25, ipady=18, pady=5)



root.mainloop()
