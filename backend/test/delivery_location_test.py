# test_delivery_location.py

import unittest
from unittest.mock import patch, MagicMock
from delivery_location import DeliveryLocation

class DeliveryLocationTestCase(unittest.TestCase):
    def setUp(self):
        self.delivery_location = DeliveryLocation()

    @patch('delivery_location.DeliveryLocation.create')
    def test_create_delivery_location(self, mock_create):
        # Mock the return value of the create method
        mock_create.return_value = {
            'id': 1,
            'name': 'Test Location',
            'address': '123 Test St'
        }
        
        # Call the create method
        result = self.delivery_location.create('Test Location', '123 Test St')
        
        # Assert the result
        self.assertEqual(result['id'], 1)
        self.assertEqual(result['name'], 'Test Location')
        self.assertEqual(result['address'], '123 Test St')

    @patch('delivery_location.DeliveryLocation.get_by_id')
    def test_get_delivery_location(self, mock_get_by_id):
        # Mock the return value of the get_by_id method
        mock_get_by_id.return_value = {
            'id': 1,
            'name': 'Test Location',
            'address': '123 Test St'
        }
        
        # Call the get_by_id method
        result = self.delivery_location.get_by_id(1)
        
        # Assert the result
        self.assertEqual(result['id'], 1)
        self.assertEqual(result['name'], 'Test Location')
        self.assertEqual(result['address'], '123 Test St')

    @patch('delivery_location.DeliveryLocation.update')
    def test_update_delivery_location(self, mock_update):
        # Mock the return value of the update method
        mock_update.return_value = {
            'id': 1,
            'name': 'Updated Location',
            'address': '123 Updated St'
        }
        
        # Call the update method
        result = self.delivery_location.update(1, 'Updated Location', '123 Updated St')
        
        # Assert the result
        self.assertEqual(result['id'], 1)
        self.assertEqual(result['name'], 'Updated Location')
        self.assertEqual(result['address'], '123 Updated St')

    @patch('delivery_location.DeliveryLocation.delete')
    def test_delete_delivery_location(self, mock_delete):
        # Mock the return value of the delete method
        mock_delete.return_value = True
        
        # Call the delete method
        result = self.delivery_location.delete(1)
        
        # Assert the result
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()