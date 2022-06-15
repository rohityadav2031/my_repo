

import tkinter as tk

#creating a window 
root=tk.Tk()
root.geometry('1200x600+0+0')
root.title('result 0.1')
root.config(bg='white')
#creating a frame 
top_frame=tk.Frame(root,bg='blue')
top_frame.place(x=10,y=10,width=1180,height=100)

btn_frame=tk.Frame(root,bg='blue')
btn_frame.place(x=10,y=440,width=1180,height=140)

left_frame=tk.Frame(root,bg='red')
left_frame.place(x=10,y=120,width=585,height=300)

right_frame=tk.Frame(root,bg='red')
right_frame.place(x=600,y=120,width=585,height=300)




root.mainloop()
