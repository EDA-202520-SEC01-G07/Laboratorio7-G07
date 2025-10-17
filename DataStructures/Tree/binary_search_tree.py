def new_map():
    return {"root": None}
def size(my_bst):
    def size_tree(node):
        if node is None:
            return 0
        else:
            return 1 + size_tree(node['left']) + size_tree(node['right'])
def insert_node(root, key, value):
    if root is None:
        return {'key': key, 'value':value, 'left': None, 'right': None}
    else:
        if key == root['key']:
            root['value'] = value
        elif key < root['key']:
            root['left'] = insert_node(root['left'], key, value)
        else:
            root['right'] = insert_node(root['right'], key, value)
    return root

def put(my_bst, key, value):
    my_bst = insert_node(my_bst, key, value)
    return my_bst


def get(bst, key):
    valor = None
    get_node(bst["root"], key)
    return valor

def get_node(root, key):
    if root["key"] == None:
        return None
    elif root["key"] == key:
        return root["value"]
    else:
        if key < root["key"]:
            return get_node(root["left"])
        if key > root["key"]:
            return get_node(root["right"])