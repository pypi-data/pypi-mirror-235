import sklearn
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, f1_score, recall_score,\
                            roc_auc_score, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def eval(
    gs: sklearn.model_selection.GridSearchCV,
    X_train: pd.DataFrame,
    y_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_test: pd.DataFrame,
    LABEL_NAMES: list,
    nb_display: bool = False,
):
    y_pred_train = gs.best_estimator_.predict(X_train)
    AVERAGE = 'weighted'
    tn, fp, fn, tp = confusion_matrix(y_train, y_pred_train).ravel()
    accuracy_train = accuracy_score(y_train, y_pred_train)
    precision_train = precision_score(y_train, y_pred_train, average=AVERAGE)
    f1_train = f1_score(y_true=y_train, y_pred=y_pred_train, average=AVERAGE)
    sensitivity_train = recall_score(y_true=y_train, y_pred=y_pred_train)
    specificity_train = recall_score(y_true=y_train, y_pred=y_pred_train, pos_label=0)
    auc_train = roc_auc_score(y_train, y_pred_train, average=AVERAGE)
    print("TRAIN SET RESULTS")
    print("TN, FP, FN, TP       :", tn, fp, fn, tp)
    print("Accuracy (Train)     :", accuracy_train)
    print("Precision (Train)    :", precision_train)
    print("Sensitivity (Train)  :", sensitivity_train)
    print("Specificity (Train)  :", specificity_train)
    print("F1-Score (Train)     :", f1_train)
    print("AUC Score (Train)    :", auc_train)
    print(classification_report(y_train, y_pred_train, target_names=LABEL_NAMES))
    if nb_display:
        print()
        ConfusionMatrixDisplay.from_predictions(
            y_train, y_pred_train,
            display_labels=LABEL_NAMES,
            cmap=plt.cm.Blues,
            text_kw={
                "fontsize": 16
            }
        )
        plt.show()
        print()


    y_pred = gs.best_estimator_.predict(X_test)
    AVERAGE = 'weighted'
    f1 = f1_score(y_true=y_test, y_pred=y_pred, average=AVERAGE)

    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    accuracy = (tp + tn) / (tp + fp + tn + fn)
    num_positives = len(np.where(y_test == 1)[0])
    num_negatives = len(np.where(y_test == 0)[0])
    precision = (num_positives*(tp / (tp + fp)) + num_negatives*(tn / (tn + fn))) / (num_positives + num_negatives)
    sensitivity = tp / (tp + fn)
    specificity = tn / (tn + fp)
    auc = roc_auc_score(y_test, y_pred, average=AVERAGE)
    print("TEST SET RESULTS")
    print("TN, FP, FN, TP       :", tn, fp, fn, tp)
    print("Accuracy             :", accuracy)
    print("Precision            :", precision)
    print("Sensitivity          :", sensitivity)
    print("Specificity          :", specificity)
    print("F1-Score             :", f1)
    print("AUC Score            :", auc)
    print(classification_report(y_test, y_pred, target_names=LABEL_NAMES))
    if nb_display:
        print()
        ConfusionMatrixDisplay.from_predictions(
            y_test, y_pred,
            display_labels=LABEL_NAMES,
            cmap=plt.cm.Blues,
            text_kw={
                "fontsize": 16,
            },
        )
        plt.show()