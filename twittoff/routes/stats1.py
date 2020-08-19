from flask import Blueprint, request, jsonify,  flash, redirect # render_template
from sklearn.datasets import load_iris # just to have some data to use when predicting
from sklearn.linear_model import LogisticRegression
from twittoff.stats_models import load_model

stats1 = Blueprint("stats1", __name__)

# TODO: accept somem imputs related to the iris training data...
@stats1.route("/stats/iris")
def iris():
    #model = load_model()
    X, y = load_iris(return_X_y=True) # just to have some data to use when predicting
    #clf = load_model()
    clf =LogisticRegression(random_state=0, solver="lbfgs", multi_class="multinomial")
    clf.fit(X, y)

    #result = model.predict(X[:2, :])
    result = str(clf.predict(X[:2, :]))
    print("PREDICTION", result)
    return result
    #return str(results)