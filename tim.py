import tkinter as tk
import threading
from PIL import Image as img
import controller as an
import dataControl as res
import cMath as calc

class mkInterface:
    '''Class used to generate the user interface'''
    count = 0
    E1 = ''
    topText = ''
    test = an.AnalyseInput()
   # current = ''
    
    
    def __init__(self, root):
        root.title("Andromeda")
        scale = 4
        #Config main window
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry(str(int(width/scale)) + 'x' + str(int(height/scale)*3))
        print(height)
        print(width)
        print(str(int(width/scale)) + 'x' + str(int(height/scale)))
        root.grid_columnconfigure(0, weight=1)
        self.configRow(tk.Grid, root, 0, 0)
        self.configRow(tk.Grid, root, 1, 1)
        self.configRow(tk.Grid, root, 2, 1)
        self.configCol(tk.Grid, root, 0, 1)

        ##Config image
        imgHolder = self.mkFrameGrid(root, 0, 0, width, height)
        imgPath = r"pluto.png"
        im_temp = img.open("pluto.jpg")
        im_temp = im_temp.resize((int((width/4)),int((width/4))), img.ANTIALIAS)
        im_temp.save("test.ppm", "ppm")
        photo = tk.PhotoImage(file = "test.ppm")
        label = tk.Label(imgHolder, image = photo, anchor = tk.E)
        label.image = photo # keep a reference!
        label.grid(row = 3, column = 1)#padx = 5, pady = 5
         
        ##Config upper body
        mainHolder = self.mkFrameGrid(root, 1, 0, width, height)
        holderCan = self.mkCanvasPack(mainHolder, width, height)
        scrollbar = self.mkScrollBar(mainHolder, holderCan)

        ##Config Canvas in upper body
        holderCan.config(yscrollcommand = scrollbar.set)
        holderCan.config(width=int((width/scale)*0.75),height=int((height/scale)*0.75))
        self.topText = tk.Frame(holderCan, bg='black', pady = 20)
        holderCan.create_window((4,4), window=self.topText, width = int((width/scale)))
        ##Adapted from https://stackoverflow.com/questions/28573432/tkinter-fill-scrollable-canvas-with-frame-content
        self.topText.bind("<Configure>", lambda event, canvas=holderCan: self.onFrameConfigure(holderCan))
        ##End adaptation
        self.configCol(tk.Grid, self.topText, 1, 1)
        self.configCol(tk.Grid, self.topText, 2, 1)

        ##Config text entry
        textEntry = tk.Frame(root)
        textEntry.grid(row=2,column=0,sticky=tk.N+tk.E+tk.S+tk.W)
        hold = tk.StringVar()
        submit = tk.Button(textEntry, text = "\u25B2", bg = 'grey', command = self.getInput)
        root.bind('<Return>', self.getInput)
        tk.Grid.rowconfigure(textEntry, 0, weight=1)
        tk.Grid.columnconfigure(textEntry, 0, weight=1)
        submit.grid(row = 0, column = 1, sticky = tk.W)
        self.E1 = tk.Entry(textEntry, bd = 5, bg = 'lightgrey',
           font = 'arial', relief = tk.FLAT,
           textvariable=hold)
        self.E1.grid(row = 0, sticky='we')

        ##Init message
        welcomeMsg = ("Hello, I am Andromeda,"
                      " I am currently in training but can tell you some"
                      " fun facts about your solar system."
                      " For more information type and enter 'help'"
                      " and I will tell you somethings I can do."
                      " size and distance are in kilometers")
        self.makeLabel(welcomeMsg, "blue", "white", "e", self.count, 2)
        self.count += 1
        
    def mkFrameGrid(self, place, ro, col, width, height):
        '''Set up the grid place for tk widgets'''
        frame = tk.Frame(place)
        frame.grid(row=ro,column=col,sticky=tk.N+tk.E+tk.S+tk.W)
        frame.config(width=int((width/5)*0.75),height=int((height/5)*0.75))
        return frame
        
    def mkScrollBar(self, place, obj):
        '''Set up the scroll bar for the canvas'''
        scrollbar = tk.Scrollbar(place, orient= tk.VERTICAL)
        scrollbar.config(command=obj.yview)
        scrollbar.pack( side = tk.RIGHT, fill = tk.Y )
        return scrollbar

    def mkCanvasPack(self, place, width, height):
        holderCan = tk.Canvas(place, scrollregion=(0,0,200,5))
        #holderCan.pack_propagate(False)
        holderCan.pack(side = tk.LEFT,expand=True,fill=tk.BOTH)
        return holderCan
    
    def configRow(self, obj, place, count, wght):
        obj.rowconfigure(place, count, weight= wght)
        
    def configCol(self, obj, place, count, wght):
        obj.columnconfigure(place, count, weight= wght)
        
    def makeLabel(self, message, backGround, fontColour, position, count, col):
        '''Configure labels'''
        label = tk.Label( self.topText, text=message, relief=tk.FLAT, anchor = position,
                   bg = backGround, fg = fontColour, padx = 5, pady = 5, wraplength = 100)
        #, wraplength = 30 justify = tk.RIGHT
        label.grid(row = count, column = col)
        
    def addWeight(self, count):
            tk.Grid.rowconfigure(self.topText, count, weight=1)
    
##    def run_before(lastfunc, *args1, **kwargs1):
##        def run(func):
##            def wrapped_func(self, *args, **kwargs):
##                try:
##                    result = func(self, *args, **kwargs)
##                except:
##                    result = None
##                finally:
##                    lastfunc(self, *args1, **kwargs1)
##                    return result
##            return wrapped_func
##        return run

    
    def getOutput(self, current): #, current
        '''Call the functions needed to determine what the user wants and generate output'''
        holdAn = calc.translate(current)
        print(holdAn)
        if holdAn == "Can't work with that input":
            holdAn2 = res.trueStatement(current)#specificInfoP1(current)
            print(type(holdAn2))
            print("Hold Answer 2 = ", holdAn2)
            if holdAn2 == [[],[]] or holdAn2 == []:
                holdAn1 = self.test.readInput(current)
                print("holdAn1 = ", holdAn1)
                tempAn2 = ' '.join(holdAn1[0])
                print(tempAn2)
                holdAn4 = res.trueStatement(tempAn2)
                print("Fianl Answer is ", holdAn4)
                holdAn = holdAn1
            else:
                holdAn = holdAn2
        self.makeLabel(holdAn, "blue", "white", "e", self.count, 2)
        self.count += 1
        
    def firstStep(self, current):
        '''Output thinking message'''
        size = len(current)
        self.E1.delete(0,size)
        tk.Grid.rowconfigure(self.topText, self.count, weight=1)
        self.addWeight(self.count)
        self.makeLabel(current, "lightgrey", "black", "w", self.count, 1)
        self.count += 1
        holdAn = ''
        thinkMsg = "Let me think about that"
        self.makeLabel(thinkMsg, "blue", "white", "e", self.count, 2)
               
    def getInput(self, event = None):
        '''Get the users input, start output messages, and pass user input into getOutput function to determine output'''
        current = self.E1.get()
        print(current)
        self.firstStep(current)
        self.count += 1
        self.getOutput(current)


    #Function from https://stackoverflow.com/questions/28573432/tkinter-fill-scrollable-canvas-with-frame-content   
    def onFrameConfigure(self, canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))
        

if __name__ == "__main__":
    root = tk.Tk()
    mkInterface(root)
    root.mainloop()
