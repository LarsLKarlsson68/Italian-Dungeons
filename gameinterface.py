# -*- coding: latin_1 -*-
import tkinter
import _thread
import tkinter.filedialog
#import Image
#import ImageTk


class GameInterface(tkinter.Frame):
    def __init__(self,xsize=10,ysize=10,tilesize=10):
        print("Entering GameInterface.init")
        tkinter.Frame.__init__(self,None)
        self.canvas = tkinter.Canvas(self,width=xsize*tilesize,height=xsize*tilesize,bg='black')
        self.canvas.pack(expand=1,anchor=tkinter.CENTER,side=tkinter.LEFT)
        self.text = tkinter.Text(self,width=60,height=24,font="Times 14",wrap=tkinter.WORD)
        self.text.pack()
        self.input = tkinter.Entry(self,width=53,font="Times 14 bold")
        self.input.pack()
        self.input.bind('<Return>', self._has_input)
        self.pack()
        self.xsize=xsize
        self.ysize=ysize
        self.tilesize=tilesize
        self.xoffset = 0
        self.yoffset = 0        
        self.input_lock = _thread.allocate_lock()
        self.mutex = _thread.allocate_lock()
        self.input_lock.acquire()
        self.update_queue = []
        self.updates_ready_flag = False
        self.text_entered = ''
        self.update_map_and_text()
        self.text.tag_config("<bf>",font="Times 14 bold")
        self.text.tag_config("<it>",font="Times 14 italic")
        self.text.tag_config("<rm>",font="Times 14")
        self.tag_list = ["<bf>","<it>","<rm>"]
        self.image_repository = dict()
        print("Exiting GameInterface.init")
        self.tkraise()
        
    def add_update(self,update):
        self.mutex.acquire()
        self.update_queue += [update]
        self.mutex.release()

    def updates_ready(self):
        self.mutex.acquire()
        self.updates_ready_flag = True
        self.mutex.release()
    
    def update_map_and_text(self):
        self.mutex.acquire()
        if self.updates_ready_flag:
            for u in self.update_queue:
                if u[0] == 'clear':
                    self.clear_map_foreground()
                elif u[0] == 'center':
                    self.center_map(u[1],u[2])
                elif u[0] in ('foreground','background'):
                    self.add_to_map(u[1],u[2],u[3],u[0])
                elif u[0] == 'text':
                    self.text.insert(tkinter.END,u[1],u[2])
                    self.text.see(tkinter.END)                
                elif u[0] == 'textimage':
                    image = self.get_image(u[1])
                    self.text.image_create(tkinter.END,image=image)
                    self.text.see(tkinter.END)
                elif u[0] == 'newmap':
                    self.new_map(u[1])
                elif u[0] == 'quit':
                    print('Bye!')
                    self.destroy()
                elif u[0] == 'savefile':
                    self.text_entered = tkinter.filedialog.asksaveasfilename(parent=self,initialdir="./saved",title='Please provide a file to save in')
                    self.input_lock.release()
                elif u[0] == 'loadfile':
                    self.text_entered = tkinter.filedialog.askopenfilename(parent=self,initialdir="./saved",title='Please select a file to load')
                    self.input_lock.release()
            self.update_queue = []
            self.updates_ready_flag = False
        self.mutex.release()
        self.after(100,self.update_map_and_text)
        
    def add_to_map(self,image,xpos,ypos,tag):
        xpos = xpos-self.xoffset
        ypos = ypos-self.yoffset
        if '.' in image: #isinstance(image,tkinter.PhotoImage):
            image = self.get_image(image)
            self.canvas.create_image(int(xpos*self.tilesize),int(ypos*self.tilesize),
                                     image=image, anchor=tkinter.NW,
                                     tag=tag)
        else: # Color code given
            self.canvas.create_rectangle(xpos*self.tilesize,ypos*self.tilesize,
                                         ((xpos+1)*self.tilesize-1),((ypos+1)*self.tilesize-1),
                                         fill=image,outline=image,tag=tag)

    def get_image(self,image_name):
        try:
            image = self.image_repository[image_name]
        except KeyError:
            image_filename,x,y=split_filename(image_name)
            try:
                image = self.image_repository[image_filename]
            except KeyError:
                image = tkinter.PhotoImage(file=image_filename)
                self.image_repository[image_filename] = image
            if x or y:
                image = subimage(image,x*self.tilesize,y*self.tilesize,(x+1)*self.tilesize,(y+1)*self.tilesize)
            self.image_repository[image_name] = image
        return image


    def center_map(self,xpos,ypos):
        xoffset = xpos-(self.xsize/2)
        yoffset = ypos-(self.ysize/2)
        self.canvas.move('background',self.tilesize*(self.xoffset-xoffset),self.tilesize*(self.yoffset-yoffset))
        self.canvas.move('foreground',self.tilesize*(self.xoffset-xoffset),self.tilesize*(self.yoffset-yoffset))
        self.xoffset =xoffset  
        self.yoffset =yoffset  
        
    def clear_map_foreground(self):
        self.canvas.delete('foreground')


    def new_map(self,image_array):
        self.canvas.delete('foreground')
        self.canvas.delete('background')
        self.xoffset = 0
        self.yoffset = 0
        for y in range(len(image_array)):
            for x in range(len(image_array[y])):
                if image_array[y][x]:
                    self.add_to_map(image_array[y][x],x,y,'background')
                
    def _has_input(self,event):
        if(self.input_lock.locked()):
            self.text_entered = self.input.get() #.encode('latin-1')
            if self.text_entered:
                self.input.delete('0',tkinter.END)
            self.input_lock.release()

    def get_input(self):
        self.input_lock.acquire()
        return self.text_entered
    
    def prn(self,*strings):
        self.mutex.acquire()
        l = len(strings)
        string = ''
        tags = tuple()
        for i in range(l):
            if strings[i] in self.tag_list:
                tags += (strings[i],)
            else:    
                string += string_when_needed(strings[i])
                if i+1 == l:
                   string += '\n'
                else:
                   string += ' '                
        self.update_queue += [('text',string,tags)]
        self.updates_ready_flag = True
        self.mutex.release()
        
    def pr(self,*strings):
        self.mutex.acquire()
        l = len(strings)
        string = ''
        tags = tuple()
        for i in range(l):
            if strings[i] in self.tag_list:
                tags += (strings[i],)
            else:    
                string += string_when_needed(strings[i])+' '
        self.update_queue += [('text',string,tags)]
        self.updates_ready_flag = True
        self.mutex.release()
        
    def prim(self,image):
        self.mutex.acquire()
        self.update_queue += [('textimage',image)]
        self.updates_ready_flag = True
        self.mutex.release()

    def guiquit(self):
        print('Bye!')
        self.quit()

    def ask_for_load_file(self):
        self.mutex.acquire()
        self.update_queue += [('loadfile',)]
        self.updates_ready_flag = True
        self.mutex.release()
        self.input_lock.acquire()
        return self.text_entered

    def ask_for_save_file(self):
        self.mutex.acquire()
        self.update_queue += [('savefile',)]
        self.updates_ready_flag = True
        self.mutex.release()
        self.input_lock.acquire()
        return self.text_entered
        
def string_when_needed(obj):
    if isinstance(obj,str):  #unicode
        return obj
    else:
        return str(obj)

# Takes a file name "<name>'['<int1>']''['<int2>']'
# and return <name>,<int1>,<int2>
def split_filename(fn):
    if not '[' in fn:
        return fn, 0, 0
    else:
        return fn[:fn.find('[')], int(fn[fn.find('[')+1:fn.find(',')]), int(fn[fn.find(',')+1:-1])

# To get a recangular subimage of an existing image        
def subimage(src, l, t, r, b):
    dst = tkinter.PhotoImage()
    dst.tk.call(dst, 'copy', src, '-from', l, t, r, b, '-to', 0, 0)
    return dst
    
