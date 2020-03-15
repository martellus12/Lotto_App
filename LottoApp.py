
import tkinter as tk
from tkinter import font
import requests
import random
#import pillow
#print(tk.font.families())

HEIGHT = 550
WIDTH = 800
END = 1000
INSERT = 0

lotto = tk.Tk()
lotto.title('Lotto')

canvas = tk.Canvas(lotto, height = HEIGHT, width = WIDTH)
canvas.pack()

def btn_click(game):
    '''This function identifies the Game, and populates the boxes with numbers
        using the appropriate number ranges required for the Game.'''
    if game == 'mm':
        nums = range(1,71)
        mb = random.randint(1,25)
        num_picks = random.sample(nums, k=5)
        mm_num1.delete(0,END)
        mm_num1.insert(0,num_picks[0])
        mm_num2.delete(0,END)
        mm_num2.insert(0,num_picks[1])
        mm_num3.delete(0,END)
        mm_num3.insert(0,num_picks[2])
        mm_num4.delete(0,END)
        mm_num4.insert(0,num_picks[3])
        mm_num5.delete(0,END)
        mm_num5.insert(0,num_picks[4])
        mm_megab.delete(0,END)
        mm_megab.insert(0,mb)

    elif game == 'pb':
        nums = range(1,70)
        powerball = random.randint(1,26)
        num_picks = random.sample(nums, k=5)
        pb_num1.delete(0,END)
        pb_num1.insert(0,num_picks[0])
        pb_num2.delete(0,END)
        pb_num2.insert(0,num_picks[1])
        pb_num3.delete(0,END)
        pb_num3.insert(0,num_picks[2])
        pb_num4.delete(0,END)
        pb_num4.insert(0,num_picks[3])
        pb_num5.delete(0,END)
        pb_num5.insert(0,num_picks[4])
        pb_powb.delete(0,END)
        pb_powb.insert(0,powerball)
    

    else:
        print('Something went wrong with the "Generate Number" Button values.')

###############################################################################
#               START OF MEGAMILLIONS CODE                                    #
###############################################################################


############# FRAMES ##################################################### 
mm_frame = tk.Frame(lotto)
mm_frame.place(relheight = 1, relwidth = 0.5, relx = 0)

mm_numFrame = tk.Frame(mm_frame)
mm_numFrame.place(relheight = 0.3, relwidth = 0.7, relx = 0.15, rely = 0.2)

mm_last5DrawsFrame = tk.Frame(mm_frame,)
mm_last5DrawsFrame.place(relheight = .3, relwidth = 0.8, relx = 0.1, rely = 0.6)



############# LABELS #####################################################
mm_image = tk.PhotoImage(file = 'MMlogo.png')
bg_label = tk.Label(mm_frame, image = mm_image)
bg_label.place(relx = .05, rely = .02)

mm_label = tk.Label(mm_numFrame, text = 'Number Generator')
mm_label.place(relheight = .3, relwidth = .8, relx = .1, rely = 0)

mm_num1Label = tk.Label(mm_numFrame, text = '1')
mm_num2Label = tk.Label(mm_numFrame, text = '2')
mm_num3Label = tk.Label(mm_numFrame, text = '3')
mm_num4Label = tk.Label(mm_numFrame, text = '4')
mm_num5Label = tk.Label(mm_numFrame, text = '5')
mm_mbLabel = tk.Label(mm_numFrame, text = 'MB')
mm_last5drawsLabel1 = tk.Label(mm_last5DrawsFrame, text = 'Last 5 Draws')
mm_last5drawsLabel2 = tk.Label(mm_last5DrawsFrame, anchor=tk.W)
mm_last5Date = tk.Label(mm_last5drawsLabel2, text = 'Date')
mm_last1 = tk.Label(mm_last5drawsLabel2, text = '1')
mm_last2 = tk.Label(mm_last5drawsLabel2, text = '2')
mm_last3 = tk.Label(mm_last5drawsLabel2, text = '3')
mm_last4 = tk.Label(mm_last5drawsLabel2, text = '4')
mm_last5 = tk.Label(mm_last5drawsLabel2, text = '5')
mm_lastMB = tk.Label(mm_last5drawsLabel2, text = 'MB')

mm_num1Label.place(relheight = 0.45, relwidth = 0.15, relx = 0, rely = .3)
mm_num2Label.place(relheight = 0.45, relwidth = 0.15, relx = 0.15, rely = .3)
mm_num3Label.place(relheight = 0.45, relwidth = 0.15, relx = 0.30, rely = .3)
mm_num4Label.place(relheight = 0.45, relwidth = 0.15, relx = 0.45, rely = .3)
mm_num5Label.place(relheight = 0.45, relwidth = 0.15, relx = 0.60, rely = .3)
mm_mbLabel.place(relheight = 0.45, relwidth = 0.15, relx = 0.8, rely = 0.3)
mm_last5drawsLabel1.place(relheight = 0.1, relwidth = 0.4, relx = 0.28, rely = 0.13)
mm_last5drawsLabel2.place(relheight  = 0.11, relwidth = .8, relx = .09, rely = .23)
mm_last5Date.grid(row = 0, column = 0, padx = 33, sticky = tk.W)
mm_last1.grid(row = 0, column = 1, padx = 4)
mm_last2.grid(row = 0, column = 2, padx = 10)
mm_last3.grid(row = 0, column = 3, padx = 2)
mm_last4.grid(row = 0, column = 4, padx = 10)
mm_last5.grid(row = 0, column = 5, padx = 2)
mm_lastMB.grid(row = 0, column = 6, padx = 20)


#############BUTTONS##########################################################################
mm_numgenButton = tk.Button(mm_numFrame, text='Generate Number', command = lambda: btn_click('mm'))
mm_numgenButton.place(relx = .3, rely = 0.84)

############# ENTRY FIELDS ####################################################################
mm_num1 = tk.Entry(mm_numFrame, bd=4, justify = 'center')
mm_num2 = tk.Entry(mm_numFrame, bd=4, justify = 'center')
mm_num3 = tk.Entry(mm_numFrame, bd=4, justify = 'center')
mm_num4 = tk.Entry(mm_numFrame, bd=4, justify = 'center')
mm_num5 = tk.Entry(mm_numFrame, bd=4, justify = 'center')
mm_megab = tk.Entry(mm_numFrame, bd=4, justify = 'center')

mm_num1.place(relheight=0.22, relwidth=0.15, relx=0, rely = 0.6)
mm_num2.place(relheight=0.22, relwidth=0.15, relx=0.15, rely = 0.6)
mm_num3.place(relheight=0.22, relwidth=0.15, relx=0.3, rely = 0.6)
mm_num4.place(relheight=0.22, relwidth=0.15, relx=0.45, rely = 0.6)
mm_num5.place(relheight=0.22, relwidth=0.15, relx=0.60, rely = 0.6)
mm_megab.place(relheight=0.22, relwidth=0.15, relx=0.8, rely = 0.6)

############# TextBoxes #####################################################################
mm_last5Text = tk.Text(mm_last5DrawsFrame, bd = 3)
mm_last5Text.place(relheight = 0.43, relwidth = 0.8, relx = 0.1, rely = 0.35)
r = requests.get('https://data.ny.gov/resource/5xaw-6ayf.json')
if r.status_code < 400:
    draws = r.json()
    for i in range(0,5):
        mm_last5Text.insert(tk.INSERT, draws[i]['draw_date'][0:10])
        mm_last5Text.insert(tk.INSERT, '  ')
        mm_last5Text.insert(tk.INSERT, draws[i]['winning_numbers'])
        mm_last5Text.insert(tk.INSERT, '   ')
        mm_last5Text.insert(tk.INSERT, draws[i]['mega_ball'])
        mm_last5Text.insert(tk.INSERT, '\n')
    mm_last5Text.config(state='disabled')
    print(r.status_code)
    print(type(r.status_code))
else:
    print('There was a problem with the server response.')
###########################################################################################
#                       START OF POWERBALL CODE                                           #
###########################################################################################

############# FRAMES ##################################################### 
pb_frame = tk.Frame(lotto, bg = 'white')
pb_frame.place(relheight = 1, relwidth = 0.5, relx = 0.5)

pb_numFrame = tk.Frame(pb_frame, bg = 'white')
pb_numFrame.place(relheight = 0.3, relwidth = 0.7, relx = 0.15, rely = 0.2, )

pb_last5DrawsFrame = tk.Frame(pb_frame, bg = 'white')
pb_last5DrawsFrame.place(relheight = .3, relwidth = 0.8, relx = 0.1, rely = 0.6)

############# LABELS #####################################################
pb_image = tk.PhotoImage(file = 'PBlogo4.png')
bg_label = tk.Label(pb_frame, image = pb_image)
bg_label.place(relx = 0, rely = 0)

pb_label = tk.Label(pb_numFrame, text = 'Number Generator', bg = 'white')
pb_label.place(relheight = .3, relwidth = .8, relx = .1, rely = 0.05)

pb_num1Label = tk.Label(pb_numFrame, text = '1', bg = 'white')
pb_num2Label = tk.Label(pb_numFrame, text = '2', bg = 'white')
pb_num3Label = tk.Label(pb_numFrame, text = '3', bg = 'white')
pb_num4Label = tk.Label(pb_numFrame, text = '4', bg = 'white')
pb_num5Label = tk.Label(pb_numFrame, text = '5', bg = 'white')
pb_mbLabel = tk.Label(pb_numFrame, text = 'MB', bg = 'white')
pb_last5drawsLabel1 = tk.Label(pb_last5DrawsFrame, text = 'Last 5 Draws', bg = 'white')
pb_last5drawsLabel2 = tk.Label(pb_last5DrawsFrame, anchor=tk.W)
pb_last5Date = tk.Label(pb_last5drawsLabel2, text = 'Date')
pb_last1 = tk.Label(pb_last5drawsLabel2, text = '1')
pb_last2 = tk.Label(pb_last5drawsLabel2, text = '2')
pb_last3 = tk.Label(pb_last5drawsLabel2, text = '3')
pb_last4 = tk.Label(pb_last5drawsLabel2, text = '4')
pb_last5 = tk.Label(pb_last5drawsLabel2, text = '5')
pb_lastMB = tk.Label(pb_last5drawsLabel2, text = 'MB')

pb_num1Label.place(relheight = 0.45, relwidth = 0.15, relx = 0, rely = .3)
pb_num2Label.place(relheight = 0.45, relwidth = 0.15, relx = 0.15, rely = .3)
pb_num3Label.place(relheight = 0.45, relwidth = 0.15, relx = 0.30, rely = .3)
pb_num4Label.place(relheight = 0.45, relwidth = 0.15, relx = 0.45, rely = .3)
pb_num5Label.place(relheight = 0.45, relwidth = 0.15, relx = 0.60, rely = .3)
pb_mbLabel.place(relheight = 0.45, relwidth = 0.15, relx = 0.8, rely = 0.3)
pb_last5drawsLabel1.place(relheight = 0.1, relwidth = 0.4, relx = 0.28, rely = 0.13)
pb_last5drawsLabel2.place(relheight  = 0.11, relwidth = .8, relx = .09, rely = .23)
pb_last5Date.grid(row = 0, column = 0, padx = 33, sticky = tk.W)
pb_last1.grid(row = 0, column = 1, padx = 4)
pb_last2.grid(row = 0, column = 2, padx = 10)
pb_last3.grid(row = 0, column = 3, padx = 2)
pb_last4.grid(row = 0, column = 4, padx = 10)
pb_last5.grid(row = 0, column = 5, padx = 2)
pb_lastMB.grid(row = 0, column = 6, padx = 20)


#############BUTTONS##########################################################################

pb_numgenButton = tk.Button(pb_numFrame, text='Generate Number', command = lambda: btn_click('pb'))
pb_numgenButton.place(relx = .3, rely = 0.84)

############# ENTRY FIELDS ####################################################################

pb_num1 = tk.Entry(pb_numFrame, bd=4, justify = 'center')
pb_num2 = tk.Entry(pb_numFrame, bd=4, justify = 'center')
pb_num3 = tk.Entry(pb_numFrame, bd=4, justify = 'center')
pb_num4 = tk.Entry(pb_numFrame, bd=4, justify = 'center')
pb_num5 = tk.Entry(pb_numFrame, bd=4, justify = 'center')
pb_powb = tk.Entry(pb_numFrame, bd=4, justify = 'center')

pb_num1.place(relheight=0.22, relwidth=0.15, relx=0, rely = 0.6)
pb_num2.place(relheight=0.22, relwidth=0.15, relx=0.15, rely = 0.6)
pb_num3.place(relheight=0.22, relwidth=0.15, relx=0.3, rely = 0.6)
pb_num4.place(relheight=0.22, relwidth=0.15, relx=0.45, rely = 0.6)
pb_num5.place(relheight=0.22, relwidth=0.15, relx=0.60, rely = 0.6)
pb_powb.place(relheight=0.22, relwidth=0.15, relx=0.8, rely = 0.6)

############# TextBox #####################################################################

pb_last5Text = tk.Text(pb_last5DrawsFrame, bd = 3)
pb_last5Text.place(relheight = 0.42, relwidth = 0.8, relx = 0.1, rely = 0.35)
r = requests.get('https://data.ny.gov/resource/d6yy-54nr.json')
if r.status_code < 400:
    draws = r.json()
    for i in range(0,5):
        pb_last5Text.insert(tk.INSERT, draws[i]['draw_date'][0:10])
        pb_last5Text.insert(tk.INSERT, '  ')
        pb_last5Text.insert(tk.INSERT, draws[i]['winning_numbers'][0:14])
        pb_last5Text.insert(tk.INSERT, '   ')
        pb_last5Text.insert(tk.INSERT, draws[i]['winning_numbers'][15:18])
        pb_last5Text.insert(tk.INSERT, '\n')
    pb_last5Text.config(state='disabled')
else:
    print('There was a problem with the server response.')
    
lotto.mainloop()




