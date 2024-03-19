e() else "cpu")

with open(
    "Interface\Chatbot\Datasets\intents.json", "r", encoding="utf-8"
) as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)