import os
from pathlib import Path
import yaml

DIR_NAME = 'my_project'
STRUCTURE_ONE = [{
    DIR_NAME: ['settings', "mainapp", "adminapp", "authapp"]
}]
STRUCTURE_TWO = [
        {
            DIR_NAME: [
                {"setting": [
                    "__init__.py",
                    "dev.py",
                    "prod.py"
                ]},
                {"mainapp": [
                    "__init__.py",
                    "models.py",
                    "views.py",
                    {"templates": [
                        {"mainapp": [
                            "base.html",
                            "index.html"
                        ]}
                    ]}
                ]},
                {"authapp": [
                    "__init__.py",
                    "models.py",
                    "views.py",
                    {"templates" : [
                        {"authapp": [
                            "base.html",
                            "index.html"
                        ]}
                    ]}
                ]}
            ]
        }
    ]
FILE_CONFIG_ONE = "config_one.yaml"
FILE_CONFIG_TWO = "config.yaml"


def create_element(path):
    print(path, os.path.basename, "." in os.path.basename(path))
    if "." in os.path.basename(path):
        print("IsFile")
        try:
            open(path, 'w').close()
        except OSError as e:
            print(e)
    else:
        print("IsDir")
        p = Path(path)
        p.mkdir(parents=True, exist_ok=True)


def init_yaml(data, filename):
    with open(filename, 'w') as file:
        yaml.dump(data, file)
        print(f"{filename} init successful")


def task_one(dir_name=DIR_NAME):
    task_name = "task_one"
    create_element(task_name)
    create_element(os.path.join(task_name, dir_name))
    inner_path = [os.path.join(task_name, dir_name, folder)
                  for folder in STRUCTURE_ONE[0].get(dir_name, [])]
    for folder_name in inner_path:
        create_element(folder_name)


def task_two(dir_name=DIR_NAME):
    task_name = "task_two"
    path = os.path.join(task_name)
    create_element(path)
    with open(FILE_CONFIG_TWO, "r") as file:
        structure = yaml.load(file, Loader=yaml.FullLoader)
        print(structure)
        create(structure, path)


def create(struct, start_path):
    for file in struct:
        if isinstance(file, dict):
            path = os.path.join(start_path, tuple(file.keys())[0])
            print("path: ", path)
            create_element(path)
            create(file.get(tuple(file.keys())[0], []), path)
        else:
            create_element(os.path.join(start_path, file))


if __name__ == '__main__':
    init_yaml(STRUCTURE_ONE, FILE_CONFIG_ONE)
    task_one()
    init_yaml(STRUCTURE_TWO, FILE_CONFIG_TWO)
    task_two()
