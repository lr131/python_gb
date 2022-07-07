import time


class TrafficLight:
    __states = (('red', 7), ('yellow', 2), ('green', 10))
    __color = 'red'

    def running(self, work_time):
        """Запуск светофора

        @:param work_time длительность работы светофора"""
        start_time = time.time()
        print(f"Заданное время: {work_time}"
              f"Светофор запущен")
        if work_time < self.__states[0][1]:
            print(f"Предупреждение! Светофор всегда запускается с режима "
                  f"{self.__states[0][0]} продолжительностью "
                  f"{self.__states[0][1]} секунд. Продолжительность неизменна "
                  f"по условиям задачи. Время работы будет изменено на "
                  f"минимально допустимое!\n"
                  f"Светофор будет работать {self.__states[0][1]} секунд")

        while (time.time() - start_time) <= work_time:
            for state in self.__states:
                self.__color = state[0]
                print(f"Цвет светофора: {self.__color}; "
                      f"время работы: {state[1]}")
                time.sleep(state[1])
                if (time.time() - start_time) > work_time:
                    print("Завершение работы светофора")
                    break
