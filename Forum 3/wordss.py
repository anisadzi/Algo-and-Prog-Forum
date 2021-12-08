#driverr


from listss import GroceryStoreAD



#funtionss
def thelistAD() :
    listAD = []
    quantityAD = eval(input("How many items will you order today?")) #quantity of items
       
    while quantityAD < 1 :
        print("Number of items must be at least 1.") #q must atleast be 1
        quantityAD = eval(input("How many items will you order today?"))


    else :
        for i in range (quantityAD) :
            nameAD = input("Enter food:") #enter food
            amountAD = eval(input("Enter amount of pounds:"))

            while amountAD <= 0 :
                print("Amount of pounds must be greater than 0.") #pounds greater thna 0
                amountAD = eval(input("Enter amount of pounds:"))


            itemsAD = GroceryStoreAD (nameAD, amountAD)
            listAD.append(itemsAD)

    return listAD



#put content
def display(item_listAD) :
    print("Here's a summary of the items purchased:")
    for items in item_listAD :
        print(items.__str__())



#total price
def total_amount(item_listAD) :
        Total = 0
        for item in item_listAD :
            Total += item.TotalCostAD
            print(f"Total: $", (Total))
        


#put together before functions
def putall():
    listAD = thelistAD()
    total_amount(listAD)

putall()

