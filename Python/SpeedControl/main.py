print("Система расчёта штрафов")
is_country=True

r_fine_for_20_to_40=500
r_fine_for_40_to_60=1000
r_fine_for_60_to_80=2000
r_fine_for_80_and_more=5000
r_town_speed=60
r_country_speed=90

g_fine_for_4_to_10=15
g_fine_for_40_to_60=200
g_fine_for_60_to_80=400
g_fine_for_80_and_more=1000
g_town_speed=50
g_country_speed=70

car_speed=150
is_town=True
revocation_drive="Вас лишают водительских прав!"

if is_country:
  print("для России, валюта рубль")
  if is_town:
    over_speed = car_speed - r_town_speed
  else:
    over_speed = car_speed - r_country_speed

  if over_speed < 20:
    print("Скорость не превышена или превышена незначительно!")
  elif over_speed >= 4 and over_speed <= 10:
    print("Скорость превышена. Штраф: " + str(g_fine_for_4_to_10))
  elif over_speed >= 40 and over_speed < 60:
    print("Скорость превышена. Штраф: " + str(r_fine_for_40_to_60))

  elif over_speed >= 60 and over_speed < 80:
    print("Скорость превышена. Штраф: " + str(r_fine_for_60_to_80))
    print(revocation_drive)
  elif over_speed >= 80:
    print("Скорость превышена. Штраф: " + str(r_fine_for_80_and_more))
    print(revocation_drive)

else:
  print("для Германии, валюта евро")
  if is_town:
    over_speed = car_speed - g_town_speed
  else:
    over_speed = car_speed - g_country_speed

  if over_speed < 3:
    print("Скорость не превышена или превышена незначительно!")
  elif over_speed >= 4 and over_speed <= 10:
    print("Скорость превышена. Штраф: " + str(g_fine_for_4_to_10))
  elif over_speed >= 40 and over_speed < 60:
    print("Скорость превышена. Штраф: " + str(g_fine_for_40_to_60))
  elif over_speed >= 60 and over_speed < 80:
    print("Скорость превышена. Штраф: " + str(g_fine_for_60_to_80))
  elif over_speed >= 80:
    print("Скорость превышена. Штраф: " + str(g_fine_for_80_and_more))




