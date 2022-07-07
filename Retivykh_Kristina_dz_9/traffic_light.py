import time


class TrafficLight:
    __states = (('red', 7), ('yellow', 2), ('green', 10))
    __color = 'red'

    def running(self, work_time):
        """Запуск светофора

        @:param work_time длительность работы светофора"""
        start_time = time.time()
        print("work_time", work_time)
        while (time.time() - start_time) <= work_time:
                for state in self.__states:
                    self.__color = state[0]
                    print(f"Цвет светофора: {self.__color}; "
                      f"время работы: {state[1]}")
                    time.sleep(state[1])
                    if (time.time() - start_time) > work_time:
                        print("Завершение работы светофора")
                        break


