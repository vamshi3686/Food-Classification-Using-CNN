````md
# 🍔 Food Classification & Nutrition Analysis System

An AI-powered web application that classifies food images using Deep Learning models and displays nutritional information instantly.

---

## 🚀 Features

✅ Food Image Classification  
✅ Nutrition Information Display  
✅ Deep Learning Models (VGG16, VGG19, ResNet50)  
✅ Fast Data Retrieval using Redis  
✅ Prediction History/Profile Section  
✅ Responsive Web Interface  
✅ Transfer Learning-based CNN Architecture  

---

## 🧠 Models Used

- VGG16
- VGG19
- ResNet50

---

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Deep Learning
- TensorFlow
- Keras

### Database
- Redis

---

# 📂 Project Structure

```bash
food-classifier/
│
├── static/
│   ├── css/
│   ├── js/
│   └── uploads/
│
├── templates/
│   └── index.html
│
├── models/
│   └── trained_model.h5
│
├── nutrition_data/
│   └── food_nutrition.json
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
````

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/food-classifier.git
```

```bash
cd food-classifier
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate environment:

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
```

Activate environment:

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔥 Redis Setup

## Install Redis

### Windows

Download Redis from:

👉 [https://github.com/microsoftarchive/redis/releases](https://github.com/microsoftarchive/redis/releases)

### Linux

```bash
sudo apt install redis-server
```

### Mac

```bash
brew install redis
```

---

## Start Redis Server

### Windows

```bash
redis-server
```

### Linux / Mac

```bash
sudo service redis-server start
```

---

# ▶️ Run the Application

```bash
python app.py
```

or

```bash
python main.py
```

---

# 🌐 Open in Browser

```bash
http://127.0.0.1:5000
```

---

# 📸 How to Use

1. Upload a food image
2. Model predicts the food category
3. Nutrition details are displayed
4. Prediction history/profile updates automatically

---

# 📊 Example Output

| Food Image | Prediction | Calories |
| ---------- | ---------- | -------- |
| Pizza      | Pizza      | 266 kcal |
| Burger     | Burger     | 295 kcal |
| Apple      | Apple      | 52 kcal  |

---

# 🎯 Future Improvements

* Mobile App Integration
* Real-time Camera Detection
* Multi-food Detection
* Voice Assistant Integration
* Calorie Tracking Dashboard

---

# 🤝 Contributing

Contributions are welcome!

Fork the repository and create a pull request.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Vamshi Krishna**

📧 Connect with me on LinkedIn
🔗 GitHub: [https://github.com/your-username](https://github.com/your-username)

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub!

```
```
# 📸 Application Preview

## 🔹 Before Prediction

![Before Prediction](sandbox:/mnt/data/image.png)

---

## 🔹 After Prediction

![After Prediction](sandbox:/mnt/data/image.png)
