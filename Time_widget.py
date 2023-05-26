from tkinter import *
from tkinter import font
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.configure(text=current_time)
    root.after(1000, update_time)  # updates the time every second

def dateformat():
    ctime = time.localtime(time.time())
    year = ctime.tm_year
    month = ctime.tm_mon
    day = ctime.tm_mday
    weekday = ctime.tm_wday

    wdaylist = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    mlist = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    return str(wdaylist[weekday]) + " " + str(day) + " " + str(mlist[month-1]) + " " + str(year)

def quitwin(event):
    root.destroy()
    quit()

def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)

root =Tk()
root.attributes("-alpha", 0.4)  # sets the transparency of the widget
root.geometry("250x100+1100-100")  # sets the size of the widget
root.overrideredirect(True)  # removes the title bar from the widget
root.config(bg="white")  # sets the background color


# creating a font and a label to display the time
my_font = font.Font(family="calibri", size=36, weight="bold")
clock_label =Label(root, text="", font=my_font, bg="white", fg="black")
clock_label.pack(fill=BOTH, expand=1)

datefont = font.Font(family="lucida handwriting",size =16, weight="bold")
dateshow = Label(root, text=dateformat(), font=datefont, bg="white", fg= "blue")
dateshow.pack()
# function to update the time on the label


update_time()
dateformat()

root.bind("<F12>", quitwin) # to bind the key for quit


root.mainloop()
