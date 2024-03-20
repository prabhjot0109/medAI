import requests
import matplotlib.pyplot as plt

def generate_text(prompt):
    API_URL = "https://api-inference.huggingface.co/models/duxprajapati/symptom-disease-model"
    headers = {"Authorization": f"Bearer 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"}
    data = {"inputs": prompt}

    response = requests.request("POST", API_URL, headers=headers, json=data)
    labels = response.json()[0][:5]

    # Convert string values to float and get the first 5 labels
    values = [float(x["score"]) for x in labels]
    labels = [x["label"] for x in labels]

    return labels, values  # Return the predicted diseases and their scores

def plot_diseases(labels, values):
    # If there are more than 5 labels, group the rest into an "Others" category
    if len(labels) > 5:
        values.append(sum(float(x["score"]) for x in labels[5:]))
        labels.append("Others")

    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%1.1f%%")
    plt.show()

# Example usage:
# prompt = "I have a headache and a runny nose. What do I have?"
# labels, values = generate_text(prompt)
# plot_diseases(labels, values)