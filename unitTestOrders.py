import unittest
import orders as app

class TestMyApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app
    
    def test_show(self):
        lst = ["106", "107"]
        self.assertEqual(app.show(lst), "106, 107")

    def test_maxrnge(self):
        self.assertTrue(app.maxrnge(["106", "107"]))
        self.assertFalse(app.maxrnge(["106", "107", "108", "109", "110", "111", "112", "113", "114", "115"]))
        self.assertFalse(app.maxrnge(["106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117"]))
    
    def test_minrnge(self):
        self.assertTrue(app.minrnge(["106", "107"]))
        self.assertTrue(app.minrnge(["106", "107", "108", "109", "110", "111", "112", "113", "114", "115"]))
        self.assertFalse(app.minrnge([]))

    def test_ifexits(self):
        self.assertFalse(app.ifexits(["106", "107", "108", "109", "110", "111", "112", "113", "114", "115"],"115"))
        self.assertTrue(app.ifexits(["106", "107", "108", "109", "110", "111", "112", "113", "114", "115"],"456"))
        self.assertTrue(app.ifexits([],""))

if __name__ == '__main__':
    unittest.main()