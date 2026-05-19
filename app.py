from flask import Flask, render_template, request, jsonify
import os
import json
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import warnings

warnings.filterwarnings('ignore')

app = Flask(__name__)

# =========================================
# CREATE STATIC UPLOAD FOLDER
# =========================================

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# =========================================
# LOAD FOOD DETAILS JSON
# =========================================

with open("Food_Detail.json", "r") as f:
    food_details = json.load(f)

# =========================================
# GET CLASS NAMES
# =========================================

class_names = list(food_details.keys())
class_names.sort()

# =========================================
# LOAD MODELS
# =========================================

print("Loading Models...")

custom_model = load_model(
    "Custom_CNN/food_classification_custom_model.h5"
)

vgg_model = load_model(
    "VGG_16/vgg16_food_classification_model.keras"
)

resnet_model = load_model(
    "ResNet/food_classification_custom_Resnetmodel.keras"
)

print("All Models Loaded Successfully!")

# =========================================
# LOAD METRICS
# =========================================

with open("Custom_CNN/custom_cnn_metrics.json", "r") as f:
    custom_metrics = json.load(f)

with open("VGG_16/model_evaluation_results_vgg16.json", "r") as f:
    vgg_metrics = json.load(f)

with open("ResNet/model_evaluation_resnet_results.json", "r") as f:
    resnet_metrics = json.load(f)

# =========================================
# HOME PAGE
# =========================================

@app.route("/")
def home():

    return render_template(
        "index.html",
        classes=class_names
    )

# =========================================
# IMAGE PREPROCESS FUNCTION
# =========================================

def preprocess_image(img_path, model_name):

    # ==========================
    # VGG16
    # ==========================

    if model_name == "vgg":

        from tensorflow.keras.applications.vgg16 import preprocess_input

        img = image.load_img(
            img_path,
            target_size=(224, 224)
        )

        img_array = image.img_to_array(img)

        img_array = preprocess_input(img_array)

    # ==========================
    # RESNET
    # ==========================

    elif model_name == "resnet":

        from tensorflow.keras.applications.resnet50 import preprocess_input

        img = image.load_img(
            img_path,
            target_size=(255, 255)
        )

        img_array = image.img_to_array(img)

        img_array = preprocess_input(img_array)

    # ==========================
    # CUSTOM CNN
    # ==========================

    else:

        img = image.load_img(
            img_path,
            target_size=(256, 256)
        )

        img_array = image.img_to_array(img)

        img_array = img_array / 255.0

    img_array = np.expand_dims(img_array, axis=0)

    return img_array

# =========================================
# FORMAT METRICS
# =========================================

def format_metric(value):

    try:
        return round(float(value), 5)
    except:
        return 0.00000

# =========================================
# PREDICTION ROUTE
# =========================================

@app.route("/predict", methods=["POST"])
def predict():

    # =====================================
    # CHECK IMAGE
    # =====================================

    if "image" not in request.files:

        return jsonify({
            "error": "No image uploaded"
        })

    file = request.files["image"]

    model_name = request.form.get("model")

    if file.filename == "":

        return jsonify({
            "error": "No file selected"
        })

    # =====================================
    # SAVE IMAGE
    # =====================================

    filename = file.filename

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    # =====================================
    # IMAGE PATH FOR HTML
    # =====================================

    image_path = f"uploads/{filename}"

    # =====================================
    # SELECT MODEL
    # =====================================

    if model_name == "cnn":

        model = custom_model
        metrics = custom_metrics

    elif model_name == "vgg":

        model = vgg_model
        metrics = vgg_metrics

    elif model_name == "resnet":

        model = resnet_model
        metrics = resnet_metrics

    else:

        return jsonify({
            "error": "Invalid model selected"
        })

    # =====================================
    # PREPROCESS IMAGE
    # =====================================

    processed_image = preprocess_image(
        filepath,
        model_name
    )

    # =====================================
    # PREDICT
    # =====================================

    prediction = model.predict(processed_image)

    predicted_index = int(np.argmax(prediction))

    confidence = float(np.max(prediction) * 100)

    predicted_class = class_names[predicted_index]

    # =====================================
    # GET FOOD DETAILS
    # =====================================

    nutrition = food_details.get(predicted_class)

    # =====================================
    # GET METRICS
    # =====================================

    accuracy = format_metric(
        metrics.get("accuracy", 0)
    )

    precision = format_metric(
        metrics.get("precision", 0)
    )

    # GET FROM CLASSIFICATION REPORT

    classification_report = metrics.get(
        "classification_report",
        {}
    )

    weighted_avg = classification_report.get(
        "weighted avg",
        {}
    )

    recall = format_metric(
        weighted_avg.get("recall", 0)
    )

    f1_score = format_metric(
        weighted_avg.get("f1-score", 0)
    )
    # =====================================
    # RENDER TEMPLATE
    # =====================================

    return render_template(

        "index.html",

        prediction=predicted_class,

        confidence=round(confidence, 2),

        image_path=image_path,

        nutrition=nutrition,

        model_used=model_name.upper(),

        accuracy=accuracy,

        precision=precision,

        recall=recall,

        f1_score=f1_score,

        classes=class_names
    )

# =========================================
# RUN FLASK APP
# =========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )