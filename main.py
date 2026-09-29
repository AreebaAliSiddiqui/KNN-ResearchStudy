import pandas as pd
from src.preprocessing import load_and_preprocess_data
from src.model import run_knn_sweep
from src.evaluation import summarize_results

DATASETS = [
    {
        "label": "Dataset A",
        "path": "data/diabetes.csv",
        "target": "Outcome",
        "paper_acc": 0.8571
    },
    {
        "label": "Dataset B",
        "path": "data/dataset_b.csv",
        "target": "Target",
        "paper_acc": 0.7800
    },
    {
        "label": "Dataset C",
        "path": "data/dataset_c.csv",
        "target": "Class",
        "paper_acc": 0.9210
    },
    {
        "label": "Dataset D",
        "path": "data/dataset_d.csv",
        "target": "Label",
        "paper_acc": 0.8150
    }
]

K_VALUES = list(range(1, 31, 2))

if __name__ == "__main__":
    all_summaries = []

    for ds in DATASETS:
        X_train, X_test, y_train, y_test = load_and_preprocess_data(
            csv_path=ds["path"], 
            target_col=ds["target"]
        )

        results_df = run_knn_sweep(
            X_train, X_test, y_train, y_test, 
            k_values=K_VALUES
        )

        summary = summarize_results(
            results_df=results_df, 
            dataset_label=ds["label"], 
            paper_accuracy=ds["paper_acc"]
        )
        summary["dataset"] = ds["label"]
        all_summaries.append(summary)

    final_table = pd.concat(all_summaries, ignore_index=True)
    final_table.to_csv("summary_results.csv", index=False)
    print("\nBatch execution complete. Results saved to summary_results.csv.")