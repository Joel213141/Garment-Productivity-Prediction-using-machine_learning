# Garment Productivity Prediction

## Project Overview
This repository contains the code and analysis for predicting employee productivity in the garment manufacturing industry using machine learning models. The project evaluates multiple models including Elastic Net, Support Vector Regression, K-Nearest Neighbors, and Random Forest to identify the most effective predictor of actual productivity. Insights drawn from this analysis can help optimize manufacturing processes and guide strategic decision-making.

## Repository Structure
├── data
│ └── garments_worker_productivity.csv # Dataset used for analysis
├── output
│ ├── model_performance_results.csv # CSV file with model evaluations
│ └── figures
│ └── feature_importance_histogram.png # Histogram of feature importance
├── src
│ ├── preprocessing.py # Script for data preprocessing
│ ├── models.py # Script containing the machine learning models
│ ├── evaluation.py # Script for evaluating models
│ └── main.py # Main script that orchestrates the workflow
└── README.md


### Usage
Run the main script to execute the preprocessing, model training, and evaluation:


## Outputs
The analysis outputs are stored in the `output/` directory. Key outputs include:
- `output/model_performance_results.csv`: A CSV file containing the performance metrics of the evaluated models. [View the CSV file](output/model_performance_results.csv)
- `output/figures/feature_importance_histogram.png`: A histogram showing the importance of different features in the Elastic Net model. ![Feature Importance Histogram](output/figures/feature_importance_histogram.png)
