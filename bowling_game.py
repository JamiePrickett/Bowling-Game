"""
Bowling Game Implementation
A module for calculating bowling game scores.
"""


class BowlingGame:
    def __init__(self):
        # Initialize a new game with 10 frames
        # Each frame has up to 2 rolls (except the 10th frame which can have 3)
        self.rolls = []

    def roll(self, pins):
        """
        Records a roll in the game.

        Args:
            pins: Number of pins knocked down in this roll
        """
        self.rolls.append(pins)

    def score(self):
        """Calculate the score for the current game.
        
        Returns:
            The total score of the game
        """
        score = 0
        frame_index = 0

        for frame in range(10): # There are 10 frames in a bowling game
            if self._is_strike(frame_index):
                # Strike
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                # Spare
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                # Open frame
                score += self.rolls[frame_index] + self.rolls[frame_index + 1] # sum of the two rolls
                frame_index += 2

        return score

    def _is_strike(self, frame_index):
        """
        Check if the roll at frame_index is a strike.

        Args:
            frame_index: Index of the roll to check

        Returns:
            True if the roll is a strike, False otherwise
        """
        return frame_index < len(self.rolls) and self.rolls[frame_index] == 10

    def _is_spare(self, frame_index):
        """
        Check if the rolls at frame_index and frame_index + 1 form a spare.

        Args:
            frame_index: Index of the first roll in a frame

        Returns:
            True if the rolls form a spare, False otherwise
        """
        return frame_index + 1 < len(self.rolls) and self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def _strike_bonus(self, frame_index):
        """
        Calculate the bonus for a strike.

        Args:
            frame_index: Index of the strike roll

        Returns:
            The value of the next two rolls after the strike
        """
        if frame_index + 2 < len(self.rolls):
            return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]
        return 0

    def _spare_bonus(self, frame_index):
        """
        Calculate the bonus for a spare.

        Args:
            frame_index: Index of the first roll in a spare

        Returns:
            The value of the roll after the spare
        """
        if frame_index + 2 < len(self.rolls):
            return self.rolls[frame_index + 2]
        return 0