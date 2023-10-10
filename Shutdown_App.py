from tkinter import *
import os


def on_enter(event):
    event.widget.config(bg="OrangeRed")

def on_leave(event):
    event.widget.config(bg="LightCoral")



def restart():
    os.system("shutdown /r /t 1")


def restart_time():
    os.system("shutdown /r /t 20")


def logout():
    os.system("shutdown -l")


def shutdown():
    os.system("shutdown /s /t 1")


st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="DeepSkyBlue")

r_button = Button(st, text="Restart", font=("Time New Roman", 20, "bold"), bg="LightCoral",
                  relief=RAISED, cursor="plus", command=restart)
r_button.place(x=150, y=60, height=50, width=200)
r_button.bind("<Enter>", on_enter)
r_button.bind("<Leave>", on_leave)

rt_button = Button(st, text="Restart Time", font=("Time New Roman", 20, "bold"), bg="LightCoral",
                   relief=RAISED, cursor="plus", command=restart_time)
rt_button.place(x=150, y=170, height=50, width=200)
rt_button.bind("<Enter>", on_enter)
rt_button.bind("<Leave>", on_leave)

lg_button = Button(st, text="Log-Out", font=("Time New Roman", 20, "bold"), bg="LightCoral",
                   relief=RAISED, cursor="plus", command=logout)
lg_button.place(x=150, y=270, height=50, width=200)
lg_button.bind("<Enter>", on_enter)
lg_button.bind("<Leave>", on_leave)

st_button = Button(st, text="ShutDown", font=("Time New Roman", 20, "bold"), bg="LightCoral",
                   relief=RAISED, cursor="plus", command=shutdown)
st_button.place(x=150, y=370, height=50, width=200)
st_button.bind("<Enter>", on_enter)
st_button.bind("<Leave>", on_leave)

st.mainloop()
