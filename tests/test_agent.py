import unittest
from src.agent import run

class AgentTests(unittest.TestCase):
    def test_constant(self):
        r = run([1,1,1,1])
        self.assertAlmostEqual(r["spectrum"][0],4)
        self.assertAlmostEqual(r["spectrum"][1],0)
    def test_identity(self):
        self.assertEqual(run([1,2])["input_id"],run([1,2])["input_id"])
        self.assertNotEqual(run([1,2])["input_id"],run([2,1])["input_id"])
    def test_empty(self):
        with self.assertRaises(ValueError): run([])
