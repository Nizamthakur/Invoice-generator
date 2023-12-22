import tkinter
from tkinter import ttk 
from docxtpl import DocxTemplate
# from docx import Document
import datetime 
import os 



def clear_item (): 
    qty_spinbox.delete(0, tkinter.END)
    qty_spinbox.insert(0, '1')
    discription_entry.delete(0, tkinter.END)
    unit_price_spinbox.delete(0, tkinter.END)
    unit_price_spinbox.insert(0,"0.0")
    # delivery_charge_entry.delete(0 , tkinter.END)

invoice_list = []
def add_item():
    qty = int(qty_spinbox.get())
    description = discription_entry.get()
    price = int(unit_price_spinbox.get())
    line_total = qty * price
    delivery_charge = int(delivery_charge_entry.get())

    invoice_item = [qty, description, price, line_total, delivery_charge]

    tree.insert('', 0, values=invoice_item)
    clear_item()

    invoice_list.append(invoice_item)

    
def new_invoice():
    first_name_entry.delete(0,tkinter.END)
    last_name_entry.delete(0,tkinter.END)
    phone_entry.delete(0,tkinter.END)
    clear_item()
    tree.delete(*tree.get_children())
    invoice_list.clear()

def Generate_invoice(): 
##change
    script_dir = os.path.dirname(os.path.abspath(__file__))
    docx_path = os.path.join(script_dir, "invoice.docx")
##change 
    doc = DocxTemplate(docx_path)

    # doc = DocxTemplate("invoice.docx")
    name  = first_name_entry.get ()
    address = last_name_entry.get()
    phone  = phone_entry.get()
    subtotal = sum(item[3]for item in invoice_list)
    delivery_charge_str = delivery_charge_entry.get()
        # Check if delivery_charge_str is not empty and is a valid integer
    if delivery_charge_str and delivery_charge_str.isdigit():
        delivery_charge = int(delivery_charge_str)
    else:
        # Display an error message or handle invalid input as needed
        print("Please enter a valid delivery charge.")
        return

    print(f"Subtotal: {subtotal}")
    print(f"Delivery Charge: {delivery_charge}")

    total = subtotal + delivery_charge

    print(f"Total: {total}")


    doc.render({
        "name":name, 
        "address": address,
        "phone":phone,
        "invoice_list": invoice_list, 
        "subtotal": subtotal, 
        "salestax": delivery_charge, 
        "total" : total
    })
    doc_name = "new_invoice"+ name + datetime.datetime.now().strftime("%y-%m-%d-%H%M%S") + ".docx"
    doc.save(doc_name)

    



window = tkinter.Tk()
window.title ("Invoice Generator Form")

frame  = tkinter.Frame(window)
frame.pack(padx=20 , pady= 20 )

first_name_label = tkinter.Label(frame ,text = "First name")
first_name_label.grid(row = 0 , column= 0)
first_name_entry =tkinter.Entry(frame)
first_name_entry.grid( row = 1, column= 0)

last_name_label  = tkinter.Label(frame ,text = "address") 
last_name_label.grid(row = 0 , column= 1)
last_name_entry =tkinter.Entry(frame)
last_name_entry.grid( row = 1, column= 1)

phone = tkinter.Label(frame, text = "Phone number")
phone.grid (row = 0 , column= 2 )
phone_entry = tkinter.Entry(frame)
phone_entry.grid(row=1 , column=2 )

qty_label  = tkinter.Label(frame , text ="Qty")
qty_label.grid  (row = 2 , column = 0 )
qty_spinbox = tkinter.Spinbox(frame, from_= 1, to= 100)
qty_spinbox.grid(row=3, column=0)

discription_label  = tkinter.Label(frame , text = "discription")
discription_label.grid(row = 2, column= 1)
discription_entry = tkinter.Entry(frame)
discription_entry.grid(row =3 , column=1)

unit_price_label  =tkinter.Label(frame, text = "Unit Price")
unit_price_label.grid(row=2, column=2)
unit_price_spinbox = tkinter.Spinbox(frame, from_ = 0.0,  to = 5000)
unit_price_spinbox.grid(row=3, column=2)

delivery_charge_label = tkinter.Label(frame, text = "Delivery charge")
delivery_charge_label.grid( row= 4 , column = 0)
delivery_charge_entry = tkinter.Entry(frame)
delivery_charge_entry.grid(row = 5 , column = 0)


add_item_button = tkinter.Button(frame, text = "Add item" , command= add_item)
add_item_button.grid (row= 4 , column= 2 , pady = 5 )

columns = ('Qty', 'Discription', 'price', 'total') 
tree  = ttk.Treeview (frame , columns = columns , show = "headings")

tree.heading('Qty', text = "Qty")
tree.heading('Discription', text = "Discription")
tree.heading('price', text = "price")
tree.heading('total', text = "total")

save_invoice_button =  tkinter.Button(frame, text = "Generate Invoice", command = Generate_invoice  )
save_invoice_button.grid (row= 7 , column= 0 , columnspan= 3 , sticky=" news ", padx = 20 , pady= 5)
new_invoice_button = tkinter.Button (frame, text = "New Invoice" , command = new_invoice )
new_invoice_button.grid (row= 8 , column= 0 , columnspan= 3 , sticky=" news ", padx = 20 , pady= 5)

tree.grid( row=6, column= 0, columnspan=3 , padx = 20 , pady = 10)
window.mainloop()
