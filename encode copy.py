#   encode.py 5-13-22
#   Note this will not run in the code editor and must be downloaded
# import the required modules
import tkinter as tk
import turtle as trtl
from PIL import ImageGrab, Image, ImageDraw
import mss
import platform
import tkinter as tk


#store the message to a variable 
message = "subscribe to Mr.V" # Change this to encode a different message. Length limit 20 characters.


def encodemsg():
  global message
  message = msg_entry.get()

  tkwin.quit() 
  tkwin.destroy()
  



tkwin = tk.Tk()
tkwin.wm_geometry("425x225")
tkwin.title("Enter your message")
frame = tk.Frame(tkwin,cursor="cross")
frame.pack()
url_label = tk.Label(frame, text="Enter the message to be encoded: ")
url_label.pack()
msg_entry= tk.Entry(frame,  font=("comic sans", 14)) # change font
msg_entry.pack()
msg_button = tk.Button(frame,text="Encode message",command=encodemsg)
msg_button.pack()

tk.mainloop() 

# Parse through the character and appened them to a list
characters_as_ints = []
for cha in message:
  characters_as_ints.append(ord(cha))
print(characters_as_ints)

characters_as_bits = []
for integ in characters_as_ints:
  characters_as_bits.append('{0:08b}'.format(integ))
print(characters_as_bits)

bits_as_ints = []
for index in range(0,len(characters_as_bits)):
  for bit in characters_as_bits[index]:
    bits_as_ints.append(bit)
print(bits_as_ints)

screen = trtl.getscreen()
painter = trtl.Turtle()
print(screen.window_width(), " x ", screen.window_height())
painter.penup()
painter.goto(-200,221)
painter.shape("square")
painter.goto(-221,221)
painter.color("red")
painter.stamp()
painter.forward(21)
painter.color("blue")

message_length = len(bits_as_ints)
index = 0
while index < message_length:
  if index % 8 == 0:
    painter.goto(-32, painter.ycor()-21)
  if bits_as_ints[index]=='1':
    painter.stamp()
  painter.forward(-21)
  index = index + 1

screen = painter.getscreen()
root = trtl.getcanvas().winfo_toplevel()

def create_image(widget):
  with mss.mss() as sct:
    sct.shot(mon=1,output='fullscreen.gif') #mon is the monitor number of the primary display. Change if capturing incorrect display.
    
    x=root.winfo_rootx()
    y=root.winfo_rooty()
    
    #Uncomment this section to get details about the upper left coordinate, height, and width of the window
    """
    width = widget.window_width()
    height = widget.window_height()
    print("width =", width, "height = ", height)
    print("x is: ", x , " y is: ", y)
    """
    x1=x+widget.window_width()
    y1=y+widget.window_height()

    im = Image.open("fullscreen.gif")
    bounds = x,y,x1,y1 
    #Retina displays require a coefficient of 2 for pixel numbers
    if platform.system() == 'Darwin': 
      bounds = 2*x,2*y,2*x1,2*y1
    print("Turtle bounding box: ", bounds)
    im = im.crop(box=bounds)
    im.save("output.gif")


create_image(screen)

#screen.mainloop()