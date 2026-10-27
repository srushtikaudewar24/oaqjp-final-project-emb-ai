"""Flask app serving the emotion detection project."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """Render the landing page."""
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET', 'POST'])
def detect_emotion():
    """Detect and format emotion scores for the provided text."""
    text = request.values.get('textToAnalyze', '')
    result = emotion_detector(text)
    if result['dominant_emotion'] is None:
        return 'Invalid text! Please try again!', 400
    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
