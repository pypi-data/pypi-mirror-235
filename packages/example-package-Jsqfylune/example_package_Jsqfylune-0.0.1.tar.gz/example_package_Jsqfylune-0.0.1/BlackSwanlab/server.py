from flask import Flask, jsonify

app = Flask(__name__)

# Data
losses = []
accuracies = []


@app.route('/metrics', methods=['GET'])
def get_metrics():
    return jsonify({'loss': losses, 'accuracy': accuracies})


def update_metrics(loss, accuracy):
    global losses, accuracies
    losses.append(loss)
    accuracies.append(accuracy)
