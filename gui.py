import tkinter as tk
import time as tm
import os
import sys

from generator import *
from creatures import *
from game_funcs import *
from creatures import Hero

# Configuring the window, should be self-explanatory
master = tk.Tk()
master.configure(bg="black")
master.title("The Game You Don't Play")
master.geometry("1000x500")
master.update()

startup = True

# you can't change the window size
master.minsize(int(master.winfo_width()), int(master.winfo_height()))
master.maxsize(int(master.winfo_width()), int(master.winfo_height()))

# sets the path for settings.txt as the current path + in a folder called Data
setting_path = sys.path[0] + "\Data"

try:
    master.iconbitmap(setting_path + "\icon.ico")
except tk.TclError:
    pass

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
    file.write("startup: True\n")
    file = open(os.path.join(setting_path, "setting.txt"), "r+")


offset = {"x": -185, "y": -20}


# makes the settings the ones in the folder
for line in file:
    if "move_to" in line:
        move_to_butt = line[-2:].lower()
    if "attack_button" in line:
        attack_this_butt = line[-2:].lower()
    if "interact_with" in line:
        interact_with = line[-2:].lower()
    if "x_offset" in line:
        offset["x"] = int(line[-5:])
    if "y_offset" in line:
        offset["y"] = int(line[-5:])
    if line == "startup: True":
        startup = True
    if line == "startup: False":
        startup = False

if startup:
    global times
    times = 0

    def start_up(*args):
        master.bind("<Return>", start_up)
        global times
        times += 1
        if times == 1:
            global startup_window, layro_startup, fake_window, plus, layro_startupp
            startup_window = tk.Canvas(master, width=master.winfo_width(), height=master.winfo_height(), bg="black")
            startup_window.pack()
            startup_window.create_text(70, 12,
                                       text="This is Layro: ", fill="white", font=("times", 15))
            layro_startup = startup_window.create_text(130, 12, text=' ☺', fill="white", font=("times", 20), tags="layro_startup")
        if times == 2:
            startup_window.create_text(300, 12, text='Layro wants to be an adventurer', fill="white", font=("times", 15))

        if times == 3:
            startup_window.create_text(120, 40, text='Unfortunately, they suck at it', fill="white",
                                       font=("times", 15))
            startup_window.itemconfig(layro_startup, text=" ☹", font=("times", 28))
        if times == 4:
            startup_window.create_text(400, 40, text='Although, you can help them get better', fill="white",
                                       font=("times", 15))
            startup_window.itemconfig(layro_startup, text=' ☺', font=("times", 20))
        if times == 5:
            startup_window.create_text(115, 70, text="This is the game window", fill="white", font=("times", 15))
            fake_window = tk.Canvas(master, width=master.winfo_width() / 4.5, height=master.winfo_height() / 4.5, bg="black")
            fake_window.place(relx=.23, rely=.12)

        if times == 6:
            startup_window.create_text(115, 100, text="This is where Layro lives", fill="white", font=("times", 15))
            layro_startupp = fake_window.create_text(master.winfo_width() / 9, master.winfo_height() / 9, text="☺", fill="white")

        if times == 7:
            plus = fake_window.create_text(master.winfo_width() / 6, master.winfo_height() / 9, text="+", fill="white")
            startup_window.create_text(82, 140, text="You can press " + move_to_butt.capitalize(), fill="white", font=("times", 15))
            startup_window.create_text(100, 160, text="to make Layro move", fill="white", font=("times", 15))
        if times == 8:
            def move_guy():
                global layro_startupp, plus
                if not int(fake_window.coords(layro_startupp)[0]) == int(fake_window.coords(plus)[0] - 30):
                    fake_window.coords(layro_startupp, int(fake_window.coords(layro_startupp)[0] + 1), int(fake_window.coords(layro_startupp)[1]))
                    fake_window.after(20, move_guy)
                else:
                    startup_window.create_text(135, 190, text="But sometimes, they won't listen", fill="white", font=("times", 15))
            move_guy()
        if times == 9:
                def move_guy2():
                    global layro_startupp, plus
                    if not int(fake_window.coords(layro_startupp)[1]) == 120:
                        fake_window.coords(layro_startupp, int(fake_window.coords(layro_startupp)[0]),
                                           int(fake_window.coords(layro_startupp)[1]) + 1)
                        fake_window.after(10, move_guy2)
                    else:
                        start_up()
                move_guy2()
        if times == 10:
            fake_window.create_text(100, 50, text="G", fill="light green")
            fake_window.create_text(150, 50, text="□", fill="white")
            fake_window.delete(plus)
            startup_window.create_text(90, 230, text="You can also use " + attack_this_butt.capitalize(), fill="white", font=("times", 15))
            startup_window.create_text(300, 220, text="to tell them to attack something", fill="white", font=("times", 15))
            fake_window.create_rectangle(90, 40, 110, 60, outline="red", dash=(2, 6), tags="fuck")
        if times == 11:
            fake_window.delete("fuck")
            startup_window.create_text(90, 265, text="You can also use " + interact_with.capitalize(), fill="white",
                                       font=("times", 15))
            startup_window.create_text(330, 256, text="to tell them to interact with something", fill="white",
                                       font=("times", 15))
        if times == 12:
            startup_window.delete("all")
            startup_window.create_text(90, 270, text="But be careful", fill="white",
                                       font=("times", 15))
        if times == 13:
            startup_window.create_text(90, 290, text="This castle", fill="white",
                                       font=("times", 15))
            fake_window.create_rectangle(140, 40, 160, 60, outline="yellow", dash=(2, 6))

        if times == 14:
            startup_window.create_text(100, 310, text="Contains dark secrets", fill="white",
                                       font=("times", 15))
            master.unbind("<Return>")
            fake_window.place_forget()

            def help_us():
                for i in range(100):
                    startup_window.create_text(ra.randint(0, master.winfo_width()), ra.randint(0, master.winfo_height()), text="help us", fill="white",
                                                          font=("times", 15), tags="help")
                if not len(startup_window.find_withtag("help")) > 1500:
                    master.after(1, help_us)
                else:
                    start_up()
            help_us()

        if times >= 15:
            startup_window.pack_forget()

    start_up()


# FIXME: not sure why the above is in gui, is there a better place?


def draw_game():

        global sug_x, sug_y, rorx, rory

        # checks if there is a door on each side of the room
        left, right, bot, top = room_walls(layro.map_x, layro.map_y)

        temp_map = []
        enemies = []
        enemy_sprites = []
        button.pack_forget()
        title_screen.pack_forget()
        options_butt.pack_forget()
        quit_butt.pack_forget()

        msg0.config(text=mess[0], bg='black', fg="white", font=('times', console_size), aspect=300)
        msg1.config(text=mess[1], bg='black', fg="white", font=('times', map_size), aspect=300)
        msg2.config(text=mess[2], bg='black', fg="white", justify="center", font=('times', game_size), aspect=300)

        # places the console
        console.place(relx=0.0, rely=0.037)

        def send_to_console(phrase):

            console.insert("end", phrase)

            # if there's too many items in the console, it draws a scrollbar
            if console.size() > console.cget("height"):
                console.config(yscrollcommand=scrollbarv.set)
                scrollbarv.config(command=console.yview)
                scrollbarv.place(relx=.97, rely=-0.01, relheight=1.023)

            # if there's too long of an item in the console, it draws a scrollbar
            for pos in (0, console.size() + 1):
                if len(console.get(pos)) > console.cget("width"):
                    console.config(xscrollcommand=scrollbarh.set)
                    scrollbarh.config(command=console.xview)
                    scrollbarh.place(relx=-0.01, rely=0.97, relwidth=.195)

            console.update()

        # draws the map
        for xcor in range(len(dungeon)):
            del temp_map[:]
            for ycor in dungeon[xcor]:
                temp_map.append(str(int(ycor)))
            dev_map.insert("end", temp_map)
        dev_map.place(relx=.888, rely=0.41)

        player_map.place(relx=.888, rely=0.037)

        def draw_map():
            for x_pos in range(len(dungeon_map)):
                for y_pos, room in enumerate(dungeon_map[x_pos]):
                    if room.x_pos == layro.map_x and room.y_pos == layro.map_y:
                        if not room.discovered:
                            room.set_discovered(True)

                    if room.discovered:
                        if room.x_pos == layro.map_x and room.y_pos == layro.map_y:
                            player_map.create_text((room.y_pos * 13) + 7, (room.x_pos * 13) + 7,
                                                   text="X", fill="light green", tags="room")
                        else:
                            player_map.create_text((room.y_pos * 13) + 7, (room.x_pos * 13) + 7,
                                                   text="X", fill="white", tags="room")

        draw_map()

        # makes the actual game window, with sides representing the game walls
        game_win.place(relx=.18565, rely=0.037, height="480")
        left, right, bot, top = room_walls(layro.map_x, layro.map_y)

        def draw_dung(left_d, right_d, bot_d, top_d):

            # checks if there is a door on each side of the room
            global top_wall, bot_wall, left_wall, right_wall

            game_win.delete("wall")

            # draws the walls with no doors first, then checks if there's doors and draws the walls if not
            game_win.create_line(0, 0, 250, 0, fill="white", tags="wall")
            game_win.create_line(450, 0, 800, 0, fill="white", tags="wall")

            game_win.create_line(0, 479, 250, 479, fill="white", tags="wall")
            game_win.create_line(450, 479, 800, 479, fill="white", tags="wall")

            game_win.create_line(0, 0, 0, 180, fill="white", tags="wall")
            game_win.create_line(0, 300, 0, 479, fill="white", tags="wall")

            game_win.create_line(699, 0, 699, 180, fill="white", tags="wall")
            game_win.create_line(699, 300, 699, 479, fill="white", tags="wall")

            if not top_d or layro.map_y == 0:
                top_wall = game_win.create_line(250, 0, 450, 0, fill="white", tags="wall")
            else:
                top_wall = 0

            if not bot_d:
                bot_wall = game_win.create_line(250, 479, 450, 479, fill="white", tags="wall")
            else:
                bot_wall = 0

            if not left_d or layro.map_x == 0:
                left_wall = game_win.create_line(0, 180, 0, 300, fill="white", tags="wall")
            else:
                left_wall = 0

            if not right_d:
                right_wall = game_win.create_line(699, 180, 699, 300, fill="white", tags="wall")
            else:
                right_wall = 0

        draw_dung(left, right, bot, top)

        # makes layro
        dude = game_win.create_text(layro.posx, layro.posy, text="☺", fill="white", tags="dude")

        # places the console, game, map labeler s. Are these even necessary? we might want the screen space more
        msg0.place(relx=.035, rely=-0.005)
        msg1.place(relx=.92, rely=-0.005)
        msg2.place(relx=.45, rely=-0.005)

        health.place(relx=.89, rely=.26)
        locations.place(relx=.89, rely=.3)
        controls1.place(relx=.89, rely=.34)

        # Different "suggestions", which layro will ignore if they're high enough level

        # Creates a moveto, which is self-explanitory
        def move_to(event):
            # if there's already a MoveTo, replace it an it's console message
            if not event.x == layro.posx and not event.y == layro.posy:
                if game_win.find_withtag("target"):
                    game_win.delete("target")
                    if "MoveTo" in console.get("end"):
                        console.delete("end")
                # Makes a MoveTO if one doesn't already exist there
                if not (str(event.y + offset["y"]) in console.get("end")
                        and str(event.x + offset["x"]) in console.get("end")):
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

            game_win.delete("attack")

            for item in game_win.find_withtag("enemy"):
                if item in game_win.find_overlapping(event.x - 3 + offset["x"],
                                                     event.y - 3 + offset["y"],
                                                     event.x + 3 + offset["x"],
                                                     event.y + 3 + offset["y"]):

                    game_win.create_rectangle(game_win.coords(item)[0] - 10,
                                              game_win.coords(item)[1] - 10,
                                              game_win.coords(item)[0] + 10,
                                              game_win.coords(item)[1] + 10,
                                              outline="red", dash=(2, 6), tags=("attack", "room-specific"))
                    global att_x, att_y
                    att_x = (game_win.coords("attack")[0] + game_win.coords("attack")[2]) / 2
                    att_y = (game_win.coords("attack")[1] + game_win.coords("attack")[3]) / 2

        # FIXME: make this pick up the selected item, with visual indicator
        def interact(event):
            print(event.x, event.y, "interact")

        # FIXME: make this delete things with the room-specific tag, and delete their associated object instances
        def change_rooms():
            locations.config(text="locations: (" + str(layro.map_y) + "," + str(layro.map_x) + ")")
            game_win.delete("room-specific")
            global left, right, bot, top
            left, right, bot, top = room_walls(layro.map_x, layro.map_y)
            draw_dung(left, right, bot, top)
            draw_map()
            for x_pos in range(len(dungeon_map)):
                for y_pos, room in enumerate(dungeon_map[x_pos]):
                    if room.x_pos == layro.map_x and room.y_pos == layro.map_y:
                        if "gob_pos1" in room.contents:
                            enemies.append(Goblin(enemies, layro))
                            enemy_sprites.append(game_win.create_text(enemies[len(enemies) - 1].xpos,
                                                                      enemies[len(enemies) - 1].ypos,
                                                                      text=enemies[len(enemies) - 1].symbol,
                                                                      fill=enemies[len(enemies) - 1].color,
                                                                      tags=("enemy", "room-specific",)))
                        if "shade_pos1" in room.contents:
                            enemies.append(Shade(enemies, layro))
                            enemy_sprites.append(game_win.create_text(enemies[len(enemies) - 1].xpos,
                                                                      enemies[len(enemies) - 1].ypos,
                                                                      text=enemies[len(enemies) - 1].symbol,
                                                                      fill=enemies[len(enemies) - 1].color,
                                                                      tags=("enemy", "room-specific",)))

        def change_floors():
            for x_pos in range(len(dungeon_map)):
                for y_pos, room in enumerate(dungeon_map[x_pos]):
                    room.set_discovered(False)
            player_map.delete("room")
            change_rooms()

        # Binds all the buttons in settings.txt to their respective commands
        master.bind(move_to_butt, move_to)
        master.bind(attack_this_butt, attack)
        master.bind(interact_with, interact)

        def game_loop():
            global rorx_inc, rory_inc, rorx, rory
            for z, q in zip(enemies, enemy_sprites):
                try:
                    if z.map_x == layro.map_x and z.map_y == layro.map_y:
                        z.behavior(q, dude, game_win, layro)
                except NameError or ValueError:
                        pass

            # if there's a suggestion, go near it, otherwise, move randomly (randomly will be replace with ml stuff
            # FIXME: make this do different behaviors depending on suggestion type
            if len(game_win.find_withtag("target")) > 0:
                layro.posx, layro.posy = layro.sug_step(sug_x, sug_y, "MoveTo")
                if layro.posx == sug_x and layro.posy == sug_y:
                    game_win.delete("target")
            elif len(game_win.find_withtag("attack")) > 0:
                layro.posx, layro.posy = layro.sug_step(att_x, att_y, "AttackThis")
            else:
                layro.posx, layro.posy = layro.rand_step()
            game_win.coords("dude", layro.posx, layro.posy)

            # are you in a door? is the door open? then go through it
            if 450 > layro.posx > 250:
                if 490 > layro.posy > 470 and bot_wall not in game_win.find_all():
                    layro.map_x += 1
                    layro.posx, layro.posy = layro.posx, 100.0
                    game_win.delete("target")
                    change_rooms()
                if 20 > layro.posy > -10 and top_wall not in game_win.find_all():
                    layro.map_x -= 1
                    layro.posx, layro.posy = layro.posx, 100.0
                    game_win.delete("target")
                    change_rooms()

            if 300 > layro.posy > 180:
                if 710 > layro.posx > 690 and right_wall not in game_win.find_all():
                    layro.map_y += 1
                    layro.posx, layro.posy = 100.0, layro.posy
                    game_win.delete("target")
                    change_rooms()
                if 20 > layro.posx > -10 and left_wall not in game_win.find_all():
                    layro.map_y -= 1
                    layro.posx, layro.posy = 600.0, layro.posy
                    game_win.delete("target")
                    change_rooms()

            # for y in range(len(dungeon_map)):
            #     for x in range(len(dungeon_map[y])):
            #         if dungeon_map[y][x].room_type == 3:
            #             layro.map_y, layro.map_x = y, x

            if dungeon_map[layro.map_y][layro.map_x].room_type == 3:
                rec_x = master.winfo_width() / 3
                rec_y = master.winfo_height() / 2

                if rorx > 20:
                    if ra.randint(0, 6) > 3 or rorx > 25:
                        rorx_inc = False
                if rorx < 0:
                    if ra.randint(0, 6) > 3:
                        rorx_inc = True

                if rorx_inc:
                    rorx += 1
                if not rorx_inc:
                    rorx -= 1

                if rory > 20:
                    if ra.randint(0, 6) > 3 or rory > 25:
                        rory_inc = False
                if rory < 0:
                    if ra.randint(0, 6) > 3:
                        rory_inc = True

                if rory_inc:
                    rory += 1
                if not rory_inc:
                    rory -= 1

                if len(game_win.find_withtag("exit")) == 0:
                    game_win.create_rectangle(rec_x + rorx, rec_y + rory, rec_x - rorx, rec_y - rory,
                                              outline="#e5b329", tags=("exit", "room-specific"))
                if not len(game_win.find_withtag("exit")) == 0:
                    game_win.coords("exit", rec_x + rorx, rec_y + rory, rec_x - rorx, rec_y - rory)

                if dude in game_win.find_overlapping(game_win.coords("exit")[0],
                                                     game_win.coords("exit")[1],
                                                     game_win.coords("exit")[2],
                                                     game_win.coords("exit")[3]):
                    regenerate(8, 8)
                    change_floors()

            master.after(10, game_loop)

        game_loop()


def dis_options():

    # The options screen
    # FIXME: make it so you can change settings here
    title_screen.pack_forget()
    button.pack_forget()
    options_butt.pack_forget()
    quit_butt.pack_forget()

    test_window.place(x=400, y=100)

    back_butt.place(relx=0.0, rely=0.95)

    tk.mainloop()


def dis_title():

    # The title screen

    back_butt.place_forget()
    test_window.place_forget()

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

sug_x, sug_y = 0, 0
rorx, rory = 20, 20
rorx_inc, rory_inc = False, False

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

console = tk.Listbox(master, bg="black", fg="white", selectmode="single", font=("times", 9), height="29", width="30")

dev_map = tk.Listbox(master, bg="black", fg="white", selectmode="single", height="8", width="12", font=("times", 14),
                     highlightthickness=0, relief="ridge", bd=0)

player_map = tk.Canvas(master, width=105, height=105, bg="black")

game_win = tk.Canvas(master, width=700, height=480, bg="black", bd=0, highlightthickness=0, relief='ridge')

scrollbarv = tk.Scrollbar(master=console, orient="vertical")
scrollbarh = tk.Scrollbar(orient="horizontal")

health = tk.Message(master, text="health: " + str(Hero.health), bg="black", fg="white")

controls1 = tk.Message(master, text="create MoveTo: " + move_to_butt, bg="black", fg="white", width="400")

locations = tk.Message(master, text="locations: (" + str(layro.map_y) + "," + str(layro.map_x) + ")", bg="black",
                       fg="white", width="400")

test_window = tk.Canvas(master, width=700, height=480, bg="black")


# gotta make sure the title is the first thing displayed
dis_title()
