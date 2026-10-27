# Final Project

## Srushti's AI Emotion Detection Application

Course final project using IBM Watson NLP, Flask, Python packaging, automated unit tests and Pylint.

## Run
```bash
python -m pip install -r requirements.txt
python -m unittest -v test_emotion_detection.py
python -m pylint EmotionDetection server.py
python server.py
```

The server listens on port 5000. Open the page at http://localhost:5000 and enter text, or use:
`curl -G --data-urlencode 'textToAnalyze=I am happy today' http://localhost:5000/emotionDetector`

## Required project deliverables
- `EmotionDetection/emotion_detection.py` — IBM Watson NLP emotion classification
- `EmotionDetection/__init__.py` — package exports
- `test_emotion_detection.py` — mock-based unit tests for five emotions and HTTP responses
- `server.py` — Flask deployment and invalid-text handling
- `static/` and `templates/` — browser interface from the IBM starter repository

The remote Watson service requires network access. Unit tests mock Watson API responses to run without that network access.
