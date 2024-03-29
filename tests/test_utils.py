import pytest
from utils import *
import random

def test_sequence():
    assert sequence(1) == (1,)
    assert sequence("helloworld") == "helloworld"
    assert sequence({"hello":4, "world":5}) == ({"hello":4, "world":5},)
    assert sequence([1, 2, 3]) == [1, 2, 3]
    assert sequence((4, 5, 6)) == (4, 5, 6)
    assert sequence([(1, 2),(2, 3),(4, 5)]) == [(1, 2), (2, 3),(4, 5)]
    assert sequence(([1, 2],[3, 4],[5, 6])) == ([1, 2], [3, 4],[5, 6])

def test_removeall_list():
    assert removeall(4, []) == []
    assert removeall(4, [1, 2, 3, 4]) == [1, 2, 3]
    assert removeall(4, [4, 1, 4, 2, 3, 4, 4]) == [1, 2, 3]
    assert removeall(1, [2,3,4,5,6]) == [2,3,4,5,6]


def test_removeall_string():
    assert removeall('s', '') == ''
    assert removeall('s', 'This is a test. Was a test.') == 'Thi i a tet. Wa a tet.'
    assert removeall('a', 'artificial intelligence: a modern approach') == 'rtificil intelligence:  modern pproch'	


def test_unique():
    assert unique([1, 2, 3, 2, 1]) == [1, 2, 3]
    assert unique([1, 5, 6, 7, 6, 5]) == [1, 5, 6, 7]
    assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]	


def test_count():
    assert count([1, 2, 3, 4, 2, 3, 4]) == 7
    assert count("aldpeofmhngvia") == 14
    assert count([True, False, True, True, False]) == 3
    assert count([5 > 1, len("abc") == 3, 3+1 == 5]) == 2
    assert count("aima") == 4 	

def test_multimap():
    assert multimap([(1, 2),(1, 3),(1, 4),(2, 3),(2, 4),(4, 5)]) == \
        {1: [2, 3, 4], 2: [3, 4], 4: [5]}
    assert multimap([("a", 2), ("a", 3), ("a", 4), ("b", 3), ("b", 4), ("c", 5)]) == \
        {'a': [2, 3, 4], 'b': [3, 4], 'c': [5]}

def test_product():
    assert product([1, 2, 3, 4]) == 24
    assert product(list(range(1, 11))) == 3628800


def test_first():
    assert first('word') == 'w'
    assert first('') is None
    assert first('', 'empty') == 'empty'
    assert first([1, 2, 3, 4, 5]) == 1
    assert first([]) == None
    assert first(range(10)) == 0
    assert first(x for x in range(10) if x > 3) == 4
    assert first(x for x in range(10) if x > 100) is None
    assert first((1, 2, 3)) == 1
    assert first(range(2, 10)) == 2
    assert first([(1, 2),(1, 3),(1, 4)]) == (1, 2)
    assert first({1:"one", 2:"two", 3:"three"}) == 1


def test_is_in():
    e = []
    assert is_in(e, [1, e, 3]) is True
    assert is_in(e, [1, [], 3]) is False


def test_mode():
    assert mode([12, 32, 2, 1, 2, 3, 2, 3, 2, 3, 44, 3, 12, 4, 9, 0, 3, 45, 3]) == 3
    assert mode("absndkwoajfkalwpdlsdlfllalsflfdslgflal") == 'l'
    assert mode("artificialintelligence") == 'i'	


def test_powerset():
    assert powerset([1, 2, 3]) == [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]


def test_argminmax():
    assert argmin([-2, 1], key=abs) == 1
    assert argmin(['one', 'to', 'three'], key=len) == 'to'
    assert argmax([-2, 1], key=abs) == -2
    assert argmax(['one', 'to', 'three'], key=len) == 'three'


def test_histogram():
    assert histogram([1, 2, 4, 2, 4, 5, 7, 9, 2, 1]) == [(1, 2), (2, 3),
                                                         (4, 2), (5, 1),
                                                         (7, 1), (9, 1)]
    assert histogram([1, 2, 4, 2, 4, 5, 7, 9, 2, 1], 0, lambda x: x*x) == [(1, 2), (4, 3),
                                                                           (16, 2), (25, 1),
                                                                           (49, 1), (81, 1)]
    assert histogram([1, 2, 4, 2, 4, 5, 7, 9, 2, 1], 1) == [(2, 3), (4, 2),
                                                            (1, 2), (9, 1),
                                                            (7, 1), (5, 1)]


def test_dotproduct():
    assert dotproduct([1, 2, 3], [1000, 100, 10]) == 1230
    assert dotproduct([1, 2, 3], [0, 0, 0]) == 0


def test_element_wise_product():
    assert element_wise_product([1, 2, 5], [7, 10, 0]) == [7, 20, 0]
    assert element_wise_product([1, 6, 3, 0], [9, 12, 0, 0]) == [9, 72, 0, 0]


def test_matrix_multiplication():
    assert matrix_multiplication([[1, 2, 3],
                                  [2, 3, 4]],
                                 [[3, 4],
                                  [1, 2],
                                  [1, 0]]) == [[8, 8], [13, 14]]

    assert matrix_multiplication([[1, 2, 3],
                                  [2, 3, 4]],
                                 [[3, 4, 8, 1],
                                  [1, 2, 5, 0],
                                  [1, 0, 0, 3]],
                                 [[1, 2],
                                  [3, 4],
                                  [5, 6],
                                  [1, 2]]) == [[132, 176], [224, 296]]


def test_vector_to_diagonal():
    assert vector_to_diagonal([1, 2, 3]) == [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
    assert vector_to_diagonal([0, 3, 6]) == [[0, 0, 0], [0, 3, 0], [0, 0, 6]]


def test_vector_add():
    assert vector_add((0, 1), (8, 9)) == (8, 10)
    assert vector_add((1, 1, 1), (2, 2, 2)) == (3, 3, 3)


def test_scalar_vector_product():
    assert scalar_vector_product(2, [1, 2, 3]) == [2, 4, 6]
    assert scalar_vector_product(0, [9, 9, 9]) == [0, 0, 0]

def test_scalar_matrix_product():
    assert rounder(scalar_matrix_product(-5, [[1, 2], [3, 4], [0, 6]])) == [[-5, -10], [-15, -20],
                                                                            [0, -30]]
    assert rounder(scalar_matrix_product(0.2, [[1, 2], [2, 3]])) == [[0.2, 0.4], [0.4, 0.6]]


def test_inverse_matrix():
    assert rounder(inverse_matrix([[1, 0], [0, 1]])) == [[1, 0], [0, 1]]
    assert rounder(inverse_matrix([[2, 1], [4, 3]])) == [[1.5, -0.5], [-2.0, 1.0]]
    assert rounder(inverse_matrix([[4, 7], [2, 6]])) == [[0.6, -0.7], [-0.2, 0.4]]


def test_rounder():
    assert rounder(5.3330000300330) == 5.3330
    assert rounder(10.234566) == 10.2346
    assert rounder([1.234566, 0.555555, 6.010101]) == [1.2346, 0.5556, 6.0101]
    assert rounder([[1.234566, 0.555555, 6.010101],
                   [10.505050, 12.121212, 6.030303]]) == [[1.2346, 0.5556, 6.0101],
                                                          [10.5051, 12.1212, 6.0303]]


def test_num_or_str():
    assert num_or_str('42') == 42
    assert num_or_str(' 42x ') == '42x'


def test_normalize():
    assert normalize([1, 2, 1]) == [0.25, 0.5, 0.25]


def test_norm():
    assert isclose(norm([1, 2, 1], 1), 4)
    assert isclose(norm([3, 4], 2), 5)
    assert isclose(norm([-1, 1, 2], 4), 18**0.25)


def test_clip():
    assert [clip(x, 0, 1) for x in [-1, 0.5, 10]] == [0, 0.5, 1]


def test_sigmoid():
    assert isclose(0.5, sigmoid(0))
    assert isclose(0.7310585786300049, sigmoid(1))
    assert isclose(0.2689414213699951, sigmoid(-1))


def test_gaussian():
    assert gaussian(1,0.5,0.7) == 0.6664492057835993
    assert gaussian(5,2,4.5) == 0.19333405840142462
    assert gaussian(3,1,3) == 0.3989422804014327


def test_sigmoid_derivative():
    value = 1
    assert sigmoid_derivative(value) == 0

    value = 3
    assert sigmoid_derivative(value) == -6


def test_weighted_choice():
    choices = [('a', 0.5), ('b', 0.3), ('c', 0.2)]
    choice = weighted_choice(choices)
    assert choice in choices


def compare_list(x, y):
    return all([elm_x == y[i] for i, elm_x in enumerate(x)])


def test_distance():
    assert distance((1, 2), (5, 5)) == 5.0


def test_distance_squared():
    assert distance_squared((1, 2), (5, 5)) == 25.0


def test_vector_clip():
    assert vector_clip((-1, 10), (0, 0), (9, 9)) == (0, 9)


def test_turn_heading():
	assert turn_heading((0, 1), 1) == (-1, 0)
	assert turn_heading((0, 1), -1) == (1, 0)
	assert turn_heading((1, 0), 1) == (0, 1)
	assert turn_heading((1, 0), -1) == (0, -1)
	assert turn_heading((0, -1), 1) == (1, 0)
	assert turn_heading((0, -1), -1) == (-1, 0)
	assert turn_heading((-1, 0), 1) == (0, -1)
	assert turn_heading((-1, 0), -1) == (0, 1)


def test_turn_left():
	assert turn_left((0, 1)) == (-1, 0)


def test_turn_right():
	assert turn_right((0, 1)) == (1, 0)


def test_step():
    assert step(1) == step(0.5) == 1
    assert step(0) == 1
    assert step(-1) == step(-0.5) == 0


def test_Expr():
    A, B, C = symbols('A, B, C')
    assert symbols('A, B, C') == (Symbol('A'), Symbol('B'), Symbol('C'))
    assert A.op == repr(A) == 'A'
    assert arity(A) == 0 and A.args == ()

    b = Expr('+', A, 1)
    assert arity(b) == 2 and b.op == '+' and b.args == (A, 1)

    u = Expr('-', b)
    assert arity(u) == 1 and u.op == '-' and u.args == (b,)

    assert (b ** u) == (b ** u)
    assert (b ** u) != (u ** b)

    assert A + b * C ** 2 == A + (b * (C ** 2))

    ex = C + 1 / (A % 1)
    assert list(subexpressions(ex)) == [(C + (1 / (A % 1))), C, (1 / (A % 1)), 1, (A % 1), A, 1]
    assert A in subexpressions(ex)
    assert B not in subexpressions(ex)


def test_expr():
    P, Q, x, y, z, GP = symbols('P, Q, x, y, z, GP')
    assert (expr(y + 2 * x)
            == expr('y + 2 * x')
            == Expr('+', y, Expr('*', 2, x)))
    assert expr('P & Q ==> P') == Expr('==>', P & Q, P)
    assert expr('P & Q <=> Q & P') == Expr('<=>', (P & Q), (Q & P))
    assert expr('P(x) | P(y) & Q(z)') == (P(x) | (P(y) & Q(z)))
    # x is grandparent of z if x is parent of y and y is parent of z:
    assert (expr('GP(x, z) <== P(x, y) & P(y, z)')
            == Expr('<==', GP(x, z), P(x, y) & P(y, z)))

def test_min_priorityqueue():
    queue = PriorityQueue(f=lambda x: x[1])
    queue.append((1,100))
    queue.append((2,30))
    queue.append((3,50))
    assert queue.pop() == (2,30)
    assert len(queue) == 2
    assert queue[(3,50)] == 50
    assert (1,100) in queue
    del queue[(1,100)]
    assert (1,100) not in queue
    queue.extend([(1,100), (4,10)])
    assert queue.pop() == (4,10)
    assert len(queue) == 2

def test_max_priorityqueue():
    queue = PriorityQueue(order='max', f=lambda x: x[1])
    queue.append((1,100))
    queue.append((2,30))
    queue.append((3,50))
    assert queue.pop() == (1,100)

def test_priorityqueue_with_objects():
    class Test:
        def __init__(self, a, b):
            self.a = a
            self.b = b
        def __eq__(self, other):
            return self.a==other.a

    queue = PriorityQueue(f=lambda x: x.b)
    queue.append(Test(1,100))
    other = Test(1,10)
    assert queue[other]==100
    assert other in queue
    del queue[other]
    assert len(queue)==0

if __name__ == '__main__':
    pytest.main()
