from generator import layro
from sys import path
from os import path as pth, remove

inv_path = path[0] + "\Data"
finished = False

# Gear Ids
gear = {0: "Bear Claw", 1: "Goblin Sword", 2: "Makeshift Slingshot"}

# Gear Descriptions
description_list = {"Bear Claw": "Where did you even find this? There's no bears in this tower",
                    "Goblin Sword": "Confusingly named, this is actually just  \na goblin secured to a stick via rope",
                    "Makeshift Slingshot": "An Y-shaped stick with a rubber band \nconnecting the two protrusions"}

# Materials
materials_list = {"Bear Claw": ("Natural,", "Sharp"),
                  "Goblin Sword": ("Natural,", "Insanity"),
                  "Makeshift Slingshot": ("Wood,", "Rubber")}

# Souls
soul_amount = {"Bear Claw": 1,
               "Goblin Sword": 3,
               "Makeshift Slingshot": 2}

# Stats
stats_list = {"Bear Claw": {"Attack": 10, "Defense": -5, "Health": 10},
              "Goblin Sword": {"Attack": 15, "Defense": -10, "Health": -15},
              "Makeshift Slingshot": {"Attack": 5, "Defense": 10, "Health": 10}}

# FIXME: is there any way to put these in files? If we expand on these lists then they'll take up a lot of memory

set_up = False

# makes the inventory file if it doesn't yet exist
try:
    file = open(pth.join(inv_path, "inventory.txt"), "r")
except FileNotFoundError:
    file = open(pth.join(inv_path, "inventory.txt"), "w")
    file.write("0\n")
    file.write("1\n")
    file.write("2\n")
    file.write("s0\n")
    file.write("n0\n")
    file.write("p0\n")
    file.write("i0\n")
    file.write("w0\n")
    file.write("r0\n")
    file = open(pth.join(inv_path, "inventory.txt"), "r+")


def start(draw_game):
    item_info.grid_forget()
    gear_list.grid_forget()
    file.close()
    draw_game()


def equip_gear():
    # If the gear is already equipped, subtract their affect
    if gear_list.get("active") == layro.equipped_weapon:
        layro.equipped_weapon = "Nothing"
        layro.attack = layro.attack - stats_list[gear_list.get("active")]["Attack"]
        layro.defense = layro.defense - stats_list[gear_list.get("active")]["Defense"]
        layro.health = layro.health - stats_list[gear_list.get("active")]["Health"]

    # Otherwise, add their affect
    elif not gear_list.get("active") == "":
        layro.equipped_weapon = gear_list.get("active")
        layro.attack = layro.attack + stats_list[gear_list.get("active")]["Attack"]
        layro.defense = layro.defense + stats_list[gear_list.get("active")]["Defense"]
        layro.health = layro.health + stats_list[gear_list.get("active")]["Health"]


# asked you if you really want to get rid of your items
def are_you_sure(mestype, tk):
    global fuck
    if not gear_list.get("active") == "":
        fuck = tk.Canvas(width=400, height=200, bg="black")
        fuck.place(relx=.5, rely=.5, anchor="center")
        if mestype == "break down":
            fuck.create_text(20, 0, text="Are you sure you want to break down \n " +
                                        gear_list.get("active") + " for it's materials?",
                             fill="white", anchor="nw", font=("times", 18))

            yes = tk.Button(fuck, text="< Yes >", width=8, height=1, activebackground="black", bg="black",
                            foreground="white", fg="white", bd=0, highlightthickness=0, relief='ridge',
                            font=("times", 15),
                            command=lambda: get_materials_or_soul("materials", materials_list[gear_list.get("active")]))

        if mestype == "get soul":
            fuck.create_text(20, 0, text="Are you sure you want to break down \n " +
                                         gear_list.get("active") + " for "
                                         + str(soul_amount[gear_list.get("active")]) + " soul?",
                             fill="white", anchor="nw", font=("times", 18))

            yes = tk.Button(fuck, text="< Yes >", width=8, height=1, activebackground="black", bg="black",
                            foreground="white", fg="white", bd=0, highlightthickness=0, relief='ridge',
                            font=("times", 15),
                            command=lambda: get_materials_or_soul("soul", int(soul_amount[gear_list.get("active")])))

        no = tk.Button(fuck, text="< No >", width=8, height=1, activebackground="black", bg="black",
                       foreground="white", fg="white", bd=0, highlightthickness=0, relief='ridge',
                       font=("times", 15), command=lambda: fuck.place_forget())

        yes.place(relx=.03, rely=.83, anchor="nw")
        no.place(relx=.75, rely=.83, anchor="nw")


def get_materials_or_soul(rtype, val):
    file2 = open(pth.join(inv_path, "temporary.txt"), "w")
    file = open(pth.join(inv_path, "inventory.txt"), "r")
    if rtype == "soul":
        for l in file:
            # finds the line in the file that stores the current soul count, and adds the "val"
            if "s" in l:
                val2 = l[1:]
                val = int(val2) + int(val)
                file2.write("s" + str(val) + "\n")
            else:
                # finds and deletes the selected item, and writes the rest ot a temporary file
                try:
                    if list(gear.keys())[list(gear.values()).index(gear_list.get("active"))] == int(l):
                        for sel in gear_list.curselection():
                            gear_list.delete(sel)
                        gear_list.activate("end")
                    else:
                        file2.write(l)
                except ValueError:
                    file2.write(l)

    if rtype == "materials":
        used_materials = []
        for m in val:
            # stores what variables to add to
            if "," in m:
                m = m[:-1]
            if not m == "Sharp":
                used_materials.append(m.lower()[:1])
            else:
                used_materials.append("p")

        for line in file:
            # if the variable is one of the ones we're using, then great we add that
            if line[:1] in used_materials:
                new_amount = str(int(line[1:]) + 1)
                file2.write(line[:1] + new_amount + "\n")
            else:
                # then delete the selected item and write the rest to a temp file
                try:
                    if list(gear.keys())[list(gear.values()).index(gear_list.get("active"))] == int(line):
                        for sel in gear_list.curselection():
                            gear_list.delete(sel)
                        gear_list.activate("end")
                    else:
                        file2.write(line)
                except ValueError:
                    file2.write(line)

    # replaces the inventory file with the temp file
    file.close()
    file2.close()
    fuck.place_forget()
    remove(pth.join(inv_path, "inventory.txt"))
    file = open(pth.join(inv_path, "inventory.txt"), "w")
    file2 = open(pth.join(inv_path, "temporary.txt"), "r")

    for line in file2:
        file.write(line)

    file2.close()
    file.close()
    remove(pth.join(inv_path, "temporary.txt"))


def before_dungeon(tk, master, draw_game):
    global set_up, gear_list, item, item_info, description, materials, souls
    global equip, break_down, make_soul, start_run, health, attack, defense

    if not set_up:
        # places all the everything on the screen
        gear_list = tk.Listbox(master, bg="black", fg="white", selectmode="single",
                               font=("times", 9), height="31", width="30")
        item_info = tk.Canvas(master, width=650, height=496, bg="black")
        item_info.create_text(5, 0, text="Item :", fill="white", anchor="nw", font=("times", 20))
        item = item_info.create_text(75, 8, text="", fill="white", anchor="nw", font=("times", 15))
        item_info.create_text(5, 50, text="Description :", fill="white", anchor="nw", font=("times", 20))
        description = item_info.create_text(150, 58, text="", fill="white", anchor="nw", font=("times", 15))
        item_info.create_text(5, 110, text="Materials : ", fill="white", anchor="nw", font=("times", 20))
        materials = item_info.create_text(130, 118, text="", fill="white", anchor="nw", font=("times", 15))
        item_info.create_text(5, 170, text="Souls : ", fill="white", anchor="nw", font=("times", 20))
        souls = item_info.create_text(90, 178, text="", fill="white", anchor="nw", font=("times", 15))
        equip = tk.Button(item_info, text="< Equip >", width=9, height=1, activebackground="black", bg="black",
                          activeforeground="white", fg="white", bd=0, highlightthickness=0, relief='ridge',
                          font=("times", 15), command=lambda: equip_gear())
        inventory = tk.Canvas(master, width=163, height=248, bg="black")
        crafting = tk.Canvas(master, width=163, height=248, bg="black")
        soul_select = tk.Canvas(master, width=163, height=248, bg="black")
        break_down = tk.Button(item_info, text="< Break Down >", width=12, height=1, activebackground="black",
                               bg="black", activeforeground="white", fg="white", bd=0, highlightthickness=0,
                               relief='ridge', font=("times", 15), command=lambda: are_you_sure("break down", tk))
        make_soul = tk.Button(item_info, text="< Make Soul >", width=12, height=1, activebackground="black",
                              bg="black", activeforeground="white", fg="white", bd=0, highlightthickness=0,
                              relief='ridge', font=("times", 15),
                              command=lambda: are_you_sure("get soul", tk))

        start_run = tk.Button(item_info, text="< Depart >", width=12, height=1, activebackground="black",
                              bg="black", activeforeground="white", fg="white", bd=0, highlightthickness=0,
                              relief='ridge', font=("times", 15), command=lambda: start(draw_game))

        item_info.create_text(5, 230, text="Health --> ", fill="white", anchor="nw", font=("times", 20))

        health = item_info.create_text(130, 238, text="", fill="white", anchor="nw", font=("times", 15))

        item_info.create_text(5, 290, text="Attack --> ", fill="white", anchor="nw", font=("times", 20))

        attack = item_info.create_text(130, 298, text="", fill="white", anchor="nw", font=("times", 15))

        item_info.create_text(5, 350, text="Defense --> ", fill="white", anchor="nw", font=("times", 20))

        defense = item_info.create_text(140, 358, text="", fill="white", anchor="nw", font=("times", 15))

        gear_list.grid(row=0, column=0)
        item_info.grid(row=0, column=1)
        inventory.grid(row=0, column=2, sticky="s")
        crafting.grid(row=0, column=2, sticky="n")
        soul_select.grid(row=0, column=2)
        # makes your inventory equal to the one in the inventory file
        for line in file:
            try:
                gear_list.insert("end", gear[int(line)])
            except KeyError:
                continue
            except ValueError:
                continue
        gear_list.insert("end", "")
        gear_list.activate("end")
        equip.place(relx=.1, rely=.99, anchor="s")
        break_down.place(relx=.4, rely=.99, anchor="se")
        make_soul.place(relx=.62, rely=.99, anchor="se")
        start_run.place(relx=.99, rely=.99, anchor="se")
        set_up = True
        file.close()

    # displays all the stats of the current selected weapon
    if not gear_list.get("active") == "":
        item_info.itemconfig(item, text=gear_list.get("active"))
        item_info.itemconfig(description, text=description_list[gear_list.get("active")])
        item_info.itemconfig(materials, text=materials_list[gear_list.get("active")])
        item_info.itemconfig(souls, text=soul_amount[gear_list.get("active")])
        if not layro.equipped_weapon == gear_list.get("active"):
            item_info.itemconfig(health, text=layro.health + stats_list[gear_list.get("active")]["Health"])
            item_info.itemconfig(attack, text=layro.attack + stats_list[gear_list.get("active")]["Attack"])
            item_info.itemconfig(defense, text=layro.defense + stats_list[gear_list.get("active")]["Defense"])
        else:
            item_info.itemconfig(health, text=layro.health - stats_list[gear_list.get("active")]["Health"])
            item_info.itemconfig(attack, text=layro.attack - stats_list[gear_list.get("active")]["Attack"])
            item_info.itemconfig(defense, text=layro.defense - stats_list[gear_list.get("active")]["Defense"])

    if gear_list.get("active") == "":
        item_info.itemconfig(item, text="Nothing")
        item_info.itemconfig(description, text="Literally Nothing")
        item_info.itemconfig(materials, text="")
        item_info.itemconfig(souls, text="")

    if gear_list.get("active") == layro.equipped_weapon:
        equip.config(text="< Unequip >")
    else:
        equip.config(text="< Equip >")

    master.after(5, before_dungeon, tk, master, draw_game)
