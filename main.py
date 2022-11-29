from Classes.car import Car

car1 = Car('Lada', "03", 'Black', 1992, 92, True)
car1.set_brand('Toyota')
car1.set_model('Supra')
car1.set_production_year(1999)
car1.change_color("Black")
car1.increase_horse_power(32)

print(f" Make: {car1.get_brand()}\n"
      f" Model: {car1.get_model()}\n "
      f"Color: {car1.get_color()}\n"
      f" Year: {car1.get_production_year()}\n "
      f"Horse Power: {car1.get_hp()}\n"
      f" is Sport Car: {car1.get_is_sport_car()} ")

""" Output

  Make: Toyota
  Model: Supra
  Color: False
  Year: 1999
  Horse Power: True
  is Sport Car: True 

"""