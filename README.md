# 🌍 Human Development Index (HDI) Prediction using Machine Learning

An end-to-end Machine Learning project developed as part of the **SmartBridge Internship Program**. This project predicts a country's **Human Development Index (HDI)** using a **Linear Regression** model based on four important socio-economic indicators. The trained model is deployed through a **Flask Web Application** with an interactive user interface.

---

# 📋 Table of Contents

- Overview
- Features
- Technologies Used
- Project Structure
- Workflow
- Dataset
- Machine Learning Model
- Installation
- Running the Project
- Web Application
- Screenshots
- Future Enhancements
- GitHub Repository
- Author

---

# 📖 Overview

The Human Development Index (HDI) is a statistical measure developed by the **United Nations Development Programme (UNDP)** to evaluate the overall development of a country.

This project predicts the HDI score using four important indicators:

- 🌍 Life Expectancy
- 📚 Mean Years of Schooling
- 🎓 Expected Years of Schooling
- 💰 Gross National Income (GNI) per Capita

The project follows the complete Machine Learning workflow from data preprocessing to model deployment using Flask.

---

# ✨ Features

- HDI Prediction using Machine Learning
- Data Visualization using Matplotlib & Seaborn
- Data Preprocessing
- Linear Regression Model
- Model Evaluation
- Model Serialization using Pickle
- Flask Web Application
- Responsive User Interface
- GitHub Version Control

---

# 🛠 Technologies Used

## Programming Language

- Python

## Machine Learning

- Scikit-learn
- NumPy
- Pandas

## Data Visualization

- Matplotlib
- Seaborn

## Web Development

- Flask
- HTML5
- CSS3

## Development Tools

- Visual Studio Code
- Jupyter Notebook
- Git
- GitHub

---

# 📂 Project Structure

```
A-Comprehensive-Measure-of-Well-Being
│
├── Dataset
│   └── HDI.csv
│
├── Training
│   └── HumDevIndex.ipynb
│
├── Flask
│   ├── app.py
│   ├── HDI.pkl
│   ├── static
│   │   ├── style.css
│   │   └── bp.png
│   │
│   └── templates
│       ├── home.html
│       ├── indexnew.html
│       └── result.html
│
├── requirements.txt
│
└── README.md
```

---

# 🔄 Project Workflow

### Epic 1 – Environment Setup

- Install Python packages
- Create project folder structure

### Epic 2 – Import Libraries

- Import NumPy
- Import Pandas
- Import Matplotlib
- Import Seaborn
- Import Scikit-learn
- Import Flask

### Epic 3 – Dataset Understanding

- Load Dataset
- Explore Dataset
- Data Visualization

### Epic 4 – Data Preprocessing

- Select Features
- Handle Missing Values
- Prepare Dataset

### Epic 5 – Train-Test Split

- Split dataset into Training and Testing data

### Epic 6 – Model Training

- Train Linear Regression Model
- Generate Predictions
- Evaluate Model

### Epic 7 – Save Model

- Save trained model using Pickle (.pkl)

### Epic 8 – Flask Deployment

- Build Flask Backend
- Create HTML Templates
- Predict HDI Score through Web Application

---

# 📊 Dataset

### Input Features

- Life Expectancy
- Mean Years of Schooling
- Expected Years of Schooling
- Gross National Income (GNI)

### Target Variable

- Human Development Index (HDI)

---

# 🤖 Machine Learning Model

**Algorithm Used**

- Linear Regression

**Model Output**

- Predicted Human Development Index (HDI)

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/Harshithachitikina/A-Comprehensive-Measure-of-Well-Being-project-.git
```

## Open Project

```bash
cd A-Comprehensive-Measure-of-Well-Being
```

## Install Required Packages

```bash
pip install -r requirements.txt
```

If you don't have a requirements file, install manually:

```bash
pip install flask numpy pandas matplotlib seaborn scikit-learn
```

---

# ▶️ Running the Project

Start the Flask Application

```bash
python Flask/app.py
```

Open Browser

```
http://127.0.0.1:5000
```

---

# 🌐 Web Application

The web application consists of three pages:

### 🏠 Home Page

- Introduction to Human Development Index
- Predict button to navigate to prediction page

### 📊 Prediction Page

Users enter:

- Life Expectancy
- Mean Years of Schooling
- Expected Years of Schooling
- Gross National Income

Click **Predict** to generate the HDI score.

### 🎯 Result Page

Displays:

- Predicted Human Development Index (HDI) Score

---



# 🚀 Future Enhancements

- Add Country Dropdown
- Compare Multiple Machine Learning Algorithms
- Improve UI Design
- Deploy Application on Render
- Add User Authentication
- Improve Model Accuracy

---

# 🔗 GitHub Repository

https://github.com/Harshithachitikina/A-Comprehensive-Measure-of-Well-Being-project-

---

# 👩‍💻 Author

**Chitikina Sri Harshitha** and team members

B.Tech – Computer Science and Engineering

SmartBridge Machine Learning Project

---

# 🙏 Acknowledgements

- SmartBridge
- United Nations Development Programme (UNDP)
- Scikit-learn
- Flask
- Python Community
