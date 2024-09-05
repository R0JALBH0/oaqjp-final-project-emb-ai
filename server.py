from flask import Flask, render_template, request
from emotionDetector.emotion_detection import emotion_detector

"""
This module defines a Flask web application that provides an endpoint for emotion detection
from text input and renders an index page.
"""

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Endpoint to detect emotion from a given text input.
    If no text is provided, returns an appropriate message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "No text provided for analysis."

    response = emotion_detector(text_to_analyze)

    result_string = (f"For the given statement, the system response is "
                     f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
                     f"'fear': {response['fear']}, 'joy': {response['joy']} and "
                     f"'sadness': {response['sadness']}. "
                     f"The dominant emotion is {response['dominant_emotion']}.")
    return result_string

@app.route("/")
def render_index_page():
    """
    Renders the index page of the web application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
