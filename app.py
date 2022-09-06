import cv2
from flask import Flask, render_template, Response
import Adafruit_DHT

app = Flask(__name__)
camera = cv2.VideoCapture(0)

def gen_frames():  
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/test')
def test_route():
    humidity1, temperature1 = Adafruit_DHT.read_retry(22, 4)
    humidity2, temperature2 = Adafruit_DHT.read_retry(22, 17)
    user_details = {
        'Left': f'Temp Left: {temperature1} C  Humidity Left: {humidity1} %',
        'Right': f'Temp Right: {temperature2} C  Humidity Right: {humidity2} %'
    }
    return render_template('test.html', data=user_details)

if __name__ == "__main__":
    app.run(debug=True)