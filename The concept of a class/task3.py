class Employee:
    """Базовый класс сотрудника"""

    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority
        self.grade = 1

    def grade_up(self):
        """Повышение грейда"""
        self.grade += 1

    def publish_grade(self):
        """Публикация результатов грейда"""
        print(f"{self.name}: грейд {self.grade}")

    def check_if_it_is_time_for_upgrade(self):
        pass


class Designer(Employee):
    def __init__(self, name, seniority, awards=2):
        """
        Инициализация дизайнера
        :param name: имя сотрудника
        :param seniority: стаж в годах
        :param awards: количество международных премий (по умолчанию 2)
        """
        super().__init__(name, seniority)
        self.awards = awards

    def check_if_it_is_time_for_upgrade(self):
        """
        Проверка на повышение грейда.
        Каждый год стажа дает 1 балл, каждая международная премия дает 2 балла.
        Для повышения грейда нужно 7 баллов.
        """
        # Стаж дает 1 балл за каждый год
        experience_points = self.seniority
        # Премии дают 2 балла за каждую
        awards_points = self.awards * 2
        # Общее количество баллов
        total_points = experience_points + awards_points

        if total_points >= 7:
            # Повышаем грейд
            self.grade_up()
            # Сбрасываем накопленные баллы (вычитаем 7 баллов)
            points_to_subtract = 7
            # Сначала вычитаем из стажа
            if self.seniority >= points_to_subtract:
                self.seniority -= points_to_subtract
            else:
                points_to_subtract -= self.seniority
                self.seniority = 0
                # Остаток вычитаем из премий (каждая премия "стоит" 2 балла)
                if points_to_subtract > 0:
                    awards_to_subtract = (
                        points_to_subtract + 1
                    ) // 2  # Округляем вверх
                    self.awards = max(0, self.awards - awards_to_subtract)

            print(
                f"{self.name} повышен до грейда {self.grade}! Осталось: стаж {self.seniority} лет, премий {self.awards}"
            )
            return True
        return False


# Пример использования
if __name__ == "__main__":
    # Создаем дизайнера с 2 премиями (по умолчанию)
    designer = Designer("Анна", seniority=0, awards=2)
    print(
        f"Начальные данные: {designer.name}, грейд {designer.grade}, стаж {designer.seniority} лет, премий {designer.awards}"
    )

    # Проверяем повышение (2 премии * 2 = 4 балла, нужно 7)
    designer.check_if_it_is_time_for_upgrade()

    # Добавляем стаж
    designer.seniority = 3  # 3 года стажа + 4 балла от премий = 7 баллов
    designer.check_if_it_is_time_for_upgrade()

    # Публикуем итоговый грейд
    designer.publish_grade()
