import tkinter as tk
import time as tm
import os
import sys
import gc

from game_funcs import *
from generator_working import *
from creatures import *

# Configuring the window, should be self-explanitory
master = tk.Tk()
master.configure(bg="black")
master.title("The Game You Don't Play")
master.geometry("1000x500")
master.update()

# you can't change the window size
master.minsize(int(master.winfo_width()), int(master.winfo_height()))
master.maxsize(int(master.winfo_width()), int(master.winfo_height()))

# sets the path for settings.txt as the current path + in a folder called Data
setting_path = sys.path[0] + "\Data"

# make the Data folder if it doesn't exist
if not os.path.exists(setting_path):
    os.makedirs(setting_path)

# If the settings file exists, use the setting in it
try:
    file = open(os.path.join(setting_path, "setting.txt"), "r+")

# Otherwise, write to it the default settings
except FileNotFoundError:
    file = open(os.path.join(setting_path, "setting.txt"), "w")
    file.write("move_to_button: W\n")
    file.write("attack_button: A\n")
    file.write("interact_with: D\n")
    file.write("x_offset: -185\n")
    file.write("y_offset: -20\n")


offset = {"x": -185, "y": -20}

# FIXME: better way to change a file to write? cuz if we didn't have this is would crash on the first time running it
file.close()
file = open(os.path.join(setting_path, "setting.txt"), "r+")

# makes the settings the ones in the folder
for line in file:
    if "move_to" in line:
        move_to_butt = line[-2:].lower()
    if "attack_button" in line:
        attack_this_butt = line[-2:].lower()
    if "interact_with" in line:
        interact_with = line[-2:].lower()
    if "x_offset" in line:
        offset[x] = int(line[-4:])
    if "y_offset" in line:
        offset[y] = int(line[-4:])

# FIXME: not sure why the above is in gui, is there a better place?


def draw_game():
        # checks if there is a door on each side of the room
        left, right, bot, top = room_walls(current_room[0], current_room[1])
        current_cors = [300, 225]

        temp_map = []
        button.pack_forget()
        title_screen.pack_forget()
        options_butt.pack_forget()
        quit_butt.pack_forget()

        msg0.config(text=mess[0], bg='black', fg="white", font=('times', console_size), aspect=300)
        msg1.config(text=mess[1], bg='black', fg="white", font=('times', map_size), aspect=300)
        msg2.config(text=mess[2], bg='black', fg="white", justify="center", font=('times', game_size), aspect=300)

        # places the console
        # FIXME: could you rename this to "console" in all places where the variable is referenced, not the datatype
        listbox.place(relx=0.0, rely=0.037)

        def send_to_console(phrase):

            listbox.insert("end", phrase)

            # if there's too many items in the console, it draws a scrollbar
            if listbox.size() > listbox.cget("height"):
                listbox.config(yscrollcommand=scrollbarv.set)
                scrollbarv.config(command=listbox.yview)
                scrollbarv.place(relx=.97, rely=-0.01, relheight=1.023)

            # if there's too long of an item in the console, it draws a scrollbar
            for pos in (0, listbox.size() + 1):
                if len(listbox.get(pos)) > listbox.cget("width"):
                    listbox.config(xscrollcommand=scrollbarh.set)
                    scrollbarh.config(command=listbox.xview)
                    scrollbarh.place(relx=-0.01, rely=0.97, relwidth=.195)

            listbox.update()

        # draws the map, temporary for now, soon it'll just show discovered rooms
        # FIXME: any way you could make it just discovered rooms?
        for xcor in range(len(dungeon)):
            del temp_map[:]
            for ycor in dungeon[xcor]:
                temp_map.append(str(int(ycor)))
            dung_map.insert("end", temp_map)
        dung_map.place(relx=.888, rely=0.037)

        # makes the actual game window, with sides representing the game walls
        game_win.place(relx=.18565, rely=0.037, height="480")

        def draw_dung():

            # checks if there is a door on each side of the room
            global left, right, bot, top
            left, right, bot, top = room_walls(current_room[0], current_room[1])
            game_win.delete("wall")

            # FIXME: put this with the stats rather than the console
            send_to_console("current room: (" + str(current_room[1]) + "," + str(current_room[0]) + ")")

            # draws the walls with no doors first, then checks if there's doors and draws the walls if not
            game_win.create_line(0, 0, 250, 0, fill="white")
            game_win.create_line(450, 0, 800, 0, fill="white")

            game_win.create_line(0, 479, 250, 479, fill="white")
            game_win.create_line(450, 479, 800, 479, fill="white")

            game_win.create_line(0, 0, 0, 180, fill="white")
            game_win.create_line(0, 300, 0, 479, fill="white")

            game_win.create_line(699, 0, 699, 180, fill="white")
            game_win.create_line(699, 300, 699, 479, fill="white")

            if not top:
                game_win.create_line(250, 0, 450, 0, fill="white", tags="wall")
            if not bot:
                game_win.create_line(250, 479, 450, 479, fill="white", tags="wall")
            if not left:
                game_win.create_line(0, 180, 0, 300, fill="white", tags="wall")
            if not right:
                game_win.create_line(699, 180, 699, 300, fill="white", tags="wall")

        draw_dung()

        # makes layro
        game_win.create_text(current_cors[0], current_cors[1], text="☺", fill="white", tags="dude")

        # places the console, game, map labelers. Are these even necessary? we might want the screen space more
        msg0.place(relx=.035, rely=-0.005)
        msg1.place(relx=.92, rely=-0.005)
        msg2.place(relx=.45, rely=-0.005)

        # FIXME: makes these a little prettier
        health.place(relx=.89, rely=.39)
        controls1.place(relx=.89, rely=.43)

        # Where the game loop starts, above is initialization and stuff

        game = True

        # Different "suggestions", which layro will ignore if they're high enough level

        # Creates a moveto, which is self-explanitory
        def move_to(event):
            # if there's already a MoveTo, replace it an it's console message
            if not event.x == current_cors[0] and not event.y == current_cors[1]:
                if game_win.find_withtag("target"):
                    game_win.delete("target")
                    if "MoveTo" in listbox.get("end"):
                        listbox.delete("end")
                # Makes a MoveTO if one doesn't already exist there
                if not (str(event.y + offset["y"]) in listbox.get("end")
                        and str(event.x + offset["x"]) in listbox.get("end")):
                    game_win.create_text(event.x + offset["x"], event.y + offset["y"], text="+", fill="white",
                                         tags=("target", "suggestion"))
                    send_to_console("MoveTo created at (" + str(event.x + offset["x"]) + "," +
                                    str(event.y + offset["y"]) + ")")
                # Makes the location and type of the suggestion global, so layro can go to it
                global sug_x, sug_y, sug_type
                sug_x = event.x + offset["x"]
                sug_y = event.y + offset["y"]
                sug_type = "MoveTo"
        # FIXME: make this attack the selected target, with a visual indicator

        def attack(event):
            print(event.x, event.y, "attack")

        # FIXME: make this pick up the selected item, with visual indicator
        def interact(event):
            print(event.x, event.y, "interact")

        # FIXME: make this delete things with the room-specific tag, and delete their associated object instances
        def change_rooms():
            game_win.delete("room-specfic")
            draw_dung()

        # Binds all the buttons in settings.txt to their respective commands
        master.bind(move_to_butt, move_to)
        master.bind(attack_this_butt, attack)
        master.bind(interact_with, interact)

        # makes a Goblin named gob1 and an invisiblee sightline box around him
        gob1 = Goblin()
        gobbo = game_win.create_text(gob1.xpos, gob1.ypos, text=gob1.symbol, fill="light green",
                                     tags=("goblin", "enemy", "room-specific"))
        gobbo_sight = game_win.create_rectangle(gob1.xpos - Goblin.range / 4, gob1.ypos - gob1.range / 4,
                                                gob1.xpos + gob1.range / 4, gob1.ypos + gob1.range / 4,
                                                tags="rooms-specific")
        while game:

            # checks if layro is overlapping in gobbo sight
            # FIXME: remove gobbosight, make it so find_overlapping uses gobbo's coords instead
            # FIXME: Layro might not always be id 12, is there a better way to do this?
            if not gob1.chasing and 12 in game_win.find_overlapping(game_win.coords(gobbo_sight)[0],
                                                                    game_win.coords(gobbo_sight)[1],
                                                                    game_win.coords(gobbo_sight)[2],
                                                                    game_win.coords(gobbo_sight)[3]):

                # make gob1 angry if he sees layro
                game_win.itemconfig(gobbo, fill="red")
                game_win.delete(gobbo_sight)
                gob1.chasing = True
                game_win.coords(gobbo, Goblin.chase(gob1, current_cors[0], current_cors[1]))

            # If the goblin is angry, he chases layro
            if gob1.chasing:
                game_win.coords(gobbo, Goblin.chase(gob1, current_cors[0], current_cors[1]))
                gob1.xpos, gob1.ypos = Goblin.chase(gob1, current_cors[0], current_cors[1])

            tm.sleep(.01)

            # if there's a suggestion, go near it, otherwise, move randomly (randomly will be replace with ml stuff
            # FIXME: make this do different behaviors depending on suggestiong type
            if len(game_win.find_withtag("suggestion")) > 0:
                current_cors = sug_step(current_cors[0], current_cors[1], sug_x, sug_y, sug_type, 1)
                if current_cors[0] == sug_x and current_cors[1] == sug_y:
                    game_win.delete("suggestion")
            else:
                current_cors = rand_step(current_cors[0], current_cors[1], 1)
            game_win.coords("dude", current_cors[0], current_cors[1])

            # are you in a door? is the door open? then go through it
            # FIXME: maybe you could delete the room-specific things here?
            if 450 > current_cors[0] > 250:
                if 490 > current_cors[1] > 470 and bot:
                    current_room[0] += 1
                    current_cors = current_cors[0], 100.0
                    game_win.delete("target")
                    change_rooms()
                if 20 > current_cors[1] > -10 and top:
                    current_room[0] -= 1
                    current_cors = current_cors[0], 100.0
                    game_win.delete("target")
                    change_rooms()

            if 300 > current_cors[1] > 180:
                if 710 > current_cors[0] > 690 and right:
                    current_room[1] += 1
                    current_cors = 100.0, current_cors[1]
                    game_win.delete("target")
                    change_rooms()
                if 20 > current_cors[0] > -10 and left:
                    current_room[1] -= 1
                    current_cors = 600.0, current_cors[1]
                    game_win.delete("target")
                    change_rooms()
            # FIXME: constantly updating walls might take memory, but wihout it the walls are wrong
            left, right, bot, top = room_walls(current_room[0], current_room[1])
            game_win.update()
            # FIXME: make it so layro is limited by the bounds of the walls
            # FIXME: sometimes a left door is created when it shouldn't on the opening room


def dis_options():

    # The options screen
    # FIXME: make it so you can change settings here
    title_screen.pack_forget()
    button.pack_forget()
    options_butt.pack_forget()
    quit_butt.pack_forget()

    back_butt.place(relx=0.0, rely=0.95)

    tk.mainloop()


def dis_title():

    # The title screen

    back_butt.place_forget()

    title_screen.pack(fill="x", pady=50)
    button.pack(fill="x", padx=master.winfo_width() / 4, pady=25)
    options_butt.pack(fill="x", padx=master.winfo_width() / 4, pady=25)
    quit_butt.pack(fill="x", padx=master.winfo_width() / 4, pady=25)

    tk.mainloop()


# array of messages
mess = ["console", "map", "game"]

# individual sizes for the messages
console_size = 10
map_size = 10
game_size = 10

msg0 = tk.Message(master)
msg1 = tk.Message(master)
msg2 = tk.Message(master)

title_screen = tk.Message(master, text="The Game You Don't Play", bg="black",
                          fg="white", font=32, padx="0", justify="center")

button = tk.Button(master, text='Play', width=25, activebackground="black",
                   activeforeground="white", command=draw_game)

options_butt = tk.Button(master, text='Options', width=25, activebackground="black",
                         activeforeground="white", command=dis_options)

back_butt = tk.Button(master, text="Back", width=25, activebackground="black",
                      activeforeground="white", command=dis_title)

quit_butt = tk.Button(master, text="Quit", width=25, activebackground="black",
                      activeforeground="white", command=master.destroy)


listbox = tk.Listbox(master, bg="black", fg="white", selectmode="single", font=("times", 9), height="29", width="30")

dung_map = tk.Listbox(master, bg="black", fg="white", selectmode="single", height="8", width="12", font=("times", 14),
                      highlightthickness=0, relief="ridge", bd=0)

game_win = tk.Canvas(master, width=700, height=480, bg="black", bd=0, highlightthickness=0, relief='ridge')

scrollbarv = tk.Scrollbar(master=listbox, orient="vertical")
scrollbarh = tk.Scrollbar(orient="horizontal")

health = tk.Message(master, text="health: " + str(Hero.health), bg="black", fg="white")

controls1 = tk.Message(master, text="create MoveTo: " + move_to_butt, bg="black", fg="white", width="400")

# gotta make sure the title is the first thing displayed
dis_title()
