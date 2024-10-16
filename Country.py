#Class 1
class India():
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the most widely spoken language in India")
    def type(self):
        print("India is a developing country")

#Class 2
class Bangladesh():
    def capital(self):
        print("Dhaka is the capital of Bangaldesh")
    def language(self):
        print("Bangla is the most widely spoken language in Bangaldesh")
    def type(self):
        print("Bangaldesh is a developing country")

#Object Creation
objInd = India()
objBD = Bangladesh()

#Polymorphism
for country in (objInd, objBD):
    country.capital()
    country.language()
    country.type()
    print()