from Tkinter import *
import tkMessageBox
from PIL import Image, ImageTk
from os import listdir
from os.path import isfile, join
import platform
import os
import re
import subprocess
import Lisa_tape_funcs

token = 'BQAg9WczhvZ5mqzTdFDHvm1O3J9XZh9wYbJfXHhhTrV0Z30J8_9nI4O0vJhUe8knFmBr6If00S9qX9HfXAAgr4Uw_bcWychrDcD2yISjL3CskQFcWlPz04AL3m3gQxaJpghWP7tPV_FdS80kOoSJ1eKCQQ'
import token_for_spotipy


class App(object):


    class input_box:
        def __init__(self,App_instance,parent_frame):
            row = 0
            column = 0
            self.parent_frame = parent_frame
            self.height = 200
            self.width = 500
            self.cell_width= 18
            self.cell_height= 1
            self.canvas = Canvas(self.parent_frame, width=self.width, height=self.height, background='black')
            self.label1 = Label(self.canvas, text="Enter Song Name and Artist Name", fg="white")
            self.label_window1 = self.canvas.create_window(132, 20,  window=self.label1)

            # Text input box
            self.entrytext = StringVar()
            self.entry_box = Entry(self.canvas, textvariable=self.entrytext, fg="white",bg='grey',width=20)
            self.canvas.create_window(115, 50, window=self.entry_box)

            # Go Button
            self.buttontext = StringVar()
            self.buttontext.set("Seed")
            self.seed_button = Button(self.canvas, textvariable=self.buttontext, command=lambda: App_instance.clicked1(self.entrytext),width=self.cell_width,height=self.cell_height)
            self.canvas.create_window(115, 80, window=self.seed_button)

            # Download Button
            self.buttontext = StringVar()
            self.buttontext.set("Download")
            self.download_button = Button(self.canvas, textvariable=self.buttontext, command=lambda: App_instance.download(),width=self.cell_width,height=self.cell_height)
            self.canvas.create_window(115, 110, window=self.download_button)

            #Draw Seperators

            self.canvas.create_line(265,15,265,120,fill='white')
            self.canvas.create_line(20, 140, 470, 140, fill='white')


            self.canvas.pack(side=TOP, anchor='c', padx=0, pady=0)
            #Draw Checkboxes
            option1=IntVar()
            self.option1 = Checkbutton(self.canvas, text="", variable=option1,fg='white')
            self.option1_text = Label(self.canvas,text="option1",fg='white')
            self.canvas.create_window(70,160,window=self.option1_text)
            self.canvas.create_window(30,160,window=self.option1)


        def show_found_song(self,App_instance,parent_frame,title,artist_name,index):
            pass

            self.App_instance = App_instance
            self.image_size = 100
            self.mypath = os.getcwd() + '/webfiles/'
            self.song_title = title
            self.image_path = self.mypath + title + '_image.jpeg'
            self.tkobjects = []
            self.parent_frame = parent_frame
            self.index = index
            self.track_name = title
            self.artist_name = artist_name
            im = Image.open(self.image_path)
            resized = im.resize((self.image_size, self.image_size), Image.ANTIALIAS)
            self.tkimage = ImageTk.PhotoImage(resized)
            self.found_song = self.canvas.create_image(380,self.image_size+15 , image=self.tkimage, anchor='se')

            s = title
            if len(s) > 20:
                s = s[:20] + '...'
                TEXT = s
                print("concatenated to " + TEXT)
            else:
                TEXT = s
            self.tkobjects.append(Label(self.canvas, text=TEXT, fg="white"))
            self.canvas.create_window(430, 25, window=self.tkobjects[0])

            s = self.artist_name
            if len(s) > 20:
                s = s[:20] + '...'
                TEXT = s
                print("concatenated to " + TEXT)
            else:
                TEXT = s
            self.tkobjects.append(Label(self.canvas, text=TEXT, fg="white"))
            self.canvas.create_window(430, 45, window=self.tkobjects[1])

    class Song_spotify:
        def __init__(self,App_instance, parent_frame, title,artist_name,index):
            self.App_instance = App_instance
            self.image_size = 150
            self.mypath = os.getcwd() +'/webfiles/'
            self.song_title = title
            self.image_path = self.mypath + title + '_image.jpeg'
            self.tkobjects = []
            self.parent_frame = parent_frame
            self.index = index
            self.track_name = title
            self.artist_name = artist_name
            #print("got track name " +track_name)
            # path = mypath + title
            # infile = path


            # Add image


            im = Image.open(self.image_path)
            resized = im.resize((self.image_size, self.image_size), Image.ANTIALIAS)
            self.tkimage = ImageTk.PhotoImage(resized)
            #image_widget = Label(self.parent_frame, image=self.tkimage)
            #image_widget.image = self.tkimage
            #image_widget.bind("<Button-1>", lambda x: self.add_to_selected())
            #self.tkobjects.append(self.image_widget)
            self.canvas = Canvas(self.parent_frame, width=self.image_size, height=self.image_size, background='black')
            self.canvas.create_image(self.image_size, self.image_size, image=self.tkimage,anchor='se')
            self.canvas.bind("<Button-1>", lambda x: self.add_to_selected())
            self.tkobjects.append(self.canvas)
            #self.canvas.pack()
            # Add name
            s = title
            if len(s) > 20:
                s = s[:20] + '...'
                TEXT = s
                print("concatenated to " + TEXT)
            else:
                TEXT = s
            self.tkobjects.append(Label(self.parent_frame, text=TEXT, fg="white"))

            s = self.artist_name
            if len(s) > 20:
                s = s[:20] + '...'
                TEXT = s
                print("concatenated to " + TEXT)
            else:
                TEXT = s
            self.tkobjects.append(Label(self.parent_frame, text=TEXT, fg="white"))


        def add_to_grid(self, row, column):
            self.row = row
            self.column = column
            self.tkobjects[0].grid(row=row, column=column) #Album Art
            self.tkobjects[1].grid(row=row+ 1, column=column) #Song Title
            self.tkobjects[2].grid(row=row + 2, column=column) #Artist Title
            pass

        def add_to_selected(self):
            #print(type((self.song_title)))
            self.App_instance.add_to_selected(self.song_title, self.index)
            row = self.row
            column = self.column
            #self.tkobjects[3].append()

            self.progress_id = self.tkobjects[0].create_text(self.image_size//2,self.image_size//2,anchor='c',fill='white')
            #self.button_outline = self.tkobjects[0].create_circle(self.image_size//2,self.image_size//2,anchor='c',fill='white')
            self.tkobjects[0].itemconfig(self.progress_id,text="TICK")

            #self.tkobjects[0].insert(self.progress_id,12,"TICK",color='white')
            #self.tkobjects[3].grid(row=row, column=column)  # Album Art



        def complete_download(self):
            self.tkobjects[0].itemconfig(self.progress_id,text="Downloaded")

    def __init__(self):
        f = open('token.txt', 'r')
        token = f.read()
        self.seeder = Lisa_tape_funcs.Song_seeder(tolken=token)
        self.COLUMNS = 3
        self.cwd = os.getcwd()
        self.root = Tk()
        self.root.tk_setPalette(background='#000000', foreground='black',
                                activeBackground='black', activeForeground='black')
        #self.root.wm_attributes('-transparent', 'true')

        self.root.geometry('500x500')  # Size 200, 200
        self.selected = []
        # self.root['bg'] = 'black'


        #Window Title
        self.root.wm_title("BPM Matcher")
        self.label = Label(self.root, text="Enter Song Name and Artist Name", fg="white")
        #self.label.pack()
        #self.label.grid(row=0,column=0)

        self.header = self.input_box(self,self.root)
        #Text input box
        self.entrytext = StringVar()
        self.entry_box = Entry(self.root, textvariable=self.entrytext, fg="white")
        #self.entry_box.pack()

        #Go Button
        self.buttontext = StringVar()
        self.buttontext.set("Seed")
        self.seed_button = Button(self.root, textvariable=self.buttontext, command=self.clicked1)
        #self.seed_button.pack(side='top')

        #Download Button
        self.buttontext = StringVar()
        self.buttontext.set("Download")
        self.download_button = Button(self.root, textvariable=self.buttontext, command=lambda: self.download())
        #self.download_button.pack(side='top')

        self.label = Label(self.root, text="")
        #self.label.pack()

        #Init  Tile Window
        self.canvas = Canvas(self.root, height=200)  # a canvas in the parent object
        self.canvas.addtag_all('song_window')
        self.frame = Frame(self.canvas)  # a frame in the canvas


        #Init Scrollbar
        # a scrollbar in the parent
        scrollbar = Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        # connect the canvas to the scrollbar
        self.canvas.configure(yscrollcommand=scrollbar.set, yscrollincrement=5)
        scrollbar.pack(side="right", fill="y")  # comment out this line to hide the scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)  # pack the canvas
        # make the frame a window in the canvas
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw", tags="frame")
        # bind the frame to the scrollbar
        self.frame.bind("<Configure>", lambda x: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        def on_vertical(event):
            self.canvas.yview_scroll(-1 * event.delta, 'units')
        self.canvas.bind_all('<MouseWheel>', on_vertical)
        self.root.bind("<Down>", lambda x: self.canvas.yview_scroll(2, 'units'))  # bind "Down" to scroll down
        self.root.bind("<Up>", lambda x: self.canvas.yview_scroll(-2, 'units'))  # bind "Up" to scroll up

        # bind the mousewheel to scroll up/down
        # parent.bind("<MouseWheel>", lambda x: canvas.yview_scroll(int(1*(x.delta/40)), "units"))

        self.root.mainloop()

    def add_to_selected(self,song_title,index):
        if (song_title,index) not in self.selected:
            self.selected.append((song_title,index))
        print(self.selected)

    def clicked1(self,query):

        for label in self.root.grid_slaves():
            label.grid_forget()
        #input = self.input_box.entrytext.get()
        input = query.get()
        self.seeder.clear()
        titles,indexes = self.seeder.get_from_seed(input)
        self.sourced_song = self.seeder.sourced_song
        self.sourced_song_artist = self.seeder.sourced_song_artist
        self.sourced_song_image_url =self.seeder.sourced_song_image_url
        self.seeder.write_image(0,source=self.sourced_song_image_url,title_string=self.sourced_song)

        self.header.show_found_song(self,self.root,self.sourced_song,self.sourced_song_artist,0)
        self.root.update()
        self.indexes = indexes
        self.track_names = titles
        self.artist_names = self.seeder.found_artist_names
        #self.seeder.write_images()
        self.seeder.clear_images()
        os.chdir(self.cwd)

        image_count = 0
        self.Grid_Objects = []
        num_rows = int(len(self.track_names) / self.COLUMNS) + (len(self.track_names) % self.COLUMNS > 0)
        #print("num rows" )
        #print(num_rows)
        r_num = 0


        while r_num < num_rows:
            c_num = 0
            while c_num < self.COLUMNS and image_count < len(self.track_names):
                track_name = self.track_names[image_count]
                artist_name = self.artist_names[image_count]
                self.seeder.write_image(image_count)

                index = image_count
                print("creating widget obj " + str(track_name))
                new_song_obj = self.Song_spotify(self, self.frame, track_name, artist_name, index)
                r = r_num*3
                c = c_num
                new_song_obj.add_to_grid(r, c)
                self.Grid_Objects.append(new_song_obj)
                self.root.update()
                image_count += 1
                c_num += 1
            r_num += 1


    def download(self):
        print("Download clicked")
        print(self.selected)

        try:
            cwd = os.getcwd()
            print(cwd)
            os.chdir('songs')
        except:
            cwd = os.getcwd()
            print(cwd)
            print("PROBLEM WITH DIRECTORIES")
            #raise IOError

        for items in self.selected:
            song,index = items[0],items[1]
            print("Downloading")
            print(items,index)
            self.seeder.download_a_song(song,index)
            self.Grid_Objects[index].complete_download()
            self.root.update()
        os.chdir(cwd)
        if platform.system() == "Windows":
            subprocess.Popen('explorer "cwd  + "/songs/tmp"')
        if platform.system() == "Darwin":
            file_to_show = cwd  + "/songs/tmp"
            subprocess.call(["open", "-R", file_to_show])

    def button_click(self, e):
        self.seeder = Lisa_tape_funcs.Song_seeder()
        self.seeder.get_from_seed('kanye west all of the lights')
        self.seeder.write_images()





App()