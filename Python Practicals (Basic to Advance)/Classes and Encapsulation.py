# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:11:42 2020

@author: EdUnbox
"""

#Classes and Encapsualtion:

class Computer:
    def __init__(self):
        self.__maxprice = 900
        self.__minprice = 500 	

    def getMaxPrice(self):   
    	return("Selling Price: {}".format(self.__maxprice))
	
    def getMinPrice(self):    
    	return("Selling Price: {}".format(self.__minprice))    

    def sell(self):
    	self.__sellPrice = self.__maxprice + self.__minprice
    	return("Total Selling Price: {}".format(self.__sellPrice))
    	
    def setMaxPrice(self, price):
        self.__maxprice = price
        return("Maximum Selling Price: {}".format(self.__maxprice))

if __name__ == '__main__':

	c = Computer()
	print(c.getMaxPrice())
	print(c.getMinPrice())
	print(c.sell())
	# using setter function
	print(c.setMaxPrice(5000))

"""
# This is a Private Class

class Computer:
	def __init__(self):

		self.maxprice = 900
		self._minprice = 500
		self.__price = 10000 	  

	def __getMaxPrice(self):   
		return("Selling Price: {}".format(self.maxprice))

	def __getMinPrice(self):    
		return("Selling Price: {}".format(self._minprice))    

	def __sell(self):
		sellPrice = self.maxprice + self._minprice
		return("Total Selling Price: {}".format(sellPrice))

	def __setMaxPrice(self, price):
		self.maxprice = price
		return("Maximum Selling Price: {}".format(self.maxprice))
	   
# Outside class  
        
if __name__ == '__main__':
	c = Computer()
	print(c.maxprice)
	print(c._minprice)
	print(c.__price)
	print(c.__getMaxPrice())
	print(c.__getMinPrice())
	print(c.__sell())
	print(c.__setMaxPrice(5000))

"""    