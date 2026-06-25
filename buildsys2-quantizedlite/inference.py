import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import random
from memory_profiler import profile
# Load the TFLite model
interpreter = tf.lite.Interpreter(model_path="models/cnn_image_classification_model_quantized.tflite")
interpreter.allocate_tensors()

# Get input/output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(150, 150))  # Adjust if needed
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img /= 255.0
    return img.astype(np.float32)

@profile
def predict_single_image(image_path):
    img = preprocess_image(image_path)
    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])
    return "Positive" if output[0][0] > 0.5 else "Negative"

def main(input_path):
    if os.path.isfile(input_path):
        print("Input should be a directory containing images.")
        return

    elif os.path.isdir(input_path):
        num_iterations = 1
        batch_size = 100
        all_predictions = []

        for _ in range(num_iterations):
            batch_predictions = []
            files = os.listdir(input_path)
            random.shuffle(files)
            for i, filename in enumerate(files):
                if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                    image_path = os.path.join(input_path, filename)
                    predicted_class = predict_single_image(image_path)
                    batch_predictions.append((filename, predicted_class))
                    if (i + 1) % batch_size == 0:
                        break
            all_predictions.append(batch_predictions)
            print(batch_predictions)
            print("--------------------------------------")

    else:
        print("Invalid input path.")

input_path = os.path.join(os.getcwd(), 'Images100')  # test folder path
main(input_path)
