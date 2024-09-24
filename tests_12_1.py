import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name




class RunnerTest(unittest.TestCase):
    def test_walk(self):
        name = Runner("Marina")
        for i in range(10):
            name.walk()
        self.assertEqual(name.distance, 50)

    def test_run(self):
        name = Runner("Marina")
        for i in range(10):
            name.run()
        self.assertEqual(name.distance, 100)

    def test_challenge(self):
        name = Runner("Marina")
        for i in range(10):
            name.run()
        name2 = Runner("Urban")
        for i in range(10):
            name2.walk()
        self.assertNotEqual(name.distance, name2.distance)


