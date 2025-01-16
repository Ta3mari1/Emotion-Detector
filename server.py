'''
Executing this function initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on
localhost:5000.
'''
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer", methods=["GET", "POST"])
def sent_analyzer():
    if request.method == "POST":
        data = request.json
        statement = data.get('statement')
    else:  # For GET requests
        statement = request.args.get('textToAnalyze')
    
    if not statement:
        return jsonify({"error": "Please provide a valid statement"}), 400
    
    result = emotion_detector(statement)
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
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    ''' This function executes the Flask app and deploys it on localhost:5000
    '''
    app.run(host='0.0.0.0', port=8000)
