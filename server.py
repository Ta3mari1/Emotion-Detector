"""
This module provides a Flask web application for emotion detection.
It processes text input from users and returns emotion analysis results.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer", methods=["GET", "POST"])
def sent_analyzer():
    """
    Handles requests to analyze emotions from a given text input.

    Returns:
        JSON response with the emotion analysis results or an error message.
    """
    if request.method == "POST":
        data = request.json
        statement = data.get('statement')
    else:
        statement = request.args.get('textToAnalyze')

    if not statement or not statement.strip():
        return jsonify({"response": "Invalid text! Please try again!"}), 400

    result = emotion_detector(statement)

    if result["dominant_emotion"] is None:
        return jsonify({"response": "Invalid text! Please try again!"}), 400

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return jsonify({"response": response_text})

@app.route("/")
def render_index_page():
    """
    Renders the main application page.

    Returns:
        Rendered HTML page.
    """
    return render_template("index.html")

if __name__ == "__main__":
    """
    Runs the Flask application on localhost at port 8000.
    """
    app.run(host='0.0.0.0', port=8000)
