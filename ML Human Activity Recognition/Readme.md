# Machine Learning — Human Activity Recognition

## 📌 Project Overview
This project implements a **Human Activity Recognition (HAR)** system using machine learning techniques.  
The dataset consists of smartphone sensor measurements (accelerometer and gyroscope) collected from individuals performing daily activities such as walking, sitting, standing, laying, walking upstairs, and walking downstairs.  

The objective was to build, train, and evaluate models capable of automatically classifying human activity from sensor data.

---

## 🏗️ Methodology

### 1. Data Preprocessing
- Cleaned and normalized accelerometer and gyroscope readings.  
- Split dataset into **training and test sets** (stratified to preserve class distribution).  
- Applied feature extraction (time and frequency domain features).  

### 2. Model Development
Several machine learning algorithms were trained and compared:
- **Logistic Regression**  
- **Random Forest Classifier**  
- **Support Vector Machines (SVM)**  
- **Neural Networks (MLP)**  

### 3. Evaluation
- Used **accuracy, precision, recall, F1-score** as metrics.  
- Generated **confusion matrices** to analyze per-class performance.  
- Applied **cross-validation** to validate generalization.

---

## 📊 Results
- **Random Forest** achieved the best performance overall (highest accuracy and balanced precision/recall across classes).  
- Activities like *walking upstairs* and *walking downstairs* showed higher confusion with each other, while *sitting* and *laying* were easily distinguishable.  
- The final model achieved over **93% accuracy** on the test set.  

---

## 💻 Demo Notebook
- The complete workflow is implemented in [`Assignment_Human_Recognition.ipynb`](./Assignment_Human_Recognition.ipynb).  
- The notebook includes:
  - Data preprocessing steps.  
  - Model training and evaluation.  
  - Visualization of confusion matrices and metrics.  

---

## ✅ Benefits & Applications
- **Healthcare**: Monitor patients’ physical activities remotely.  
- **Sports science**: Analyze athletes’ movement and performance.  
- **Smart devices**: Enable activity-based personalization on wearables.  

---

## 🔒 Confidentiality Disclosure
This repository contains only **public dataset experiments and demo code**.  
No personal or confidential sensor data has been included.
