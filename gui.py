import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
productList = {}

class App(Tk):

    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.title("  .  ")
        self.switch(Menu)
        self.geometry('1280x800')
        self.config(bg="#000E19")

    def switch(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class Menu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg="#000E19")

        label = Label(
            self,
            text="Nutrition Calculator V0.4.3\n Choose an option.",
            bg="#000E19",
            fg="#79C7C5")
        label.pack()
        button = Button(self, text="Calculator", width=20, bg='#79C7C5', fg='#000E19',
                        command=lambda: master.switch(Calculator))
        button.pack(padx=10, pady=10)
        button2 = Button(self, text="Food Datas", width=20, bg='#79C7C5', fg='#000E19',
                         command=lambda: master.switch(foodDatas))
        button2.pack(padx=10, pady=10)
        button3 = Button(self, text="Add a food", width=20, bg='#79C7C5', fg='#000E19',
                         command=lambda: master.switch(File_Write))
        button3.pack(padx=10, pady=10)
        exit = Button(self, text="Exit", width=20, bg='#79C7C5', fg='#000E19', 
                      command=self.close)
        exit.pack(padx=10, pady=10)
    
    
    def close(self):
        self.destroy()
        exit()

class foodDatas(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg="#000E19")

        def result(product, gram):
            kcalValue = proteinValue = carbValue = fatValue = 0
            # check user value = database value
            if product in productList:
                (product, kcal, protein, carb, fat) = productList[product]
                # calculate
                kcalValue += gram * float(kcal)
                proteinValue += gram * float(protein)
                carbValue += gram * float(carb)
                fatValue += gram * float(fat)
                outcome = f"Your product provided you with:\n Calories: {kcalValue:.2f} kcal\n Protein: {proteinValue:.2f}\n Carbs: {carbValue:.2f}\n Fat: {fatValue:.2f}"
            else:
                outcome = "Sorry, but we don't have this food in our database: %s, but you can add it! :)" % (
                    product)
                button3 = Button(self, text="Add the food", width=20, bg='#79C7C5', fg='#000E19',
                         command=lambda: master.switch(File_Write))
                button3.pack(padx=10, pady=10)
            return outcome

        def file_open():
            with open("food_nutrients.txt") as file:
                for row in file:
                    if not row:
                        continue
                    else:
                        name, kcal, protein, carb, fat = row.split(',')
                        productList[name] = (
                            name, kcal, protein, carb, fat)

        def on_click():
            product = entryProduct.get()
            output.delete(0.0, END)

            Error = False
            gram = int(1)
            try:
                x = int(product)
                Error = True
            except BaseException:
                pass
            if Error == True:
                messagebox.showerror("Error", "Please enter correct data!")
            else:
                file_open()
                output.insert(END, result(product, gram))

        label = Label(
            self,
            text="Enter a food",
            bg="#000E19",
            fg="white")
        label.pack()
        # user input, food
        label2 = Label(self, text="Name: ", bg="#000E19", fg="white")
        label2.pack()
        entryProduct = Entry(self, width=20, bg="#000E19", fg="#79C7C5")
        entryProduct.pack()
        # submit
        submit = Button(self, text="Submit", width=8, command=on_click)
        submit.pack(padx=10, pady=10)
        # output
        label4 = Label(
            self,
            text="These are the nutrition values:",
            bg="#000E19",
            fg="#000E19")
        label4.pack()
        output = Text(self, width=40, height=20, wrap=WORD)
        output.pack()
        # going back to menu
        button3 = Button(
            self,
            text="Back",
            width=20, bg='#79C7C5', fg='#000E19',
            command=lambda: master.switch(Menu))
        button3.pack(padx=10, pady=10)
        
class Calculator(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg="#000E19")

        def result(product, gram):
            kcalValue = proteinValue = carbValue = fatValue = 0
            # check user value = database value
            if product in productList:
                (product, kcal, protein, carb, fat) = productList[product]
                # calculate
                kcalValue += gram * float(kcal)
                proteinValue += gram * float(protein)
                carbValue += gram * float(carb)
                fatValue += gram * float(fat)
                outcome = f"Your product provided you with:\n Calories: {kcalValue:.2f} kcal\n Protein: {proteinValue:.2f}\n Carbs: {carbValue:.2f}\n Fat: {fatValue:.2f}"
            else:
                outcome = "Sorry, but we don't have this food in our database: %s, but you can add it! :)" % (
                    product)
                button3 = Button(self, text="Add the food", width=20, bg='#79C7C5', fg='#000E19',
                         command=lambda: master.switch(File_Write))
                button3.pack(padx=10, pady=10)
            return outcome

        def file_open():
            with open("food_nutrients.txt") as file:
                for row in file:
                    if not row:
                        continue
                    else:
                        name, kcal, protein, carb, fat = row.split(',')
                        productList[name] = (
                            name, kcal, protein, carb, fat)

        def on_click():
            product = entryProduct.get()
            gram = entryGram.get()
            output.delete(0.0, END)

            Error = False
            try:
                gram = float(entryGram.get())
            except BaseException:
                Error = True
            try:
                x = int(product)
                Error = True
            except BaseException:
                pass
            if Error == True:
                messagebox.showerror("Error", "Please enter correct data!")
            else:
                file_open()
                output.insert(END, result(product, gram))

        label = Label(
            self,
            text="Enter a food that you ate.",
            bg="#000E19",
            fg="white")
        label.pack()
        # user input, food
        label2 = Label(self, text="Name: ", bg="#000E19", fg="white")
        label2.pack()
        entryProduct = Entry(self, width=20, bg="#79C7C5", fg="#000E19")
        entryProduct.pack()
        # user input, amount
        label3 = Label(self, text="Amount per 100g: ", bg="#000E19", fg="white")
        label3.pack()
        entryGram = Entry(self, width=20, bg="#79C7C5", fg="#000E19")
        entryGram.pack()
        # submit
        submit = Button(self, text="Submit", width=8, command=on_click)
        submit.pack(padx=10, pady=10)
        # output
        label4 = Label(
            self,
            text="These are the nutrition values:",
            bg="#000E19",
            fg="#000E19")
        label4.pack()
        output = Text(self, width=40, height=20, wrap=WORD)
        output.pack()
        # going back to menu
        button3 = Button(
            self,
            text="Back",
            width=20, bg='#79C7C5', fg='#000E19',
            command=lambda: master.switch(Menu))
        button3.pack(padx=10, pady=10)
        
class File_Write(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg="#000E19")

        def validate():
            def write(name, kcal, protein, carb, fat):
                file = open("food_nutrients.txt", "a")
                productValue = "%s,%s,%s,%s,%s" % (
                    name, kcal, protein, carb, fat)
                file.write("\n" + productValue)
                file.close()

            error = False
            try:
                name = int(nameEntry.get())
                error = True
            except BaseException:
                name = nameEntry.get()
            try:
                kcal = (kcalEntry.get())
                protein = (proteinEntry.get())
                carb = (carbEntry.get())
                fat = (fatEntry.get())
            except BaseException:
                error = True
            if error == True:
                messagebox.showerror("Error", "Please enter correct data!")
            else:
                write(name, kcal, protein, carb, fat)
                tk.messagebox.showinfo("Success", "Food added to the database!")
                master.switch(Menu)

        label = Label(self, text="Enter the product name and its nutritional "
                      "values per 100 gram", bg="#000E19", fg="white")
        label.pack()
        label1 = Label(self, text="Name:", bg="#000E19", fg="white")
        label1.pack()
        nameEntry = Entry(self, width=20, bg="#79C7C5", fg="#000E19")
        nameEntry.pack()

        label2 = Label(self, text="Calories:", bg="#000E19", fg="white")
        label2.pack()
        kcalEntry = Entry(self, width=20, bg="#79C7C5", fg="#000E19")
        kcalEntry.pack()

        label3 = Label(self, text="Protein:", bg="#000E19", fg="white")
        label3.pack()
        proteinEntry = Entry(self, width=20, bg="#79C7C5", fg="#000E19")
        proteinEntry.pack()

        label4 = Label(self, text="Carbohydrates:", bg="#000E19", fg="white")
        label4.pack()
        carbEntry = Entry(self, width=20, bg="#79C7C5", fg="#000E19")
        carbEntry.pack()

        label5 = Label(self, text="Fat:", bg="#000E19", fg="white")
        label5.pack()
        fatEntry = Entry(self, width=20, bg="#79C7C5", fg="#000E19")
        fatEntry.pack()

        submit = Button(self, text="Submit", width=8, command=validate)
        submit.pack(padx=10, pady=10)

        button3 = Button(
            self,
            text="Back",
            width=20, bg='#79C7C5', fg='#000E19',
            command=lambda: master.switch(Menu))
        button3.pack(padx=10, pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()