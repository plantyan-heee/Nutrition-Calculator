productList = {}
import gui

def file_open():
    with open("food_nutrients.txt") as file:
        for row in file:
            if not row:
                continue
            else:
                product, kcal, protein, carb, fat = row.split(',')
                productList[product] = (product, kcal, protein, carb, fat)


def result(product, gram):            
    kcalValue = proteinValue = carbValue = fatValue = 0
    #check user value = database value
    if product in productList:
        (product, kcal, protein, carb, fat) = productList[product]
        #calculate
        kcalValue += gram * float(kcal)
        proteinValue += gram * float(protein)
        carbValue += gram * float(carb)
        fatValue += gram * float(fat)
        outcome = "Your product provided you with %d kcal, "\
           "%d protein, %d carbs oraz %d fat."\
           % (kcalValue, proteinValue, carbValue, fatValue)
    else: 
        outcome = "Sorry, but we don't have this food in our database: %s, but you can add it! :)"% (product)
    return outcome
