import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import random
from memory_profiler import profile

# Load the trained Keras model
model = tf.keras.models.load_model("models/cnn_image_classification_model.h5")

def preprocess_image(image_path):
    """Load and preprocess an image for the CNN model."""
    img = image.load_img(image_path, target_size=(150, 150))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  # Normalize to [0,1]
    return img

@profile  # Optional: uncomment to profile memory
def calling_decorators(image_path):
    img = preprocess_image(image_path)
    prediction = model.predict(img, verbose=0)
    return prediction

def predict_single_image(image_path):
    prediction = calling_decorators(image_path)
    return "Positive" if prediction[0][0] > 0.5 else "Negative"

def main(input_path):
    """Classify all images in a given folder."""
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
                    print(f"{filename}: {predicted_class}")
                    if (i + 1) % batch_size == 0:
                        break
            all_predictions.append(batch_predictions)
            print("--------------------------------------")

    else:
        print("Invalid input path.")

# Run the pipeline
input_path = os.path.join(os.getcwd(), 'Images100')  # Adjust if needed
main(input_path)
