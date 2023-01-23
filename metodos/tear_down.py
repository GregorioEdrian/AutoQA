import unittest


class TearDown(unittest.TestCase):
    def tear_down(self):
        self.driver.implicitly_wait(3)
        self.driver.close()
