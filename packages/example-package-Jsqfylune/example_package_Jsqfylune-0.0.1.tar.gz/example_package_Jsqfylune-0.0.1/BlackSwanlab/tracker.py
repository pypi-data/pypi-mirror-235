import threading
import time
from .server import app, update_metrics


class BlackCat:
    def __init__(self, epochs, user_training_func=None):
        self.epochs = epochs
        self.user_training_func = user_training_func or self.default_training_func

    @staticmethod
    def default_training_func(epoch):
        time.sleep(0.1)  # Replace this with actual training code
        loss, accuracy = epoch / 100.0, (
                    100 - epoch) / 100.0  # example metrics, replace with actual metrics calculation
        return loss, accuracy

    def track(self):
        # Start Flask server
        threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 5000}).start()

        # Training loop
        for epoch in range(self.epochs):
            print(f'Starting epoch {epoch + 1}/{self.epochs}')

            # Execute training function and record metrics
            loss, accuracy = self.user_training_func(epoch)
            update_metrics(loss, accuracy)
