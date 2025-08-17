import numpy as np
import sklearn.model_selection
import sklearn.neural_network
import sklearn.metrics
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
x = data.data
y = data.target
split_data = sklearn.model_selection.train_test_split(
    x, y, test_size=0.2, random_state=42)

x_train = split_data[0]
x_test  = split_data[1]
y_train = split_data[2]
y_test  = split_data[3]

clf = sklearn.neural_network.MLPClassifier(
    hidden_layer_sizes=(10,),
    activation="relu",
    solver="sgd",
    learning_rate_init=0.01,
    max_iter=1,         
    warm_start=True,    
    random_state=42)


for epoch in range(20):
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    acc = sklearn.metrics.accuracy_score(y_test, y_pred)
    print("Epoch", epoch + 1, "accuracy:", round(acc, 3))

p_test = x_test[0].reshape(1, -1)
a = clf.predict(p_test)

print("\nPrediction for first test sample:")
if a[0] == 1:
    print("benign")
else:
    print("malignant")