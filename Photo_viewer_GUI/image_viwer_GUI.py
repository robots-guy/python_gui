#Building a Photo Viewer using python

#import tkinter modules
from tkinter import *
from PIL import ImageTk, Image

#Creating a window
window = Tk()
window.title("Image Viewer")

#Set a font style for using later
large_font = ('Verdana',16)

#confiure window background
window.configure(bg = "white")

#adding image inside tkinter
'''
Declare the images 
Cgange the file path accordingly as per your folder 
var =  ImageTk.PhotoImage(Image.open("<---your file path--->"))
'''
myim1 = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/p1.png"))
myim2 = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/p2.png"))
myim3 = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/p3.png"))
myim4 = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/p4.png"))
myim5 = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/p5.png"))
myim6 = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/p6.png"))
left = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/left.png"))
right = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/right.png"))

#adding list of images
imlist=[myim1, myim2, myim3, myim4, myim5, myim6]

#initialize variables
current = 0


#create labels to use
mylabel = Label(image= imlist[0])
mylabel.config(height=600, width=600, bg ="white")
mylabel.grid(row=0, column =0, columnspan=3)

#define buttons
def back():
    global mylabel
    global current
    buttonnext.config(state="active")
    i = current
    
    
    if(i== 1):
        mylabel.grid_forget()
        mylabel = Label(image= imlist[i-1], bg ="white")
        mylabel.config(height=600, width=600)
        mylabel.grid(row=1, column =0, columnspan=3)
        buttonback.config(state="disabled")
        current = current - 1
        statusbar()
        #print (current)
       
        
        
    else:
        mylabel.grid_forget()
        mylabel = Label(image= imlist[i-1], bg ="white")
        mylabel.config(height=600, width=600)
        mylabel.grid(row=1, column =0, columnspan=3)
        #statusbar()
        current = current - 1
        statusbar()
        #print (current)
        return 

def nextim():
    global mylabel
    global current
    buttonback.config(state="active")
    i = current
     
    
    if(i == 4):
        mylabel.grid_forget()
        mylabel = Label(image= imlist[i+1], bg ="white")
        mylabel.config(height=600, width=600)
        mylabel.grid(row=1, column =0, columnspan=3)
        #statusbar()
        buttonnext.config(state="disabled")
        current = current + 1
        statusbar()
        #print (current)
    else:  
        mylabel.grid_forget()
        mylabel = Label(image= imlist[i+1], bg ="white")
        mylabel.config(height=600, width=600)
        mylabel.grid(row=1, column =0, columnspan=3)
        #statusbar()
        current = current + 1
        statusbar()
        #print (current)
        return 
     

def statusbar():
    print (current)
    value = current + 1
    statuslabel = Label(text ="Image: " + str(value) + "/6", font=large_font, bd=1, relief=SUNKEN)
    statuslabel.grid(row=4, column =0, columnspan=3, sticky=W+E)
  
statusbar() #always run the status bar function

##quita tkinter window securely 
def ask_quit():
    window.destroy()

#create buttons 
buttonquit = Button(window, text = "Exit program", font=large_font, command= ask_quit)
buttonquit.grid(row =2, column =1, pady =20)

buttonback = Button(window, image = left, bg = "white", command= back )
buttonback.config(state="disabled", bg="white")
buttonback.grid(row =2, column =0, pady =20)

buttonnext = Button(window, image = right, bg ="white", command= nextim)
buttonnext.grid(row =2, column =2)

#run the window
window.mainloop()


