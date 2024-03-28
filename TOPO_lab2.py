import myModule
import unittest

class MyTests(unittest.TestCase):

    # Тесты для сортировки по возрастанию
    def testSortAscNoAction(self):
        sequence = [0, 1, 2, 3]
        params = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        paramNumber = 2

        expectedResult = [0, 1, 2, 3]

        result = myModule.SortAsc(params, sequence, paramNumber)

        self.assertEqual(result, expectedResult)


    def testSortAscOneParam(self):
        sequence = [0]
        params = [[1, 2, 3]]
        paramNumber = 2

        expectedResult = [0]

        result = myModule.SortAsc(params, sequence, paramNumber)

        self.assertEqual(result, expectedResult)


    def testSortAscReverse(self):
        sequence = [0, 1, 2, 3]
        params = [[10, 11, 12], [7, 8, 9], [4, 5, 6], [1, 2, 3]]
        paramNumber = 2

        expectedResult = [3, 2, 1, 0]

        result = myModule.SortAsc(params, sequence, paramNumber)

        self.assertEqual(result, expectedResult)


    def testSortAscMixed(self):
        sequence = [0, 1, 2, 3]
        params = [[7, 8, 9], [4, 5, 6], [10, 11, 12], [1, 2, 3]]
        paramNumber = 2

        expectedResult = [3, 1, 0, 2]

        result = myModule.SortAsc(params, sequence, paramNumber)

        self.assertEqual(result, expectedResult)


    def testSortAscEqual(self):
        sequence = [0, 1, 2, 3]
        params = [[7, 8, 5], [4, 5, 5], [10, 11, 5], [1, 2, 5]]
        paramNumber = 2

        expectedResult = [0, 1, 2, 3]

        result = myModule.SortAsc(params, sequence, paramNumber)

        self.assertEqual(result, expectedResult)
        

    # Тесты для сортировки по убыванию
    def testSortDescNoAction(self):
        sequence = [0, 1, 2, 3]
        params = [[10, 11, 12], [7, 8, 9], [4, 5, 6], [1, 2, 3]]
        paramNumber = 2

        expectedResult = [0, 1, 2, 3]

        result = myModule.SortDesc(params, sequence, paramNumber)

        self.assertEqual(result, expectedResult)
    

    def testSortDescOneParam(self):
        sequence = [0]
        params = [[1, 2, 3]]
        paramNumber = 2

        expectedResult = [0]

        result = myModule.SortDesc(params, sequence, paramNumber)

        self.assertEqual(result, expectedResult)


    def testSortDescReverse(self):
        sequence = [0, 1, 2, 3]
        params = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        paramNumber = 2

        expectedResult = [3, 2, 1, 0]

        result = myModule.SortDesc(params, sequence, paramNumber)

        self.assertEqual(result, expectedResult)


    def testSortDescMixed(self):
        sequence = [0, 1, 2, 3]
        params = [[7, 8, 9], [4, 5, 6], [10, 11, 12], [1, 2, 3]]
        paramNumber = 2

        expectedResult = [2, 0, 1, 3]

        result = myModule.SortDesc(params, sequence, paramNumber)

        self.assertEqual(result, expectedResult)


    def testSortDescEqual(self):
        sequence = [0, 1, 2, 3]
        params = [[7, 8, 5], [4, 5, 5], [10, 11, 5], [1, 2, 5]]
        paramNumber = 2

        expectedResult = [0, 1, 2, 3]

        result = myModule.SortDesc(params, sequence, paramNumber)

        self.assertEqual(result, expectedResult)

if __name__ == '__main__':
    unittest.main()
