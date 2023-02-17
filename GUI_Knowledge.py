from tkinter import *
from tkinter import ttk #theme ของ tk
from tkinter import messagebox

GUI = Tk() # หน้าจอหลัก
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x400') #ขนาดหน้าต่าง

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้', font=('Angsana New' ,30), fg='green')
#########################################
B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท?')
B1.pack(ipadx=20,ipady=20) #ปุ่ม B1 ขนาด

def Button2():
    text = 'ตอนนี้มีเงินอยู่ ๓๐๐ บาท'
    messagebox.showinfo('เงินในบัญชี',text) #หน้าต่าง popup

#B1 =Button(GUI,text='เงินมีอยู่กี่บาท?')
#B1.pack() #ปุ่ม B1 อยู่กลางหน้าต่าง

FB1 = Frame(GUI) #สร้างเฟรม
FB1.place(x=100,y=300) 
B2 = ttk.Button(FB1,text='เงินมีอยู่เท่าไร?')
B2.pack(ipadx=20,ipady=20) #ปุ่ม B2 ระบุตำแหน่ง
#############################################
B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท?')
B1.pack(ipadx=20,ipady=20) #ปุ่ม B1 ขนาด

def Button3():
    text = 'Python 101, Math'
    messagebox.showinfo("วิชาเรียนวันที่ 10-20 ก.พ.",text) #หน้าต่าง popup

FB2 = Frame(GUI) #สร้างเฟรม
FB2.place(x=100,y=100) 
B3 = ttk.Button(FB1,text='วันนี้เรียนอะไร?')
B3.pack(ipadx=20,ipady=20) #ปุ่ม B3 ระบุตำแหน่ง

GUI.mainloop()
