from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn

if __name__ == "__main__":
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=44)
    logreg = LogisticRegression()
    logreg.fit(X_train, y_train)
    y_pred = logreg.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    print("Score: %s" % score)
    mlflow.log_metric("score", score)
    mlflow.sklearn.log_model(logreg, "model")
    print("Model saved in run %s" % mlflow.active_run().info.run_uuid)
