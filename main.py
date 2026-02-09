import tkinter as tk
from service_opp import Service_opp

intrests= ["animals", "cleaning", "cooking", "serving"]

service_opp=["spca","park","soup kichen", "nursing home"]

root= tk.Tk()
root.geometry("800x800")
title = tk.Label(root, text="Community Service Tracker", font=("Helvetica", 30))
title.grid(row=0, column=0, padx=10, pady=10)

description = tk.Label(root, text="This a app that helps you keep track of your community servie hours ", font=("Helvetica", 12))
description.grid(row=1, column=0, padx=10, pady=10,sticky="w")
description2 = tk.Label(root, text=" and places to start your community service work", font=("Helvetica", 12))
description2.grid(row=2, column=0, padx=10, pady=10,sticky="w")
"""
frame = tk.Frame(root, width=150, height=10)
frame.pack(side="left", anchor="nw", pady=10)
"""

# Label
name_label = tk.Label(root, text="Name:")
name_label.grid(row=3, column=0, padx=10, pady=10,sticky="w")

# Entry
name_entry = tk.Entry(root)

name_entry.grid(row=4, column=0, padx=10, pady=10,sticky="w")
# intrests
intrests_des= tk.Label(root, text="select your intrests:")
intrests_des.grid(row=5, column=0, padx=10, pady=10,sticky="w")

row = 6
tempjobs = []
serviceobj = []

with open("service.txt", "r") as file:
    tempjobs = file.readlines()

    
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


# 3. Loop through the list to create widgets
for item in intrests:
    var = tk.IntVar()
    
    cb = tk.Checkbutton(root, text=item, variable=var)
    cb.grid(row=row, column=0, padx=10, pady=10,sticky="w")
    
    # Store the variable in our dictionary using the topping name as the key
    selected_intrests[item] = var
    row+=1

# Function to see suggestions
suggestion_dic={}
def get_selected(row):
    selected = [name for name, var in selected_intrests.items() if var.get() == 1]
    row+=1
    sug_title = tk.Label(root, text="Sugestions:")
    sug_title.grid(row=row, column=0, padx=10, pady=10,sticky="w")
    suggestedservice = []
    for item in selected:
        for opp in serviceobj:
            if item in opp.interests:
                print(opp.name)
                suggestedservice.append(opp.name)
                
    row+=1
                

    listbox = tk.Listbox(root, height=10, width=20, selectmode=tk.SINGLE) 
    listbox.grid(row=row, column=0, padx=10, pady=10,sticky="w")
    for item in suggestedservice:
        listbox.insert(tk.END, item)







    
    """for intrest in selected:
        row+=1
        if intrest == "animals":
            var = tk.IntVar()
        
            cb = tk.Checkbutton(root, text=service_opp[0], variable=var)
            cb.grid(row=row, column=0, padx=10, pady=10,sticky="w")
    
        # Store the variable in our dictionary using the topping name as the key
            suggestion_dic[service_opp[0]] = var
        if intrest == "cleaning":
            var = tk.IntVar()
        
            cb = tk.Checkbutton(root, text=service_opp[1], variable=var)
            cb.grid(row=row, column=0, padx=10, pady=10,sticky="w")
    
        # Store the variable in our dictionary using the topping name as the key
            suggestion_dic[service_opp[1]] = var
        
"""






    
tk.Button(root, text="Submit", command=lambda: get_selected(row)).grid(row=row, column=0, padx=10, pady=10,sticky="w")

root.mainloop()


root.mainloop()
