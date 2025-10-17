# DSA4213 Assignment 3

## Installation

1. Clone this repository:
```bash
git clone https://github.com/ZhiSherng/dsa4213_assignment3.git
```

2. Change directory:
```bash
cd dsa4213_assignment3
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Reproducing Results

### Option 1: Run all experiments automatically
```bash
python main.py
```

This will:
- Install dependencies
- Fine-tune all 4 models (DistilBERT-Full, DistilBERT-LoRA, PubMedBERT-Full, PubMedBERT-LoRA)
- Generate evaluation metrics and visualizations
- Save results to `final_results.csv`

### Option 2: Run notebook interactively
If Option 1 does not work, download `assignment3.ipynb` and run all the cells.

## Output Files

After running experiments, the following files will be generated:
- `final_results.csv` - comprehensive results table
- `model_comparison.png` - model performance comparison
- `confusion_matrices.png` - confusion matrices for all models
- `per_class_performance.png` - per-class metrics visualization

## Dataset

The Medical Abstracts dataset (`TimSchopf/medical_abstracts`) will be automatically downloaded from HuggingFace when running the code.
