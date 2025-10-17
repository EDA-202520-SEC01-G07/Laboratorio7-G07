from DataStructures.Tree import bst_node as n
def new_map():
    return {"root": None}

def size(my_bst):
    return size_tree(my_bst["root"])
    
def size_tree(node):
    if node is None:
        return 0
    else:
        return 1 + size_tree(node['left']) + size_tree(node['right'])

def put(my_bst, key, value):
    return insert_node(my_bst["root"], key, value)

def insert_node(root, key, value):
    if root is None:
        root["root"] = n.new_node(key, value)
    elif key == root['key']:
        root['value'] = value
        return root
    elif key < root['key']:
        return insert_node(root['left'], key, value)
    else:
        return insert_node(root['right'], key, value)

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
def contains(my_bst, key):
    if get(my_bst, key) is not None:
        return True
    else:
        return False