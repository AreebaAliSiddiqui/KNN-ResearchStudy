import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def run_knn_sweep(X_train, X_test, y_train, y_test, k_values, minkowski_p=3):
    """
    Sweeps KNN classifiers across Euclidean, Manhattan, and Minkowski metrics for a range of K values.
    """
    distance_metrics = {
        "euclidean": {"metric": "minkowski", "p": 2},
        "manhattan": {"metric": "minkowski", "p": 1},
        "minkowski": {"metric": "minkowski", "p": minkowski_p},
    }

    results = []
    for dist_name, params in distance_metrics.items():
        for k in k_values:
            model = KNeighborsClassifier(
                n_neighbors=k, 
                metric=params["metric"], 
                p=params["p"]
            )
            model.fit(X_train, y_train)
            preds = model.predict(X_test)
            acc = accuracy_score(y_test, preds)
            results.append({"distance": dist_name, "k": k, "accuracy": acc})

    return pd.DataFrame(results)