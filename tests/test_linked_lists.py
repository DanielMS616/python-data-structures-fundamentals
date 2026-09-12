from linked_lists.linked_list_append_o1 import LinkedList as AppendLinkedList
from linked_lists.linked_list_find_middle import LinkedList as MiddleLinkedList
from linked_lists.linked_list_remove_duplicates import (
    LinkedList as DuplicateLinkedList,
)
from linked_lists.linked_list_reverse import LinkedList as ReverseLinkedList


def test_append_preserves_order_and_tail_invariants():
    linked_list = AppendLinkedList()

    linked_list.append(5)
    linked_list.append(6)
    linked_list.append(7)

    assert str(linked_list) == "5->6->7"
    assert linked_list.head.data == 5
    assert linked_list.tail.data == 7
    assert linked_list.tail.next is None


def test_append_first_node_is_head_and_tail():
    linked_list = AppendLinkedList()

    linked_list.append(5)

    assert linked_list.head is linked_list.tail


def test_reverse_reverses_multiple_nodes():
    linked_list = ReverseLinkedList()

    for value in [5, 6, 7]:
        linked_list.append(value)

    linked_list.reverse()

    assert str(linked_list) == "7->6->5"


def test_reverse_handles_empty_list():
    linked_list = ReverseLinkedList()

    linked_list.reverse()

    assert linked_list.head is None


def test_reverse_handles_single_node():
    linked_list = ReverseLinkedList()

    linked_list.append(5)
    linked_list.reverse()

    assert str(linked_list) == "5"


def test_remove_duplicates_preserves_first_occurrence():
    linked_list = DuplicateLinkedList()

    for value in [5, 5, 6, 5, 7, 6]:
        linked_list.append(value)

    linked_list.remove_duplicates()

    assert str(linked_list) == "5->6->7"


def test_remove_duplicates_handles_empty_list():
    linked_list = DuplicateLinkedList()

    linked_list.remove_duplicates()

    assert linked_list.head is None


def test_find_middle_returns_middle_of_odd_length_list():
    linked_list = MiddleLinkedList()

    for value in [5, 6, 7]:
        linked_list.append(value)

    assert linked_list.find_middle() == 6


def test_find_middle_returns_second_middle_of_even_length_list():
    linked_list = MiddleLinkedList()

    for value in [5, 6, 7, 8]:
        linked_list.append(value)

    assert linked_list.find_middle() == 7


def test_find_middle_handles_empty_and_single_node_lists():
    linked_list = MiddleLinkedList()

    assert linked_list.find_middle() is None

    linked_list.append(5)

    assert linked_list.find_middle() == 5