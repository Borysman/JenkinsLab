import unittest
import cherga as app

class TestMyApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app
    
    def test_show(self):
        lst = ["Valentyn", "Maksym"]
        self.assertEqual(app.show(lst), "Valentyn, Maksym")

    def test_maxrnge(self):
        self.assertTrue(app.maxrnge(["Valentyn", "Maksym"]))
        self.assertFalse(app.maxrnge(["Valentyn", "Maksym", "Petro", "Stepan", "Mykola", "Borys", "Semen", "Dmytro", "Taras", "Bulba"]))
        self.assertFalse(app.maxrnge(["Valentyn", "Maksym", "Petro", "Stepan", "Mykola", "Borys", "Semen", "Dmytro", "Taras", "Bulba", "Avgust", "Muhtar"]))
    
    def test_minrnge(self):
        self.assertTrue(app.minrnge(["Valentyn", "Maksym"]))
        self.assertTrue(app.minrnge(["Valentyn", "Maksym", "Petro", "Stepan", "Mykola", "Borys", "Semen", "Dmytro", "Taras", "Bulba"]))
        self.assertFalse(app.minrnge([]))

    def test_ifexits(self):
        self.assertFalse(app.ifexits(["Valentyn", "Maksym", "Petro", "Stepan", "Mykola"],"Valentyn"))
        self.assertTrue(app.ifexits(["Valentyn", "Maksym", "Petro", "Stepan", "Mykola"],"Badname"))
        self.assertTrue(app.ifexits([],""))

if __name__ == '__main__':
  
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner (output='test-reports'))
    # runner = xmlrunner.XMLTestRunner(output='test-reports')
    # unittest.main(TestRunner-runner)
    # unittest.main()