#the classs



#number 1
class GroceryStoreAD :
    def __init__(self, name, amount) :
        self.__nameAD   = name
        self.__amountAD = amount
        self.__priceperlbAD()
        self.TotalCostAD = self.__TotalCostsAD()



#thee getter
    def getpriceperlbAD(self) :
        return self.__price_per_lb

    def getTotalCostAD(self) :
        return self.TotalCostAD



#number 2
    def __priceperlbAD(self) :
        if self.__nameAD.lower()=="dry cured iberian ham":
            self.__price_per_lb = 177.80
        elif self.__nameAD.lower()=="wagyu steaks":
            self.__price_per_lb = 450.00
        elif self.__nameAD.lower()=="matsutake mushrooms":
            self.__price_per_lb = 272.00
        elif self.__nameAD.lower()=="kopi luwak coffee":
            self.__price_per_lb = 306.50
        elif self.__nameAD.lower()=="moose cheese":
            self.__price_per_lb = 487.20
        elif self.__nameAD.lower()=="white truffle":
            self.__price_per_lb = 3600.00
        elif self.__nameAD.lower()=="blue fin tuna":
            self.__price_per_lb = 3603.00
        elif self.__nameAD.lower()=="le bonnotte potatoes":
            self.__price_per_lb = 270.81

        else :
            self.__price_per_lb = 0



#number 3
    def __TotalCostsAD(self) :
        self.__priceperlbAD()
        self.TotalCostAD = self.__amountAD * self.__price_per_lb
        return self.TotalCostAD



#number 4
    def __str__(self) :
        self.__priceperlbAD()
        return f"Item: {self.__nameAD} \nAmount ordered: {self.__amountAD}pounds \nPrice per pound: ${self.__price_per_lb} \nPrice of order: ${self.TotalCostAD}"


    