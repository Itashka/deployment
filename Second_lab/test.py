def count_element(array, elem):
    """
    Возвращает количество вхождений элемента elem в последовательности array
    >>> count_element([1,1,1], 1)
    3
    >>> count_element([1,1,1], 3)
    0
    """
    return array.count(elem)

class TestClass:
    def test_one():
        assert count_element([1,1,1], 1) == 3


    def test_two():
        assert count_element([1,1,1], 3) == 0


    def test_empty():
        assert count_element([], 3) == 0
        