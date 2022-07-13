import unittest

from main import get_direction_id, get_place_code, get_route_id

class TestMain(unittest.TestCase):
        
    def test_get_route_id(self):
        test = get_route_id("METRO Blue Line")
        result = "901"
        self.assertEqual(test, result)
        
        test = get_route_id("Route 6")
        result = "6"
        self.assertEqual(test, result)
        
        test = get_route_id("Route 475")
        result = "475"
        self.assertEqual(test, result)
        
        test = get_route_id("Airport Shuttle")
        result = "906"
        self.assertEqual(test, result)
        
    def test_get_direction_id(self):
        test = get_direction_id("north")
        result = "0"
        self.assertEqual(test,result)
        
        test = get_direction_id("East")
        result = "0"
        self.assertEqual(test,result)
        
        test = get_direction_id("SOUth")
        result = "1"
        self.assertEqual(test,result)
        
        test = get_direction_id("WEST")
        result = "1"
        self.assertEqual(test,result)
        
    def test_get_place_code(self):
        test = get_place_code("MSP Airport Terminal 1 - Lindbergh Station", "901", "1")
        result = "LIND"
        self.assertEqual(test, result)
        
        test = get_place_code("2nd Ave and Washington Ave", "475", "0")
        result = "WA2A"
        self.assertEqual(test, result)
        
        test = get_place_code("MSP Airport Terminal 2 - Humphrey Station", "906", "1")
        result = "HHTE"
        self.assertEqual(test, result)
        
        test = get_place_code("Southdale Transit Center", "6", "1")
        result = "SODA"
        self.assertEqual(test,result)