salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0
current_spend = spend
current_month = 1

while current_month <= months:
  if current_month > 1:
    current_spend *= (1 + increase)
  money_capital += max(0, current_spend - salary)
  current_month += 1

needed_money_capital = round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", needed_money_capital)
