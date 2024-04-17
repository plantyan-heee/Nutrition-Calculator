import main
from tkinter import messagebox
from tkinter import *
productList = {}

function = main


class App(Tk):

    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.title("App calculating nutrition values")
        self.switch(Menu)
        self.geometry('350x350')
        self.config(bg="black")

    def switch(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class Menu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg="black")

        label = Label(
            self,
            text="Nutrition Calculator V0.3.1\n Choose an option.",
            bg="black",
            fg="grey")
        label.pack()
        button = Button(self, text="Calculator", width=20,
                        command=lambda: master.switch(Calculator))
        button.pack(padx=10, pady=10)
        button2 = Button(self, text="Add a food", width=20,
                         command=lambda: master.switch(File_Write))
        button2.pack()
        button3 = Button(self, text="Exit", width=20, command=self.close)
        button3.pack(padx=10, pady=10)

    def close(self):
        self.destroy()
        exit()


class Calculator(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg="black")

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
                outcome = "Your product provided you with : \n %d kcal \n "\
                    "%d protein \n %d carbs \n %d fat"\
                    % (kcalValue, proteinValue, carbValue, fatValue)
            else:
                outcome = "Sorry, but we don't have this food in our database: %s, but you can add it! :)" % (
                    product)
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
                gram = int(entryGram.get())
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
            bg="black",
            fg="white")
        label.pack()
        # user input, food
        label2 = Label(self, text="Name: ", bg="black", fg="white")
        label2.pack()
        entryProduct = Entry(self, width=20, bg="#000621", fg="white")
        entryProduct.pack()
        # user input, amount
        label3 = Label(self, text="Amount per 100g: ", bg="black", fg="white")
        label3.pack()
        entryGram = Entry(self, width=20, bg="#000621", fg="white")
        entryGram.pack()
        # submit
        submit = Button(self, text="Submit", width=8, command=on_click)
        submit.pack(padx=10, pady=10)
        # output
        label4 = Label(
            self,
            text="These are the nutrition values:",
            bg="black",
            fg="white")
        label4.pack()
        output = Text(self, width=20, height=6, wrap=WORD, bg="#000621", fg="white")
        output.pack()
        # going back to menu
        self.button = Button(
            self,
            text="Back",
            width=8,
            command=lambda: master.switch(Menu))
        self.button.pack(padx=10, pady=10)


class File_Write(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg="black")

        def validate():
            def write(name, kcal, protein, carb, fat):
                file = open("food_nutrients.txt", "a")
                productValue = "%s,%s:%s:%s:%s" % (
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
                kcal = int(kcalEntry.get())
                protein = int(proteinEntry.get())
                carb = int(carbEntry.get())
                fat = int(fatEntry.get())
            except BaseException:
                error = True
            if error == True:
                messagebox.showerror("Error", "Please enter correct data!")
            else:
                write(name, kcal, protein, carb, fat)

        label = Label(self, text="Enter the product name and its nutritional "
                      "values per 100 gram", bg="black", fg="white")
        label.pack()
        label1 = Label(self, text="Name:", bg="black", fg="white")
        label1.pack()
        nameEntry = Entry(self, width=20, bg="#000621", fg="white")
        nameEntry.pack()

        label2 = Label(self, text="Calories:", bg="black", fg="white")
        label2.pack()
        kcalEntry = Entry(self, width=20, bg="#000621", fg="white")
        kcalEntry.pack()

        label3 = Label(self, text="Protein:", bg="black", fg="white")
        label3.pack()
        proteinEntry = Entry(self, width=20, bg="#000621", fg="white")
        proteinEntry.pack()

        label4 = Label(self, text="Carbohydrates:", bg="black", fg="white")
        label4.pack()
        carbEntry = Entry(self, width=20, bg="#000621", fg="white")
        carbEntry.pack()

        label5 = Label(self, text="Fat:", bg="black", fg="white")
        label5.pack()
        fatEntry = Entry(self, width=20, bg="#000621", fg="white")
        fatEntry.pack()

        submit = Button(self, text="Submit", width=8, command=validate)
        submit.pack(padx=10, pady=10)

        button3 = Button(
            self,
            text="Back",
            width=20,
            command=lambda: master.switch(Menu))
        button3.pack(padx=10, pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()