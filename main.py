from tkinter import *
from PIL import ImageTk

window = Tk()
window.iconbitmap('images/logos/ezgif.com-gif-maker (12).ico')
window.config(bg='black')
window.geometry("730x490")
window.title("4-BAND RESISTOR COLOR CALCULATOR")


# Resistor body and logos
photo1 = ImageTk.PhotoImage(file='images/bodyOfResistor/resistornatalaga.png')
photo2 = ImageTk.PhotoImage(file='images/logos/logopython.png')
photo3 = ImageTk.PhotoImage(file='images/logos/nailawnaresistor.png')


color = {
    'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4',
    'green': '5', 'blue': '6', 'violet': '7', 'grey': '8', 'white': '9'
}


multiplier = {
    'black': 'x10^0', 'brown': 'x10^1', 'red': 'x10^2', 'orange': 'x10^3', 'yellow': 'x10^4', 'green': 'x10^5',
    'blue': 'x10^6', 'violet': 'x10^7', 'grey': 'x10^8', 'white': 'x10^9', 'gold': 'x10^-1', 'silver': 'x10^-2'
}

tolerance = {
    'brown': '±1.00%', 'red': '±2.00%', 'orange': '±3.00%', 'yellow': '±4.00%', 'green': '±0.50%',
    'blue': '±0.25%', 'violet': '±0.10%', 'grey': '±0.05%', 'gold': '±5.00%', 'silver': '±10.00%'
}


# Creating Buttons from images

x1 = PhotoImage(file="images/buttons/itim.png")
x10 = PhotoImage(file="images/buttons/kayumanggi.png")
x100 = PhotoImage(file="images/buttons/pula.png")
x1k = PhotoImage(file="images/buttons/orange.png")
x10k = PhotoImage(file="images/buttons/yellow.png")
x100k = PhotoImage(file="images/buttons/green.png")
x1M = PhotoImage(file="images/buttons/blue.png")
x10M = PhotoImage(file="images/buttons/violet.png")
x100M = PhotoImage(file="images/buttons/grey.png")
x1G = PhotoImage(file="images/buttons/white.png")
x100m = PhotoImage(file="images/buttons/gold.png")
x10m = PhotoImage(file="images/buttons/silver.png")


# Creating Label
lblresistor = Label(window, image=photo1)
lbllogo = Label(window, image=photo2)
lblresistorlogo = Label(window, image=photo3)
lbl1 = Label(window, bg="black", width=2, height=6)
lbl2 = Label(window, bg="black", width=2, height=6)
lbl3 = Label(window, bg="black", width=2, height=6)
lbl4 = Label(window, bg="black", width=2, height=6)
lblOutput = Label(window, bg="grey", width=60, height=6)
lblValue = Label(window, text="Value: ", bg="grey", fg="black", width=8, height=1, font=('Verdana', 10))
lblFirst_DigOut = Label(window, text='0', bg="white", width=3, height=2, font=('Verdana', 10))
lblSecond_DigOut = Label(window, text='0', bg="white", width=3, height=2, font=('Verdana', 10))
lblMultiplier = Label(window, text='x10^0', bg="white", width=6, height=2, font=('Verdana', 10))
lblOhm = Label(window, text="Ω", bg="white", width=3, height=2, font=('Verdana', 10))
lblTolerance = Label(window, text="Tolerance: ", bg="grey", fg="black", width=8, height=1, font=('Verdana', 8))
lblToleOut = Label(window, text='±0%', bg="white", width=15, height=2, font=('Verdana', 10))
lbltolerance = Label(window, text="TOLERANCE", fg='white', bg="black", width=9, height=1, font=('Verdana', 10))
lblProject = Label(window, text="Resistor Color Calculator", bg="black", fg="white", width='20',
                   height='1', font=('Verdana', 23, 'bold', 'italic'))
lbldeveloper = Label(window, text="By: Michael Rhey Palaganas", bg="black", fg="white", width='22',
                     height='1', font=('Times', 14, 'bold', 'italic'))
lbloptions = Label(window, text="Also Try: ", bg="black", fg="white", width='22',
                     height='1', font=('Times', 14, 'bold', 'italic'))
lblblack = Label(window, text="x1", bg="black", fg="white")
lblbrown = Label(window, text="x10", bg="black", fg="white")
lblred = Label(window, text="x100", bg="black", fg="white")
lblorange = Label(window, text="x1k", bg="black", fg="white")
lblyellow = Label(window, text="x10k", bg="black", fg="white")
lblgreen = Label(window, text="x100k", bg="black", fg="white")
lblblue = Label(window, text="x1M", bg="black", fg="white")
lblviolet = Label(window, text="x10M", bg="black", fg="white")
lblgrey = Label(window, text="100M", bg="black", fg="white")
lblwhite = Label(window, text="1G", bg="black", fg="white")
lblgold = Label(window, text="x0.1", bg="black", fg="white")
lblsilver = Label(window, text="x0.01", bg="black", fg="white")

# Creating Buttons
# Buttons for 1st Digit/Band
btn1 = Button(window, text="0", bg="black", fg="white", command=lambda n="black": changecolor_value1(n))
btn2 = Button(window, text="1", bg="brown", fg="black", command=lambda n="brown": changecolor_value1(n))
btn3 = Button(window, text="2", bg="red", fg="black", command=lambda n="red": changecolor_value1(n))
btn4 = Button(window, text="3", bg="orange", fg="black", command=lambda n="orange": changecolor_value1(n))
btn5 = Button(window, text="4", bg="yellow", fg="black", command=lambda n="yellow": changecolor_value1(n))
btn6 = Button(window, text="5", bg="green", fg="black", command=lambda n="green": changecolor_value1(n))
btn7 = Button(window, text="6", bg="blue", fg="black", command=lambda n="blue": changecolor_value1(n))
btn8 = Button(window, text="7", bg="violet", fg="black", command=lambda n="violet": changecolor_value1(n))
btn9 = Button(window, text="8", bg="grey", fg="black", command=lambda n="grey": changecolor_value1(n))
btn10 = Button(window, text="9", bg="white", fg="black", command=lambda n="white": changecolor_value1(n))

# Buttons for 2nd Digit/Band
btn11 = Button(window, text="0", bg="black", fg="white", command=lambda m="black": changecolor_value2(m))
btn12 = Button(window, text="1", bg="brown", fg="black", command=lambda m="brown": changecolor_value2(m))
btn13 = Button(window, text="2", bg="red", fg="black", command=lambda m="red": changecolor_value2(m))
btn14 = Button(window, text="3", bg="orange", fg="black", command=lambda m="orange": changecolor_value2(m))
btn15 = Button(window, text="4", bg="yellow", fg="black", command=lambda m="yellow": changecolor_value2(m))
btn16 = Button(window, text="5", bg="green", fg="black", command=lambda m="green": changecolor_value2(m))
btn17 = Button(window, text="6", bg="blue", fg="black", command=lambda m="blue": changecolor_value2(m))
btn18 = Button(window, text="7", bg="violet", fg="black", command=lambda m="violet": changecolor_value2(m))
btn19 = Button(window, text="8", bg="grey", fg="black", command=lambda m="grey": changecolor_value2(m))
btn20 = Button(window, text="9", bg="white", fg="black", command=lambda m="white": changecolor_value2(m))

btn21 = Button(window, bg="black", image=x1, bd=0, command=lambda o="black": changecolor_value3(o))
btn22 = Button(window, bg="black", image=x10, bd=0, command=lambda o="brown": changecolor_value3(o))
btn23 = Button(window, bg="black", image=x100, bd=0, command=lambda o="red": changecolor_value3(o))
btn24 = Button(window, bg="black", image=x1k, bd=0, command=lambda o="orange": changecolor_value3(o))
btn25 = Button(window, bg="black", image=x10k, bd=0, command=lambda o="yellow": changecolor_value3(o))
btn26 = Button(window, bg="black", image=x100k, bd=0, command=lambda o="green": changecolor_value3(o))
btn27 = Button(window, bg="black", image=x1M, bd=0, command=lambda o="blue": changecolor_value3(o))
btn28 = Button(window, bg="black", image=x10M, bd=0, command=lambda o="violet": changecolor_value3(o))
btn29 = Button(window, bg="black", image=x100M, bd=0, command=lambda o="grey": changecolor_value3(o))
btn30 = Button(window, bg="black", image=x1G, bd=0, command=lambda o="white": changecolor_value3(o))
btn31 = Button(window, bg="black", image=x100m, bd=0, command=lambda o="gold": changecolor_value3(o))
btn32 = Button(window, bg="black", image=x10m, bd=0, command=lambda o="silver": changecolor_value3(o))


btn41 = Button(window, text="±1.00%", bg="brown", fg="black", command=lambda p="brown": changecolor_value4(p))
btn42 = Button(window, text="±2.00%", bg="red", fg="black", command=lambda p="red": changecolor_value4(p))
btn43 = Button(window, text="±3.00%", bg="orange", fg="black", command=lambda p="orange": changecolor_value4(p))
btn44 = Button(window, text="±4.00%", bg="yellow", fg="black", command=lambda p="yellow": changecolor_value4(p))
btn45 = Button(window, text="±0.50%", bg="green", fg="black", command=lambda p="green": changecolor_value4(p))
btn46 = Button(window, text="±0.25%", bg="blue", fg="black", command=lambda p="blue": changecolor_value4(p))
btn47 = Button(window, text="±0.10%", bg="violet", fg="black", command=lambda p="violet": changecolor_value4(p))
btn48 = Button(window, text="±0.05%", bg="grey", fg="black", command=lambda p="grey": changecolor_value4(p))
btn49 = Button(window, text="±5.00%", bg="gold", fg="black", command=lambda p="gold": changecolor_value4(p))
btn50 = Button(window, text="±10.00%", bg="silver", fg="black", command=lambda p="silver": changecolor_value4(p))


# Aligning Buttons and Labels
lblresistor.place(x=100, y=150)
lbllogo.place(x=30, y=20)
lblresistorlogo.place(x=600, y=20)
lblProject.place(x=150, y=15)
lbldeveloper.place(x=230, y=60)
lbloptions.place(x=180, y=95)
lblOutput.place(x=125, y=290)
lblValue.place(x=215, y=310)
lblFirst_DigOut.place(x=280, y=300)
lblSecond_DigOut.place(x=305, y=300)
lblMultiplier.place(x=330, y=300)
lblOhm.place(x=380, y=300)
lblTolerance.place(x=217, y=350)
lblToleOut.place(x=280, y=340)
lbltolerance.place(x=300, y=440)

lbl1.place(x=236, y=170)
btn1.place(x=30, y=150)
btn2.place(x=30, y=175)
btn3.place(x=30, y=200)
btn4.place(x=30, y=225)
btn5.place(x=30, y=250)
btn6.place(x=30, y=275)
btn7.place(x=30, y=300)
btn8.place(x=30, y=325)
btn9.place(x=30, y=350)
btn10.place(x=30, y=375)

lbl2.place(x=276, y=170)
btn11.place(x=70, y=150)
btn12.place(x=70, y=175)
btn13.place(x=70, y=200)
btn14.place(x=70, y=225)
btn15.place(x=70, y=250)
btn16.place(x=70, y=275)
btn17.place(x=70, y=300)
btn18.place(x=70, y=325)
btn19.place(x=70, y=350)
btn20.place(x=70, y=375)

lbl3.place(x=400, y=170)
btn21.place(x=596, y=144)
btn22.place(x=600, y=175)
btn23.place(x=600, y=200)
btn24.place(x=600, y=225)
btn25.place(x=600, y=250)
btn26.place(x=600, y=275)
btn27.place(x=600, y=300)
btn28.place(x=600, y=325)
btn29.place(x=600, y=350)
btn30.place(x=600, y=375)
btn31.place(x=600, y=400)
btn32.place(x=600, y=425)


lblblack.place(x=645, y=146)
lblbrown.place(x=645, y=175)
lblred.place(x=645, y=200)
lblorange.place(x=645, y=225)
lblyellow.place(x=645, y=250)
lblgreen.place(x=645, y=275)
lblblue.place(x=645, y=300)
lblviolet.place(x=645, y=325)
lblgrey.place(x=645, y=350)
lblwhite.place(x=645, y=375)
lblgold.place(x=645, y=400)
lblsilver.place(x=645, y=425)


lbl4.place(x=316, y=170)
btn41.place(x=115, y=400)
btn42.place(x=160, y=400)
btn43.place(x=205, y=400)
btn44.place(x=250, y=400)
btn45.place(x=295, y=400)
btn46.place(x=340, y=400)
btn47.place(x=385, y=400)
btn48.place(x=430, y=400)
btn49.place(x=475, y=400)
btn50.place(x=520, y=400)

# Label para sa output


def changecolor_value1(n):
    lbl1.config(bg=n)
    lblFirst_DigOut.config(text=color[n], font=('Verdana', 10))
    # return first_digit


def changecolor_value2(m):
    lbl2.config(bg=m)
    lblSecond_DigOut.config(text=color[m], font=('Verdana', 10))
    # return second_digit


def changecolor_value3(o):
    lbl4.config(bg=o)
    lblMultiplier.config(text=multiplier[o], font=('Verdana', 10))
    # return multiplier


def changecolor_value4(p):
    lbl3.config(bg=p)
    lblToleOut.config(text=tolerance[p])


def five_band():
    tab1 = Toplevel()
    tab1.iconbitmap('images/logos/ezgif.com-gif-maker (12).ico')
    tab1.config(bg='black')
    tab1.geometry("800x490")
    tab1.title("5-BAND RESISTOR COLOR CALCULATOR")

    # Resistor body and logos
    photoResistor = ImageTk.PhotoImage(file='images/bodyOfResistor/resistornatalaga.png')
    photoPython = ImageTk.PhotoImage(file='images/logos/logopython.png')
    photoDesign = ImageTk.PhotoImage(file='images/logos/nailawnaresistor.png')

    color_5 = {
        'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4',
        'green': '5', 'blue': '6', 'violet': '7', 'grey': '8', 'white': '9'
    }

    multiplier_5 = {
        'black': 'x10^0', 'brown': 'x10^1', 'red': 'x10^2', 'orange': 'x10^3', 'yellow': 'x10^4', 'green': 'x10^5',
        'blue': 'x10^6', 'violet': 'x10^7', 'grey': 'x10^8', 'white': 'x10^9', 'gold': 'x10^-1', 'silver': 'x10^-2'
    }

    tolerance_5 = {
        'brown': '±1.00%', 'red': '±2.00%', 'orange': '±3.00%', 'yellow': '±4.00%', 'green': '±0.50%',
        'blue': '±0.25%', 'violet': '±0.10%', 'grey': '±0.05%', 'gold': '±5.00%', 'silver': '±10.00%'
    }

    # Creating Buttons from images

    x15 = PhotoImage(file="images/buttons/itim.png")
    x105 = PhotoImage(file="images/buttons/kayumanggi.png")
    x1005 = PhotoImage(file="images/buttons/pula.png")
    x1k5 = PhotoImage(file="images/buttons/orange.png")
    x10k5 = PhotoImage(file="images/buttons/yellow.png")
    x100k5 = PhotoImage(file="images/buttons/green.png")
    x1M5 = PhotoImage(file="images/buttons/blue.png")
    x10M5 = PhotoImage(file="images/buttons/violet.png")
    x100M5 = PhotoImage(file="images/buttons/grey.png")
    x1G5 = PhotoImage(file="images/buttons/white.png")
    x100m5 = PhotoImage(file="images/buttons/gold.png")
    x10m5 = PhotoImage(file="images/buttons/silver.png")

    # Creating Label
    lblresistor_5 = Label(tab1, image=photoResistor)
    lbllogo_5 = Label(tab1, image=photoPython)
    lblresistorlogo_5 = Label(tab1, image=photoDesign)
    lbl1_5 = Label(tab1, bg="black", width=2, height=6)
    lbl2_5 = Label(tab1, bg="black", width=2, height=6)
    lbl3_5 = Label(tab1, bg="black", width=2, height=6)
    lbl4_5 = Label(tab1, bg="black", width=2, height=6)
    lbl5_5 = Label(tab1, bg="black", width=2, height=6)
    lblOutput_5 = Label(tab1, bg="grey", width=60, height=6)
    lblValue_5 = Label(tab1, text="Value: ", bg="grey", fg="black", width=8, height=1, font=('Verdana', 10))
    lblFirst_DigOut_5 = Label(tab1, text='0', bg="white", width=3, height=2, font=('Verdana', 10))
    lblSecond_DigOut_5 = Label(tab1, text='0', bg="white", width=3, height=2, font=('Verdana', 10))
    lblThird_DigOut_5 = Label(tab1, text='0', bg="white", width=3, height=2, font=('Verdana', 10))
    lblMultiplier_5 = Label(tab1, text='x10^0', bg="white", width=6, height=2, font=('Verdana', 10))
    lblOhm_5 = Label(tab1, text="Ω", bg="white", width=3, height=2, font=('Verdana', 10))
    lblTolerance_5 = Label(tab1, text="Tolerance: ", bg="grey", fg="black", width=8, height=1, font=('Verdana', 8))
    lblToleOut_5 = Label(tab1, text='±0%', bg="white", width=15, height=2, font=('Verdana', 10))
    lbltolerance_5 = Label(tab1, text="TOLERANCE", fg='white', bg="black", width=9, height=1, font=('Verdana', 10))
    lblProject_5 = Label(tab1, text="Resistor Color Calculator", bg="black",
                        fg="white", width='20', height='1', font=('Verdana', 23, 'bold', 'italic'))
    lbldeveloper_5 = Label(tab1, text="By: Michael Rhey Palaganas", bg="black",
                        fg="white", width='22', height='1', font=('Times', 14, 'bold', 'italic'))
    lblblack_5 = Label(tab1, text="x1", bg="black", fg="white")
    lblbrown_5 = Label(tab1, text="x10", bg="black", fg="white")
    lblred_5 = Label(tab1, text="x100", bg="black", fg="white")
    lblorange_5 = Label(tab1, text="x1k", bg="black", fg="white")
    lblyellow_5 = Label(tab1, text="x10k", bg="black", fg="white")
    lblgreen_5 = Label(tab1, text="x100k", bg="black", fg="white")
    lblblue_5 = Label(tab1, text="x1M", bg="black", fg="white")
    lblviolet_5 = Label(tab1, text="x10M", bg="black", fg="white")
    lblgrey_5 = Label(tab1, text="100M", bg="black", fg="white")
    lblwhite_5 = Label(tab1, text="1G", bg="black", fg="white")
    lblgold_5 = Label(tab1, text="x0.1", bg="black", fg="white")
    lblsilver_5 = Label(tab1, text="x0.01", bg="black", fg="white")

    # Creating Buttons
    # Buttons for 1st Digit/Band
    btn1_5 = Button(tab1, text="0", bg="black", fg="white", command=lambda n="black": changecolor_value1_5(n))
    btn2_5 = Button(tab1, text="1", bg="brown", fg="black", command=lambda n="brown": changecolor_value1_5(n))
    btn3_5 = Button(tab1, text="2", bg="red", fg="black", command=lambda n="red": changecolor_value1_5(n))
    btn4_5 = Button(tab1, text="3", bg="orange", fg="black", command=lambda n="orange": changecolor_value1_5(n))
    btn5_5 = Button(tab1, text="4", bg="yellow", fg="black", command=lambda n="yellow": changecolor_value1_5(n))
    btn6_5 = Button(tab1, text="5", bg="green", fg="black", command=lambda n="green": changecolor_value1_5(n))
    btn7_5 = Button(tab1, text="6", bg="blue", fg="black", command=lambda n="blue": changecolor_value1_5(n))
    btn8_5 = Button(tab1, text="7", bg="violet", fg="black", command=lambda n="violet": changecolor_value1_5(n))
    btn9_5 = Button(tab1, text="8", bg="grey", fg="black", command=lambda n="grey": changecolor_value1_5(n))
    btn10_5 = Button(tab1, text="9", bg="white", fg="black", command=lambda n="white": changecolor_value1_5(n))

    # Buttons for 2nd Digit/Band
    btn11_5 = Button(tab1, text="0", bg="black", fg="white", command=lambda m="black": changecolor_value2_5(m))
    btn12_5 = Button(tab1, text="1", bg="brown", fg="black", command=lambda m="brown": changecolor_value2_5(m))
    btn13_5 = Button(tab1, text="2", bg="red", fg="black", command=lambda m="red": changecolor_value2_5(m))
    btn14_5 = Button(tab1, text="3", bg="orange", fg="black", command=lambda m="orange": changecolor_value2_5(m))
    btn15_5 = Button(tab1, text="4", bg="yellow", fg="black", command=lambda m="yellow": changecolor_value2_5(m))
    btn16_5 = Button(tab1, text="5", bg="green", fg="black", command=lambda m="green": changecolor_value2_5(m))
    btn17_5 = Button(tab1, text="6", bg="blue", fg="black", command=lambda m="blue": changecolor_value2_5(m))
    btn18_5 = Button(tab1, text="7", bg="violet", fg="black", command=lambda m="violet": changecolor_value2_5(m))
    btn19_5 = Button(tab1, text="8", bg="grey", fg="black", command=lambda m="grey": changecolor_value2_5(m))
    btn20_5 = Button(tab1, text="9", bg="white", fg="black", command=lambda m="white": changecolor_value2_5(m))

    # Buttons for 3rd Digit/Band
    btn51_5 = Button(tab1, text="0", bg="black", fg="white", command=lambda q="black": changecolor_value5_5(q))
    btn52_5 = Button(tab1, text="1", bg="brown", fg="black", command=lambda q="brown": changecolor_value5_5(q))
    btn53_5 = Button(tab1, text="2", bg="red", fg="black", command=lambda q="red": changecolor_value5_5(q))
    btn54_5 = Button(tab1, text="3", bg="orange", fg="black", command=lambda q="orange": changecolor_value5_5(q))
    btn55_5 = Button(tab1, text="4", bg="yellow", fg="black", command=lambda q="yellow": changecolor_value5_5(q))
    btn56_5 = Button(tab1, text="5", bg="green", fg="black", command=lambda q="green": changecolor_value5_5(q))
    btn57_5 = Button(tab1, text="6", bg="blue", fg="black", command=lambda q="blue": changecolor_value5_5(q))
    btn58_5 = Button(tab1, text="7", bg="violet", fg="black", command=lambda q="violet": changecolor_value5_5(q))
    btn59_5 = Button(tab1, text="8", bg="grey", fg="black", command=lambda q="grey": changecolor_value5_5(q))
    btn60_5 = Button(tab1, text="9", bg="white", fg="black", command=lambda q="white": changecolor_value5_5(q))

    btn21_5 = Button(tab1, bg="black", image=x15, bd=0, command=lambda o="black": changecolor_value3_5(o))
    btn22_5 = Button(tab1, bg="black", image=x105, bd=0, command=lambda o="brown": changecolor_value3_5(o))
    btn23_5 = Button(tab1, bg="black", image=x1005, bd=0, command=lambda o="red": changecolor_value3_5(o))
    btn24_5 = Button(tab1, bg="black", image=x1k5, bd=0, command=lambda o="orange": changecolor_value3_5(o))
    btn25_5 = Button(tab1, bg="black", image=x10k5, bd=0, command=lambda o="yellow": changecolor_value3_5(o))
    btn26_5 = Button(tab1, bg="black", image=x100k5, bd=0, command=lambda o="green": changecolor_value3_5(o))
    btn27_5 = Button(tab1, bg="black", image=x1M5, bd=0, command=lambda o="blue": changecolor_value3_5(o))
    btn28_5 = Button(tab1, bg="black", image=x10M5, bd=0, command=lambda o="violet": changecolor_value3_5(o))
    btn29_5 = Button(tab1, bg="black", image=x100M5, bd=0, command=lambda o="grey": changecolor_value3_5(o))
    btn30_5 = Button(tab1, bg="black", image=x1G5, bd=0, command=lambda o="white": changecolor_value3_5(o))
    btn31_5 = Button(tab1, bg="black", image=x100m5, bd=0, command=lambda o="gold": changecolor_value3_5(o))
    btn32_5 = Button(tab1, bg="black", image=x10m5, bd=0, command=lambda o="silver": changecolor_value3_5(o))

    btn41_5 = Button(tab1, text="±1.00%", bg="brown", fg="black", command=lambda p="brown": changecolor_value4_5(p))
    btn42_5 = Button(tab1, text="±2.00%", bg="red", fg="black", command=lambda p="red": changecolor_value4_5(p))
    btn43_5 = Button(tab1, text="±3.00%", bg="orange", fg="black", command=lambda p="orange": changecolor_value4_5(p))
    btn44_5 = Button(tab1, text="±4.00%", bg="yellow", fg="black", command=lambda p="yellow": changecolor_value4_5(p))
    btn45_5 = Button(tab1, text="±0.50%", bg="green", fg="black", command=lambda p="green": changecolor_value4_5(p))
    btn46_5 = Button(tab1, text="±0.25%", bg="blue", fg="black", command=lambda p="blue": changecolor_value4_5(p))
    btn47_5 = Button(tab1, text="±0.10%", bg="violet", fg="black", command=lambda p="violet": changecolor_value4_5(p))
    btn48_5 = Button(tab1, text="±0.05%", bg="grey", fg="black", command=lambda p="grey": changecolor_value4_5(p))
    btn49_5 = Button(tab1, text="±5.00%", bg="gold", fg="black", command=lambda p="gold": changecolor_value4_5(p))
    btn50_5 = Button(tab1, text="±10.00%", bg="silver", fg="black", command=lambda p="silver": changecolor_value4_5(p))

    # Aligning Buttons and Labels
    lblresistor_5.place(x=140, y=150)
    lbllogo_5.place(x=30, y=20)
    lblresistorlogo_5.place(x=640, y=20)
    lblProject_5.place(x=170, y=15)
    lbldeveloper_5.place(x=250, y=60)
    lblOutput_5.place(x=165, y=290)
    lblValue_5.place(x=255, y=310)
    lblFirst_DigOut_5.place(x=320, y=300)
    lblSecond_DigOut_5.place(x=345, y=300)
    lblThird_DigOut_5.place(x=370, y=300)
    lblMultiplier_5.place(x=395, y=300)
    lblOhm_5.place(x=445, y=300)
    lblTolerance_5.place(x=257, y=350)
    lblToleOut_5.place(x=320, y=340)
    lbltolerance_5.place(x=340, y=440)

    lbl1_5.place(x=276, y=170)
    btn1_5.place(x=30, y=150)
    btn2_5.place(x=30, y=175)
    btn3_5.place(x=30, y=200)
    btn4_5.place(x=30, y=225)
    btn5_5.place(x=30, y=250)
    btn6_5.place(x=30, y=275)
    btn7_5.place(x=30, y=300)
    btn8_5.place(x=30, y=325)
    btn9_5.place(x=30, y=350)
    btn10_5.place(x=30, y=375)

    lbl2_5.place(x=316, y=170)
    btn11_5.place(x=70, y=150)
    btn12_5.place(x=70, y=175)
    btn13_5.place(x=70, y=200)
    btn14_5.place(x=70, y=225)
    btn15_5.place(x=70, y=250)
    btn16_5.place(x=70, y=275)
    btn17_5.place(x=70, y=300)
    btn18_5.place(x=70, y=325)
    btn19_5.place(x=70, y=350)
    btn20_5.place(x=70, y=375)

    lbl5_5.place(x=356, y=170)
    btn51_5.place(x=110, y=150)
    btn52_5.place(x=110, y=175)
    btn53_5.place(x=110, y=200)
    btn54_5.place(x=110, y=225)
    btn55_5.place(x=110, y=250)
    btn56_5.place(x=110, y=275)
    btn57_5.place(x=110, y=300)
    btn58_5.place(x=110, y=325)
    btn59_5.place(x=110, y=350)
    btn60_5.place(x=110, y=375)

    lbl3_5.place(x=465, y=170)
    btn21_5.place(x=636, y=144)
    btn22_5.place(x=640, y=175)
    btn23_5.place(x=640, y=200)
    btn24_5.place(x=640, y=225)
    btn25_5.place(x=640, y=250)
    btn26_5.place(x=640, y=275)
    btn27_5.place(x=640, y=300)
    btn28_5.place(x=640, y=325)
    btn29_5.place(x=640, y=350)
    btn30_5.place(x=640, y=375)
    btn31_5.place(x=640, y=400)
    btn32_5.place(x=640, y=425)

    lblblack_5.place(x=685, y=146)
    lblbrown_5.place(x=685, y=175)
    lblred_5.place(x=685, y=200)
    lblorange_5.place(x=685, y=225)
    lblyellow_5.place(x=685, y=250)
    lblgreen_5.place(x=685, y=275)
    lblblue_5.place(x=685, y=300)
    lblviolet_5.place(x=685, y=325)
    lblgrey_5.place(x=685, y=350)
    lblwhite_5.place(x=685, y=375)
    lblgold_5.place(x=685, y=400)
    lblsilver_5.place(x=685, y=425)

    lbl4_5.place(x=396, y=170)
    btn41_5.place(x=155, y=400)
    btn42_5.place(x=200, y=400)
    btn43_5.place(x=245, y=400)
    btn44_5.place(x=290, y=400)
    btn45_5.place(x=335, y=400)
    btn46_5.place(x=380, y=400)
    btn47_5.place(x=425, y=400)
    btn48_5.place(x=470, y=400)
    btn49_5.place(x=515, y=400)
    btn50_5.place(x=560, y=400)

    # Label para sa output

    def changecolor_value1_5(n):
        lbl1_5.config(bg=n)
        lblFirst_DigOut_5.config(text=color_5[n], font=('Verdana', 10))
        # return first_digit

    def changecolor_value2_5(m):
        lbl2_5.config(bg=m)
        lblSecond_DigOut_5.config(text=color_5[m], font=('Verdana', 10))
        # return second_digit

    def changecolor_value3_5(o):
        lbl4_5.config(bg=o)
        lblMultiplier_5.config(text=multiplier_5[o], font=('Verdana', 10))
        # return multiplier

    def changecolor_value4_5(p):
        lbl3_5.config(bg=p)
        lblToleOut_5.config(text=tolerance_5[p])
        # return tolerance

    def changecolor_value5_5(q):
        lbl5_5.config(bg=q)
        lblThird_DigOut_5.config(text=color_5[q], font=('Verdana', 10))

    tab1.mainloop()


def six_band():
    tab2 = Toplevel()
    tab2.iconbitmap('images/logos/ezgif.com-gif-maker (12).ico')
    tab2.config(bg='black')
    tab2.geometry("800x570")
    tab2.title("6-BAND RESISTOR COLOR CALCULATOR")

    # Resistor body and logos
    photoResistor = ImageTk.PhotoImage(file='images/bodyOfResistor/resistornatalaga.png')
    photoPython = ImageTk.PhotoImage(file='images/logos/logopython.png')
    photoDesign = ImageTk.PhotoImage(file='images/logos/nailawnaresistor.png')

    color_6 = {
        'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4',
        'green': '5', 'blue': '6', 'violet': '7', 'grey': '8', 'white': '9'
    }

    multiplier_6 = {
        'black': 'x10^0', 'brown': 'x10^1', 'red': 'x10^2', 'orange': 'x10^3', 'yellow': 'x10^4', 'green': 'x10^5',
        'blue': 'x10^6', 'violet': 'x10^7', 'grey': 'x10^8', 'white': 'x10^9', 'gold': 'x10^-1', 'silver': 'x10^-2'
    }

    tolerance_6 = {
        'brown': '±1.00%', 'red': '±2.00%', 'orange': '±3.00%', 'yellow': '±4.00%', 'green': '±0.50%',
        'blue': '±0.25%', 'violet': '±0.10%', 'grey': '±0.05%', 'gold': '±5.00%', 'silver': '±10.00%'
    }

    tempcoef_6 = {
        'black': '250 ppm/K', 'brown': '100 ppm/K', 'red': '50 ppm/K', 'orange': '15 ppm/K', 'yellow': '25 ppm/K',
        'green': '20 ppm/K', 'blue': '10 ppm/K', 'violet': '5 ppm/K', 'grey': '1 ppm/K'
    }
    # Creating Buttons from images

    x16 = PhotoImage(file="images/buttons/itim.png")
    x106 = PhotoImage(file="images/buttons/kayumanggi.png")
    x1006 = PhotoImage(file="images/buttons/pula.png")
    x1k6 = PhotoImage(file="images/buttons/orange.png")
    x10k6 = PhotoImage(file="images/buttons/yellow.png")
    x100k6 = PhotoImage(file="images/buttons/green.png")
    x1M6 = PhotoImage(file="images/buttons/blue.png")
    x10M6 = PhotoImage(file="images/buttons/violet.png")
    x100M6 = PhotoImage(file="images/buttons/grey.png")
    x1G6 = PhotoImage(file="images/buttons/white.png")
    x100m6 = PhotoImage(file="images/buttons/gold.png")
    x10m6 = PhotoImage(file="images/buttons/silver.png")

    # Creating Label
    lblresistor_6 = Label(tab2, image=photoResistor)
    lbllogo_6 = Label(tab2, image=photoPython)
    lblresistorlogo_6 = Label(tab2, image=photoDesign)
    lbl1_6 = Label(tab2, bg="black", width=1, height=6)
    lbl2_6 = Label(tab2, bg="black", width=1, height=6)
    lbl3_6 = Label(tab2, bg="black", width=1, height=6)
    lbl4_6 = Label(tab2, bg="black", width=1, height=6)
    lbl5_6 = Label(tab2, bg="black", width=1, height=6)
    lbl6_6 = Label(tab2, bg="black", width=1, height=6)
    lblOutput_6 = Label(tab2, bg="grey", width=60, height=6)
    lblValue_6 = Label(tab2, text="Value: ", bg="grey", fg="black", width=8, height=1, font=('Verdana', 10))
    lblFirst_DigOut_6 = Label(tab2, text='0', bg="white", width=3, height=2, font=('Verdana', 10))
    lblSecond_DigOut_6 = Label(tab2, text='0', bg="white", width=3, height=2, font=('Verdana', 10))
    lblThird_DigOut_6 = Label(tab2, text='0', bg="white", width=3, height=2, font=('Verdana', 10))
    lblMultiplier_6 = Label(tab2, text='x10^0', bg="white", width=6, height=2, font=('Verdana', 10))
    lblTempOut_6 = Label(tab2, text='0 ppm/K', bg="white", width=9, height=2, font=('Verdana', 10))
    lblOhm_6 = Label(tab2, text="Ω", bg="white", width=3, height=2, font=('Verdana', 10))
    lblTolerance_6 = Label(tab2, text="Tolerance: ", bg="grey", fg="black", width=8, height=1, font=('Verdana', 8))
    lbltemperature_6 = Label(tab2, text="Tc: ", fg='black', bg="grey", width=2, height=1, font=('Verdana', 8))
    lblTempCoef_6 = Label(tab2, text="TEMPERATURE COEFFICIENT", bg="black", fg="white", width=26, height=1, font=('Verdana', 8))
    lblToleOut_6 = Label(tab2, text='±0%', bg="white", width=15, height=2, font=('Verdana', 10))
    lbltolerance_6 = Label(tab2, text="TOLERANCE", fg='white', bg="black", width=9, height=1,font=('Verdana', 8))
    lblProject_6 = Label(tab2, text="Resistor Color Calculator", bg="black",
                         fg="white", width='20', height='1', font=('Verdana', 23, 'bold', 'italic'))
    lbldeveloper_6 = Label(tab2, text="By: Michael Rhey Palaganas", bg="black",
                           fg="white", width='22', height='1', font=('Times', 14, 'bold', 'italic'))
    lblblack_6 = Label(tab2, text="x1", bg="black", fg="white")
    lblbrown_6 = Label(tab2, text="x10", bg="black", fg="white")
    lblred_6 = Label(tab2, text="x100", bg="black", fg="white")
    lblorange_6 = Label(tab2, text="x1k", bg="black", fg="white")
    lblyellow_6 = Label(tab2, text="x10k", bg="black", fg="white")
    lblgreen_6 = Label(tab2, text="x100k", bg="black", fg="white")
    lblblue_6 = Label(tab2, text="x1M", bg="black", fg="white")
    lblviolet_6 = Label(tab2, text="x10M", bg="black", fg="white")
    lblgrey_6 = Label(tab2, text="100M", bg="black", fg="white")
    lblwhite_6 = Label(tab2, text="1G", bg="black", fg="white")
    lblgold_6 = Label(tab2, text="x0.1", bg="black", fg="white")
    lblsilver_6 = Label(tab2, text="x0.01", bg="black", fg="white")

    # Creating Buttons
    # Buttons for 1st Digit/Band
    btn1_6 = Button(tab2, text="0", bg="black", fg="white", command=lambda n="black": changecolor_value1_6(n))
    btn2_6 = Button(tab2, text="1", bg="brown", fg="black", command=lambda n="brown": changecolor_value1_6(n))
    btn3_6 = Button(tab2, text="2", bg="red", fg="black", command=lambda n="red": changecolor_value1_6(n))
    btn4_6 = Button(tab2, text="3", bg="orange", fg="black", command=lambda n="orange": changecolor_value1_6(n))
    btn5_6 = Button(tab2, text="4", bg="yellow", fg="black", command=lambda n="yellow": changecolor_value1_6(n))
    btn6_6 = Button(tab2, text="5", bg="green", fg="black", command=lambda n="green": changecolor_value1_6(n))
    btn7_6 = Button(tab2, text="6", bg="blue", fg="black", command=lambda n="blue": changecolor_value1_6(n))
    btn8_6 = Button(tab2, text="7", bg="violet", fg="black", command=lambda n="violet": changecolor_value1_6(n))
    btn9_6 = Button(tab2, text="8", bg="grey", fg="black", command=lambda n="grey": changecolor_value1_6(n))
    btn10_6 = Button(tab2, text="9", bg="white", fg="black", command=lambda n="white": changecolor_value1_6(n))

    # Buttons for 2nd Digit/Band
    btn11_6 = Button(tab2, text="0", bg="black", fg="white", command=lambda m="black": changecolor_value2_6(m))
    btn12_6 = Button(tab2, text="1", bg="brown", fg="black", command=lambda m="brown": changecolor_value2_6(m))
    btn13_6 = Button(tab2, text="2", bg="red", fg="black", command=lambda m="red": changecolor_value2_6(m))
    btn14_6 = Button(tab2, text="3", bg="orange", fg="black", command=lambda m="orange": changecolor_value2_6(m))
    btn15_6 = Button(tab2, text="4", bg="yellow", fg="black", command=lambda m="yellow": changecolor_value2_6(m))
    btn16_6 = Button(tab2, text="5", bg="green", fg="black", command=lambda m="green": changecolor_value2_6(m))
    btn17_6 = Button(tab2, text="6", bg="blue", fg="black", command=lambda m="blue": changecolor_value2_6(m))
    btn18_6 = Button(tab2, text="7", bg="violet", fg="black", command=lambda m="violet": changecolor_value2_6(m))
    btn19_6 = Button(tab2, text="8", bg="grey", fg="black", command=lambda m="grey": changecolor_value2_6(m))
    btn20_6 = Button(tab2, text="9", bg="white", fg="black", command=lambda m="white": changecolor_value2_6(m))

    # Buttons for 3rd Digit/Band
    btn51_6 = Button(tab2, text="0", bg="black", fg="white", command=lambda q="black": changecolor_value5_6(q))
    btn52_6 = Button(tab2, text="1", bg="brown", fg="black", command=lambda q="brown": changecolor_value5_6(q))
    btn53_6 = Button(tab2, text="2", bg="red", fg="black", command=lambda q="red": changecolor_value5_6(q))
    btn54_6 = Button(tab2, text="3", bg="orange", fg="black", command=lambda q="orange": changecolor_value5_6(q))
    btn55_6 = Button(tab2, text="4", bg="yellow", fg="black", command=lambda q="yellow": changecolor_value5_6(q))
    btn56_6 = Button(tab2, text="5", bg="green", fg="black", command=lambda q="green": changecolor_value5_6(q))
    btn57_6 = Button(tab2, text="6", bg="blue", fg="black", command=lambda q="blue": changecolor_value5_6(q))
    btn58_6 = Button(tab2, text="7", bg="violet", fg="black", command=lambda q="violet": changecolor_value5_6(q))
    btn59_6 = Button(tab2, text="8", bg="grey", fg="black", command=lambda q="grey": changecolor_value5_6(q))
    btn60_6 = Button(tab2, text="9", bg="white", fg="black", command=lambda q="white": changecolor_value5_6(q))

    # Buttons for Temp Coefficient
    btn61_6 = Button(tab2, text="250 ppm/K", bg="black", fg="white", command=lambda r="black": changecolor_value6_6(r))
    btn62_6 = Button(tab2, text="100 ppm/K", bg="brown", fg="black", command=lambda r="brown": changecolor_value6_6(r))
    btn63_6 = Button(tab2, text="50 ppm/K", bg="red", fg="black", command=lambda r="red": changecolor_value6_6(r))
    btn64_6 = Button(tab2, text="15 ppm/K", bg="orange", fg="black", command=lambda r="orange": changecolor_value6_6(r))
    btn65_6 = Button(tab2, text="25 ppm/K", bg="yellow", fg="black", command=lambda r="yellow": changecolor_value6_6(r))
    btn66_6 = Button(tab2, text="20 ppm/K", bg="green", fg="black", command=lambda r="green": changecolor_value6_6(r))
    btn67_6 = Button(tab2, text="10 ppm/K", bg="blue", fg="black", command=lambda r="blue": changecolor_value6_6(r))
    btn68_6 = Button(tab2, text="5 ppm/K", bg="violet", fg="black", command=lambda r="violet": changecolor_value6_6(r))
    btn69_6 = Button(tab2, text="1 ppm/K", bg="grey", fg="black", command=lambda r="grey": changecolor_value6_6(r))

    btn21_6 = Button(tab2, bg="black", image=x16, bd=0, command=lambda o="black": changecolor_value3_6(o))
    btn22_6 = Button(tab2, bg="black", image=x106, bd=0, command=lambda o="brown": changecolor_value3_6(o))
    btn23_6 = Button(tab2, bg="black", image=x1006, bd=0, command=lambda o="red": changecolor_value3_6(o))
    btn24_6 = Button(tab2, bg="black", image=x1k6, bd=0, command=lambda o="orange": changecolor_value3_6(o))
    btn25_6 = Button(tab2, bg="black", image=x10k6, bd=0, command=lambda o="yellow": changecolor_value3_6(o))
    btn26_6 = Button(tab2, bg="black", image=x100k6, bd=0, command=lambda o="green": changecolor_value3_6(o))
    btn27_6 = Button(tab2, bg="black", image=x1M6, bd=0, command=lambda o="blue": changecolor_value3_6(o))
    btn28_6 = Button(tab2, bg="black", image=x10M6, bd=0, command=lambda o="violet": changecolor_value3_6(o))
    btn29_6 = Button(tab2, bg="black", image=x100M6, bd=0, command=lambda o="grey": changecolor_value3_6(o))
    btn30_6 = Button(tab2, bg="black", image=x1G6, bd=0, command=lambda o="white": changecolor_value3_6(o))
    btn31_6 = Button(tab2, bg="black", image=x100m6, bd=0, command=lambda o="gold": changecolor_value3_6(o))
    btn32_6 = Button(tab2, bg="black", image=x10m6, bd=0, command=lambda o="silver": changecolor_value3_6(o))

    btn41_6 = Button(tab2, text="±1.00%", bg="brown", fg="black", command=lambda p="brown": changecolor_value4_6(p))
    btn42_6 = Button(tab2, text="±2.00%", bg="red", fg="black", command=lambda p="red": changecolor_value4_6(p))
    btn43_6 = Button(tab2, text="±3.00%", bg="orange", fg="black", command=lambda p="orange": changecolor_value4_6(p))
    btn44_6 = Button(tab2, text="±4.00%", bg="yellow", fg="black", command=lambda p="yellow": changecolor_value4_6(p))
    btn45_6 = Button(tab2, text="±0.50%", bg="green", fg="black", command=lambda p="green": changecolor_value4_6(p))
    btn46_6 = Button(tab2, text="±0.25%", bg="blue", fg="black", command=lambda p="blue": changecolor_value4_6(p))
    btn47_6 = Button(tab2, text="±0.10%", bg="violet", fg="black", command=lambda p="violet": changecolor_value4_6(p))
    btn48_6 = Button(tab2, text="±0.05%", bg="grey", fg="black", command=lambda p="grey": changecolor_value4_6(p))
    btn49_6 = Button(tab2, text="±5.00%", bg="gold", fg="black", command=lambda p="gold": changecolor_value4_6(p))
    btn50_6 = Button(tab2, text="±10.00%", bg="silver", fg="black", command=lambda p="silver": changecolor_value4_6(p))

    # Aligning Buttons and Labels
    lblresistor_6.place(x=140, y=150)
    lbllogo_6.place(x=30, y=20)
    lblresistorlogo_6.place(x=640, y=20)
    lblProject_6.place(x=170, y=15)
    lbldeveloper_6.place(x=250, y=60)
    lblOutput_6.place(x=165, y=290)
    lblValue_6.place(x=255, y=310)
    lblFirst_DigOut_6.place(x=320, y=300)
    lblSecond_DigOut_6.place(x=345, y=300)
    lblThird_DigOut_6.place(x=370, y=300)
    lblMultiplier_6.place(x=395, y=300)
    lblOhm_6.place(x=445, y=300)
    lblTolerance_6.place(x=177, y=350)
    lblToleOut_6.place(x=240, y=340)
    lbltolerance_6.place(x=340, y=440)
    lblTempCoef_6.place(x=280, y=520)
    lblTempOut_6.place(x=470, y=340)
    lbltemperature_6.place(x=440, y=350)

    lbl1_6.place(x=276, y=170)
    btn1_6.place(x=30, y=150)
    btn2_6.place(x=30, y=175)
    btn3_6.place(x=30, y=200)
    btn4_6.place(x=30, y=225)
    btn5_6.place(x=30, y=250)
    btn6_6.place(x=30, y=275)
    btn7_6.place(x=30, y=300)
    btn8_6.place(x=30, y=325)
    btn9_6.place(x=30, y=350)
    btn10_6.place(x=30, y=375)

    lbl2_6.place(x=306, y=170)
    btn11_6.place(x=70, y=150)
    btn12_6.place(x=70, y=175)
    btn13_6.place(x=70, y=200)
    btn14_6.place(x=70, y=225)
    btn15_6.place(x=70, y=250)
    btn16_6.place(x=70, y=275)
    btn17_6.place(x=70, y=300)
    btn18_6.place(x=70, y=325)
    btn19_6.place(x=70, y=350)
    btn20_6.place(x=70, y=375)

    lbl5_6.place(x=336, y=170)
    btn51_6.place(x=110, y=150)
    btn52_6.place(x=110, y=175)
    btn53_6.place(x=110, y=200)
    btn54_6.place(x=110, y=225)
    btn55_6.place(x=110, y=250)
    btn56_6.place(x=110, y=275)
    btn57_6.place(x=110, y=300)
    btn58_6.place(x=110, y=325)
    btn59_6.place(x=110, y=350)
    btn60_6.place(x=110, y=375)

    # Tolerance
    lbl3_6.place(x=426, y=170)
    btn21_6.place(x=636, y=144)
    btn22_6.place(x=640, y=175)
    btn23_6.place(x=640, y=200)
    btn24_6.place(x=640, y=225)
    btn25_6.place(x=640, y=250)
    btn26_6.place(x=640, y=275)
    btn27_6.place(x=640, y=300)
    btn28_6.place(x=640, y=325)
    btn29_6.place(x=640, y=350)
    btn30_6.place(x=640, y=375)
    btn31_6.place(x=640, y=400)
    btn32_6.place(x=640, y=425)

    lblblack_6.place(x=685, y=146)
    lblbrown_6.place(x=685, y=175)
    lblred_6.place(x=685, y=200)
    lblorange_6.place(x=685, y=225)
    lblyellow_6.place(x=685, y=250)
    lblgreen_6.place(x=685, y=275)
    lblblue_6.place(x=685, y=300)
    lblviolet_6.place(x=685, y=325)
    lblgrey_6.place(x=685, y=350)
    lblwhite_6.place(x=685, y=375)
    lblgold_6.place(x=685, y=400)
    lblsilver_6.place(x=685, y=425)

    # Multiplier
    lbl4_6.place(x=366, y=170)
    btn41_6.place(x=155, y=400)
    btn42_6.place(x=200, y=400)
    btn43_6.place(x=245, y=400)
    btn44_6.place(x=290, y=400)
    btn45_6.place(x=335, y=400)
    btn46_6.place(x=380, y=400)
    btn47_6.place(x=425, y=400)
    btn48_6.place(x=470, y=400)
    btn49_6.place(x=515, y=400)
    btn50_6.place(x=560, y=400)

    lbl6_6.place(x=456, y=170)
    btn61_6.place(x=115, y=480)
    btn62_6.place(x=185, y=480)
    btn63_6.place(x=250, y=480)
    btn64_6.place(x=310, y=480)
    btn65_6.place(x=370, y=480)
    btn66_6.place(x=430, y=480)
    btn67_6.place(x=490, y=480)
    btn68_6.place(x=550, y=480)
    btn69_6.place(x=605, y=480)

    # Label para sa output

    def changecolor_value1_6(n):
        lbl1_6.config(bg=n)
        lblFirst_DigOut_6.config(text=color_6[n], font=('Verdana', 10))
        # return first_digit

    def changecolor_value2_6(m):
        lbl2_6.config(bg=m)
        lblSecond_DigOut_6.config(text=color_6[m], font=('Verdana', 10))
        # return second_digit

    def changecolor_value3_6(o):
        lbl4_6.config(bg=o)
        lblMultiplier_6.config(text=multiplier_6[o], font=('Verdana', 10))
        # return multiplier

    def changecolor_value4_6(p):
        lbl3_6.config(bg=p)
        lblToleOut_6.config(text=tolerance_6[p])

    def changecolor_value5_6(q):
        lbl5_6.config(bg=q)
        lblThird_DigOut_6.config(text=color_6[q], font=('Verdana', 10))

    def changecolor_value6_6(r):
        lbl6_6.config(bg=r)
        lblTempOut_6.config(text=tempcoef_6[r], font=('Verdana', 10))


    tab2.mainloop()


five_bandTab = Button(window, text="5-Band", bg="grey", fg="black", command=five_band, relief=RAISED)
five_bandTab.place(x=350, y=95)

six_bandTab = Button(window, text="6-Band", bg="grey", fg="black", command=six_band, relief=RAISED)
six_bandTab.place(x=400, y=95)
window.mainloop()
