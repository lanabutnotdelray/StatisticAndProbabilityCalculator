import unittest
import probability


class TestStatistic(unittest.TestCase):

    def test_change_data_x(self):
        testing = probability.Statistic()
        testing.change_data([1], [1])
        self.assertEqual(testing.nlist, [1])
        self.assertEqual(testing.xlist, [1])

        testing = probability.Statistic()
        testing.change_data([5, 10], [2, 3])
        self.assertEqual(testing.nlist, [2, 3])
        self.assertEqual(testing.xlist, [5, 10])

        testing.change_data([5, 10], [2, 3])
        self.assertRaises(ValueError, testing.change_data, [2], [3, 6])

        testing.change_data([5, 10], [2, 3])
        self.assertRaises(ValueError, testing.change_data, [5, 10], [-2, 3])

    def test_mathexpect(self):
        testing = probability.Statistic()
        testing.change_data([5, 10], [2, 3])
        self.assertEqual(testing.mathexpect(), 8)

        testing = probability.Statistic()
        testing.change_data([10], [2])
        self.assertEqual(testing.mathexpect(), 10)

    def test_squaremathexpectt(self):
        testing = probability.Statistic()
        testing.change_data([5, 10], [2, 3])
        self.assertEqual(testing.squaremathexpect(), 70)

        testing = probability.Statistic()
        testing.change_data([1], [1])
        self.assertEqual(testing.squaremathexpect(), 1)

    def test_dispersion(self):
        testing = probability.Statistic()
        testing.change_data([1], [1])
        self.assertEqual(testing.dispersion(), 0)

    def test_sigma(self):
        testing = probability.Statistic()
        testing.change_data([1], [1])
        self.assertEqual(testing.sigma(), 0)

    def test_get_data(self):
        testing = probability.Statistic()
        testing.change_data([5, 10], [2, 3])
        self.assertEqual(testing.get_data(), [[5, 10], [2, 3]])

    def test_get_x_prabability(self):
        testing = probability.Statistic()
        testing.change_data([5, 10], [2, 3])
        self.assertEqual(testing.get_x_prabability(5), 2)

    def test_fashion(self):
        testing = probability.Statistic()
        testing.change_data([5, 10], [2, 3])
        self.assertEqual(testing.fashion(), 10)

        testing = probability.Statistic()
        testing.change_data([170, 60], [1, 30])
        self.assertEqual(testing.fashion(), 60)


class TestProbability(unittest.TestCase):

    def test_change_data_x(self):
        testing = probability.Probability()
        testing.change_data([1], [1])
        self.assertEqual(testing.plist, [1])
        self.assertEqual(testing.xlist, [1])

        testing = probability.Probability()
        testing.change_data([5, 10], [0.5, 0.5])
        self.assertEqual(testing.xlist, [5, 10])
        self.assertEqual(testing.plist, [0.5, 0.5])

        testing.change_data([5, 10], [0.3, 0.7])
        self.assertRaises(ValueError, testing.change_data, [2], [0.3, 0.7])

        testing.change_data([5, 10], [0.3, 0.7])
        self.assertRaises(ValueError, testing.change_data, [5, 10], [-0.2, 1.2])

        testing.change_data([5, 10], [0.3, 0.7])
        self.assertRaises(ValueError, testing.change_data, [5, 10], [0.01, 1.2])

        testing.change_data([5, 10], [0.3, 0.7])
        self.assertRaises(ValueError, testing.change_data, [5, 10], [0.2, 0.2])

    def test_mathexpect(self):
        testing = probability.Probability()
        testing.change_data([5, 10], [0.2, 0.8])
        self.assertEqual(testing.mathexpect(), 9)

        testing = probability.Probability()
        testing.change_data([10], [1])
        self.assertEqual(testing.mathexpect(), 10)

    def test_squaremathexpectt(self):
        testing = probability.Probability()
        testing.change_data([5, 10], [0.2, 0.8])
        self.assertEqual(testing.squaremathexpect(), 85)

        testing = probability.Probability()
        testing.change_data([1], [1])
        self.assertEqual(testing.squaremathexpect(), 1)

    def test_dispersion(self):
        testing = probability.Probability()
        testing.change_data([5, 10], [0.2, 0.8])
        self.assertEqual(testing.dispersion(), 4)

    def test_sigma(self):
        testing = probability.Probability()
        testing.change_data([5, 10], [0.2, 0.8])
        self.assertEqual(testing.sigma(), 2)

    def test_get_data(self):
        testing = probability.Probability()
        testing.change_data([5, 10], [0, 1])
        self.assertEqual(testing.get_data(), [[5, 10], [0, 1]])

    def test_get_x_prabability(self):
        testing = probability.Statistic()
        testing.change_data([5, 10], [0.2, 0.8])
        self.assertEqual(testing.get_x_prabability(5), 0.2)


if __name__ == '__main__':
    unittest.main()