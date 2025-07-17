from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Habit Tracker")
window.geometry("402x874")
window.config(bg="#0A192F")

habit_cards = []

def add_habit():
    name = entry_box.get()
    if name.strip() == "":
        return

    y = 207 + len(habit_cards) * 120
    new_card = Habit(name, y)
    habit_cards.append(new_card)
    entry_box.delete(0, END)

class Habit:
    def __init__(self, name, y):
        self.name = name
        self.streak = 0
        self.completed = False
        self.y = y

        # --- Card Background ---
        self.card_img = PhotoImage(file='C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\habit Tracker\\assets\\card.png')
        self.card = Label(window, image=self.card_img, bg="#0A192F")
        self.card.place(x=26, y=self.y)

        # --- Bullet Icon ---
        self.bullet = PhotoImage(file="C:\\Users\\LENOVO\\Downloads\\png.png")
        self.bullet_label = Label(window, image=self.bullet, bg="white")
        self.bullet_label.place(x=50, y=self.y + 14)

        # --- Habit Name Label ---
        self.name_label = Label(window, text=self.name,
                                font=("Helvetica", 16, "bold"),
                                fg="black", bg="white")
        self.name_label.place(x=73, y=self.y + 10)

        # --- Streak Label ---
        self.streak_label = Label(window, text=f"🔥 Streak: {self.streak}",
                                  font=("Helvetica", 12),
                                  fg="black", bg="white")
        self.streak_label.place(x=73, y=self.y + 45)

        # --- Done Button ---
        self.button_img = PhotoImage(file="C:\\Users\\LENOVO\\Downloads\\new done.png")
        self.button = Button(window, image=self.button_img,
                             command=self.mark_done,
                             bd=0, bg="white", activebackground="white",
                             highlightthickness=0, relief="flat",
                             cursor="hand2")
        self.button.place(x=295, y=self.y + 20)

    def mark_done(self):
        if not self.completed:
            self.completed = True
            self.streak += 1
            self.streak_label.config(text=f"🔥 Streak: {self.streak}")
            self.button.config(state="disabled")

# ========== TOP BAR ==========
menu_img = PhotoImage(file="C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\habit Tracker\\assets\\menu.png")
menu_icon = Label(window, image=menu_img, bg="#0A192F")
menu_icon.place(x=25, y=20)

menu_text = Label(window, text="Habit Tracker", font=("Helvetica", 34), fg="white", bg="#0A192F")
menu_text.place(x=80, y=16)

# ========== ENTRY BOX ==========
entry_bg = Image.open("C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\habit Tracker\\assets\\entrybox.png")
entry_bg_img = ImageTk.PhotoImage(entry_bg)
entry_bg_label = Label(window, image=entry_bg_img, bg="#0A192F", bd=0)
entry_bg_label.place(x=35, y=95)

entry_box = Entry(window, bd=0, bg="#F9F5F0", fg="#2E2E2E", font=("Poppins", 12))
entry_box.place(x=40, y=108, width=230, height=24)

# ========== ADD BUTTON ==========
button_img = PhotoImage(file="C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\habit Tracker\\assets\\button.png")
button_circle = Button(window, image=button_img, bg="#0A192F", bd=0,
                       highlightthickness=0, activebackground="#0A192F",
                       command=add_habit)
button_circle.place(x=310, y=95)

add_img = PhotoImage(file="C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\habit Tracker\\assets\\+.png")
add_button = Label(window, image=add_img, bg="white", bd=0, highlightthickness=0)
add_button.place(x=335, y=115)

# ========== PROGRESS ==========
pro_img = PhotoImage(file='C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\habit Tracker\\assets\\progress.png')
progress = Label(window, image=pro_img, bg="#0A192F")
progress.place(x=21, y=736)

laugh_img = PhotoImage(file="C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\habit Tracker\\assets\\laughing 1.png")
laughing = Label(window, image=laugh_img, bg="white")
laughing.place(x=36, y=750)

quote = Label(window, text="Consistency is the key!", font=("Helvetica", 16), bg="white")
quote.place(x=109, y=760)

window.mainloop()
