from utils import process_search_query



def test_query_processor():
    assert process_search_query("hello") == ["ehllo", "5"]
    assert process_search_query("lol") == ["llo", "3"]
    assert process_search_query("cook") == ["ckoo", "4"]
    assert process_search_query("cat") == ["act", "3"]
    assert process_search_query("hola") == ["ahlo", "4"]
