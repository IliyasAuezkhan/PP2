import re
import json

# читаем файл
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 1 Извлечь все цены
prices = re.findall(r"\d[\d ]*,\d{2}", text)

# 2 Найти названия товаров
products = re.findall(r"\d+\.\n(.+)", text)

# 3 Посчитать итоговую сумму
total = sum(float(p.replace(" ", "").replace(",", ".")) for p in prices)

# 4 Извлечь дату и время
datetime = re.search(r"\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}", text)
datetime = datetime.group() if datetime else None

# 5 Метод оплаты
payment = "Банковская карта" if re.search(r"Банковская карта", text) else "Другой"

# 6 Структурированный вывод (JSON)
data = {
    "products": products,
    "prices": prices,
    "total": total,
    "datetime": datetime,
    "payment": payment
}


print(json.dumps(data, ensure_ascii=False, indent=2))
