# TODO: Add fixture with values already loaded
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
    assert linked_list.size() == 3


def test_insert_element_in_beginning(linked_list_with_elements):
    assert linked_list_with_elements.size() == 3
    assert linked_list_with_elements.insert(0, 0)
    assert linked_list_with_elements.get_element_at(0).element == 0
    assert linked_list_with_elements.get_element_at(1).element == 1
    assert linked_list_with_elements.get_element_at(2).element == 2
    assert linked_list_with_elements.get_element_at(3).element == 3
    assert linked_list_with_elements.size() == 4


def test_insert_element_in_second_position(linked_list_with_elements):
    assert linked_list_with_elements.size() == 3
    assert linked_list_with_elements.insert(0, 1)
    assert linked_list_with_elements.get_element_at(0).element == 1
    assert linked_list_with_elements.get_element_at(1).element == 0
    assert linked_list_with_elements.get_element_at(2).element == 2
    assert linked_list_with_elements.get_element_at(3).element == 3
    assert linked_list_with_elements.size() == 4


def test_insert_element_in_third_position(linked_list_with_elements):
    assert linked_list_with_elements.size() == 3
    assert linked_list_with_elements.insert(0, 2)
    assert linked_list_with_elements.get_element_at(0).element == 1
    assert linked_list_with_elements.get_element_at(1).element == 2
    assert linked_list_with_elements.get_element_at(2).element == 0
    assert linked_list_with_elements.get_element_at(3).element == 3
    assert linked_list_with_elements.size() == 4


def test_insert_element_in_forth_position(linked_list_with_elements):
    assert linked_list_with_elements.size() == 3
    assert linked_list_with_elements.insert(0, 3)
    assert linked_list_with_elements.get_element_at(0).element == 1
    assert linked_list_with_elements.get_element_at(1).element == 2
    assert linked_list_with_elements.get_element_at(2).element == 3
    assert linked_list_with_elements.get_element_at(3).element == 0
    assert linked_list_with_elements.size() == 4


def test_try_insert_element_in_invalid_position_before_begin(linked_list_with_elements):
    assert not linked_list_with_elements.insert(0, -1)


def test_try_insert_element_in_invalid_position_after_end(linked_list_with_elements):
    assert not linked_list_with_elements.insert(0, 99)


def test_get_element_at_first_position(linked_list_with_elements):
    assert linked_list_with_elements.get_element_at(0).element == 1


def test_get_element_at_second_position(linked_list_with_elements):
    assert linked_list_with_elements.get_element_at(1).element == 2


def test_get_element_at_third_position(linked_list_with_elements):
    assert linked_list_with_elements.get_element_at(2).element == 3


def test_try_get_element_at_before_beginning(linked_list_with_elements):
    assert linked_list_with_elements.get_element_at(-1) is None


def test_remove_first_element(linked_list_with_elements):
    assert linked_list_with_elements.size() == 3
    assert linked_list_with_elements.remove(1) == 1
    assert linked_list_with_elements.get_element_at(0).element == 2
    assert linked_list_with_elements.get_element_at(1).element == 3
    assert linked_list_with_elements.size() == 2


def test_remove_second_element(linked_list_with_elements):
    assert linked_list_with_elements.size() == 3
    assert linked_list_with_elements.remove(2) == 2
    assert linked_list_with_elements.get_element_at(0).element == 1
    assert linked_list_with_elements.get_element_at(1).element == 3
    assert linked_list_with_elements.size() == 2


def test_remove_third_element(linked_list_with_elements):
    assert linked_list_with_elements.size() == 3
    assert linked_list_with_elements.remove(3) == 3
    assert linked_list_with_elements.get_element_at(0).element == 1
    assert linked_list_with_elements.get_element_at(1).element == 2
    assert linked_list_with_elements.size() == 2


def test_try_remove_non_existing_element_should_return_none(linked_list_with_elements):
    assert linked_list_with_elements.remove(99) is None
    assert linked_list_with_elements.get_element_at(0).element == 1
    assert linked_list_with_elements.get_element_at(1).element == 2
    assert linked_list_with_elements.get_element_at(2).element == 3
    assert linked_list_with_elements.size() == 3


def test_index_of(linked_list_with_elements):
    assert linked_list_with_elements.index_of(1) == 0
    assert linked_list_with_elements.index_of(2) == 1
    assert linked_list_with_elements.index_of(3) == 2


def test_index_of_with_non_existing_value(linked_list_with_elements):
    assert linked_list_with_elements.index_of(99) == -1


def test_remove_at_first_element(linked_list_with_elements):
    assert linked_list_with_elements.size() == 3
    assert linked_list_with_elements.remove_at(0) == 1
    assert linked_list_with_elements.size() == 2


def test_remove_at_second_element(linked_list_with_elements):
    assert linked_list_with_elements.size() == 3
    assert linked_list_with_elements.remove_at(1) == 2
    assert linked_list_with_elements.size() == 2


def test_remove_at_third_element(linked_list_with_elements):
    assert linked_list_with_elements.size() == 3
    assert linked_list_with_elements.remove_at(2) == 3
    assert linked_list_with_elements.size() == 2


def test_remove_at_invalid_element_before_beginning(linked_list_with_elements):
    assert linked_list_with_elements.size() == 3
    assert linked_list_with_elements.remove_at(-1) is None
    assert linked_list_with_elements.size() == 3


def test_remove_at_invalid_element_after_end(linked_list_with_elements):
    assert linked_list_with_elements.size() == 3
    assert linked_list_with_elements.remove_at(99) is None
    assert linked_list_with_elements.size() == 3


def test_is_empty(linked_list):
    assert linked_list.is_empty()


def test_is_not_empty(linked_list_with_elements):
    assert not linked_list_with_elements.is_empty()


def test_size_when_empty(linked_list):
    assert linked_list.size() == 0


def test_size_when_not_empty(linked_list_with_elements):
    assert linked_list_with_elements.size() == 3


def test_to_string(linked_list_with_elements):
    assert linked_list_with_elements.to_string() == '1,2,3'


def test_to_string_when_empty(linked_list):
    assert linked_list.to_string() == ''