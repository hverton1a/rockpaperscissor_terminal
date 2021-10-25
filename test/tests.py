import unittest
from unittest.mock import patch
import pytest

from game.adversary import *
from game.game import *
from game.gui import *
from game.player import *


class JunKenPoTests (unittest.TestCase):

    def test_adversary_choice(self):
        choice = get_adversary_play()
        self.assertTrue(choice in GAME_CHOICES)

    def test_game_quitting(self) :
        with self.assertRaises(SystemExit):
            quit_game()

    # Rock win
    @patch("game.game.win_game")
    def test_game_rock_won(self, mock_win_game):
        player_play = GAME_CHOICES[0]        # Rock
        adversary_play = GAME_CHOICES[2]     # Scissor
        game_result(player_play, adversary_play)
        mock_win_game.assert_called_once()

    # Paper win
    @patch("game.game.win_game")
    def test_game_paper_won(self, mock_win_game):
        player_play = GAME_CHOICES[1]        # Paper
        adversary_play = GAME_CHOICES[0]     # Rock
        game_result(player_play, adversary_play)
        mock_win_game.assert_called_once()

    # Scissor win
    @patch("game.game.win_game")
    def test_game_scissor_won(self, mock_win_game):
        player_play = GAME_CHOICES[2]        # Scissor
        adversary_play = GAME_CHOICES[1]     # Paper
        game_result(player_play, adversary_play)
        mock_win_game.assert_called_once()

    # Rock loose
    @patch("game.game.loose_game")
    def test_game_rock_loose(self, mock_loose_game):
        player_play = GAME_CHOICES[0]        # Rock
        adversary_play = GAME_CHOICES[1]     # Paper
        game_result(player_play, adversary_play)
        mock_loose_game.assert_called_once()

    # Paper loose
    @patch("game.game.loose_game")
    def test_game_paper_loose(self, mock_loose_game):
        player_play = GAME_CHOICES[1]        # Paper
        adversary_play = GAME_CHOICES[2]     # Scissor
        game_result(player_play, adversary_play)
        mock_loose_game.assert_called_once()

    # Scissor loose
    @patch("game.game.loose_game")
    def test_game_scissor_loose(self, mock_loose_game):
        player_play = GAME_CHOICES[2]        # Scissor
        adversary_play = GAME_CHOICES[0]     # Rock
        game_result(player_play, adversary_play)
        mock_loose_game.assert_called_once()

    # Rock Tie
    @patch("game.game.draw_game")
    def test_game_rock_draw(self, mock_draw_game):
        player_play = GAME_CHOICES[0]        # Rock
        adversary_play = GAME_CHOICES[0]     # Rock
        game_result(player_play, adversary_play)
        mock_draw_game.assert_called_once()

    # Paper Tie
    @patch("game.game.draw_game")
    def test_game_paper_draw(self, mock_draw_game):
        player_play = GAME_CHOICES[1]        # Paper
        adversary_play = GAME_CHOICES[1]     # Paper
        game_result(player_play, adversary_play)
        mock_draw_game.assert_called_once()

    # Scissor Tie
    @patch("game.game.draw_game")
    def test_game_scissor_draw(self, mock_draw_game):
        player_play = GAME_CHOICES[2]        # Scissor
        adversary_play = GAME_CHOICES[2]     # Scissor
        game_result(player_play, adversary_play)
        mock_draw_game.assert_called_once()


    @patch('builtins.print')
    def test_print_player_play(self, mock_print):
        player_play = GAME_CHOICES[0]        # Rock
        print_player_play(player_play)
        mock_print.assert_called_with('        You choose ' + player_play)

    @patch('builtins.print')
    def test_print_adversary_play(self, mock_print):
        adversary_play = GAME_CHOICES[1]        # Paper
        print_adversary_play(adversary_play)
        mock_print.assert_called_with('        You adversary choose ' +\
                                             adversary_play + \
                                             ' \n')

    @patch("game.gui.print_player_play")
    @patch("game.gui.print_adversary_play")
    def test_print_plays(self, mock_print_player, mock_print_adversary_play):
        player_play = GAME_CHOICES[0]           # Rock
        adversary_play = GAME_CHOICES[1]        # Paper
        print_plays(player_play, adversary_play)
        mock_print_player.assert_called_once()
        mock_print_adversary_play.assert_called_once()



    def test_get_player_play(self):
        output = get_player_play(0)
        self.assertEqual(output,'Rock')
        output = get_player_play(1)
        self.assertEqual(output,'Paper')
        output = get_player_play(2)
        self.assertEqual(output,'Scissor')


    def test_validate_player_choice(self):
        result = validate_player_choice('0')
        self.assertEqual(result, 0)

        result = validate_player_choice('1')
        self.assertEqual(result, 1)

        result = validate_player_choice('2')
        self.assertEqual(result, 2)

        result = validate_player_choice('3')
        self.assertEqual(result, None)

        result = validate_player_choice('-1')
        self.assertEqual(result, None)

        result = validate_player_choice('any text?')
        self.assertEqual(result, None)


    @patch('builtins.input', lambda *args: 'any text')
    def test_get_player_choice_with_any_text(self):
        # checking the input with any text
        result = get_player_choice()
        self.assertEqual(result, None)

    @patch('builtins.input', lambda *args: 'a3n@y ?Te2xt')
    def test_get_player_choice_with_any_alfa(self):
        # checking the input with any text
        result = get_player_choice()
        self.assertEqual(result, None)

    @patch('builtins.input', lambda *args: '  2   ')
    def test_get_player_choice_with_valid_choic_with_any_whitespace(self):
        # check the return with any spaces with a valid choice
        result = get_player_choice()
        self.assertEqual(2, result)

    @patch('builtins.input', lambda *args: '-1')
    def test_get_player_choice_choice_beyond_lower_boundary(self):
        # check the input boundary lower
        result = get_player_choice()
        self.assertEqual(None, result)

    @patch('builtins.input', lambda *args: '3')
    def test_get_player_choice_above_upper_boudary(self):
        # check the input boundary upper
        result = get_player_choice()
        self.assertEqual(None, result)

    @patch('builtins.input', lambda *args: '0')
    def test_get_player_choice_with_valid_lower_choice(self):
        # check the minimum accepted value
        result = get_player_choice()
        self.assertEqual(0, result)

    @patch('builtins.input', lambda *args: '1')
    def test_get_player_choice_with_valid_upper_choice(self):
        # check a middle accepted value
        result = get_player_choice()
        self.assertEqual(1, result)

    @patch('builtins.input', lambda *args: '2')
    def test_get_player_choice_with_valid_middle_choice(self):
        # check a maximum accepted value
        result = get_player_choice()
        self.assertEqual(2, result)

    def test_player_is_quiting_quit_input(self):
        # check true with quit input
        self.assertTrue(player_is_quiting('quit'))

    def test_player_is_quiting_empty_input(self):
        # check true with empty input
        self.assertTrue(player_is_quiting(''))

    def test_player_is_quiting_any_input(self):
        # check true with any input
        self.assertFalse(player_is_quiting(' ash e74 hds $%  '))

    @patch('builtins.input', lambda *args: '')
    def test_get_player_choice_check_quit_empty_input(self):
        # checking if quit with empty input
        with self.assertRaises(SystemExit):
            get_player_choice()

    @patch('builtins.input', lambda *args: 'quit')
    def test_get_player_choice_check_quit_with_quit_input(self):
        # checking if quit with quit input
        with self.assertRaises(SystemExit):
            get_player_choice()

    @patch('builtins.input', lambda *args: ' QuIt   ')
    def test_get_player_choice_check_quit_caseinsensitive_any_whitespace_input(self):
        # checking if quit with non standar case insensitive  QuIt    input
        with self.assertRaises(SystemExit):
            get_player_choice()
