from tkinter import *
import random
from tkinter import messagebox
import json
from datetime import datetime, timedelta

FONT_NAME = "Courier"
BLUE = "#002B5B"
RED = "#EA5455"
DCOFFIE = "#E4DCCF"
LCOFFIE = "#F9F5EB"

windows = Tk()
windows.title("ONLINE BUS PASS SYSTEM")
windows.minsize(width=1230, height=500)
windows.config(pady=60, bg=LCOFFIE)

# ---------------------------- END DATE CALCULATOR ------------------------------- #

def calculate():
    try:
        start_date_str = pass_start_date_entry.get()
        num_days = int(no_of_days_entry.get())

        start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
        final_date = start_date + timedelta(days=num_days)
        date_into_int = str(final_date.strftime('%d-%m-%Y'))

        pass_end_date_entry.insert(0, date_into_int)
    except ValueError:
        pass_end_date_entry.insert(0, "Invalid input")

# ---------------------------- SEARCH DATA ------------------------------- #
def test():
    publish_label = Label(text=f"# This is the passs of {name} #\nBirthdate: {bdate}\nGender: {gender}\nProfession: {profession}\nNo. of Days: {nodays}\nPhone Number: {phoneno}\nAadhar no. :{aadhar}\nFrom Stop:{s1}\nTo Stop: {s2}\nUID : {uid}", font=(FONT_NAME, 15), bg=LCOFFIE, fg=BLUE)
    publish_label.grid(row=3, column=3, rowspan=15)


def save():
        global name, bdate,gender, profession, nodays, phoneno, aadhar, s1, s2, uid
        name = name_entry.get()
        bdate = birth_date_entry.get()
        gender = gender_entry.get()
        profession = profession_entry.get()
        nodays = no_of_days_entry.get()
        phoneno = phone_number_entry.get()
        aadhar = aadhar_number_entry.get()
        s1 = stop1_entry.get()
        s2 = stop2_entry.get()
        uid = uid_entry.get()

        new_data = {
            name : {
               "Bdate" : bdate,
                "Gender" : gender,
                "Profession" : profession,
                "Num of Days ": nodays,
                "Phone Number" : phoneno,
                "Aadhar" : aadhar,
                "From Stop" : s1,
                "To Stop" : s2,
                "UID" : uid
            }
        }



        if len(name) == 0 or len(bdate) == 0 or len(gender) == 0 or len(profession) == 0 or len(nodays) == 0 or len(phoneno) == 0 or len(aadhar) == 0 or len(s1) == 0 or len(s2) == 0 or len(uid) ==0 :
            messagebox.showinfo(title="Oops", message="Dont leave any entry Empty..")
        else:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                name_entry.delete(0, END)
                birth_date_entry.delete(0, END)
                gender_entry.delete(0, END)
                profession_entry.delete(0, END)
                no_of_days_entry.delete(0, END)
                phone_number_entry.delete(0, END)
                aadhar_number_entry.delete(0, END)
                stop1_entry.delete(0, END)
                stop2_entry.delete(0, END)
                uid_entry.delete(0, END)
                pass_start_date_entry.delete(0, END)
                pass_end_date_entry.delete(0, END)

# ---------------------------- SAVE DATA ------------------------------- #

def search_data():
    name = name_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message=f"No Data FIle of {name} Found ")
    else:

        if name in data:
            bdate = data[name]["Bdate"]
            gender = data[name]["Gender"]
            profession = data[name]["Profession"]
            nodays = data[name]["Num of Days "]
            phoneno = data[name]["Phone Number"]
            aadhar = data[name]["Aadhar"]
            s1 = data[name]["From Stop"]
            s2 = data[name]["To Stop"]
            uid = data[name]["UID"]
            messagebox.showinfo(title="Information", message=f"following are the details of {name}\nBirthdate: {bdate}\nGender: {gender}\nProfession: {profession}\nNo, of Days: {nodays}\nPhone Number: {phoneno}\nAAdhar no. :{aadhar}\nFrom Stop:{s1}\nTo Stop: {s2}\nUID : {uid}")
        else:
            messagebox.showinfo(title="Oops", message=f"No details for {name} exists")

# ---------------------------- COMMAND FUNCTIONS ------------------------------- #

def UID_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(letters) for _ in range(nr_symbols)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]

    uid_number = letter_list + symbol_list + number_list
    random.shuffle(uid_number)

    uid = "".join(uid_number)
    uid_entry.insert(0, uid)

def payment_check():
    payment_status.delete(0, END)
    payment_status.insert(0, "\tPaid")

# ---------------------------- LABELS ------------------------------- #

title_label = Label(text="ONLINE BUS\nPASS SYSTEM", font=(FONT_NAME, 35), bg=DCOFFIE, fg=BLUE)
title_label.grid(row=0, column=1)

space_label = Label(text=" ", bg=LCOFFIE)
space_label.grid(row=1, column=0)
space_label = Label(text=" ", bg=LCOFFIE)
space_label.grid(row=2, column=0)
space_label = Label(text="        ", bg=LCOFFIE)
space_label.grid(row=3, column=3)

name_label = Label(text="          Name: ", font=(FONT_NAME, 15), bg=LCOFFIE, fg=BLUE)
name_label.grid(row=3, column=0)

birth_date_label = Label(text = "          Birth Date: ", font=(FONT_NAME, 15), bg=LCOFFIE, fg=BLUE)
birth_date_label.grid(row=4, column=0)

enter_gender_label = Label(text = "          Gender: ", font=(FONT_NAME, 15), bg=LCOFFIE, fg=BLUE)
enter_gender_label.grid(row=5, column=0)

enter_Profession_label = Label(text = "          Enter Profession: ", font=(FONT_NAME, 15), bg=LCOFFIE, fg=BLUE)
enter_Profession_label.grid(row=6, column=0)

number_of_days = Label(text = "          No. of Days: ", font=(FONT_NAME, 15), bg=LCOFFIE, fg=BLUE)
number_of_days.grid(row=7, column=0)

enter_ph_number = Label(text="          Phone Number:", font=(FONT_NAME, 15), bg=LCOFFIE, fg=BLUE)
enter_ph_number.grid(row=8,column=0)

aadhar_label = Label(text="          Aadhar No:", font=(FONT_NAME, 15), bg=LCOFFIE, fg=BLUE)
aadhar_label.grid(row=9, column=0)

stop1_label = Label(text="          From Stop:", font=(FONT_NAME, 15), bg=LCOFFIE, fg=BLUE)
stop1_label.grid(row=10, column=0)

stop2_label = Label(text="          To Stop:", font=(FONT_NAME, 15), bg=LCOFFIE, fg=BLUE)
stop2_label.grid(row=11, column=0)

pass_start_date_label = Label(text = "          Pass Start Date: ", font=(FONT_NAME, 15), bg=LCOFFIE, fg=BLUE)
pass_start_date_label.grid(row=12, column=0)

pass_end_date_label = Label(text = "          Pass End Date: ", font=(FONT_NAME, 15), bg=LCOFFIE, fg=BLUE)
pass_end_date_label.grid(row=13, column=0)

uid_no_label = Label(text="          UID Number: ", font=(FONT_NAME, 15), bg=LCOFFIE, fg=BLUE)
uid_no_label.grid(row=14, column=0)


payment_option = Label(text="          Payment Options:", font=(FONT_NAME, 15), bg=LCOFFIE, fg=BLUE)
payment_option.grid(row=15, column=0)

radio_state = IntVar()
radiobutton1 = Radiobutton(text="PhonePay", value=1, variable=radio_state, bg= LCOFFIE, fg=BLUE)
radiobutton2 = Radiobutton(text="   GPay", value=2, variable=radio_state, bg= LCOFFIE, fg=BLUE)
radiobutton1.grid(row=15, column=1)
radiobutton2.grid(row=16, column=1)

space_label = Label(text=" ", bg=LCOFFIE)
space_label.grid(row=17, column=1)

# ---------------------------- ENTRY ------------------------------- #

name_entry = Entry(width=45)
name_entry.grid(row=3, column=1)

birth_date_entry = Entry(width=45)
birth_date_entry.grid(row=4, column=1)

gender_entry = Entry(width=45)
gender_entry.grid(row=5, column=1)

profession_entry = Entry(width=45)
profession_entry.grid(row=6, column=1)

no_of_days_entry = Entry(width=45)
no_of_days_entry.grid(row=7, column=1)

phone_number_entry = Entry(width=45)
phone_number_entry.grid(row=8, column=1)

aadhar_number_entry = Entry(width=45)
aadhar_number_entry.grid(row=9, column=1)

stop1_entry = Entry(width=45)
stop1_entry.grid(row=10, column=1)

stop2_entry = Entry(width=45)
stop2_entry.grid(row=11, column=1)

pass_start_date_entry = Entry(width=45)
pass_start_date_entry.grid(row=12, column=1)

pass_end_date_entry = Entry(width=45)
pass_end_date_entry.grid(row=13, column=1)

uid_entry = Entry(width=45)
uid_entry.grid(row=14, column=1)

payment_status = Entry(width=20)
payment_status.insert(0, "            Unpaid")
payment_status.grid(row=15, column=2)

# pass_publish_entry = Entry(width=45 )
# pass_publish_entry.grid(row= 3, column= 4)
# text = Text(windows, height=22,
#               width=40,
#               bg="light cyan")
# text.insert(, "ytf")
# text.grid(row=3, column=4, rowspan=15)

# ---------------------------- BUTTONS ------------------------------- #

done_button = Button(text="DONE", width=25, command=save)
done_button.grid(row=18, column=1)

payment_button = Button(text = "Pay", width=18, command=payment_check)
payment_button.grid(row=16, column=2)

generate_button = Button(text="Generate", width=18, command=UID_generate)
generate_button.grid(row=14, column=2)

calculate_button = Button(text = "Calulate", width=18, command=calculate)
calculate_button.grid(row=12, column=2)

search_button = Button(text="Search", width=18, command=search_data)
search_button.grid(row=3, column=2)

search_button = Button(text="PASS", width=18, command=test)
search_button.grid(row=18, column=2)

windows.mainloop()

