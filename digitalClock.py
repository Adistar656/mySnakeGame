''' Aditya Tiwari
    30/11/2021
    2:00 pm '''


from tkinter import *
import time


clk = Tk()
clk.title("Digital CLock")
clk.geometry("1350x700+0+0") # (height,width,x-axis,y-axis)  as we have given 0 we will start from top-left corner
clk.config(bg = "#0C1E28") # you can give any color you want


def clock():
    hr = str(time.strftime("%H"))
    mn = str(time.strftime("%M"))
    sc = str(time.strftime("%S"))
    print(hr,mn,sc)
    if int(hr)>12 and int(mn)>0: # to convert am to pm 
        lb_dn.config(text="PM")
    if int(hr)>12:
        hr = str(int(int(hr)-12))
    lb_hr.config(text=hr)
    lb_mn.config(text=mn)
    lb_sc.config(text=sc)

    lb_hr.after(200,clock) # to make clock update every second

    


# For Hour Block
lb_hr = Label(clk, text="12", font=("Times 20 Bold",75,'bold'), bg="#087587", fg="white")
lb_hr.place(x=350,y=200,width=150,height=150)

lb_hr_text= Label(clk, text= "Hours", font=("Times 20 Bold",20,'bold'), bg="#087587", fg="white")
lb_hr_text.place(x=350,y=360,width=150,height=50)


# For minute Block
lb_mn = Label(clk, text="12", font=("Times 20 Bold",75,'bold'), bg="#008EA4", fg="white")
lb_mn.place(x=520,y=200,width=150,height=150)

lb_mn_text= Label(clk, text= "Minutes", font=("Times 20 Bold",20,'bold'), bg="#008EA4", fg="white")
lb_mn_text.place(x=520,y=360,width=150,height=50)


#For Seconds Block
lb_sc = Label(clk, text="12", font=("Times 20 Bold",75,'bold'), bg="#06B488", fg="white")
lb_sc.place(x=690,y=200,width=150,height=150)

lb_sc_text= Label(clk, text= "Seconds", font=("Times 20 Bold",20,'bold'), bg="#06B488", fg="white")
lb_sc_text.place(x=690,y=360,width=150,height=50)

# For Am/Pm
lb_dn = Label(clk, text="AM", font=("Times 20 Bold",70,'bold'), bg="#9F0646", fg="white")
lb_dn.place(x=860,y=200,width=150,height=150)

lb_dn_text= Label(clk, text= "Noon", font=("Times 20 Bold",20,'bold'), bg="#9F0646", fg="white")
lb_dn_text.place(x=860,y=360,width=150,height=50)

clock()
clk.manloop()
