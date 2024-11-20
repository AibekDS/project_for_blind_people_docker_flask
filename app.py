from flask import Flask, render_template, request, send_from_directory
from predict_qadam import predict_qadam_yolo
import os
import cv2

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './images/'
app.config['PROCESSED_FOLDER'] = './processed/'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    imagefile = request.files['imagefile']
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], imagefile.filename)
    imagefile.save(image_path)
    
    final_img = predict_qadam_yolo(image_path)
    processed_image_path = os.path.join(app.config['PROCESSED_FOLDER'], "processed_"+imagefile.filename)
    success = cv2.imwrite(processed_image_path, final_img)
    if not success:
        print(f"Failed to save image at: {processed_image_path}")

    return render_template('index.html', prediction_image=processed_image_path)

@app.route('/processed/<filename>')
def processed_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
