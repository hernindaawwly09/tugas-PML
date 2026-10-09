"""
model_lstm.py — Model LSTM untuk prediksi time series koordinat kutub
"""
import numpy as np


def build_lstm_model(input_shape, units=64, dropout=0.2):
    """
    Membangun arsitektur model LSTM.
    Memerlukan TensorFlow/Keras.
    """
    try:
        from tensorflow import keras
        from tensorflow.keras import layers

        model = keras.Sequential([
            layers.LSTM(units, activation="tanh", return_sequences=True,
                        input_shape=input_shape),
            layers.Dropout(dropout),
            layers.LSTM(units // 2, activation="tanh"),
            layers.Dropout(dropout),
            layers.Dense(1),
        ])
        model.compile(optimizer="adam", loss="mse", metrics=["mae"])
        return model
    except ImportError:
        raise ImportError("TensorFlow belum terinstall. Jalankan: pip install tensorflow")


def train_lstm(X_train, y_train, X_val, y_val,
               epochs=100, batch_size=8, patience=15):
    """Melatih model LSTM dengan EarlyStopping."""
    from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

    input_shape = (X_train.shape[1], X_train.shape[2])
    model = build_lstm_model(input_shape)

    callbacks = [
        EarlyStopping(patience=patience, restore_best_weights=True),
        ModelCheckpoint("results/best_lstm.h5", save_best_only=True),
    ]

    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=epochs,
        batch_size=batch_size,
        callbacks=callbacks,
        verbose=1,
    )
    return model, history


def reshape_for_lstm(X: np.ndarray) -> np.ndarray:
    """Reshape X dari (samples, timesteps) ke (samples, timesteps, 1)."""
    return X.reshape(X.shape[0], X.shape[1], 1)
