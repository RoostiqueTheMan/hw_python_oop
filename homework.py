from gc import set_debug
from turtle import distance


class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type: str,
                duration: float,
                distance: float,
                speed: float,
                calories: float
                ) -> None:
    
    def get_message(self) - > str:
        print(f'Тип тренировки: {self.training_type};'
              f'Длительность: {self.duration} ч.;'
              f'Дистанция: {self.distance} км;'
              f'Ср. скорость: {self.speed} км/ч;'
              f'Потрачено ккал: {self.calories}.')
        


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65
    M_IN_KM = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * LEN_STEP / M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed = distance / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        InfoMessage()


class Running(Training):
    """Тренировка: бег."""
    def __init__(self, action: int, 
                 duration: float, 
                 weight: float
                 ) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        calories = (coeff_calorie_1 * mean_speed - coeff_calorie_2) * self.weight / M_IN_KM * self.duration


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self, action: int, 
                duration: float, 
                weight: float,
                height: int
                ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        coeff_calorie_1 = 0.035
        coeff_calorie_2 = 2
        coeff_calorie_3 = 0.029
        calories = (coeff_calorie_1 * self.weight + (mean_speed**coeff_calorie_2 // self.height) * coeff_calorie_3 * weight) * self.duration

class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38
    def __init__(self, action: int, 
                duration: float, 
                weight: int, 
                length_pool: int, 
                count_pool: int
                ) -> None:
        super().__init__(action, duration, weight)
        self.lenght_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed = self.lenght_pool * self.count_pool / M_IN_KM / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        coeff_calorie_1 = 1.1
        coeff_calorie_2 = 2
        calories = (mean speed + coeff_calorie_1) * coeff_calorie_2 * self.weight
        

def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

