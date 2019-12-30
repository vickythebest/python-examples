from solution_1 import solution

def test_solution():
    list_in=[10,15,3,7]
    k=17
    expected_out =True

    result = solution(list_in, k)

    assert result == expected_out