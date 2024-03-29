from flask import Flask, render_template, Response, send_file
from picamera import PiCamera
import RPi.GPIO as GPIO
import time
import io

app = Flask(__name__)
camera = PiCamera()

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def gen_frames():
    """Generate frames from the camera."""
    while True:
        stream = io.BytesIO()
        camera.capture(stream, format='jpeg', use_video_port=True)
        stream.seek(0)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + stream.read() + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Route for streaming video."""
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/take_photo')
def take_photo():
    """Route for capturing a photo."""
    stream = io.BytesIO()
    camera.capture(stream, format='jpeg')
    stream.seek(0)
    return send_file(stream, mimetype='image/jpeg', as_attachment=True, download_name='photo.jpg')

@app.route('/record_video')
def record_video():
    """Route for recording a video."""
    camera.start_recording('video.mp4')
    time.sleep(10)  # Record for 10 seconds as an example
    camera.stop_recording()
    return send_file('video.mp4', mimetype='video/mp4', as_attachment=True, download_name='video.mp4')

if __name__ == '__main__':
    try:
        camera.resolution = (640, 480)
        app.run(host='0.0.0.0', port=8000, debug=False)
    finally:
        camera.close()

