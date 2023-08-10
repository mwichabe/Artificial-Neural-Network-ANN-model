# Augmented Reality Acceptance in Nursing Education

This repository contains code for assessing the acceptance of augmented reality in nursing education using an Artificial Neural Network (ANN). The analysis is based on the paper "Assessing Acceptance of Augmented Reality in Nursing Education."

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Data](#data)
- [Running the Code](#running-the-code)
- [Results](#results)

## Introduction


This project aims to assess the acceptance of augmented reality (AR) technology in nursing education using an Artificial Neural Network (ANN). The ANN is trained on a dataset containing various input features related to nursing education and a target output representing acceptance levels.

## Getting Started

To replicate the analysis, follow the steps below:

1. Clone this repository to your local machine.
2. Make sure you have Python (>=3.6) and the required dependencies installed. You can install dependencies using the following command:

## Data

The dataset used for this analysis contains information related to nursing education and augmented reality acceptance. Features include factors such as Q1, Q2, Q3, Q4, Q5, and totalseconds. The target variable is "totalvalue," representing the acceptance level of augmented reality.

- Q1 to Q5: Various survey questions or ratings related to augmented reality acceptance.
- totalseconds: The total time spent on an augmented reality application.

The dataset is available in the file `248.csv`.

## Running the Code

1. Ensure you have the required data file (`248.csv`) in the project directory.
2. Modify the data preprocessing steps and model architecture if necessary in the `main.py` file.

The code will preprocess the data, build and train the ANN model, and evaluate its performance.

## Results

After running the code, the ANN model will be trained and evaluated. The final output will include the Mean Squared Error (MSE) on the test set, which provides a measure of the model's accuracy in predicting augmented reality acceptance.

The ANN result data, including the loss values during training, will be displayed in the terminal as the model runs. The loss values represent the difference between predicted and actual acceptance levels. Lower loss values indicate better model performance.

