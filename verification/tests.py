"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [1, 2, 3],
            "answer": [1, 2, 3]
        },
        {
            "input": [1, [2, 2, 2], 4],
            "answer": [1, 2, 2, 2, 4]
        },
        {
            "input": [[[2]], [4, [5, 6, [6], 6, 6, 6], 7]],
            "answer": [2, 4, 5, 6, 6, 6, 6, 6, 7]
        },
        {
            "input": [1, [2, [3]]],
            "answer": [1, 2, 3]
        },
        {
            "input": [100, 200, 300, [400, 500]],
            "answer": [100, 200, 300, 400, 500]
        },
        {
            "input": [2, [2, [2, [2]]]],
            "answer": [2, 2, 2, 2]
        },
        {
            "input": [[[[3], 3], 3], 3],
            "answer": [3, 3, 3, 3]
        },
        {
            "input": [[7], [6], [7]],
            "answer": [7, 6, 7]
        }
    ],
    "Extra": [
        {
            "input": [11, 21, 31],
            "answer": [11, 21, 31]
        },
        {
            "input": [13, [23, 23, 23], 43],
            "answer": [13, 23, 23, 23, 43]
        },
        {
            "input": [[[22]], [44, [55, 66, [66], 66, 66, 66], 77]],
            "answer": [22, 44, 55, 66, 66, 66, 66, 66, 77]
        },
        {
            "input": [10, [20, [30]]],
            "answer": [10, 20, 30]
        },
        {
            "input": [1001, 2001, 3001, [4001, 5001]],
            "answer": [1001, 2001, 3001, 4001, 5001]
        },
        {
            "input": [20, [20, [20, [20]]]],
            "answer": [20, 20, 20, 20]
        },
        {
            "input": [[[[53], 43], 33], 23],
            "answer": [53, 43, 33, 23]
        },
        {
            "input": [[7007], [6006], [7007]],
            "answer": [7007, 6006, 7007]
        }
    ]
}
