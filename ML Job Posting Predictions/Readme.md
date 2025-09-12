# Machine Learning — Job Posting Predictions

## 📌 Project Overview
This project focuses on predicting and analyzing job postings, using data extracted from **LinkedIn job listings**.  
The goal is to apply **machine learning and natural language processing (NLP)** to classify, cluster, and forecast characteristics of job postings — such as industry, seniority level, required skills, and potential salary range.

The project was implemented in a **Jupyter Notebook** (`Final_Linkedin_Job_postings.ipynb`), combining **data preprocessing, exploratory analysis, feature engineering, and predictive modeling**.

---

## 🏗️ Methodology

### 1. Data Collection
- Dataset of LinkedIn job postings collected through scraping and/or API access.  
- Included fields: job title, description, company, location, industry, posting date, and engagement metrics.  

### 2. Data Preprocessing
- Cleaning of job descriptions (removal of HTML tags, stopwords, punctuation).  
- Text normalization (lowercasing, tokenization, lemmatization).  
- Encoding of categorical variables (industry, seniority, contract type).  
- TF-IDF vectorization for job descriptions.

### 3. Modeling
- **Classification Models**:
  - Logistic Regression  
  - Random Forest  
  - Gradient Boosted Trees (XGBoost)  
- **Clustering**:
  - K-Means to group job postings by textual similarity.  
- **Prediction Tasks**:
  - Predicting seniority level from description text.  
  - Forecasting likelihood of high engagement (views/applicants).  

### 4. Evaluation
- Accuracy, F1-score, and ROC-AUC for classification tasks.  
- Silhouette score for clustering quality.  
- Cross-validation to validate generalization.

---

## 📊 Results
- Best performing model: **XGBoost Classifier**, with F1-score ~0.88 in predicting seniority levels.  
- Identified clusters of job postings aligned with **Tech, Finance, Healthcare, and Consulting**.  
- Extracted most relevant keywords driving classification (e.g., “Python”, “Agile”, “SQL”, “Cloud”).  
- Predictive pipeline for estimating **job posting performance** showed reliable differentiation between low vs high applicant engagement.

---

## 💻 Demo Notebook
All steps are documented in the Jupyter Notebook:  
[`Final_Linkedin_Job_postings.ipynb`](./Final_Linkedin_Job_postings.ipynb)  

It includes:
- Data cleaning and preprocessing.  
- Feature engineering (TF-IDF, categorical encoding).  
- Model training and evaluation.  
- Clustering analysis and keyword extraction.  

---

## ✅ Applications
- **Recruitment analytics**: Help HR teams understand job market dynamics.  
- **Career guidance**: Insights into in-demand skills and industries.  
- **Business intelligence**: Forecast hiring trends across industries.  

---

## 🔒 Confidentiality Disclosure
This repository contains **demo data and models for portfolio purposes**.  
No confidential or proprietary LinkedIn datasets are included.
