
import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).parent / "model.pkl"

model = joblib.load(MODEL_PATH)


def predict_sms(text: str) -> dict:
    if not isinstance(text, str) or not text.strip():
        raise ValueError("SMS text cannot be empty")

    prediction = model.predict([text])[0]
    margin = float(model.decision_function([text])[0])

    classes = list(model.classes_)

    if classes[1] == "fraud":
        fraud_margin = margin
    else:
        fraud_margin = -margin

    return {
        "label": str(prediction),
        "fraud_margin": round(fraud_margin, 4)
    }
