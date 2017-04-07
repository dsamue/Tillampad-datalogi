# test av unitest - David Samuelsson cmete 2

from program import *
import unittest

class Test(unittest.TestCase):
    def test_enkelt_program(self):
        for i in range (10):
            self.assertEqual(1+i,2)  #kollar att funktionen gör nåt gör va den ska (2-2 bör bli 0)


if __name__=='__main__':
    unittest.main(exit=False)  #Falsegrejen är tveksam men gör att man slipper felmeddelande om man inte anropar programet direkt 
        
