import requests
import matplotlib.pyplot as plt


def generate_text(prompt):

    API_URL = (
        "https://api-inference.huggingface.co/models/duxprajapati/symptom-disease-model"
    )

    headers = {"Authorization": f"Bearer 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"}

    data = {"inputs": prompt}

    response = requests.request("POST", API_URL, headers=headers, json=data)

    print(response.json())
    labels = response.json()[0][:5]
    return labels


prompt = "I have a headache and a runny nose. What do I have?"

print(generate_text(prompt))
labels = generate_text(prompt)

# Convert string values to float and get the first 5 labels
values = [float(x["score"]) for x in labels[:5]]
labels = labels[:5]

label_names = [x["label"] for x in labels]
scores = [float(x["score"]) for x in labels]
# If there are more than 5 labels, group the rest into an "Others" category
if len(label_names) > 5:
    scores.append(sum(float(x["score"]) for x in labels[5:]))
    label_names.append("Others")

# Create a pie chart
fig, ax = plt.subplots()
ax.pie(values, labels=labels, autopct="%1.1f%%")
plt.show()
