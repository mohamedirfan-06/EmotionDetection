# Emotion Detector

A web application that analyzes text and detects the emotions expressed in it
(anger, disgust, fear, joy, sadness) using the Watson NLP library, deployed
with Flask.

## Project Structure
- `EmotionDetection/` — package containing `emotion_detection.py`, the core logic
- `server.py` — Flask web server exposing the `/emotionDetector` endpoint
- `templates/index.html` — front-end page
- `test_emotion_detection.py` — unit tests for the emotion detector
- `requirements.txt` — project dependencies

## How it works
Text submitted by the user is sent to Watson NLP's EmotionPredict service,
which returns scores for anger, disgust, fear, joy, and sadness. The
application determines the dominant emotion and returns a formatted response.
Blank input is handled with a 400 status code and an error message.

## Running locally
```
pip install -r requirements.txt
python server.py
```
Then open `http://localhost:5000` in your browser.

## Running tests
```
python -m unittest test_emotion_detection.py
```

## Static code analysis
```
pylint server.py
```
