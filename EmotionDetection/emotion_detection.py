"""Use IBM Watson NLP to detect five emotions in supplied text."""
import os
import requests

URL = os.getenv('WATSON_EMOTION_URL', 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
HEADERS = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
EMOTIONS = ('anger', 'disgust', 'fear', 'joy', 'sadness')


def emotion_detector(text_to_analyze):
    """Return the five emotion scores and dominant emotion; use None on error."""
    invalid = {**{emotion: None for emotion in EMOTIONS}, 'dominant_emotion': None}
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return invalid
    try:
        response = requests.post(
            URL, json={'raw_document': {'text': text_to_analyze}},
            headers=HEADERS, timeout=15
        )
        if response.status_code != 200:
            return invalid
        scores = response.json()['emotionPredictions'][0]['emotion']
        result = {emotion: float(scores[emotion]) for emotion in EMOTIONS}
        result['dominant_emotion'] = max(EMOTIONS, key=result.get)
        return result
    except (requests.exceptions.RequestException, ValueError, KeyError, IndexError, TypeError):
        return invalid
