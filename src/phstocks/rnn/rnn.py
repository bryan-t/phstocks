import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from joblib import dump, load
import json
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout

class RNN:
    def __init__(self, f="", dataset=None):
        if f:
            self.sc = load(f+'.sc')
            self.rnn = tf.keras.models.load_model(f + ".model")
            with open(f+'.info') as dumpfile:
                info = json.load(dumpfile)
                self.accuracy = info['accuracy']
                __loaded_from_file__ = True
            return
    

    def train(self, dataset, test_size):
        train_size = len(dataset) * (1 - test_size)
        train_size = int(train_size)
        train_set = dataset[:train_size]
        test_set = dataset[train_size - 60:]

        return

        # Splitting the dataset into the Training set and Test set
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, random_state = 0)
        train_set = np.append(X_train, y_train, axis = 1)
        test_set = np.append(X_test, y_test, axis = 1)
        test_set = np.append(train_set[-60:])

        # Feature Scaling
        self.sc = MinMaxScaler(feature_range = (0, 1))
        train_set = self.sc.fit_transform(train_set)
        
        # Creating a data structure with 60 timesteps and 1 output
        X_train = []
        y_train = []
        for i in range(60, len(train_set)):
            X_train.append(train_set[i-60:i, 0])
            y_train.append(train_set[i, 0])
        X_train, y_train = np.array(X_train), np.array(y_train)

        # Reshaping
        X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

        # Initialising the RNN
        rnn = Sequential()

        # Adding the first LSTM layer and some Dropout regularisation
        rnn.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
        rnn.add(Dropout(0.2))

        # Adding a second LSTM layer and some Dropout regularisation
        rnn.add(LSTM(units = 50, return_sequences = True))
        rnn.add(Dropout(0.2))

        # Adding a third LSTM layer and some Dropout regularisation
        rnn.add(LSTM(units = 50, return_sequences = True))
        rnn.add(Dropout(0.2))

        # Adding a fourth LSTM layer and some Dropout regularisation
        rnn.add(LSTM(units = 50))
        rnn.add(Dropout(0.2))

        # Adding the output layer
        rnn.add(Dense(units = 1))

        # Compiling the RNN
        rnn.compile(optimizer = 'adam', loss = 'mean_squared_error')


        # Training the ANN on the Training set
        self.rnn.fit(X_train, y_train, batch_size = 32, epochs = 100)

        y_pred = self.rnn.predict(X_test)
        # Evaluating the Model Performance
        from sklearn.metrics import r2_score, mean_absolute_error
        self.accuracy = r2_score(y_test, y_pred)
        #self.accuracy = 1 - (mean_absolute_error(y_test, y_pred) /
        #                     np.mean(y_test))
        print('ANN Accuracy:', self.accuracy)


    def save(self, f):
        self.rnn.save(f+'.model')
        dump(self.sc, f+'.sc')
        info = {}
        info['accuracy'] = self.accuracy
        with open(f+'.info', 'w') as dumpfile:
            json.dump(info, dumpfile)

    def predict(self, X):
        return self.rnn.predict(self.sc.transform(X))
