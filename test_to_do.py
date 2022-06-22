"""
Test module for to_do.py
"""
import unittest
import to_do
from to_do import SUCCESS_STATUS, open_file

sample_json_data = "test_data/normal_data.json"
sample_empty_list = "test_data/empty_list_data.json"
# sample_empty_list = {
#     'meta': {'last_update': None},
#     'items': []
# }


class Test_to_do(unittest.TestCase):
    """
    Test the function add_item
    """

    def test_add_item_invalid_task_index_as_number(self):
        with self.assertRaises(TypeError):
            to_do.add_item(5, sample_json_data)

    def test_add_item_invalid_task_index_as_list(self):
        with self.assertRaises(TypeError):
            to_do.add_item([], sample_json_data)

    def test_add_item_success(self):
        self.assertEqual(to_do.add_item(
            'New Task', sample_json_data), SUCCESS_STATUS)

    """
    Test the function complete_item
    """

    def test_complete_item_invalid_task_index_as_number(self):
        with self.assertRaises(TypeError):
            to_do.complete_item(5, sample_json_data)

    def test_complete_item_invalid_task_index_as_list(self):
        with self.assertRaises(TypeError):
            to_do.complete_item([], sample_json_data)

    def test_complete_item_task_index_out_of_range(self):
        with self.assertRaises(ValueError):
            to_do.complete_item('8', sample_json_data)

    def test_complete_item_on_empty_list(self):
        with self.assertRaises(ValueError):
            to_do.complete_item('2', sample_empty_list)

    def test_complete_item_success(self):
        self.assertEqual(
            to_do.complete_item('3', sample_json_data),
            SUCCESS_STATUS
        )

    """
    Test the function incomplete_item
    """

    def test_incomplete_item_invalid_task_index_as_number(self):
        with self.assertRaises(TypeError):
            to_do.incomplete_item(5, sample_json_data)

    def test_incomplete_item_invalid_task_index_as_list(self):
        with self.assertRaises(TypeError):
            to_do.incomplete_item([], sample_json_data)

    def test_incomplete_item_task_index_out_of_range(self):
        with self.assertRaises(ValueError):
            to_do.incomplete_item('8', sample_json_data)

    def test_incomplete_item_on_empty_list(self):
        with self.assertRaises(ValueError):
            to_do.incomplete_item('2', sample_empty_list)

    def test_incomplete_item_success(self):
        self.assertEqual(
            to_do.incomplete_item('3', sample_json_data),
            SUCCESS_STATUS
        )

    """
    Test the function delete_item
    """

    def test_delete_item_invalid_task_index_as_number(self):
        with self.assertRaises(TypeError):
            to_do.delete_item(5, sample_json_data)

    def test_delete_item_invalid_task_index_as_list(self):
        with self.assertRaises(TypeError):
            to_do.delete_item([], sample_json_data)

    def test_delete_item_task_index_out_of_range(self):
        with self.assertRaises(ValueError):
            to_do.delete_item('8', sample_json_data)

    def test_delete_item_on_empty_list(self):
        with self.assertRaises(ValueError):
            to_do.delete_item('2', sample_empty_list)

    def test_delete_item_success(self):
        self.assertEqual(to_do.delete_item(
            '3', sample_json_data), SUCCESS_STATUS)

    """
    Test the function validate_edit_id
    """

    def test_validate_edit_id_invalid_task_index_as_number(self):
        with self.assertRaises(TypeError):
            to_do.validate_edit_id(open_file(sample_json_data), 5)

    def test_validate_edit_id_invalid_task_index_as_list(self):
        with self.assertRaises(TypeError):
            to_do.validate_edit_id(open_file(sample_json_data), [])

    def test_validate_edit_id_task_index_out_of_range(self):
        with self.assertRaises(ValueError):
            to_do.validate_edit_id(open_file(sample_json_data), '8')

    def test_validate_edit_id_invalid_task_index_as_negative(self):
        with self.assertRaises(ValueError):
            to_do.validate_edit_id(open_file(sample_json_data), '-8')

    def test_validate_edit_id_on_empty_list(self):
        with self.assertRaises(ValueError):
            to_do.validate_edit_id(open_file(sample_empty_list), '2')

    """
    Test the function validate_add_input
    """

    def test_validate_add_input_invalid_task_index_as_number(self):
        with self.assertRaises(TypeError):
            to_do.validate_add_input(5)

    def test_validate_add_input_invalid_task_index_as_integer(self):
        with self.assertRaises(TypeError):
            to_do.validate_add_input(-3)

    def test_validate_add_input_invalid_task_index_as_dict(self):
        with self.assertRaises(TypeError):
            to_do.validate_add_input({"a": "3"})

    def test_validate_add_input_invalid_task_index_as_empty_string(self):
        with self.assertRaises(ValueError):
            to_do.validate_add_input("")

    def test_validate_add_input_invalid_task_index_as_only_spaces(self):
        with self.assertRaises(ValueError):
            to_do.validate_add_input("   ")

    def test_validate_add_input_invalid_task_index_as_list(self):
        with self.assertRaises(TypeError):
            to_do.validate_add_input([])


if __name__ == '__to_do__':
    unittest.to_do()
