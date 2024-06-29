import logging
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding, Dropout, Bidirectional, Conv1D, MaxPooling1D, Flatten, GRU
from tensorflow.keras.optimizers import Adam
import numpy as np

def train_and_evaluate_model(X_train, y_train, X_test, y_test, max_len):
    # Initialize the model
    model = Sequential()
    # Add embedding layer for text data
    model.add(Embedding(input_dim=5000, output_dim=128, input_length=max_len))
    # Add convolutional layer for feature extraction
    model.add(Conv1D(filters=128, kernel_size=5, activation='relu'))
    # Add max pooling layer
    model.add(MaxPooling1D(pool_size=2))
    # Add bidirectional GRU layer
    model.add(Bidirectional(GRU(128, dropout=0.3, recurrent_dropout=0.3, return_sequences=True)))
    # Add bidirectional LSTM layer
    model.add(Bidirectional(LSTM(64, dropout=0.3, recurrent_dropout=0.3)))
    # Add dense layer
    model.add(Dense(128, activation='relu'))
    # Add dropout layer to prevent overfitting
    model.add(Dropout(0.5))
    # Flatten the output
    model.add(Flatten())
    # Add output layer
    model.add(Dense(1, activation='sigmoid'))

    # Compile the model
    model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.001), metrics=['accuracy'])

    logging.info("Training model...")
    # Train the model
    model.fit(X_train, y_train, batch_size=32, epochs=40, validation_data=(X_test, y_test))

    # Evaluate the model
    loss, accuracy = model.evaluate(X_test, y_test)
    logging.info(f"Model Accuracy: {accuracy}")

    return model

def predict_bugs(test_cases, model, tokenizer, nlp, max_len):
    from tensorflow.keras.preprocessing.sequence import pad_sequences

    predictions = []
    for case in test_cases:
        # Tokenize test case text
        doc = nlp(case['test_case'])
        tokens = [token.text for token in doc]
        # Convert tokens to sequences
        sequence = tokenizer.texts_to_sequences([tokens])
        # Pad sequences to ensure uniform length
        padded_sequence = pad_sequences(sequence, maxlen=max_len - 2, padding='post')
        # Add additional features
        padded_sequence = np.hstack((padded_sequence, np.zeros((padded_sequence.shape[0], 2))))
        # Make prediction using the model
        prediction = model.predict(padded_sequence)
        predictions.append(int(prediction[0][0] > 0.5))

    # Combine test cases with predictions
    test_cases_with_bugs = []
    for i, case in enumerate(test_cases):
        test_cases_with_bugs.append({
            'requirement': case['requirement'],
            'test_case': case['test_case'],
            'bug_prediction': predictions[i]
        })

    return test_cases_with_bugs
