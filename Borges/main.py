import pickle
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Flatten, Dense, Concatenate

datasets_path = "./datasets/datasets_pkl"

all_files_datasets = [
    f"{datasets_path}/{f}"
    for f in os.listdir(datasets_path)
    if os.path.isfile(os.path.join(datasets_path, f))
]

dataset = []

for file in all_files_datasets:
    with open(file, "rb") as f:
        print(f"Reading file {file}")
        setData = pickle.load(f)
        titles_metadata = setData["text_metadata"]
        texts = setData["text"]

        for i in range(len(titles_metadata)):
            title = titles_metadata[i]["title"]
            text = texts[i]
            dataset.append(f"{title} {text}")


tokenizer = Tokenizer()
tokenizer.fit_on_texts(dataset)
sequences = tokenizer.texts_to_sequences(dataset)
word_index = tokenizer.word_index
max_len = max(len(seq) for seq in sequences)
padded_sequences = pad_sequences(sequences, maxlen=max_len)

categorias = np.array(
    [0, 0, 0, 0, 0],  # Inicialización para una muestra sin categoría asignada
)

# Asignar las categorías para cada muestra en el conjunto de datos
categorias = np.tile(categorias, (len(padded_sequences), 1))



model = Sequential()
model.add(Embedding(input_dim=len(word_index) + 1, output_dim=32, input_length=max_len))
model.add(Flatten())
model.add(Dense(16, activation="relu"))
model.add(
    Dense(5, activation="softmax")
)  # 5 neuronas para las 5 categorías, softmax para clasificación múltiple

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

model.fit(padded_sequences, categorias, epochs=10, batch_size=1)

#ejemplo:
nuevo_titulo = "Ficciones"
nuevo_texto = "Pensar, analizar, inventar (me escribió también) no son actos anómalos, son la normal respiración de la inteligencia. Glorificar el ocasional cumplimiento de esa función, atesorar antiguos y ajenos pensamientos, recordar con incrédulo estupor lo que el doctor universalis pensó, es confesar nuestra languidez o nuestra barbarie. Todo hombre debe ser capaz de todas las ideas y entiendo que en el porvenir lo será."
nueva_entrada = f"{nuevo_titulo} {nuevo_texto}"
nueva_seq = tokenizer.texts_to_sequences([nueva_entrada])
nueva_padded_seq = pad_sequences(nueva_seq, maxlen=max_len)
prediccion = model.predict(nueva_padded_seq)

print("Predicción:", prediccion)

"""
[1, 0, 0, 0, 0],  # Metaficción
[0, 1, 0, 0, 0],  # Laberintos y Espejos
[0, 0, 1, 0, 0],  # Tiempo y Espacio No Lineales
[0, 0, 0, 1, 0],  # Intertextualidad
[0, 0, 0, 0, 1],  # Identidad y Doble
"""