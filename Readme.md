# Traffic Road Object Detection

# Project Description
This project aims to develop an efficient and accurate car detection system using the YOLOv5 framework. The model is trained on the Kaggle "Traffic Road Object Detection Dataset" and is designed for real-time traffic monitoring applications.

# Table of Content
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data Preparation](#data-preparation)
- [Model Training](#model-training)
- [Results](#results)
- [Future Work](#future-work)
- [License](#license)

# Installation
To run this project, you need to have Python installed along with the following libraries:
- torch
- torchvision
- opencv-python
- matplotlib
- numpy
- pandas

You can install the required libraries using the following command:
```bash
pip install torch torchvision opencv-python matplotlib numpy pandas
```

# Usage
1. Clone the Repository
```bash
git clone https://github.com/your_username/Traffic-Road-Object-Detection.git
cd Traffic-Road-Object-Detection
```

2. Run the Training script
```bash
python train_yolov5.py
```

# Project Structure
```bash
Traffic-Road-Object-Detection/
├── data/                     # Directory for datasets
│   ├── train/                # Training images and labels
│   ├── val/                  # Validation images and labels
│   └── data.yaml             # Dataset configuration file
├── yolov5/                   # YOLOv5 directory
├── train_yolov5.py           # Training script
└── README.md                 # Project README file
```

# Data preparation
- Ensure the dataset is organized into train and val folders with images and labels.
- Annotations should be in YOLO format with bounding boxes for the "car" class.

# Model Training
The model is trained using YOLOv5 with data augmentation techniques such as rotation, scaling, and color adjustments to enhance data variability.

# Results
- The model achieved high accuracy in detecting cars, with a peak F1 score at a confidence level of 0.7.
- Confusion Matrix and F1-Confidence Curve visualizations are included to evaluate performance.

### Confusion Matrix
![Confusion Matrix](https://github.com/user-attachments/assets/93ec12df-d5b3-401e-ab6a-468fddb04a86)

### F1-Confidence Curve
![F1-Confidence Curve](https://github.com/user-attachments/assets/b6345346-6e52-4a52-96f0-2c6cda0dec77)

### Correlogram of Bounding Box Attributes
![Correlogram](https://github.com/user-attachments/assets/eeef48d7-f384-480a-b8f6-05098367f665)

### Precision-Recall Curve
![PR Curve](https://github.com/user-attachments/assets/334ff32d-6593-453b-8d00-7888ac058aa3)

### Training Batch 0
![Train Batch 0](https://github.com/user-attachments/assets/11ac111f-d3fa-4cfb-a177-c141653aa403)

### Validation Batch 0 Labels
![Val Batch 0 Labels](https://github.com/user-attachments/assets/90336c78-2f1b-4b35-b17b-4486592b7ec8)

### Validation Batch 0 Predictions
![Val Batch 0 Predictions](https://github.com/user-attachments/assets/f529b0b7-5aec-44e9-a611-45062998b489)

# Future Work
- Explore additional data augmentation techniques.
- Implement model pruning and quantization for faster inference.
- Deploy the model for real-time traffic monitoring applications.

# License
This project is licensed under the MIT License. See the LICENSE file for details. Feel free to customize the sections as needed to fit your project specifics.
