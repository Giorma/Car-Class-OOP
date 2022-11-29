class Car:
    def __init__(self, brand=False, model=False, color=False, production_year=False, horse_power=0, is_sport_car=False):
        self.__brand = brand
        self.__model = model
        self.__color = color
        self.__production_year = production_year
        self.__horse_power = horse_power
        self.__is_sport_car = is_sport_car

    def get_brand(self):
        return self.__brand

    def set_brand(self, b):
        self.__brand = b

    def get_model(self):
        return self.__model

    def set_model(self, m):
        self.__model = m

    def get_production_year(self):
        return self.__production_year

    def set_production_year(self, y):
        self.__production_year = y

    def get_color(self):
        return self.__color

    def change_color(self, new_color):
        if self.__color == new_color:
            self.__color = False
        else:
            self.__color = new_color
            return True

    def get_hp(self):
        return self.__horse_power

    def increase_horse_power(self, hp):
        if hp > 0:
            self.__horse_power = True
        elif hp <= 0:
            self.__horse_power = False

    def get_is_sport_car(self):
        return self.__is_sport_car

    def set_is_sport_car(self, x):
        self.__is_sport_car = x









