from orders.main import run
from orders.helpers import file_checker, make_fail_excel, make_csv

"""
gui2.py
check pgmx file
generate csv

date starteded:  may 5,2023
last update: may 9,2023
last update: may 17,2023
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

window = tk.Tk()

# set window size
window.geometry("1400x500")

# set gui title
window.title("CNC Calculator")

# 4 window frames
frame1 = tk.Frame(master=window, width=350, height=500)
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=350, height=500)
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=350, height=500)
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame4 = tk.Frame(master=window, width=350, height=500)
frame4.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

####################
# Generate Cutlist #
####################

# make load cutlist label
label1_1 = tk.Label(frame1, text="SAVE CUTLIST NAME")
label1_1.place(x=20, y=20)

# make name entry variable
cutlistFilePath1 = tk.StringVar()

# make cutlistFilePath entry
cutlistFilePathEntry1 = tk.Entry(frame1, width=40, textvariable=cutlistFilePath1)
cutlistFilePathEntry1.place(x=20, y=40)


# load button handler
def loadButton1_command():
    print("load button Button clicked")

    # make open file dialog
    defalt_dir1 = r'C:\Users\jrobe\OneDrive - THE FURNITURE GUYS\TFG OFFICE\PRODUCTION\CUT LIST\TEST-CODE'

    # file dialog path
    file_path = filedialog.asksaveasfilename(initialdir=defalt_dir1, filetypes=[("excel files", "*.xlsx")])
    print(file_path)

    # check for .xlsx extension
    if not file_path.endswith('.xlsx'):
        file_path = file_path + ".xlsx"

    # display file path
    cutlistFilePath1.set(file_path)


# make loadButton button with a command
loadButton1 = tk.Button(frame1, text="Browse", command=loadButton1_command, width=6)
loadButton1.place(x=270, y=40)

# make add orders to cutlist label
label1_2 = tk.Label(frame1, text="ADD ORDERS TO CUTLIST (seperate by commas)")
label1_2.place(x=20, y=80)

# make multline text for order number entry
orderNumbersText1 = tk.Text(frame1, width=38, height=5)
orderNumbersText1.place(x=20, y=100)

# make cutlist folder label
label1_4 = tk.Label(frame1, text="CUTLIST FOLDER")
label1_4.place(x=20, y=220)

# make cutlist folder list box
cutlistFolderListBox1 = tk.Listbox(frame1, height='10', width='50')
cutlistFolderListBox1.place(x=20, y=240)


# handle Run Ordewrs button
def runOrders1_command():
    print("checkPgmxFile button was clicked")

    # get cutlistFile name
    file_path = cutlistFilePath1.get()
    print("file_path", file_path)

    # got a name?
    if file_path == "":
        tk.messagebox.showinfo(title="No file name entered", message="Please enter a file name")
        cutlistFilePathEntry1.focus()
        return

    # get order numbers
    try:
        # read the order number list
        order_nums = orderNumbersText1.get("1.0", "end").strip()
        print(order_nums)

        # check for order numbers
        if order_nums == "":
            tk.messagebox.showinfo(title="No order nunbers entered", message="Please enter order numbers")
            orderNumbersText1.focus()
            return

        # replace new lines
        order_nums = order_nums.strip().replace('\n', ',')
        if (order_nums[-1] == ','):
            order_nums = order_nums[:-1]
        print(order_nums)

        # replace ,, with ,
        order_nums = order_nums.replace(",,", ',')

        # list of order nunbers
        order_num_list = order_nums.split(",")
        print("running order lsit", order_num_list)

        # call run order helper function
        run(order_num_list, file_path)

        # print run order completed message
        tk.messagebox.showinfo(title='Cutlist Completed', message=file_path + 'Done')


    # catck any errors and report them
    except Exception as e:

        # report file errors
        tk.messagebox.showinfo(title='Run Error encountered: ' + file_path, message=e)


# make checkPgmxFile button with a command
checkPgmxFileButton2 = tk.Button(frame1, text="Run Orders", command=runOrders1_command, width='42')
checkPgmxFileButton2.place(x=20, y=420)

########################
# File Checker section #
########################


# make load cutlist label
label2_1 = tk.Label(frame2, text="LOAD CUTLIST FILE")
label2_1.place(x=20, y=20)

# make name entry variable
cutlistFilePath2 = tk.StringVar()

# make cutlistFilePath entry
cutlistFilePathEntry2 = tk.Entry(frame2, width=40, textvariable=cutlistFilePath2)
cutlistFilePathEntry2.place(x=20, y=40)


# load button handler
def loadButton2_command():
    print("load button Button clicked")

    # make open file dialog
    file_path = filedialog.askopenfilename(initialdir=".", filetypes=[("excel files", "*.xlsx")])
    print(file_path)

    # display file path
    cutlistFilePath2.set(file_path)


# make loadButton button with a command
loadButton2 = tk.Button(frame2, text="Browse", command=loadButton2_command, width=6)
loadButton2.place(x=270, y=35)

# csv part folder
# make csv folderlabel
label2_4 = tk.Label(frame2, text="CSV PART FOLDER")
label2_4.place(x=20, y=80)

# make csvFolder entry variable
csvpartFolder2 = tk.StringVar()

# make csvpartFolderEntry entry
csvpartFolderEntry2 = tk.Entry(frame2, width=40, textvariable=csvpartFolder2)
csvpartFolderEntry2.place(x=20, y=100)


# destinationFolder handler
def csvpartFolder2_command():
    print("csvFolder Button clicked")

    # make open file dialog
    folder_path = filedialog.askdirectory(parent=frame2, title='Select a CSV folder')
    print(folder_path)

    # display file path
    csvpartFolder2.set(folder_path)


# make loadButton button with a command
csvpartFolderButton2 = tk.Button(frame2, text="Browse", command=csvpartFolder2_command, width=6)
csvpartFolderButton2.place(x=270, y=100)

# fails list excel fle
# make csv fails list label
label2_5 = tk.Label(frame2, text="FAILS LIST")
label2_5.place(x=20, y=140)

# make fails list entry variable
fails_list2 = tk.StringVar()

# make csvpartFolderEntry entry
fails_listEntry2 = tk.Entry(frame2, width=40, textvariable=fails_list2)
fails_listEntry2.place(x=20, y=160)


# fails_list handler
def fails_list2_command():
    print("csvFolder Button clicked")

    # make open file dialog
    # file_path = filedialog.asksaveasfilename(parent=frame2, title='Select a ecel file name')
    defalt_dir1 = r'C:\Users\jrobe\OneDrive - THE FURNITURE GUYS\TFG OFFICE\PRODUCTION\CUT LIST\TEST-CODE'
    file_path = filedialog.asksaveasfilename(parent=frame2, title='Select a ecel file name', initialdir=defalt_dir1,
                                             filetypes=[("excel files", "*.xlsx")])
    print(file_path)
    if not file_path.endswith('.xlsx'):
        file_path = file_path + ".xlsx"
    # display file path
    fails_list2.set(file_path)


# make loadButton button with a command

fails_listButton2 = tk.Button(frame2, text="Browse", command=fails_list2_command, width=6)
fails_listButton2.place(x=270, y=160)

# make cutlist folder label
label2_2 = tk.Label(master=frame2, text="CUTLIST FOLDER")
label2_2.place(x=20, y=220)

# make cutlist folder list box
cutlistFolderListBox2 = tk.Listbox(master=frame2, height='10', width='50')
cutlistFolderListBox2.place(x=20, y=240)


# handle checkPgmxFile button
def checkPgmxFile2_command():
    print("checkPgmxFile button was clicked")

    # get cutlistFile name
    file_path = cutlistFilePath2.get()

    # got a name?
    if file_path == "":
        tk.messagebox.showinfo(title="No file name entered", message="Please enter a file name")
        cutlistFilePathEntry2.focus()
        return

    # open file
    # try:
    # f = open(file_path, 'r')

    # read all lines in file
    # for line in f.readlines():
    #     cutlistFolderListBox.insert("end", line)

    # close file
    # f.close()

    # catck any file errors and report them
    # except Exception as e:

    # report file errors
    # tk.messagebox.showinfo(title='Error opening/reading file: ' + file_path, message=e)
    # Send cutlist file name and parts folder name to file checker
    parts_folder_name = csvpartFolder2.get()
    fails = file_checker(file_path, parts_folder_name)  ####### file checker call
    # insert faild file name in list box\
    for file_name in fails:
        print(file_name)
        cutlistFolderListBox2.insert("end", file_name)
    # wrtie to excel file
    excel_file_name = fails_list2.get()
    print("excel file name", excel_file_name)
    make_fail_excel(fails, excel_file_name)


# make checkPgmxFile button with a command
checkPgmxFileButton2 = tk.Button(frame2, text="Check PGMX File", command=checkPgmxFile2_command, width='42')
checkPgmxFileButton2.place(x=20, y=420)

########################
# Generate CSV section #
########################


# make load cutlist2 label
label3_1 = tk.Label(frame3, text="LOAD CUTLIST FILE")
label3_1.place(x=20, y=20)

# make name entry variable
cutlistFilePath3 = tk.StringVar()

# make cutlistFilePath entry
cutlistFilePathEntry3 = tk.Entry(frame3, width=40, textvariable=cutlistFilePath3)
cutlistFilePathEntry3.place(x=20, y=40)


# load button handler
def loadButton3_command():
    print("load button2 Button clicked")

    # make open file dialog
    file_path = filedialog.askopenfilename(initialdir=".", filetypes=[("excel files", "*.xlsx")])
    print(file_path)

    # display file path
    cutlistFilePath3.set(file_path)


# make loadButton button with a command
loadButton3 = tk.Button(frame3, text="Browse", command=loadButton3_command, width=6)
loadButton3.place(x=270, y=35)

# make csv folderlabel
label3_3 = tk.Label(frame3, text="CSV FOLDER")
label3_3.place(x=20, y=80)

# make csvFolder entry variable
csvFolder3 = tk.StringVar()

# make cutlistFilePath entry
csvFolderEntry3 = tk.Entry(frame3, width=40, textvariable=csvFolder3)
csvFolderEntry3.place(x=20, y=100)


# csvFolder handler
def csvFolder3_command():
    print("csvFolder Button clicked")

    # make open file dialog
    folder_path = filedialog.askdirectory(parent=frame3, title='Select a CSV folder')
    print(folder_path)

    # display file path
    csvFolder3.set(folder_path)


# make loadButton button with a command
csvFolderButton3 = tk.Button(frame3, text="Browse", command=csvFolder3_command, width=6)
csvFolderButton3.place(x=270, y=100)

# make cutlist folder label
label3_5 = tk.Label(frame3, text="CSV FOLDER")
label3_5.place(x=20, y=220)

# make cutlist folder list box
cutlistFolderListBox3 = tk.Listbox(frame3, height='10', width='50')
cutlistFolderListBox3.place(x=20, y=240)


# handle checkPgmxFile button
def generateCSV3_command():
    print("checkPgmxFile button was clicked")

    # get file cutlistFile name
    file_path = cutlistFilePath3.get()

    # got a name?
    if file_path == "":
        tk.messagebox.showinfo(title="No file name entered", message="Please enter a file name")
        cutlistFilePathEntry3.focus()
        return
    # here we call the make csv function
    folder_path = csvFolder3.get()
    print(folder_path)
    folder_path = folder_path + "/"
    # got a folder name?
    if folder_path == "":
        tk.messagebox.showinfo(title="No folder name entered", message="Please enter a folder name")
        csvFolderEntry3.focus()
        return

    # here we call make csv fucntion
    make_csv(file_path, folder_path)


# make checkPgmxFile button with a command
generateCSVButton3 = tk.Button(frame3, text="Generate CSV", command=generateCSV3_command, width='42')
generateCSVButton3.place(x=20, y=420)

############################
# Calculate Sheets section #
############################


# make load cutlist2 label
label4_1 = tk.Label(frame4, text="CALCULATE SHEETS")
label4_1.place(x=20, y=20)

# make name entry variable
cutlistFilePath4 = tk.StringVar()

# make cutlistFilePath entry
cutlistFilePathEntry4 = tk.Entry(frame4, width=40, textvariable=cutlistFilePath4)
cutlistFilePathEntry4.place(x=20, y=40)


# load button handler
def loadButton4_command():
    print("load button4 Button clicked")

    # make open file dialog
    file_path = filedialog.askopenfilename(initialdir=".", filetypes=[("excel files", "*.xlsx")])
    print(file_path)

    # display file path
    cutlistFilePath4.set(file_path)


# make loadButton button with a command
loadButton4 = tk.Button(frame4, text="Browse", command=loadButton4_command, width=6)
loadButton4.place(x=270, y=35)

# make csv folderlabel
label4_3 = tk.Label(frame4, text="CSV FOLDER")
label4_3.place(x=20, y=80)

# make csvFolder entry variable
csvFolder4 = tk.StringVar()

# make cutlistFilePath entry
csvFolderEntry4 = tk.Entry(frame4, width=40, textvariable=csvFolder4)
csvFolderEntry4.place(x=20, y=100)


# csvFolder handler
def csvFolder4_command():
    print("csvFolder Button clicked")

    # make open file dialog
    folder_path = filedialog.askdirectory(parent=frame4, title='Select a CSV folder')
    print(folder_path)

    # display file path
    csvFolder4.set(folder_path)


# make loadButton button with a command
csvFolderButton4 = tk.Button(frame4, text="Browse", command=csvFolder4_command, width=6)
csvFolderButton4.place(x=270, y=100)

# make cutlist folder label
label3_5 = tk.Label(frame4, text="CUTLIST FOLDER")
label3_5.place(x=20, y=220)

# make cutlist folder list box
cutlistFolderListBox4 = tk.Listbox(frame4, height='10', width='50')
cutlistFolderListBox4.place(x=20, y=240)


# handle checkPgmxFile button
def generateCutlist4_command():
    print("checkPgmxFile button was clicked")

    # get file cutlistFile name
    file_path = cutlistFilePath4.get()

    # got a file name?
    if file_path == "":
        tk.messagebox.showinfo(title="No file name entered", message="Please enter a file name")
        cutlistFilePathEntry4.focus()
        return

    # open file
    try:
        f = open(file_path, 'r')

        # read all lines in file
        for line in f.readlines():
            cutlistFolderListBox4.insert("end", line)

        # close file
        f.close()

    # catck any file errors and report them
    except Exception as e:
        print(e)
        tk.messagebox.showinfo(title="Cannot open/read file", message=e)


# make checkPgmxFile button with a command
generateCutlistButton4 = tk.Button(frame4, text="Generate Cutlist", command=generateCutlist4_command, width='42')
generateCutlistButton4.place(x=20, y=420)


######################
# load/store buttons #
######################

# load button handler
def loadProfileButton_command():
    print("load profile Button")

    # file dialog path
    file_path = filedialog.askopenfilename(initialdir=".", initialfile='profile.txt',
                                           filetypes=[("profile files", "*.txt")])
    print(file_path)

    # got a file name?
    if file_path == "":
        tk.messagebox.showinfo(title="No file name entered", message="Please enter a file name")
        cutlistFilePathEntry4.focus()
        return

    # check for .txt extension
    if not file_path.endswith('.txt'):
        file_path = file_path + ".txt"

    try:
        f = open(file_path, 'r')

        # read all lines in file
        # set string variables
        line = f.readline().strip()
        cutlistFilePath1.set(line)
        line = f.readline().strip()
        # clear text
        orderNumbersText1.delete('1.0', tk.END)
        orderNumbersText1.insert(tk.END, line)
        line = f.readline().strip()
        cutlistFilePath2.set(line)
        line = f.readline().strip()
        csvpartFolder2.set(line)
        line = f.readline().strip()
        fails_list2.set(line)
        line = f.readline().strip()
        cutlistFilePath3.set(line)
        line = f.readline().strip()
        csvFolder3.set(line)
        line = f.readline().strip()
        cutlistFilePath4.set(line)
        line = f.readline().strip()
        csvFolder4.set(line)

        # close file
        f.close()

    except Exception as e:
        print(e)
        tk.messagebox.showinfo(title="Cannot open/read file", message=e)


# make loadButton button with a command
loadProfileButton = tk.Button(frame2, text="Load Profile", command=loadProfileButton_command, width=12)
loadProfileButton.place(x=230, y=450)


# load button handler
def saveProfileButton_command():
    # save profile button handler
    # file dialog path
    file_path = filedialog.asksaveasfilename(initialdir=".", initialfile='profile.txt',
                                             filetypes=[("profile files", "*.txt")])
    print(file_path)

    # got a file name?
    if file_path == "":
        tk.messagebox.showinfo(title="No file name entered", message="Please enter a file name")
        cutlistFilePathEntry4.focus()
        return

    # check for .txt extension
    if not file_path.endswith('.txt'):
        file_path = file_path + ".txt"

    # check for order numbers
    text = orderNumbersText1.get("1.0", "end").strip()

    # check for order numbers
    if text == "":
        tk.messagebox.showinfo(title="No order nunbers entered", message="Please enter order numbers")
        orderNumbersText1.focus()
        return

    try:

        f = open(file_path, 'w')

        f.write(cutlistFilePath1.get() + "\n")

        # change newlines into commas
        text = orderNumbersText1.get("1.0", "end").strip()

        # check for order numbers
        if text == "":
            tk.messagebox.showinfo(title="No order nunbers entered", message="Please enter order numbers")
            orderNumbersText1.focus()
            return

        text = text.replace('\n', ',')
        text = text.replace(',,', ',')
        if (text[-1] == ','):
            text = text[:-1]
        print("text", text)
        f.write(text + "\n")
        f.write(cutlistFilePath2.get() + "\n")
        f.write(csvpartFolder2.get() + "\n")
        f.write(fails_list2.get() + "\n")
        f.write(cutlistFilePath3.get() + "\n")
        f.write(csvFolder3.get() + "\n")
        f.write(cutlistFilePath4.get() + "\n")
        f.write(csvFolder4.get() + "\n")

        # close file
        f.close()

    except Exception as e:
        print(e)
        tk.messagebox.showinfo(title="Cannot open/write file", message=e)


# make loadButton button with a command
saveProfileButton = tk.Button(frame3, text="Save Profile", command=saveProfileButton_command, width=12)
saveProfileButton.place(x=20, y=450)

#########################
# event loop processing #
#########################
window.mainloop()

# manual test
# if __name__ == '__main__':
#    order_list = [
#        7549,
#        7522,
#        7538,
#        7520,
#        7534,
#        7540,
#        7499,
#        7531,
#        7532,
#            ]
#    run(order_list)
