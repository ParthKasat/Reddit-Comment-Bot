# -*- coding: cp1252 -*-
import praw
import time
import os
import random
import re
list = [
'And you have my bow.',
'THEY’RE TAKING THE HOBBITS TO ISENGARD. ',
'A red sun rises. Blood has been spilled this night.',
'THIS FOREST IS OLD. VERY OLD. FULL OF MEMORIES...AND ANGER.',
'YOUR FRIENDS ARE WITH YOU, ARAGORN.',
'A PLAGUE UPON THE STIFF NECKS OF DWARVES.',
'Shall I describe it to you? Or would you like me to find you a box?',
'WHAT ABOUT SIDE BY SIDE WITH A FRIEND?',
'This is no ordinary Ranger. He is Aragorn, son of Arathorn. You owe him your allegiance.',
'There is a fell voice on the air.',
'A lament for Gandalf',
'Have you heard nothing Lord Elrond has said? The Ring must be destroyed.',
'Come, Gimli! We are gaining on them!',
'You would die before your stroke fell!',
'One small bite is enough to fill the stomach of a grown man!',
'Something draws near. I can feel it.',
'Im on 17!',
'Final count: fourty-two.',
'He was twitching.',
'I feel something, a slight tingle in my fingers, I think its affecting me!',
'Hurry! Frodo and Sam have reached the eastern shore. You mean not to follow them.',
'They run as if the very whips of their masters were behind them!',
'I have not the heart to tell you. For me the grief is still too near.',
'That is one of the Mearas, unless my eyes are cheated by some spell.',
'We have trusted you this far and you have not led us astray. Forgive me. I was wrong to despair. '
]

def bot_login():
	print ("Logging in...")
	r = praw.Reddit(client_id='KzlFs2WOXCy4IA',
                     client_secret = 'h4_dFmp5HZMYoV8FtkooeQ4KAPs',
                     username='legolasbot',
                     password='Parth.kasat3232',
                     user_agent='legolasbot (by /u/legolasbot)')
	print ("Logged in!")
	return r

keywords = ['Legolas', 'legolas']

def run_bota(r, comment_replied_to):
    for comment in r.subreddit('lotrmemes').comments(limit=40):
        if re.search("legolas", comment.body, re.IGNORECASE) and comment.id not in comment_replied_to and not comment.author == r.user.me:
                print( "Legolas has been found")
                random_item = random.choice(list)
                comment.reply(random_item)
                comment_replied_to.append(comment.id)

                with open("comment_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
    print("sleeping for 10 seconds in lotr memes")
    time.sleep(10)
def run_bot(r, comment_replied_to):
    for comment in r.subreddit('lotr').comments(limit=40):
        if re.search("legolas", comment.body, re.IGNORECASE) and comment.id not in comment_replied_to and not comment.author == r.user.me:
                print( "Legolas has been found")
                random_item = random.choice(list)
                comment.reply(random_item)
                comment_replied_to.append(comment.id)

                with open("comment_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
    print("sleeping for 10 seconds in lotr")
    time.sleep(10)

def get_saved_comments():
    if not os.path.isfile("comment_replied_to.txt"):
        comment_replied_to = []
    else:
        with open("comment_replied_to.txt", "r") as f:
            comment_replied_to = f.read()
            comment_replied_to = comment_replied_to.split("\n")
    return comment_replied_to

r = bot_login()
comment_replied_to = get_saved_comments()
while True:
    run_bot(r, comment_replied_to)
    run_bota(r, comment_replied_to)

