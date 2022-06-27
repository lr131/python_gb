import utils_log
import utils_users


# Не используя библиотеки для парсинга, распарсить
# (получить определённые данные) файл логов web-сервера nginx_logs.txt
# Код должен работать даже с файлами, размер которых превышает объем
# ОЗУ компьютера.
def task_one():
    logs = utils_log.get_log("nginx_logs.txt")
    for log in logs:
        print(log)


def task_two():
    spamer = utils_log.get_spamer_info("nginx_logs.txt")
    print("spamer ip:", spamer[0], ", request count: ", spamer[1])


def task_three():
    data = utils_users.get_info("users.csv", "hobby.csv")
    if data == 1:
        print("1")
        return 1
    utils_users.save_file(data, "result.json")


def task_four():
    filename = "dump_task4.csv"
    data = utils_users.get_info_adv("users.csv", "hobby.csv")
    if data == 1:
        print("1")
        return 1
    utils_users.save_file_adv(["family",
                               "name",
                               "patr",
                               "hobby"], filename, ";")
    for datum in data:
        utils_users.save_file_adv(datum.values(), filename, ";")
    data_from_file = utils_users.load_row_data(filename)
    for info in data_from_file:
        print(info)


if __name__ == '__main__':
    task_one()
    task_two()
    task_three()
    task_four()
