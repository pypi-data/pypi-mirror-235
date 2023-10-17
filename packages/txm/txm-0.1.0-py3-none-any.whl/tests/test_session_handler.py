import unittest
from txm.action_handlers.session_handler import create_session

class TestSessionHandler(unittest.TestCase):

    def test_create_session(self):
        # Prepare
        session_name = "test"
        
        # Execute
        result = create_session(session_name)
        
        # Assert
        self.assertIsNotNone(result, "The result should not be None")
        self.assertEqual(result, True, f"Expected True, but got {result}")
