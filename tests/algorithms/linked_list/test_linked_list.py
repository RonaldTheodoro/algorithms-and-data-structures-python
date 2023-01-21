import pytest


@pytest.fixture
def linked_list_with_elements(linked_list):
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    return linked_list


def test_push_element(linked_list):
    assert linked_list.is_empty()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    assert len(linked_list) == 3


def test_insert_element_in_beginning(linked_list_with_elements):
    assert len(linked_list_with_elements) == 3
    assert linked_list_with_elements.insert(0, 0)
    assert linked_list_with_elements[0] == 0
    assert linked_list_with_elements[1] == 1
    assert linked_list_with_elements[2] == 2
    assert linked_list_with_elements[3] == 3
    assert len(linked_list_with_elements) == 4


def test_insert_element_in_second_position(linked_list_with_elements):
    assert len(linked_list_with_elements) == 3
    assert linked_list_with_elements.insert(0, 1)
    assert linked_list_with_elements[0] == 1
    assert linked_list_with_elements[1] == 0
    assert linked_list_with_elements[2] == 2
    assert linked_list_with_elements[3] == 3
    assert len(linked_list_with_elements) == 4


def test_insert_element_in_third_position(linked_list_with_elements):
    assert len(linked_list_with_elements) == 3
    assert linked_list_with_elements.insert(0, 2)
    assert linked_list_with_elements[0] == 1
    assert linked_list_with_elements[1] == 2
    assert linked_list_with_elements[2] == 0
    assert linked_list_with_elements[3] == 3
    assert len(linked_list_with_elements) == 4


def test_insert_element_in_forth_position(linked_list_with_elements):
    assert len(linked_list_with_elements) == 3
    assert linked_list_with_elements.insert(0, 3)
    assert linked_list_with_elements[0] == 1
    assert linked_list_with_elements[1] == 2
    assert linked_list_with_elements[2] == 3
    assert linked_list_with_elements[3] == 0
    assert len(linked_list_with_elements) == 4


def test_try_insert_element_in_invalid_position_before_begin(
    linked_list_with_elements,
):
    assert not linked_list_with_elements.insert(0, -1)


def test_try_insert_element_in_invalid_position_after_end(
    linked_list_with_elements,
):
    assert not linked_list_with_elements.insert(0, 99)


def test_get_element_at_first_position(linked_list_with_elements):
    assert linked_list_with_elements[0] == 1


def test_get_element_at_second_position(linked_list_with_elements):
    assert linked_list_with_elements[1] == 2


def test_get_element_at_third_position(linked_list_with_elements):
    assert linked_list_with_elements[2] == 3


def test_try_get_element_at_before_beginning(linked_list_with_elements):
    assert linked_list_with_elements.get_element_at(-1) is None


def test_get_last_element_with_reverse_index(linked_list_with_elements):
    # TODO: Get last element
    pass


def test_get_element_out_off_range(linked_list_with_elements):
    with pytest.raises(IndexError):
        linked_list_with_elements[-50]


def test_remove_first_element(linked_list_with_elements):
    assert len(linked_list_with_elements) == 3
    assert linked_list_with_elements.remove(1) == 1
    assert linked_list_with_elements[0] == 2
    assert linked_list_with_elements[1] == 3
    assert len(linked_list_with_elements) == 2


def test_remove_second_element(linked_list_with_elements):
    assert len(linked_list_with_elements) == 3
    assert linked_list_with_elements.remove(2) == 2
    assert linked_list_with_elements[0] == 1
    assert linked_list_with_elements[1] == 3
    assert len(linked_list_with_elements) == 2


def test_remove_third_element(linked_list_with_elements):
    assert len(linked_list_with_elements) == 3
    assert linked_list_with_elements.remove(3) == 3
    assert linked_list_with_elements[0] == 1
    assert linked_list_with_elements[1] == 2
    assert len(linked_list_with_elements) == 2


def test_try_remove_non_existing_element_should_return_none(
    linked_list_with_elements,
):
    assert linked_list_with_elements.remove(99) is None
    assert linked_list_with_elements[0] == 1
    assert linked_list_with_elements[1] == 2
    assert linked_list_with_elements[2] == 3
    assert len(linked_list_with_elements) == 3


def test_index(linked_list_with_elements):
    assert linked_list_with_elements.index(1) == 0
    assert linked_list_with_elements.index(2) == 1
    assert linked_list_with_elements.index(3) == 2


def test_index_with_non_existing_value(linked_list_with_elements):
    assert linked_list_with_elements.index(99) == -1


def test_remove_at_first_element(linked_list_with_elements):
    assert len(linked_list_with_elements) == 3
    assert linked_list_with_elements.remove_at(0) == 1
    assert len(linked_list_with_elements) == 2


def test_remove_at_second_element(linked_list_with_elements):
    assert len(linked_list_with_elements) == 3
    assert linked_list_with_elements.remove_at(1) == 2
    assert len(linked_list_with_elements) == 2


def test_remove_at_third_element(linked_list_with_elements):
    assert len(linked_list_with_elements) == 3
    assert linked_list_with_elements.remove_at(2) == 3
    assert len(linked_list_with_elements) == 2


def test_remove_at_invalid_element_before_beginning(linked_list_with_elements):
    assert len(linked_list_with_elements) == 3
    assert linked_list_with_elements.remove_at(-1) is None
    assert len(linked_list_with_elements) == 3


def test_remove_at_invalid_element_after_end(linked_list_with_elements):
    assert len(linked_list_with_elements) == 3
    assert linked_list_with_elements.remove_at(99) is None
    assert len(linked_list_with_elements) == 3


def test_is_empty(linked_list):
    assert linked_list.is_empty()


def test_is_not_empty(linked_list_with_elements):
    assert not linked_list_with_elements.is_empty()


def test_size_when_empty(linked_list):
    assert len(linked_list) == 0


def test_size_when_not_empty(linked_list_with_elements):
    assert len(linked_list_with_elements) == 3


def test_str(linked_list_with_elements):
    assert str(linked_list_with_elements) == "1,2,3"


def test_str_when_empty(linked_list):
    assert str(linked_list) == ""


def test_bool(linked_list_with_elements):
    assert bool(linked_list_with_elements)


def test_bool_when_empty(linked_list):
    assert not bool(linked_list)


def test_head(linked_list_with_elements):
    assert linked_list_with_elements.head.element == 1


def test_head_empty(linked_list):
    assert linked_list.head is None


def test_convert_linked_list_to_list(linked_list_with_elements):
    assert list(linked_list_with_elements) == [1, 2, 3]


def test_convert_empty_linked_list_to_list(linked_list):
    assert list(linked_list) == []


def test_iterate_linked_list(linked_list_with_elements):
    for num, element in zip([1, 2, 3], linked_list_with_elements):
        assert num == element
