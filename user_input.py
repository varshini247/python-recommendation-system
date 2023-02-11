#!/usr/bin/env python
# coding: utf-8

# In[1]:


# export PYTHONPATH="${PYTHONPATH}:C:\Users\v\projects_python\project1"
import sys
import time

# MODULE_FULL_PATH = r'C:\Users\v\projects_python'

# sys.path.insert(1, MODULE_FULL_PATH)
# sys.path.append(r'../')
#print(sys.path)
# %load_ext autoreload
# %autoreload 2


# In[2]:


import tkinter as tk
import main as f1
import random

# In[1]:

# inputs


root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=700)
canvas.grid(columnspan=3)
frame1 = tk.Frame(root, bg='#001219')
frame1.place(relwidth=1, relheight=1)
frame2 = tk.Frame(root, bg='#001219')
frame2.place(relwidth=1, relheight=1)
frame3 = tk.Frame(root, bg='#001219')
frame3.place(relwidth=1, relheight=1)
frame4 = tk.Frame(root, bg='#001219')
frame4.place(relwidth=1, relheight=1)
frame1.tkraise()


# actions
def clicked_tv():
    frame2.tkraise()
    ep_label = tk.Label(frame2, text='Enter the number of episodes', bg='black', fg='grey', font=20)
    ep_label.place(relx=0.15, rely=0.4, relwidth=0.7, relheight=0.09)
    # v1=tk.IntVar()
    # s1 = tk.Scale(frame2, variable =v1, from_= 1, to = 1000, orient = tk.HORIZONTAL, bg= '#5D0C7A' )
    # s1.place(relx=0.15,rely = 0.5, relwidth =0.7,relheight = 0.09)
    ep_entry = tk.Entry(frame2, bg='grey')
    ep_entry.place(relx=0.15, rely=0.6, relwidth=0.7, relheight=0.09)
    button_submit = tk.Button(frame2, text="Enter", bg='grey', command=lambda: get_val(ep_entry))
    button_submit.place(relx=0.4, rely=0.8, relwidth=0.3, relheight=0.09)


def get_val(ep_entry):
    #     frame2.update()
    ep_no = ep_entry.get()
    # print(ep_no)
    genre_list = f1.input_tv(ep_no)
    genre_display(genre_list)


# s1['state'] = 'disabled'
# s1.bind("<ButtonRelease-1>", genre_display(ep_no))
# time.sleep(10)
# s1.after(2000,genre_display(ep_no))

def genre_display(genre_list):
    frame3.tkraise()
    bg_list = ['#74508f', '#005f73','#0d331d','#e9d8a6','#ee9b00','#9b2226','#0c8dc4','#0a9396']
    posx = 0.15
    posy = 0.2
    for genre in genre_list:
        button = tk.Button(frame3, text=genre, bg=random.choice(bg_list), command=lambda genre=genre: genre_select(genre))
        button.place(relx=posx, rely=posy, relwidth=0.2, relheight=0.09)
        posx += 0.2
        # printing in the next line
        if posx == 0.75:
            posx = 0.15
            posy += 0.1


def genre_select(genre):
    # button_name = button['text']
    print(genre)
    f1.input_genre(genre)
    output()


def clicked_mv():
    ep_no, genre_list = f1.input_mv()
    genre_display(genre_list)


def output():
    frame4.tkraise()
    result = f1.result_data()
    columns = result.values.tolist()
    columns = columns[0]
    #print(columns)
    headers = result.columns.values.tolist()
    # label = tk.Label(frame4,text=result['title'],bg='black',fg='grey',font = 20)
    # label.place(relx=0.15, rely=0.2, relwidth=0.7, relheight=0.09)
    posx = 0.05
    posy = 0.02
    for header,col in zip(headers,columns):
        # if type(col) is list:
        #     col = col[0]
        label_txt = header + ' : ' + str(col)
        print(label_txt)
        label1 = tk.Label(frame4, text=label_txt, bg='black', fg='grey', font=20)
        label1.place(relx=posx, rely=posy, relwidth=0.9, relheight=0.03)
        print('hi')

        # label2 = tk.Label(frame4, text=col, bg='black', fg='grey', font=20)
        # label2.place(relx=posx+0.3, rely=posy, relwidth=0.7, relheight=0.04)
        posy += 0.04


# labels
type_label = tk.Label(frame1, text='select the type you want to watch', bg='#001219', fg='grey', font=20)
type_label.place(relx=0.15, rely=0.2, relwidth=0.7, relheight=0.09)
# type_label.grid(row=0,column=3)
button1 = tk.Button(frame1, text='TV', bg='#0a9396', command=clicked_tv)
button1.place(relx=0.15, rely=0.3, relwidth=0.35, relheight=0.09)
# button1.grid(column = 3, row = 1)
button2 = tk.Button(frame1, text='Movie', bg='#0a9396', command=clicked_mv)
button2.place(relx=0.5, rely=0.3, relwidth=0.35, relheight=0.09)

# entries
# entry = tk.Entry(frame, font = 20, bg='grey')
# entry.place(relx=0.15,rely = 0.2,relwidth = 0.7, relheight = 0.09)
root.mainloop()

# In[ ]:
