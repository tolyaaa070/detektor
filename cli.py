from backend import check


def main():
    print("================================")
    print("       SMS GUARD")
    print(" Phishing SMS Detection System")
    print("================================")
    print("Введите SMS или exit для выхода\n")

    while True:
        text = input("SMS > ").strip()

        if text.lower() == "exit":
            print("Завершение SMS Guard.")
            break

        if not text:
            print("Введите текст сообщения.")
            continue

        try:
            result = check(text)

            print("\nРЕЗУЛЬТАТ ПРОВЕРКИ")
            print("Класс:", result["label"])
            print("Уровень риска:", result["risk"])
            print("Индекс риска:", result["score"])

            print("Причины:")
            for reason in result["reasons"]:
                print("-", reason)

            print("-" * 40)

        except Exception as error:
            print("Ошибка проверки:", error)


if __name__ == "__main__":
    main()
