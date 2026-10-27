"""Unit tests that mock the remote Watson NLP service."""
import unittest
from unittest.mock import patch, Mock
from EmotionDetection import emotion_detector
from server import app


class TestEmotionDetection(unittest.TestCase):
    """Check all five dominant emotions and Flask validation."""

    def test_five_emotions(self):
        for dominant in ('anger', 'disgust', 'fear', 'joy', 'sadness'):
            with self.subTest(dominant=dominant):
                values = {emotion: 0.01 for emotion in ('anger', 'disgust', 'fear', 'joy', 'sadness')}
                values[dominant] = 0.96
                response = Mock(status_code=200)
                response.json.return_value = {'emotionPredictions': [{'emotion': values}]}
                with patch('EmotionDetection.emotion_detection.requests.post', return_value=response):
                    actual = emotion_detector('Sample statement')
                self.assertEqual(actual['dominant_emotion'], dominant)
                self.assertEqual(actual[dominant], 0.96)

    def test_invalid_text(self):
        self.assertIsNone(emotion_detector('')['dominant_emotion'])

    def test_remote_failure(self):
        with patch('EmotionDetection.emotion_detection.requests.post', return_value=Mock(status_code=400)):
            self.assertIsNone(emotion_detector('test')['dominant_emotion'])

    def test_flask_home(self):
        self.assertEqual(app.test_client().get('/').status_code, 200)

    def test_flask_error(self):
        result = app.test_client().get('/emotionDetector?textToAnalyze=')
        self.assertEqual(result.status_code, 400)
        self.assertIn(b'Invalid text!', result.data)

    def test_flask_success(self):
        values = dict(anger=0.1, disgust=0.1, fear=0.1, joy=0.6, sadness=0.1, dominant_emotion='joy')
        with patch('server.emotion_detector', return_value=values):
            result = app.test_client().get('/emotionDetector?textToAnalyze=hello')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'dominant emotion is joy', result.data)


if __name__ == '__main__':
    unittest.main()
