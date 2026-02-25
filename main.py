#importing widgets
import tkinter as tk
from service_opp import Service_opp

#this is the list of interests
intrests= ["animals", "cleaning", "food", "helping"]

service_opp=["spca","park","soup kichen", "nursing home"]

root= tk.Tk()
root.title("Community Service Suggestion Program")
root.geometry("1500x800")
root.configure(bg="lightblue")
title = tk.Label(root, text="★ Community Service Tracker ★", fg="yellow", bg="blue", font=("Comic Sans MS", 30))
title.grid(row=0, column=0, padx=10, pady=10)

description = tk.Label(root, text="This is an app that helps you keep track of your community service hours \nand suggests places to start your community service work depending on your interests.", fg="white", bg="blue", font=("Helvetica", 12))
description.grid(row=1, column=0, padx=10, pady=10,sticky="w")
"""
frame = tk.Frame(root, width=150, height=10)
frame.pack(side="left", anchor="nw", pady=10)
"""

#widgets for the name input
name_label = tk.Label(root, fg="yellow", bg="blue", text="• Name:")
name_label.grid(row=3, column=0, padx=10, pady=10,sticky="w")

name_entry = tk.Entry(root)
name_entry.grid(row=4, column=0, padx=10, pady=10,sticky="w")

usrname = name_entry.cget("text")
if usrname == "":
    print("please insert a name")
else:
    print("proceed", usrname)

#widgets for the selection
intrests_des= tk.Label(root, text="• Select your intrests:", fg="yellow", bg="blue",)
intrests_des.grid(row=5, column=0, padx=10, pady=10,sticky="w")

row = 6
tempjobs = []
serviceobj = []

#this gets the info from the text document in the folder
with open("service.txt", "r") as file:
    tempjobs = file.readlines()

#this splits the data and makes  it more readable
for i in range(1,len(tempjobs)):
    line = tempjobs[i].split(";")
    name = line[0]
    interests = line[1].split(",")
    opportunity = line[2]
    website = line[3]
    address = line[4]
    phone = line[5]
    tempopp = Service_opp(name, interests, opportunity, website, address, phone)
    serviceobj.append(tempopp)

for opp in serviceobj:
    print(opp.name)

selected_intrests = {}


#this loops through the list to create checkbox widgets
for item in intrests:
    var = tk.IntVar()
    
    cb = tk.Checkbutton(root, text=item, fg="black", bg="blue", variable=var)
    cb.grid(row=row, column=0, padx=10, pady=10,sticky="w")
    
    
    #this stores the variable in our dictionary using the topping name as the key
    selected_intrests[item] = var
    row+=1

cbval = cb.cget("variable")
if cbval == 0:
        print("please select one of the options")

#this is where it collects all of the suggestions to print it into a listbox widget
suggestion_dic={}
def get_selected(row):
    name = name_entry.get()
    print(name)
    selected = [name for name, var in selected_intrests.items() if var.get() == 1]
    row+=1
    sug_title = tk.Label(root, fg="yellow", bg="blue", text="Suggestions:")
    sug_title.grid(row=row, column=0, padx=10, pady=10,sticky="w")
    suggestedservice = []
    for item in selected:
        for opp in serviceobj:
            if item in opp.interests:
                print(opp.name)
                suggestedservice.append([opp.name, opp.opportunity, opp.website, opp.address, opp.phone])
                
    row+=1
                
#this is the lisbox widget
    listbox = tk.Listbox(root, height=12, width=150, selectmode=tk.SINGLE) 
    listbox.grid(row=row, column=0, padx=10, pady=10,sticky="w")
    for item in suggestedservice:
        listbox.insert(tk.END, item)


#this adds the submit button function
tk.Button(root, text="Submit", fg="yellow", bg="blue", command=lambda: get_selected(row)).grid(row=row, column=0, padx=10, pady=10,sticky="w")


root.mainloop()


root.mainloop()
