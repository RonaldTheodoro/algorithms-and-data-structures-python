from src.queue_hot_potato import hot_potato


def test_hot_potato():
    result = hot_potato(["John", "Jack", "Camila", "Ingrid", "Carl"], 7)
    assert result["eliminated"] == ["Camila", "Jack", "Carl", "Ingrid"]
    assert result["winner"] == "John"
