import random
import json
import numpy as np
import pickle

import torch

from model import NeuralNet
from nltk_utilis import bag_of_words, tokenize


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

with open(
    "Interface\Chatbot\Datasets\intents.json", "r", encoding="utf-8"
) as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "\n\n"


def chat(sentence):
    sentence = tokenize(sentence)

    with open("finalized_model.sav", "rb") as file:
        diseas_model = pickle.load(file)

    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                response = f"{bot_name}"

                for i in range(len(intent["responses"])):
                    response += intent["responses"][i] + "\n"

                with open("Interface\Chatbot\Datasets\disease_symptoms.csv", "r") as f:
                    response += "\nSymptoms: \n\n"
                    data = f.readlines()
                    for line in data:
                        if tag.lower() in line.split(",")[0].lower():
                            symptoms = [
                                "* " + word.strip()
                                for word in line.split(",")[1:]
                                if word.strip() != ""
                            ]
                            response += "\n".join(symptoms)
                            break
                return response

    else:
        return f"{bot_name}: I do not understand..."


if __name__ == "__main__":
    chat()
