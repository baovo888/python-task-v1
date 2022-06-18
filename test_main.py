"""
Test module for main.py
"""
import unittest
import main
from main import SUCCESS_STATUS

sample_json_data = {
    'meta': {'last_update': None},
    'items': [
        {'task': 'Buy milk', 'status': 'TO_DO'},
        {'task': 'Sell car', 'status': 'TO_DO'},
        {'task': 'Learn Python', 'status': 'TO_DO'}
    ]
}

sample_empty_list = {
    'meta': {'last_update': None},
    'items': []
}


class TestMain(unittest.TestCase):
    """
    Test the function add_item
    """

    def test_add_item_invalid_task_index_as_number(self):
        with self.assertRaises(TypeError):
            main.add_item(sample_json_data, 5)

    def test_add_item_invalid_task_index_as_list(self):
        with self.assertRaises(TypeError):
            main.add_item(sample_json_data, [])

    def test_add_item_success(self):
        self.assertEqual(main.add_item(sample_json_data, 'New Task'), SUCCESS_STATUS)

    """
    Test the function complete_item
    """

    def test_complete_item_invalid_task_index_as_number(self):
        with self.assertRaises(TypeError):
            main.complete_item(sample_json_data, 5)

    def test_complete_item_invalid_task_index_as_list(self):
        with self.assertRaises(TypeError):
            main.complete_item(sample_json_data, [])

    def test_complete_item_task_index_out_of_range(self):
        with self.assertRaises(ValueError):
            main.complete_item(sample_json_data, '8')

    def test_complete_item_on_empty_list(self):
        with self.assertRaises(ValueError):
            main.complete_item(sample_empty_list, '2')

    def test_complete_item_success(self):
        self.assertEqual(main.complete_item(
            sample_json_data, '3'), SUCCESS_STATUS)

    """
    Test the function delete_item
    """

    def test_delete_item_invalid_task_index_as_number(self):
        with self.assertRaises(TypeError):
            main.delete_item(sample_json_data, 5)

    def test_delete_item_invalid_task_index_as_list(self):
        with self.assertRaises(TypeError):
            main.delete_item(sample_json_data, [])

    def test_delete_item_task_index_out_of_range(self):
        with self.assertRaises(ValueError):
            main.delete_item(sample_json_data, '8')

    def test_delete_item_on_empty_list(self):
        with self.assertRaises(ValueError):
            main.delete_item(sample_empty_list, '2')

    def test_delete_item_success(self):
        self.assertEqual(main.delete_item(
            sample_json_data, '3'), SUCCESS_STATUS)

    """
    Test the function validate_edit_id
    """

    def test_validate_edit_id_invalid_task_index_as_number(self):
        with self.assertRaises(TypeError):
            main.validate_edit_id(sample_json_data, 5)

    def test_validate_edit_id_invalid_task_index_as_list(self):
        with self.assertRaises(TypeError):
            main.validate_edit_id(sample_json_data, [])

    def test_validate_edit_id_task_index_out_of_range(self):
        with self.assertRaises(ValueError):
            main.validate_edit_id(sample_json_data, '8')

    def test_validate_edit_id_invalid_task_index_as_negative(self):
        with self.assertRaises(ValueError):
            main.validate_edit_id(sample_json_data, '-8')

    def test_validate_edit_id_on_empty_list(self):
        with self.assertRaises(ValueError):
            main.validate_edit_id(sample_empty_list, '2')

    """
    Test the function validate_add_input
    """

    def test_validate_add_input_invalid_task_index_as_number(self):
        with self.assertRaises(TypeError):
            main.validate_add_input(5)

    def test_validate_add_input_invalid_task_index_as_integer(self):
        with self.assertRaises(TypeError):
            main.validate_add_input(-3)

    def test_validate_add_input_invalid_task_index_as_dict(self):
        with self.assertRaises(TypeError):
            main.validate_add_input({"a": "3"})

    def test_validate_add_input_invalid_task_index_as_empty_string(self):
        with self.assertRaises(ValueError):
            main.validate_add_input("")

    def test_validate_add_input_invalid_task_index_as_only_spaces(self):
        with self.assertRaises(ValueError):
            main.validate_add_input("   ")

    def test_validate_add_input_invalid_task_index_as_list(self):
        with self.assertRaises(TypeError):
            main.validate_add_input([])


if __name__ == '__main__':
    unittest.main()
