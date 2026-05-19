import json
import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True)

MODEL_METRICS_FILES = {
    "cnn": "Custom_CNN/custom_cnn_metrics.json",
    "vgg": "VGG_16/model_evaluation_results_vgg16.json",
    "resnet": "ResNet/model_evaluation_resnet_results.json"
}

for model_key, path in MODEL_METRICS_FILES.items():
    with open(path, "r") as f:
        data = json.load(f)

    # Store whole metrics JSON as one redis key
    r.set(f"metrics:{model_key}", json.dumps(data))

print("✅ Model metrics stored in Redis!")