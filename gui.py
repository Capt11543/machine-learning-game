import tkinter as tk
from inside_rooms import *

master = tk.Tk()
master.configure(bg="black")
master.title("The Game You Don't Play")
master.geometry("1000x500")
master.update()
master.minsize(int(master.winfo_width()), int(master.winfo_height()))
master.maxsize(int(master.winfo_width()), int(master.winfo_height()))


def draw_game():

        temp_map = []
        button.pack_forget()
        title_screen.pack_forget()
        options_butt.pack_forget()
        quit_butt.pack_forget()

        msg0.config(text=mess[0], bg='black', fg="white", font=('times', console_size), aspect=300)
        msg1.config(text=mess[1], bg='black', fg="white", font=('times', map_size), aspect=300)
        msg2.config(text=mess[2], bg='black', fg="white", justify="center", font=('times', game_size), aspect=300)

        for x in range(0, 50):
            if x == 20:
                listbox.insert("end", "ow, a goblin hit me for 23 damage")
            listbox.insert("end", x)

        listbox.place(relx=0.0, rely=0.0329, height="483")

        if listbox.size() > listbox.cget("height"):
            listbox.config(yscrollcommand=scrollbarv.set)
            scrollbarv.config(command=listbox.yview)
            scrollbarv.place(relx=0.9, rely=-0.01, relheight=1.023)

        for x in (0, listbox.size() + 1):
            if len(listbox.get(x, "end")) > listbox.cget("width"):
                listbox.config(xscrollcommand=scrollbarh.set)
                scrollbarh.config(command=listbox.xview)
                scrollbarh.place(relx=-0.01, rely=0.97, relwidth=1.023)

        for x in range(len(dungeon)):
            del temp_map[:]
            for y in dungeon[x]:
                temp_map.append(str(int(y)))
            dung_map.insert("end", temp_map)
        dung_map.place(relx=.864, rely=0.037)

        msg0.pack(side="left", anchor="n")
        msg1.pack(side="right", anchor="n", padx="50")
        msg2.pack(anchor="n")

        tk.mainloop()


def dis_options():

    title_screen.pack_forget()
    button.pack_forget()
    options_butt.pack_forget()
    quit_butt.pack_forget()

    back_butt.place(relx=0.0, rely=0.95)
    tk.mainloop()


def dis_title():

    back_butt.place_forget()
    title_screen.pack(fill="x", pady=50)
    button.pack(fill="x", padx=master.winfo_width() / 4, pady=25)
    options_butt.pack(fill="x", padx=master.winfo_width() / 4, pady=25)
    quit_butt.pack(fill="x", padx=master.winfo_width() / 4, pady=25)
    tk.mainloop()


left, right, bot, top = room_walls([current_room[0]], [current_room[1]])

mess = ["console", "map", "game"]

console_size = 10
map_size = 10
game_size = 12

msg0 = tk.Message(master)
msg1 = tk.Message(master)
msg2 = tk.Message(master)

title_screen = tk.Message(master, text="The Game You Don't Play", bg="black"
                                , fg="white", font=32, padx="0", justify="center")

button = tk.Button(master, text='Play', width=25, activebackground="black"
                         , activeforeground="white", command=draw_game)

options_butt = tk.Button(master, text='Options', width=25, activebackground="black"
                               , activeforeground="white", command=dis_options)

back_butt = tk.Button(master, text="Back", width=25, activebackground="black"
                            , activeforeground="white", command=dis_title)

quit_butt = tk.Button(master, text="Quit", width=25, activebackground="black"
                            , activeforeground="white", command=master.destroy)

listbox = tk.Listbox(master, bg="black", fg="white", selectmode="single", height="30", width="25")

dung_map = tk.Listbox(master, bg="black", fg="white", selectmode="single", height="8", width="12", font=".5")

scrollbarv = tk.Scrollbar(master=listbox, orient="vertical")
scrollbarh = tk.Scrollbar(master=listbox, orient="horizontal")


dis_title()
