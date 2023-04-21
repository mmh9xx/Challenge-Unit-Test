import unittest
from datetime import datetime
#create a calculator class with add, subtract, multiply, and divide methods
class StockVisualizer:
    #symbol method
    def symbol(self, a):
        if len(a) == 0:
            raise ValueError("Not Enough Characters for a Stock Symbol")
        elif len(a) > 7:
            raise ValueError("Too Many Characters for a Stock Symbol")
        return a.upper()
    
    #chart method
    def chart(self, a):
        if (a != "1" and a != "2"):
            raise ValueError("You Must Choose Either 1 or 2")
        elif len(a) > 1:
            raise ValueError("You Have Entered too Many Characters")
        else:
            return a
    
    #timeseries method
    def timeseries(self, a):
        if (a != "1" and a != "2" and a != "3" and a != "4"):
            raise ValueError("You Must Choose Either 1, 2, 3, or 4")
        elif len(a) > 4:
            raise ValueError("You Have Entered too Many Characters")
        else:
            return a
    
    #start date method
    def startdate(self, a):
        format = "%Y-%M-%D"
        check = True
        try:
            check = bool(datetime.strptime(a, format))
        except ValueError:
            check = False

        if check == False:
            raise ValueError("Your Date is Not in the Correct Format")
        else:
            return a 
        
    def enddate(self, a):
        format = "%Y-%M-%D"
        check = True
        try:
            check = bool(datetime.strptime(a, format))
        except ValueError:
            check = False

        if check == False:
            raise ValueError("Your Date is Not in the Correct Format")
        else:
            return a 
    


class TestStockVisualizer(unittest.TestCase):
    def setUp(self):
        self.calc = StockVisualizer()

    def test_symbol(self):
        self.assertEqual(self.calc.symbol("aaa"), "AAA")
        self.assertEqual(self.calc.symbol("BbB"), "BBB")
        self.assertEqual(self.calc.symbol("Ccc"), "CCC")
        with self.assertRaises(ValueError):
            self.calc.symbol("aaaaaaaaa")

    def test_chart(self):
        self.assertEqual(self.calc.chart("1"), "1")
        self.assertEqual(self.calc.chart("2"), "2")
        with self.assertRaises(ValueError):
           self.calc.chart("3")

    def test_timeseries(self):
        self.assertEqual(self.calc.timeseries("1"), "1")
        self.assertEqual(self.calc.timeseries("2"), "2")
        self.assertEqual(self.calc.timeseries("3"), "3")
        self.assertEqual(self.calc.timeseries("4"), "4")
        with self.assertRaises(ValueError):
           self.calc.timeseries("5")

    def test_startdate(self):
        from datetime import datetime
        self.assertEqual(self.calc.startdate("2023-04-20"), "2023-04-20")
        self.assertEqual(self.calc.startdate("2023-04-19"), "2023-04-20")
        with self.assertRaises(ValueError):
           self.calc.startdate("3-4-2002")

    def test_enddate(self):
        from datetime import datetime
        self.assertEqual(self.calc.enddate("2023-04-20"), "2023-04-20")
        self.assertEqual(self.calc.enddate("2023-04-19"), "2023-04-20")
        with self.assertRaises(ValueError):
           self.calc.enddate("3-4-2002")


#dunder method
if __name__ == "__main__":
    unittest.main()