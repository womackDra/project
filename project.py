
import tkinter as tk

from PIL import Image, ImageTk

#function
def openChili():
    chiliWindow = tk.Toplevel()
    Chili = Image.open("Chili.jpg")
    Chili = Chili.resize((100,100), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(Chili)
    ChiliOrder = tk.Label(chiliWindow, image=photo)
    ChiliOrder.image = photo
    ChiliOrder.pack()

def openOrder():
    orderwindow = tk.Tk()
    
def openPizza():
    pizzaWindow = tk.Toplevel()
    Pizza = Image.open("pizza.jpg")
    Pizza = Pizza.resize((100,100), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(Pizza)
    PizzaOrder = tk.Label(pizzaWindow, image=photo)
    PizzaOrder.image = photo
    PizzaOrder.pack()

def opensides():
    sidesWindow = tk.Toplevel()
    ChiliFries = Image.open("ChiliFries.jpg")
    ChiliFries = ChiliFries.resize((100,100), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(ChiliFries)
    ChiliFriesOrder = tk.Label(sidesWindow, image=photo)
    ChiliFriesOrder.image = photo
    ChiliFriesOrder.pack()
    OrderButt = tk.Button(sidesWindow, command=orderChiliFries, text = "Order")
    
foodwindow = tk.Tk()
#menu
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
  
foodwindow.mainloop()