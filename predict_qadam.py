from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
from ultralytics import YOLO

def predict_qadam_yolo(img):
    best = "best_qadam_02.pt"
    input_image = cv2.imread(img)
    model = YOLO(best)
    results = model.predict(input_image)
    annotated_image = results[0].plot() 
    return annotated_image

