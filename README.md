# PredictiveProject2
Breast Cancer Tumor Classification Using Clinical Features

**Dataset Information**

The dataset used is the Breast Cancer Wisconsin Diagnostic Dataset.

Dataset Shape

before preprocessing

Rows: 569 and 
Columns: 33 

After preprocessing:

Rows: 569 and 
Columns: 31

**Target Variable**

The target column is: diagnosis


This column represents whether the tumor is:

M → Malignant (Cancerous)

B → Benign (Non-cancerous)

After label encoding:

Benign (B) = 0

Malignant (M) = 1

Distribution of Target Variable

Benign cases: 357

Malignant cases: 212


# Model Training
Models Used
Logistic Regression
A linear model suitable for binary classification problems.

Support Vector Machine (SVM)
Finds the optimal hyperplane that separates the two classes.

Random Forest
An ensemble model that combines multiple decision trees.

# Evaluation metrics
| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|------|---------:|----------:|-------:|---------:|--------:|
| Logistic Regression | 0.964912 | 0.952381 | 0.952381 | 0.952381 | 0.996032 |
| SVM | 0.982456 | 1.0000 | 0.952381 | 0.975610 | 0.996032 |
| Random Forest | 0.973684 | 1.0000 | 0.928571 | 0.962963 | 0.995205 |

# Visualization
# Feature Selection
<img width="1297" height="602" alt="image" src="https://github.com/user-attachments/assets/b72859f0-5f63-4cc0-b956-776a9e725bc5" />

# ROC Curve
<img width="810" height="601" alt="image" src="https://github.com/user-attachments/assets/1ae7e8d8-f1cc-4802-a524-0647f3a576e6" />

# Model Accuracy
<img width="797" height="520" alt="image" src="https://github.com/user-attachments/assets/1f44967c-4b40-4646-934c-3c9a29458e72" />

# Deployment app
https://predictiveproject2-cw9kes4f3hmzgky3grkhdg.streamlit.app/
<img width="1917" height="857" alt="image" src="https://github.com/user-attachments/assets/f3339bcc-545b-45b5-a316-2ba4f8d08607" />

