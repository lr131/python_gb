import copy
import os

from starter import create_element, STRUCTURE_TWO

MY_PROJECT = 'my_project'

def create(struct, start_path):
    for key in tuple(struct.keys()):
        print(struct[key])
        if isinstance(struct[key], dict):
            path = os.path.join(start_path, tuple(struct[key].keys())[0])
            print("path: ", path)
            create_element(path)
            create(struct[key].get(tuple(struct[key].keys())[0], []), path)
        elif isinstance(struct[key], list):
            for elem in struct[key]:
                create_element(os.path.join(start_path, elem))
        else:
            create_element(os.path.join(start_path, struct[key]))


def templater():
    start_dir = 'task_two'
    structure = [{
        MY_PROJECT: [{
            "templates": [{
            }]
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
        print(structure)
        if is_templates and os.path.basename(i[0]) != 'templates':
            namespace = os.path.basename(os.path.basename(i[0]))
            print(namespace)
            for dict_ in structure[0][MY_PROJECT][0]["templates"]:
                print("dict_.get(namespace)", dict_.get(namespace))
                k = 0
                if namespace in tuple(dict_.keys()):
                    structure[0][MY_PROJECT][0]["templates"][k][namespace] = copy.deepcopy(i[2])
                    is_templates = False
                    break
                k +=1
    print(structure)
    print(STRUCTURE_TWO)
    #create(structure, start_dir)


if __name__ == '__main__':
    templater()
