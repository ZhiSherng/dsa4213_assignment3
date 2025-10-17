import subprocess
import sys
import os
def install_dependencies():
    """install required packages"""
    print("installing dependencies...")
    packages = [
        "transformers",
        "datasets", 
        "torch",
        "accelerate",
        "peft",
        "scikit-learn",
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn"
    ]

    subprocess.run([sys.executable, "-m", "pip", "install", "-q"] + packages)
    print("dependencies installed successfully\n")
  
def run_experiments():
    """execute the jupyter notebook with all experiments"""
    print("running experiments...")
    print("this will train 4 models:")
    print("  1. distilbert-full")
    print("  2. distilbert-lora")
    print("  3. pubmedbert-full")
    print("  4. pubmedbert-lora")
    print("\nexpected runtime: ~90-120 minutes on gpu")
    print("expected runtime: ~4-6 hours on cpu\n")

    #check if notebook exists
    if not os.path.exists("assignment3.ipynb"):
        print("error: assignment3.ipynb not found")
        print("Please ensure the notebook is in the current directory")
        sys.exit(1)

    #execute notebook
    result = subprocess.run([
        "jupyter", "nbconvert",
        "--to", "notebook",
        "--execute", "assignment3.ipynb",
        "--output", "assignment3_results.ipynb"
    ])

    if result.returncode != 0:
        print("\nerror: experiment failed")
        sys.exit(1)

    return result.returncode == 0
  
def check_results():
    """verify that all expected output files were created"""
    expected_files = [
        "final_results.csv",
        "model_comparison.png",
        "confusion_matrices.png",
        "per_class_performance.png"
    ]

    print("\nchecking generated files...")
    all_present = True
    for file in expected_files:
        if os.path.exists(file):
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} (missing)")
            all_present = False

    return all_present
  
def main():
    print("=" * 70)
    print("Fine-tuning pretrained models for medical text classification")
    print("=" * 70)
    print()

    #install dependencies
    try:
        install_dependencies()
    except Exception as e:
        print(f"error installing dependencies: {e}")
        sys.exit(1)

    #run experiments
    try:
        success = run_experiments()
        if not success:
            print("\nexperiments failed")
            sys.exit(1)
    except Exception as e:
        print(f"\nerror running experiments: {e}")
        sys.exit(1)

    #verify results
    print("\n" + "=" * 70)
    print("experiments complete!")
    print("=" * 70)

    if check_results():
        print("\nall results generated successfully")
        print("\noutput files:")
        print("  - final_results.csv: comprehensive results table")
        print("  - model_comparison.png: overall model comparison")
        print("  - confusion_matrices.png: confusion matrices for all models")
        print("  - per_class_performance.png: per-class metrics visualization")
        print("  - assignment3_results.ipynb: executed notebook")
    else:
        print("\nwarning: some output files are missing")
        print("please check the notebook execution for errors")

    print("\n" + "=" * 70)
  
if __name__ == "__main__":
    main()
