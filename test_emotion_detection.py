"""
test_emotion_detection.py

Unit tests validating that emotion_detector correctly identifies
the dominant emotion for a range of sample statements.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test suite for the emotion_detector function."""

    def test_emotion_detector(self):
        """Check dominant_emotion for joy, anger, disgust, fear, sadness."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

        result = emotion_detector("I am so afraid of this thing happening")
        self.assertEqual(result['dominant_emotion'], 'fear')

        result = emotion_detector("I am really sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')


if __name__ == '__main__':
    unittest.main()
