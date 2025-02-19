''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : TODO
app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def sent_detector():
    """Function sent_detector"""
    text_to_detect = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_detect)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f'''For the given statement, the system response is 'anger': {
        response['anger']}, 'disgust': {response['disgust']}, 'fear': {
        response['fear']}, 'joy': {response['joy']} and 'sadness': {
        response['sadness']}. The dominant emotion is <strong>{
        response['dominant_emotion']}</strong>.'''

@app.route("/")
def render_index_page():
    """Function render_index_page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
