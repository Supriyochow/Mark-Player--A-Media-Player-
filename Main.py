#Importing modules
import os	#for using os functions
import threading		#for running threads
import time				#for using time
import tkinter			#using Tkinter the GUI library

import tkinter.messagebox	#for printing messages using tkinter
import tkinter as tttk	#import all functions from tkinter
from tkinter import *
from tkinter import filedialog	#used for importing and exporting files it offers set of dialogs when working with files

from tkinter import ttk #for getting access to ttkthemes widgets
from ttkthemes import themed_tk as tk #used for importing ttkthemes templates

from mutagen.mp3 import MP3 #used for handling audio files
from pygame import mixer		#used for loading sound objects and controlling there playback



#Set the theme and get the root file
root=tk.ThemedTk()				#calling the theme widget
root.get_themes()				#getting a list of themes
root.set_theme("plastik")		#setting my favourite theme of ttktheme



#Canvas to create a background image
C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "E://projects//MP3 Player//33acdb7e6fe8424fbb8ea273674c745c.png")		#Only png image is supported
background_label = Label(root, image=filename)
background_label.place(x=0, y=0)



#Setting the bottom label of the window
#A relief is a border decoration. The possible values are: SUNKEN, RAISED, GROOVE, RIDGE, and FLAT.
#Anchors are used to define where text is positioned relative to a reference point.
# Fonts - Arial (corresponds to Helvetica), Courier New (Courier), Comic Sans MS, Fixedsys,
# MS Sans Serif, MS Serif, Symbol, System, Times New Roman (Times), and Verdana

statusBar1 = ttk.Label(root, text="Welcome to Mark Player", anchor=W, font="Times 10 italic")		#setting the label of the tkinter, Anchor gives the direction in West
statusBar1.pack(side=TOP, fill=X)
statusBar2=ttk.Label(root, text="Developed by Supriyo Chowdhury", relief=SUNKEN, anchor=E, font="Times 10 italic")	#giving the credits, Anchor gives the direction in East
statusBar2.pack(side=BOTTOM,fill=X)



#Setting the title and the icon of the player and also the size of the player
root.title("Mark Player")				#title of the player
root.iconbitmap(r'E://projects//MP3 Player//afasfasfasfasf.ico')		#location of the icon is used it should be of icon format
root.geometry('1200x600')


#Creating a Hover Button from stackoverflow, link: https://stackoverflow.com/questions/49888623/tkinter-hovering-over-button-color-change
class HoverButton(tttk.Button):
    def __init__(self, master, **kw):
        tttk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.defaultForeground = self["foreground"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']
        self['foreground'] = self['activeforeground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground
        self['foreground'] = self.defaultForeground

 


#These are created inaccordance with code in line , to have the first menu option of FILE


#Taking a playlist list
playlist=[]	#playlist contains the fullpath + filename which would be used for playing the file
playlistbox=[]	#playlist box just contains filename which is used for showing


#function to browse songs and play them
def browseFiles():
	global filenamePath			#used to make the variable global
	global fileSong
	filenamePath=filedialog.askopenfilenames(title="Choose A Song")	#used for opening the file
	#We are looping through the total files
	for fileSong in filenamePath:

		add_to_playlist(fileSong)	#adding to the playlist

		mixer.music.queue(fileSong)	#putting the file name into the queue of playing music using mixer of pygame
		#Simultaneously we have to initialize the mixer. The initialization is done in 



#Creating the playlist
def add_to_playlist(filename):
	global fileSong	
	filename= os.path.basename(filename)
	index = 0
	playlistbox.insert(index, filename)
	playlist.insert(index, fileSong)
	index += 1



#Funtion for deleting the playlist
def del_song():
    selected_song = playlistbox.curselection()	#selecting the song through curser
    selected_song = int(selected_song[0])	#converting the index into integer
    playlistbox.delete(selected_song)		#delete the song from playlistbox
    playlist.pop(selected_song)				#pop it from the playlist

#These are created inaccordance with code in line, to have the 2nd menu option of HELP
def about_us():
    tkinter.messagebox.showinfo("About Mark Player", "This is an interactive music player build using Python by Supriyo Chowdhury in 2020")	

def help_info():
    tkinter.messagebox.showinfo("Help","Click on the Add Song button and Select them in the playlist. Play them and enjoy your music.")    



#Creating Menu
#Creating the menu-bar
menubar=Menu(root, bg="#dbca30",tearoff=0,activebackground="#dbca30")		#selecting a color 

#Creating sub-menu
subMenu=Menu(menubar, tearoff=0)		#tearoff helps us to create a floating menu

#Creating the menu buttons
#1st Button in Menu
#Creating the File menu
menubar.add_cascade(label="File", menu=subMenu)		#has a sub menu
subMenu.add_command(label="Open", command=browseFiles)		#Browse function is in line 55
subMenu.add_command(label="Exit", command=root.destroy)		#used for exiting the file

#2nd button in Menu
#Creating the Help menu
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="Help", command=help_info)
submenu.add_command(label="About Us", command=about_us)



#initializing mixer
mixer.init()







#Creating Frame for having a rectangular container for other widgets
#In left there will be the list of songs

#Creating styles for the frame
s=ttk.Style()	#initializing style
s.configure('My.TFrame', background='#61d7ff', activebackground="#f0dc69", relief=RAISED)		#configuring style with a name

#Creating the left frame
lframe=ttk.Frame(root, style='My.TFrame')	#initializing the frame

#lframe.pack(side=LEFT, padx=100, pady=30)		#packing the frame setting the paddings in x and y axis
lframe.place(height=400, width=250, relx=0.76, rely=0.115)
lframe.config()	#configuring the frame and setting the width
#putting the frame
playlistbox=Listbox(lframe, bg='#101d33', fg='#26b7ff', width=40, height=22)
playlistbox.pack()



#Creating the necessary buttons
#Button to add the songs 
Btn1 = HoverButton(lframe, text="Add Songs",command=browseFiles, activebackground="#101d33", activeforeground="#ffffff", width=17, height=3)	#active background should be written to hover color
Btn1.pack(side=LEFT)
#addBtn.grid()

#Button to delete song
Btn2 = HoverButton(lframe, text="Delete Songs",command=del_song, activebackground="#101d33", activeforeground="#ffffff", width=17, height=3)
Btn2.pack(side=LEFT)





#Creating the music interface in the right and the top frame
rframe=Frame(root)
rframe.pack(pady=50)

#Creating the top frame of the right frame for music
tframe=Frame(rframe)
tframe.pack(pady=60)

#Creating a bottom frame for the slider
sframe=Frame(rframe)
sframe.pack()


#Getting the time label of the song i.e the total time and the current time
totalTimeLabel = ttk.Label(tframe, text='Total Length : --:--', relief=GROOVE)		#Gives the total length of the song
totalTimeLabel.pack(pady=5)
currentTimeLabel = ttk.Label(tframe, text='Time Elapsed : --:--', relief=GROOVE)
currentTimeLabel.pack()



#Function to display the details of the song
def disp_details(playSong1):
	global totalTime
	fileData=os.path.splitext(playSong1)		#used for splitting the texts inside the song details

	#Condition is checked whether it is MP3 or not
	if fileData[1] =='.mp3':				#if the 2nd element of the list is .mp3 file then we will play the file
		audio=MP3(playSong1)					#playing the MP3 using the mutagen.mp3
		totalTime=audio.info.length	#returns the total length of the song
	#Mixer is used for playing othewr format songs, here mp3 is also being played but mixer has a glitchy mp3 control hence we use mutagen.mp3	
	else:
		leftSong=mixer.Sound(playSong1)		#Playing the song for other formats
		totalTime=leftSong.get_length()	#Gives the total length of the song

	#Getting the minutes and the seconds of the song
	#We divide using 60 and modulus using 60
	mins,secs=divmod(totalTime,60)		#division modulus with 60
	#rounding the figures
	mins=round(mins)
	secs=round(secs)
	#Having the time-format with string formatting
	timef = '{:02d}:{:02d}'.format(mins,secs)	
	totalTimeLabel['text'] = "Total Time"+"-"+timef

	#Starting threads for mutlti threading
	th=threading.Thread(target=countTime, args=(totalTime,))
	th.start()


#define auto checking function
def AutoCheck():
	global presentTime
	global totalTime
	if int(presentTime)==int(totalTime+1):
		AutonextSong() 

#Functions definition to control the music playing
#Function to mute the music from music button
def muteSong():
	global ismuted 			#ismuted is a variable which takes true or false. If true it ia already mute and if false it is not muted

	if ismuted:			#we have to unmute here
		mixer.music.set_volume(0.7)		#unmuting and setting the volume to 70%
		volumeBtn.configure(image=voPhoto)		#now its unmuted with vol photo
		scale.set(70)		#setting the scale
		ismuted=FALSE 		#setting it to false
	else:				#we have to mute here
		mixer.music.set_volume(0)	#setting the volume to zero
		volumeBtn.config(image=muPhoto)			##muting now and putting the muted photo
		scale.set(0)			#setting the scale to zero 
		ismuted=TRUE 			#setting it to true


#Function to count the time elapsed for the song
def countTime(t):
	global paused			#creating a pause variable
	global presentTime			#taking the present time as zero
	global totalTime
	global songSelected
	totalTime=t
	while presentTime<=t and mixer.music.get_busy(): 	#get_busy() returns false when stop button is pressed
		if paused:
			continue
		else:
			mins, secs = divmod(presentTime, 60)		#calculating the time by division modulus function
			mins = round(mins)							#rounding the minutes
			secs = round(secs)							#rounding the seconds
			timeformat = '{:02d}:{:02d}'.format(mins, secs)		#formatting the current time using string formatting
			currentTimeLabel['text'] = "Time Elapsed" + ' - ' + timeformat
			#currentTimeLabel=ttk.Label(tframe, text="Current Time : "+timeformat, relief=GROOVE)


			
				
			if int(Slider.get()) == int(presentTime-1):
				#Slider is not moved, then normal things should happen
				#Updating the slider
				SliderLength=int(totalTime)
				Slider.config(to=SliderLength, value=int(presentTime))	#here value is made  because we need to sent the slider back to beginning when a new song is played
			else:
				#Slider is moved, then changes should be made
				#Updating the slider
				SliderLength=int(totalTime)			
				Slider.config(to=SliderLength, value=int(Slider.get()))	#here value is made 0 because we need to sent the slider back to beginning when a new song is played
				presentTime=Slider.get()
				mins, secs = divmod(presentTime, 60)		#calculating the time by division modulus function
				mins = round(mins)							#rounding the minutes
				secs = round(secs)							#rounding the seconds
				timeformat = '{:02d}:{:02d}'.format(mins, secs)		#formatting the current time using string formatting
				currentTimeLabel['text'] = "Time Elapsed" + ' - ' + timeformat

				
			#Slider.config(value=int(presentTime))	#here value is made 0 because we need to sent the slider back to beginning when a new song is played
			#sliderLabel.config(text=f'Slider: {int(Slider.get())} and Song Position: {int(presentTime)}')

			#Updating the slider
			#SliderLength=int(totalLength)
			
			#Slider.config(to=SliderLength, value=int(presentTime))	#here value is made 0 because we need to sent the slider back to beginning when a new song is played

		time.sleep(1)
		presentTime += 1						#incrementing by each second
	
	#forwardButton.invoke()
	AutoCheck()

#Function to play music
def playSong():
	global paused			#using the paused variable
	global songSelected
	global index
	global totalTime
	global totalLength


	#if it is paused then we need to unpause that
	if paused:
		playS= playlist[songSelected]
		mixer.music.unpause()		#this will unpause the music
		statusBar1['text'] = "Playing music" + ' - ' + os.path.basename(playS)		#Changing the status bar message	#Music Resumed will be printed
		paused=FALSE
	else:				#if music is not paused
		#We need to take try accept block if filedialog couldn't find the files
		try:
			stopSong()			#stopping the song initially
			time.sleep(1)		#for getting 1 second
			songSelected = playlistbox.curselection()		#select song through cursor
			songSelected = int(songSelected[0])				#taking the first element that is the mp3
			index=songSelected
			playS= playlist[songSelected]					#song selected from the playlist is taken
			mixer.music.load(playS)								#Loading the song
			mixer.music.play()								#Playing the song
			statusBar1['text'] = "Playing music" + ' - ' + os.path.basename(playS)		#Changing the status bar message
			disp_details(playS)								#displaying the details

			#Updating the slider
			SliderLength=int(totalTime)
			Slider.config(to=SliderLength, value=0)	#here value is made 0 because we need to sent the slider back to beginning when a new song is played

			

			

		except:
			tkinter.messagebox.showerror('File not found', 'Marky Player could not find the file. Please select a song from the playlist')	#Showing error through message box

	#while not mixer.music.get_busy():
		#nextSong();			

#Function to stop music
def stopSong():
	global presentTime
	presentTime=0
	mixer.music.stop()						#stopping the music
	statusBar1['text']= "Music Stopped"		#Changing the status bar message
	totalTimeLabel['text'] = "Total Time : --:--"
	currentTimeLabel['text'] = "Time Elapsed : --:--"

	Slider.config(value=0)	#here value is made 0 because we need to sent the slider back to beginning when a new song is played

paused=FALSE	#Initializing for avoiding error


#Function to pause music
def pauseSong():
	global paused
	paused=TRUE
	mixer.music.pause()
	statusBar1['text'] = "Music Paused"


#Function for auto playing next song
def AutonextSong():
	global songSelected
	global totalTime
		
	stopSong()
	#Slider.config(value=0)	#here value is made 0 because we need to sent the slider back to beginning when a new song is played
	time.sleep(1)
	songSelected+=1
	if songSelected<len(playlist):
		playS=playlist[songSelected]
		mixer.music.load(playS)								#Loading the song
		mixer.music.play()								#Playing the song
		statusBar1['text'] = "Playing music" + ' - ' + os.path.basename(playS)		#Changing the status bar message
		disp_details(playS)								#displaying the details
	#Used for getting the control the played song
	#USed for clearing all selection
	#Updating the slider
		#SliderLength=int(totalTime)
		#Slider.config(to=SliderLength, value=0)	#here value is made 0 because we need to sent the slider back to beginning when a new song is played
		#playlistbox.selection_clear(0,END)
		#playlistbox.activate(songSelected)
	else:
		songSelected-=1
		playS=playlist[songSelected]
		mixer.music.load(playS)								#Loading the song
		mixer.music.play()								#Playing the song
		statusBar1['text'] = "Playing music" + ' - ' + os.path.basename(playS)		#Changing the status bar message
		disp_details(playS)								#displaying the details
		#Used for getting the control the played song
		#USed for clearing all selection
		#Updating the slider
		#SliderLength=int(totalTime)
		#Slider.config(to=SliderLength, value=0)	#here value is made 0 because we need to sent the slider back to beginning when a new song is played
		#playlistbox.selection_clear(0,END)
		#playlistbox.activate(songSelected)		

#Function to get to the next song
def nextSong():
	global songSelected
	global totalTime

	stopSong()
	Slider.config(value=0)	#here value is made 0 because we need to sent the slider back to beginning when a new song is played
	time.sleep(1)
	songSelected+=1

	if songSelected<len(playlist):
		try:	
			playS=playlist[songSelected]
			mixer.music.load(playS)								#Loading the song
			mixer.music.play()								#Playing the song
			statusBar1['text'] = "Playing music" + ' - ' + os.path.basename(playS)		#Changing the status bar message
			disp_details(playS)								#displaying the details
			#Used for getting the control the played song
			#USed for clearing all selection
			#Updating the slider
			SliderLength=int(totalTime)
			Slider.config(to=SliderLength, value=0)	#here value is made 0 because we need to sent the slider back to beginning when a new song is played
			playlistbox.selection_clear(0,END)
			playlistbox.activate(songSelected) 
		except:
			tkinter.messagebox.showerror('File not found', 'Marky Player could not find the file. Please select a song from the playlist')	#Showing error through message box
	else:
		songSelected-=1
		playS=playlist[songSelected]
		mixer.music.load(playS)								#Loading the song
		mixer.music.play()								#Playing the song
		statusBar1['text'] = "Playing music" + ' - ' + os.path.basename(playS)		#Changing the status bar message
		disp_details(playS)								#displaying the details
		#Used for getting the control the played song
		#USed for clearing all selection
		#Updating the slider
		SliderLength=int(totalTime)
		Slider.config(to=SliderLength, value=0)	#here value is made 0 because we need to sent the slider back to beginning when a new song is played
		playlistbox.selection_clear(0,END)
		playlistbox.activate(songSelected)
	

	#while not mixer.music.get_busy():
		#nextSong();	

#Function to get to the previous song
def previousSong():
	global songSelected
	global totalTime
	stopSong()
	Slider.config(value=0)	#here value is made 0 because we need to sent the slider back to beginning when a new song is played
	time.sleep(1)
	songSelected-=1
	if songSelected>=0:
		try:	
			playS=playlist[songSelected]
			mixer.music.load(playS)								#Loading the song
			mixer.music.play()								#Playing the song
			statusBar1['text'] = "Playing music" + ' - ' + os.path.basename(playS)		#Changing the status bar message
			disp_details(playS)								#displaying the details
			#Used for getting the control the played song
			#USed for clearing all selection
			#Updating the slider
			SliderLength=int(totalTime)
			Slider.config(to=SliderLength, value=0)	#here value is made 0 because we need to sent the slider back to beginning when a new song is played
			playlistbox.selection_clear(0,END)
			playlistbox.activate(songSelected) 
		except:
			tkinter.messagebox.showerror('File not found', 'Marky Player could not find the file. Please select a song from the playlist')	#Showing error through message box
	else:
		songSelected+=1
		playS=playlist[songSelected]
		mixer.music.load(playS)								#Loading the song
		mixer.music.play()								#Playing the song
		statusBar1['text'] = "Playing music" + ' - ' + os.path.basename(playS)		#Changing the status bar message
		disp_details(playS)								#displaying the details
		#Used for getting the control the played song
		#USed for clearing all selection
		#Updating the slider
		SliderLength=int(totalTime)
		Slider.config(to=SliderLength, value=0)	#here value is made 0 because we need to sent the slider back to beginning when a new song is played
		playlistbox.selection_clear(0,END)
		playlistbox.activate(songSelected)
	

#Function to Rewind the music
def rewindMusic():
	global songSelected
	playS=playlist[songSelected]
	mixer.music.load(playS)								#Loading the song
	mixer.music.play()
	SliderLength=int(totalTime)
	Slider.config(to=SliderLength, value=0)	#here value is made 0 because we need to sent the slider back to beginning when a new song is played
	
	statusBar1['text'] = "Music Rewinded"
	statusBar1['text'] = "Playing music" + ' - ' + os.path.basename(playS)		#Changing the status bar message		

#Function to set volume
def setSound(value):
	volume=float(value)/100			# set_volume of mixer takes value only from 0 to 1. Example - 0, 0.1,0.55,0.54.0.99,1
	mixer.music.set_volume(volume)		#Setting the volume


#Function to set the Song Slider
def slide(x):
	global songSelected
	#sliderLabel.config(text=f'{int(Slider.get())} of {int(totalLength)}')		#This is done to make the song length change into integer
	#Used for playing the song and changing its precision on dragging the slider
	playS= playlist[songSelected]					#song selected from the playlist is taken
	mixer.music.load(playS)								#Loading the song
	mixer.music.play(start=int(Slider.get()))								#Playing the song and setting it 


#Designing the music playing interface in the top and right frames
#Creating a middle frame in the right
mframe=Frame(rframe)
mframe.pack(pady=30, padx=30)

#Creating the back button of the player
baPhoto=PhotoImage(file="E://projects//MP3 Player//prevF.png")	#getting the image of the button
backButton=ttk.Button(mframe,image=baPhoto, command=previousSong)
backButton.grid(row=0, column=0, padx=10)

#Creating the play button of the player
plPhoto=PhotoImage(file="E://projects//MP3 Player//playF.png")	#getting the image of the button
playButton=ttk.Button(mframe,image=plPhoto, command=playSong)
playButton.grid(row=0, column=1, padx=10)

#Creating the pause button of the player
paPhoto=PhotoImage(file="E://projects//MP3 Player//pauseF.png")	#getting the image of the button
pauseButton=ttk.Button(mframe,image=paPhoto, command=pauseSong)
pauseButton.grid(row=0, column=2, padx=10)

#Creating the stop button of the player
stPhoto=PhotoImage(file="E://projects//MP3 Player//stopF.png")	#getting the image of the button
stopButton=ttk.Button(mframe,image=stPhoto, command=stopSong)
stopButton.grid(row=0, column=3, padx=10)

#Creating the rewind button
rePhoto=PhotoImage(file='E://projects//MP3 Player//rewindF.png')	#getting the image of the button
rewindButton=ttk.Button(mframe,image=rePhoto, command= rewindMusic)
rewindButton.grid(row=0, column=4)

#Creating Forward Button of the player
foPhoto=PhotoImage(file="E://projects//MP3 Player//nextF.png")	#getting the image of the button
forwardButton=ttk.Button(mframe,image=foPhoto, command=AutonextSong)
forwardButton.grid(row=0, column=5, padx=10)


#Creating bottom frame in the right frame
bframe=Frame(rframe)
bframe.pack()


#Creating mute and volume button
muPhoto=PhotoImage(file='E://projects//MP3 Player//MuteF.png')	#getting the image of the mute button
voPhoto=PhotoImage(file='E://projects//MP3 Player//VolumeF.png')	#getting the image of the volume button
ismuted=FALSE 																		#defined previously otherwise shows an error
volumeBtn = ttk.Button(bframe, image=voPhoto, command=muteSong)
volumeBtn.grid(row=0, column=0)

#Creating the volume button horizontal bar 
#Using scale to create the horizontal bar
scale=ttk.Scale(bframe,from_=0, to=100, orient=HORIZONTAL, command=setSound)		#Making the bar horizontal
scale.set(70)			#setting the scale during starting
mixer.music.set_volume(0.7)		#setting the initial volume at 70%
scale.grid(row=0,column=2, pady=15, padx=30)		#getting the volume bar

#Creating a song Slider
#Length is used for setting the length of the slider
Slider=ttk.Scale(sframe,from_=0, to=100, orient=HORIZONTAL, length=500, command=slide)		#command=slide
Slider.pack(pady=0)


#Create temporary slider Label
#sliderLabel=Label(sframe,text='0')	#Commenting for temporary use
#sliderLabel.pack(pady=10)








#Function for operations on closing
def close():
	stopSong()		#Stopping the song
	root.destroy()		#destroying the root

	



root.config(menu=menubar)
root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()			#main loop window


