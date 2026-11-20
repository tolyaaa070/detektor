from backend import check

messages = [
    "Ваш аккаунт заблокирован! Срочно подтвердите данные",
    "Спасибо за оплату. Хорошего дня!",
    "Вы выиграли приз! Перейдите по ссылке"
]

for message in messages:
    print("\nSMS:", message)
    print(check(message))