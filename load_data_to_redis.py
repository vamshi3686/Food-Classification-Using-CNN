import json
import redis

# Connect to Redis
r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

# Load your JSON file
with open("Food_Detail.json") as f:
    nutrition_data = json.load(f)

# Store each food item in Redis
for food, details in nutrition_data.items():
    r.set(f"nutrition:{food}", json.dumps(details))

print(len(nutrition_data))
print("Nutrition data stored successfully in Redis!")
