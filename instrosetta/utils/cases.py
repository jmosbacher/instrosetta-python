import re

def pascal_case(name):
    if '_' in name:
        return ''.join(map(lambda x: x.title(), name.split('_')))
    if name[0].isupper():
        return name
    
    return name.title()


def snake_case(name):
    """
    Stolen from https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

        