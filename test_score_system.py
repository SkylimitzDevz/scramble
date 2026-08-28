from utils import find_best_match

dummy_data_same = [
    {
        "word": "snow",
        "score": 0
    },{
        "word": "fill",
        "score": 0
    },{
        "word": "wide",
        "score": 0
    }
]

dummy_data_max_1 = [
    {
        "word": "snow",
        "score": 0
    },{
        "word": "fill",
        "score": 3
    },{
        "word": "wide",
        "score": 2
    }
]


def test_best_word_finder():
    assert find_best_match(dummy_data_same) == [
        {
            "word": "snow",
            "score": 0
        },{
            "word": "fill",
            "score": 0
        },{
            "word": "wide",
            "score": 0
        }
    ]

def test_2():
    assert find_best_match(dummy_data_max_1) == {
        "word": "fill",
        "score": 3
    }

