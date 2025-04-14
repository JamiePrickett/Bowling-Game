"""
Unit tests for the Bowling Game

This module contains basic unit tests for the BowlingGame class.
Students should expand these tests to cover all functionality and edge cases.
"""

import unittest
import random
from bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        """Set up a new game before each test."""
        self.game = BowlingGame() # create a new game instance

    def roll_many(self, n, pins):
        """Helper to roll the same number of pins multiple times."""
        for _ in range(n):
            self.game.roll(pins) # roll the same number of pins n times

    def test_gutter_game(self):
        """Test a game where no pins are knocked down."""
        self.roll_many(20, 0) # 20 rolls of 0 pins
        # Expected score: 0 (0 pins × 20 rolls)
        self.assertEqual(0, self.game.score())

    def test_all_ones(self):
        """Test a game where 1 pin is knocked down on each roll."""
        self.roll_many(20, 1)
        # Expected score: 20 (1 pin × 20 rolls)
        self.assertEqual(20, self.game.score())

    def test_single_spare(self):
        """Test a game with one spare. followed 3 pins"""
        self.game.roll(5)
        self.game.roll(5) # spare
        self.game.roll(3) # normal roll (toward bonus 1)
        self.game.roll(2) # normal roll
        self.roll_many(16, 0) # rest of the rolls are 0
        # Expected score: 18 = frame 1: (5 + 5 + 3b), frame 2: (3),  frame 3: (2), rest: 1
        self.assertEqual(18, self.game.score())

    def test_single_strike(self):
        """Test a game with one strike."""
        self.game.roll(10) # strike
        self.game.roll(2) # normal roll (toward bonus 1)
        self.game.roll(2) # normal roll (toward bonus 2)
        self.game.roll(1) # normal roll
        self.roll_many(15, 0) # rest of the rolls are 0
        # Expected score: 19 = frame 1: (10 + (2b + 2b)), frame 2: (2), frame 3: (2), frame 4: (1) rest: 0
        self.assertEqual(19, self.game.score())

    def test_perfect_game(self):
        """Test a game with all strikes."""
        self.roll_many(12, 10) # 12 strikes
        # Expected score: 300 = 10 + (10b + 10b) for each of the 10 frames
        self.assertEqual(300, self.game.score())

    def test_spare_in_tenth_frame(self):
        """Test a game with a spare in the 10th frame."""
        self.roll_many(18, 0) # 18 rolls of 0
        self.game.roll(5) 
        self.game.roll(5) # spare
        self.game.roll(2) # bonus roll 1
        # Expected score: 12 = frame 10: (5 + 5 + 2b), rest: 0
        self.assertEqual(12, self.game.score())

    def test_strike_in_tenth_frame(self):
        """Test a game with a strike in the 10th frame."""
        self.roll_many(18, 0) # 18 rolls of 0
        self.game.roll(10) # strike
        self.game.roll(2) # bonus roll 1
        self.game.roll(2) # bonus roll 2
        # Expected score: 14 = frame 10: (10 + (2b + 2b)), rest: 0
        self.assertEqual(14, self.game.score())

    def test_random_game(self):
        """Test a random game."""
        rolls = [
            10, # frame 1: strike
            2, 3, # frame 2: normal rolls
            5, 5, # frame 3: spare
            4, 3, # frame 4: normal rolls
            0, 0, # frame 5: gutter
            1, 1, # frame 6: ones
            4, 5, # frame 6: normal rolls
            3, 4, # frame 7: normal rolls
            8, 2, # frame 8: spare
            6, 0, # frame 9: normal rolls
            10, # frame 10: strike
            2, 3 # bonus rolls
        ]
        expected_score = (
            (10) + (2 + 3) + # frame 1: strike + (2b + 3b) = 15
            (2 + 3) # frame 2: 5
            (5 + 5) + (4) + # frame 3: spare + (4b) = 14
            (4 + 3) + # frame 4: 7
            (0 + 0) + # frame 5: 0
            (1 + 1) + # frame 6: 1 + 1 = 2
            (4 + 5) + # frame 7: 4 + 5 = 9
            (3 + 4) + # frame 8: 3 + 4 = 7
            (8 + 2) + (6) + # frame 9: spare + (6b) = 16
            (10) + (2, 3) # frame 10: strike + (2b + 3b) = 15
        )
        self.assertEqual(expected_score, self.game.score())


if __name__ == "__main__":
    unittest.main()