import re
from predictor import predict_sms
SUSPICIOUS_WORDS = [
    "срочно", "немедленно", "заблокирован",
    "подтвердите", "пароль", "код", "карта",
    "перевод", "выиграли", "приз",
    "urgent", "verify", "password",
    "blocked", "winner", "prize", "account"
]


def get_reasons(text: str) -> list:
    text_lower = text.lower()
    reasons = []

    if re.search(r"https?://|www\.", text_lower):
        reasons.append("Сообщение содержит ссылку")

    if re.search(r"\b\d{4,6}\b", text):
        reasons.append("В сообщении есть числовой код")

    found_words = [
        word for word in SUSPICIOUS_WORDS
        if word in text_lower
    ]

    if found_words:
        reasons.append(
            "Обнаружены подозрительные слова: "
            + ", ".join(found_words[:5])
        )

    if not reasons:
        reasons.append("Явных подозрительных признаков не найдено")

    return reasons


def check(text: str) -> dict:
    if not isinstance(text, str) or not text.strip():
        raise ValueError("SMS text cannot be empty")

    prediction = predict_sms(text)

    label = str(prediction["label"])
    margin = float(prediction["fraud_margin"])

    risk = "high" if label == "fraud" else "low"

    return {
        "label": label,
        "risk": risk,
        "score": round(100 / (1 + pow(2.718281828, -margin)), 1),
        "reasons": get_reasons(text)
    }
