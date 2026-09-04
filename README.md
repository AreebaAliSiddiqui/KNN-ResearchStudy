# KNN Research Study

An experimental study investigating the performance of the **K-Nearest Neighbors (KNN)** algorithm on datasets used in existing machine learning research.

## Overview

This study explores how KNN performs on datasets obtained from existing research papers and investigates how different hyperparameter configurations and preprocessing techniques affect its performance.

Approximately **45 research papers** are analyzed to identify the datasets used in previous studies. The corresponding datasets are obtained from sources such as Kaggle and evaluated using KNN.

The results are compared with the reported findings from the original research papers to analyze the performance of KNN and identify potential research gaps.

## Objectives

* Analyze existing research papers and identify the datasets used in their experiments.
* Obtain the corresponding datasets from publicly available sources.
* Implement the K-Nearest Neighbors algorithm in Python.
* Investigate the effect of different values of `k` on model performance.
* Experiment with relevant preprocessing and hyperparameter configurations.
* Evaluate KNN using appropriate performance metrics.
* Compare KNN results with the results reported in existing research.
* Analyze patterns in KNN performance across different datasets.
* Identify potential research gaps and areas for further investigation.

## Research Questions

1. How does KNN perform on datasets used in existing machine learning research?
2. How does changing the value of `k` affect KNN performance?
3. How do preprocessing and other hyperparameter configurations influence KNN performance?
4. How does KNN performance compare with the results reported in existing research?
5. On which types of datasets does KNN perform particularly well or poorly?
6. What potential research gaps can be identified from the experimental results?

## Methodology

The study follows the following workflow:

```text
Research Papers
       ↓
Dataset Identification
       ↓
Dataset Acquisition
       ↓
Data Exploration & Preprocessing
       ↓
KNN Implementation
       ↓
Hyperparameter Experiments
       ↓
Performance Evaluation
       ↓
Comparison with Reported Results
       ↓
Research Gap Analysis
```

### 1. Research Paper Analysis

Approximately 10 research papers are reviewed to identify:

* Dataset used
* Dataset characteristics
* Machine learning model used
* Reported performance
* Evaluation metrics
* Experimental methodology

### 2. Dataset Acquisition

The datasets identified from the research papers are obtained from publicly available sources, including Kaggle where applicable.

Dataset links and relevant information are maintained in the paper metadata.

### 3. Data Preprocessing

Depending on the dataset, preprocessing may include:

* Handling missing values
* Encoding categorical variables
* Feature scaling
* Feature selection
* Train/test splitting
* Other dataset-specific preprocessing

### 4. KNN Implementation

KNN is implemented and evaluated using Python and relevant machine learning libraries.

The primary hyperparameter investigated is:

```text
k = number of nearest neighbors
```

Multiple values of `k` are tested to investigate their effect on model performance.

### 5. Performance Evaluation

KNN performance is evaluated using appropriate metrics depending on the dataset and research problem.

Possible metrics include:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion matrix

### 6. Comparative Analysis

The experimentally obtained KNN results are compared with the performance reported in the corresponding research papers.

The comparison is used to investigate whether KNN can achieve competitive performance under the experimental setup used in this study.

## Results

Experimental results will be documented in the `results/` directory.

The analysis will include:

* Performance across different values of `k`
* Best-performing KNN configuration
* Comparison with reported research results
* Dataset-level performance analysis
* Visualizations of experimental results

## Research Gap Analysis

The study will summarize observations and potential research gaps identified across the reviewed papers and experiments.

A structured research-gap table will include information such as:

| Paper   | Dataset   | Existing Method | Reported Result | Best KNN Configuration | KNN Result | Observation | Research Gap |
| ------- | --------- | --------------- | --------------: | ---------------------- | ---------: | ----------- | ------------ |
| Paper 1 | Dataset A | Model X         |               — | k = —                  |          — | —           | —            |
| Paper 2 | Dataset B | Model Y         |               — | k = —                  |          — | —           | —            |

## Technologies

* Python
* Google Colab
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Seaborn

## Repository Structure

```text
knn-research-study/
│
├── README.md
├── papers/
├── datasets/
├── notebooks/
├── src/
├── results/
├── research/
├── requirements.txt
└── .gitignore
```

## Reproducibility

The experiments are primarily developed using Google Colab notebooks.

Dataset sources, preprocessing steps, hyperparameter configurations, and experimental results will be documented to make the experiments as reproducible as possible.

## Authors

* Areeba Ali

## Status

🚧 **In Progress**

The research-paper analysis, dataset collection, KNN experiments, and research-gap analysis are currently in progress.
