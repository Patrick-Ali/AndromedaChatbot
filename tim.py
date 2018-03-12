import tkinter as tk
from PIL import Image as img
import controller as an
import dataControl as res

class mkInterface:
    count = 0
    E1 = ''
    topText = ''
    test = an.AnalyseInput()
    
    
    def __init__(self, root):
        root.title("PlanetBot")
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
        #photo = tk.PhotoImage(file="pluto.png")
        #label = tk.Label(imgHolder, image=photo)
        #label.grid(row = 0, column = 0)
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
        self.topText.bind("<Configure>", lambda event, canvas=holderCan: self.onFrameConfigure(holderCan))
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
        
    def mkFrameGrid(self, place, ro, col, width, height):
        frame = tk.Frame(place)
        frame.grid(row=ro,column=col,sticky=tk.N+tk.E+tk.S+tk.W)
        frame.config(width=int((width/5)*0.75),height=int((height/5)*0.75))
        #frame.grid_propagate(False)
        return frame
        
    def mkScrollBar(self, place, obj):
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
        label = tk.Label( self.topText, text=message, relief=tk.FLAT, anchor = position,
                   bg = backGround, fg = fontColour, padx = 5, pady = 5, wraplength = 100)
        #, wraplength = 30 justify = tk.RIGHT
        label.grid(row = count, column = col)
        
    def addWeight(self, count):
            tk.Grid.rowconfigure(self.topText, count, weight=1)
            
    def getInput(self, event = None):
        current = self.E1.get()
        print(current)
        size = len(current)
        self.E1.delete(0,size)
        tk.Grid.rowconfigure(self.topText, self.count, weight=1)
        self.addWeight(self.count)
        self.makeLabel(current, "lightgrey", "black", "w", self.count, 1)
        self.count += 1
        holdAn = ''
        holdAn1 = self.test.readInput(current)
        print("First hold ", holdAn1)
        #self.addWeight(self.count)
        holdAn2 = res.specificInfoP1(current)
        print(type(holdAn2))
        print(holdAn2)
        if holdAn2 == [[],[]]:
            holdAn = holdAn1
        else:
            holdAn = holdAn2
        self.makeLabel(holdAn, "blue", "white", "e", self.count, 2)
        self.count += 1
        
    def onFrameConfigure(self, canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))
        

if __name__ == "__main__":
    #def func(event):
    #print("You hit return.")
    root = tk.Tk()
    #root.bind('<Return>', func)
    mkInterface(root)
    root.mainloop()
