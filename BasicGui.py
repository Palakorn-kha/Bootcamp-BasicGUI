# BasicGUI.py

from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.geometry('600x700') # เครื่องหมายคูณให้ใส่ ตัวเอ็กตัวเล็ก x
GUI.title('โปรแกรมสำหรับคิดราคาทุเรียน v.0.0.1')

file = PhotoImage(file='durian.png')
IMG = Label(GUI,image=file,text='')
IMG.pack()

L1 = Label(GUI,text='โปรแกรมคำนวณทุเรียน (กิโลกร้ม)',font=('TH Sarabun New',30,'bold'),fg='green')
L1.pack() #.place(x,y) , .grid(row=0,column=0)

L2 = Label(GUI,text='กรุณากรอกจำนวนทุเรียน',font=('TH Sarabun New',20))
L2.pack()

v_quantity = StringVar() # ตำแหน่งตัวแปรที่ใช้เก็บข้อมูลของช่องกรอก
E1 = ttk.Entry(GUI,textvariable=v_quantity,font=('impact',18))
E1.pack()

def Calculate(event=None): # เมือต้องการทั้งกดปุ่มหรือ กด Enter ให้ใส่ = None ไปด้วย
	quantity = v_quantity.get()
	price = 100
	print('จำนวน', float(quantity) * price) # ใส่ float เพื่อแปลงให้เป็นตัวเลขทศนิยม
	cal = float(quantity) * price
	# EN DATE
	# stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	# writetext(quantity,cal)
	#data = [timestamp(), quantity, cal]
	#writecsv(data)

	
	title = 'ยอดที่ลูกค้าต้องจ่าย'
	text = 'ทุเรียนจำนวน {} กิโลกร้ม ราคาทั้งหมด: {:,.2f} บาท'.format(quantity,cal)
	messagebox.showinfo(title,text)

	v_quantity.set('') #เป็นการเคลียร์ ข้อมูล
	E1.focus()


B1 = ttk.Button(GUI,text='คำนวณ',command=Calculate)
B1.pack(ipadx=25,ipady=15,pady=20)

E1.bind('<Return>', Calculate)

def SummaryData(event):
	# pop up
	sm = sumdata()
	title = 'ยอดที่ลูกค้าต้องจ่าย'
	text = 'จำนวนที่ขายได้: {} กก. \nยอดขาย: {:,.2f} บาท'.format(sm[0],sm[1])
	messagebox.showinfo(title,text)

GUI.bind('<F1>',SummaryData)
GUI.bind('<F2>',SummaryData)

E1.focus() # ให้ cursor ไปยังตำแหน่งของ E1
GUI.mainloop()