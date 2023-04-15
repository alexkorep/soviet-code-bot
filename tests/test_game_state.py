import unittest
from unittest.mock import patch, MagicMock
from models.game_state import GameState

class TestGameState(unittest.TestCase):
    def test_load_from_dynamodb_exists(self):
        user_id = 1
        with patch('models.game_state.GameState.get') as mock_get:
            mock_game_state = MagicMock()
            mock_get.return_value = mock_game_state
            result = GameState.load_from_dynamodb(user_id)
            mock_get.assert_called_once_with(user_id)
            self.assertEqual(result, mock_game_state)

    def test_load_from_dynamodb_does_not_exist(self):
        user_id = 2
        with patch('models.game_state.GameState.get') as mock_get:
            mock_get.side_effect = GameState.DoesNotExist
            result = GameState.load_from_dynamodb(user_id)
            mock_get.assert_called_once_with(user_id)
            self.assertIsInstance(result, GameState)
            self.assertEqual(result.user_id, user_id)

    def test_save_to_dynamodb(self):
        game_state = GameState(user_id=3)
        with patch.object(game_state, 'save') as mock_save:
            game_state.save_to_dynamodb()
            mock_save.assert_called_once_with()

