import os
from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy
from flask_celery import make_celery
from algorithm import tfidf, dump_model, test_SVM, load_model
from sklearn import cross_validation
import json

app = Flask(__name__)
app.secret_key = "flask_algorithm"
app.config.update(
    CELERY_BROKER_URL="redis://redis:6379",
    CELERY_RESULT_BACKEND="redis://redis:6379",
    SQLALCHEMY_DATABASE_URI="postgresql://postgres:postgres@db:5432/postgres",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
db = SQLAlchemy(app)
celery = make_celery(app)


def create_data():
    labels = []
    texts = []
    with db.engine.connect() as con:
        r = con.execute("SELECT * FROM data_data")
        for raw in r:
            labels.append(raw[1])
            texts.append(raw[2])
    return labels, texts


@celery.task()
def celery_train():
    label, text = create_data()
    training, vectorizer = tfidf(text)
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(training, label, test_size=0.25,
                                                                         random_state=0)
    model, accuracy, precision, recall = test_SVM(x_train, x_test, y_train, y_test)
    dump_model(model, 'model.pickle')
    dump_model(vectorizer, 'vectorizer.pickle')
    return "OK"


@app.route('/train', methods=["POST"])
def train():
    celery_train.delay()
    return Response(json.dumps({"status": 200}), status=200, mimetype="application/json")


@app.route('/predict/<string:user_text>', methods=["POST"])
def predict(user_text):
    if os.path.exists("app/model.pickle") and os.path.exists("app/vectorizer.pickle"):
        model = load_model('app/model.pickle')
        vectorizer = load_model('app/vectorizer.pickle')
        result = model.predict(vectorizer.transform([user_text]))
        prediction = {"prediction": result[0]}
        return prediction
    else:
        return Response(json.dumps({"error": "There is no pickle, please run train"}), status=500,
                        mimetype="application/json")
