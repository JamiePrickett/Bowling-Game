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
        self.game = BowlingGame()

    def roll_many(self, n, pins):
        """Helper to roll the same number of pins multiple times."""
        for _ in range(n):
            self.game.roll(pins)

    def test_gutter_game(self):
        """Test a game where no pins are knocked down."""
        self.roll_many(20, 0)
        self.assertEqual(0, self.game.score())

    def test_all_ones(self):
        """Test a game where one pin is knocked down on each roll."""
        self.roll_many(20, 1)
        # Expected score: 20 (1 pin × 20 rolls)
        self.assertEqual(20, self.game.score())
    def test_single_spare(self):
        """Test a game with one spare."""
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.roll_many(17, 0)
        # Expected score: 16 (1 spare + 3 + (3 bonus))
        self.assertEqual(16, self.game.score())
    def test_single_strike(self):
        """Test a game with one strike."""
        self.game.roll(10)
        self.game.roll(2)
        self.game.roll(2)
        self.roll_many(16, 0)
        # Expected score: 18 (1 strike + 2 + 2 + (2 + 2 bonus))
        self.assertEqual(18, self.game.score())
    def test_perfect_game(self):
        """Test a game with all strikes."""
        self.roll_many(12, 10)
        # Expected score: 300 (10 )
        self.assertEqual(300, self.game.score())
    def test_spare_in_tenth_frame(self):
        """Test a game with a spare in the 10th frame."""
        self.roll_many(18, 0)
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(2)
        # Expected score: 12 (1 spare + 2)
        self.assertEqual(12, self.game.score())
    def test_strike_in_tenth_frame(self):
        """Test a game with a strike in the 10th frame."""
        self.roll_many(18, 0)
        self.game.roll(10)
        self.game.roll(2)
        self.game.roll(2)
        # Expected score: 14 (1 strike + 2 + 2)
        self.assertEqual(14, self.game.score())
    def test_random_game(self):
        """Test a random game."""
        rolls = [random.randint(0, 10) for _ in range(20)]
        for pins in rolls:
            self.game.roll(pins)
        # Expected score: sum of all rolls
        expected_score = sum(rolls)
        self.assertEqual(expected_score, self.game.score())


if __name__ == "__main__":
    unittest.main()