import copy
import os

from starter import create, STRUCTURE_TWO

MY_PROJECT = 'my_project'


def templater():
    start_dir = 'task_two'
    structure = [{
        MY_PROJECT: [{
            "templates": []
        }]
    }]
    tree = os.walk(os.path.join(start_dir, MY_PROJECT))

    is_templates = False
    for i in tree:
        print(i)
        if os.path.basename(i[0]) == 'templates':
            is_templates = True
            for folder in i[1]:
                structure[0][MY_PROJECT][0]["templates"].append({folder: []})
        if is_templates and os.path.basename(i[0]) != 'templates':
            namespace = os.path.basename(os.path.basename(i[0]))
            for dict_ in structure[0][MY_PROJECT][0]["templates"]:
                if namespace in tuple(dict_.keys()):
                    index = structure[0][MY_PROJECT][0]["templates"].index(
                        {namespace: []})
                    structure[0][MY_PROJECT][0]["templates"][index][
                        namespace] = copy.deepcopy(i[2])
                    is_templates = False
                    break
    print(structure)
    print(STRUCTURE_TWO)
    create(structure, start_dir)


if __name__ == '__main__':
    templater()
