import numpy as np
import pytest

from maxima import find_maxima

test_cases = [([0, 1, 2, 1, 2, 1, 0], [2, 4]),
              ([-i**2 for i in range(-3, 4)], [3]),
              ([np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)], [16,78]),
              ([4, 2, 1, 3, 1, 2], [0, 3, 5]),
              ([4, 2, 1, 3, 1, 5], [0, 3, 5]),
              ([4, 2, 1, 3, 1], [0, 3]),
              ]

@pytest.mark.parametrize("input, expected", test_cases)
def test_maxima(input, expected):
    #Given:
    #input
    
    #When:
    output = find_maxima(input)
    
    #Then:
    assert output == expected

# additional tests for
# - max on both borders
#   x = [4, 2, 1, 3, 1, 2]
# - max on both borders, absolute max on right border
#   x = [4, 2, 1, 3, 1, 5]
# - one max (absolute) on left border
#   x = [4, 2, 1, 3, 1]
# - plateau
#   x = [1, 2, 2, 1]
#   (decide for a sensible output in this case)
# - test cases for plateau
#   x = [1, 2, 2, 3, 1]
#   x = [1, 3, 2, 2, 1]
#   x = [3, 2, 2, 3]
