'''
Created on Sep 18, 2015

@author: Steve
'''

import praw
import tkinter
from tkinter import *
import webbrowser

guilogin = tkinter.Tk()
guipost = tkinter.Tk()
#open login window and hide post window at first
guilogin.deiconify()
guipost.withdraw()

#set title for 2 windows
guilogin.title("Please Log in here:")
guipost.title("Reddit News Posts")

#define user name & password variable
#string var has to be defined after tkinter tk()
vname = tkinter.StringVar() 
vpp = tkinter.StringVar()

def display():
    # switch windows
    guilogin.withdraw()
    guipost.deiconify()
    
    # a tuple for user agent
    my_agent = ("windows10:com.pthonstarting.redditApi:v1.0 by /u/MilkyBB")
    r = praw.Reddit(user_agent=my_agent)
    myPosts = r.get_subreddit('news').get_hot(limit = 30)
    r.login(str(vname.get()), str(vpp.get()))
    print("log in succeed!")
    
    already_done = set()
    i = 0
    for cur in myPosts:
        if cur.id not in already_done:
            #lambda function only be executed once, might good fit for button vote situation here
            ptitle = Button(guipost, bd = 0, text = cur, command = lambda url = cur.url: webbrowser.open(url))
            #bd = 0 to make button like text
            ptitle.grid(column = 0, row = i)
            b1 = Button(guipost, text = "Up Vote", command = lambda cur2 = cur : cur2.upvote())
            b1.grid(column = 1, row = i)
            b2 = Button(guipost, text = "Down Vote", command = lambda cur3 = cur : cur3.downvote())
            b2.grid(column = 2, row = i)
            b2 = Button(guipost, text = "Clear Vote", command = lambda cur4 = cur : cur4.clear_vote())
            b2.grid(column = 3, row = i)
            
            already_done.add(cur.id)
            i += 1


# r.send_message('MilkyBB', 'Test Message', "You are awesome tester")
# print("TTTT2")

#user log in windows at start
ulabel = Label(guilogin, text = "User Name: ")
plabel = Label(guilogin, text = "Password: ")
ulabel.grid(column = 0, row = 0)
plabel.grid(column = 0, row = 1)

uentry = Entry(guilogin, textvariable = vname)
vname.set("MilkyBB")
uentry.grid(column = 1, row = 0)
pentry = Entry(guilogin, textvariable = vpp)
vpp.set("guess my password :)")
pentry.grid(column = 1, row = 1)

login_button = Button(guilogin, text = "Login", command = display)
login_button.grid(column = 1, row = 2)

guilogin.mainloop()

# print("end point")
