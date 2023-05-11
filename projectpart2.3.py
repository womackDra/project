
import tkinter as tk

from PIL import Image, ImageTk
#order list
Order = []

#function
#cancels order and closes order window
def cancel():
    Order.clear()
    orderwindow.destroy()
    
#add selected item to Order list
def orderChiliFries():
    Order.append("Chili Fries")
    
def orderChili():
    Order.append("Chili")
    
def orderPizza():
    Order.append("Pizza")
#chili window, image, and button
def openChili():
    chiliWindow = tk.Toplevel()
    Chili = Image.open("Chili.jpg")
    Chili = Chili.resize((100,100), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(Chili)
    ChiliOrder = tk.Label(chiliWindow, image=photo)
    ChiliOrder.image = photo
    ChiliOrder.pack()
    OrderButt = tk.Button(chiliWindow, command=orderChili, text = "Order")
    OrderButt.pack()

#order window
def openOrder():
    global orderwindow
    orderwindow = tk.Toplevel()
    for item in Order:
        order_label = tk.Label(orderwindow, text=item)
        order_label.pack()
    OrderMeal = tk.Button(orderwindow, text = "Order Meal")
    OrderMeal.pack()
    CancelButton = tk.Button(orderwindow, command=cancel, text = "Cancel Meal")
    CancelButton.pack()
    
#pizza Window
def openPizza():
    pizzaWindow = tk.Toplevel()
    Pizza = Image.open("pizza.jpg")
    Pizza = Pizza.resize((100,100), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(Pizza)
    PizzaOrder = tk.Label(pizzaWindow, image=photo)
    PizzaOrder.image = photo
    PizzaOrder.pack()
    OrderButt = tk.Button(pizzaWindow, command=orderPizza, text = "Order")
    OrderButt.pack()

#sides window
def opensides():
    sidesWindow = tk.Toplevel()
    ChiliFries = Image.open("ChiliFries.jpg")
    ChiliFries = ChiliFries.resize((100,100), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(ChiliFries)
    ChiliFriesOrder = tk.Label(sidesWindow, image=photo)
    ChiliFriesOrder.image = photo
    ChiliFriesOrder.pack()
    OrderButt = tk.Button(sidesWindow, command=orderChiliFries, text = "Order")
    OrderButt.pack()
#main Window
foodwindow = tk.Tk()
#menu sections
chiliButt = tk.Button(foodwindow,command=openChili, text = "Chili")
chiliButt.pack()
PizzaButt = tk.Button(foodwindow,command=openPizza, text = "Pizza")
PizzaButt.pack()
sides = tk.Button(foodwindow,command=opensides, text = "Sides")
sides.pack()
order = tk.Button(command=openOrder, text = "Check Order" )
order.pack()    
    
'''
#window 
mainWindow = tk.Tk()
#button 
menu = tk.Button(command=openFood, text = "Menu")
menu.pack()
'''
#automaticly opens main window
foodwindow.mainloop()