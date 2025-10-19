from DataStructures.Tree import bst_node as n
from DataStructures.List import single_linked_list as lt
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
    if my_bst["root"] != None:
        my_bst["root"] = insert_node(my_bst["root"], key, value)
        return my_bst
    else:
        my_bst["root"] = n.new_node(key, value)
        return my_bst

def insert_node(root, key, value):
    if root is None:
        root = n.new_node(key, value)
    elif key == root['key']:
        root['value'] = value
    elif key < root['key']:
        root["left"] = insert_node(root['left'], key, value)
    else:
        root["right"] = insert_node(root['right'], key, value)
    return root

def get(bst, key):
    return get_node(bst["root"], key)

def get_node(root, key):
    if root == None:
        return None
    elif root["key"] == key:
        return root["value"]
    else:
        if key < root["key"]:
            return get_node(root["left"], key)
        if key > root["key"]:
            return get_node(root["right"], key)
        

def contains(my_bst, key):
    if get(my_bst, key) is not None:
        return True
    else:
        return False

def is_empty(bst):
    if bst["root"] is None:
        return True
    return False

def key_set(bst):
    lista = lt.new_list()
    key_set_tree(bst["root"], lista)
    return lista
    
def key_set_tree(root, key_list):
    if root is None:
        return key_list
    else:
        lt.add_last(key_list, root["key"])
        key_set_tree(root["left"], key_list)
        key_set_tree(root["right"], key_list)
        return key_list
    
def value_set(bst):
    lista = lt.new_list()
    value_set_tree(bst["root"], lista)
    return lista
    
def value_set_tree(root, value_list):
    if root is None:
        return value_list
    else:
        lt.add_last(value_list, root["value"])
        key_set_tree(root["left"], value_list)
        key_set_tree(root["right"], value_list)
        return value_list
    
def get_min(bst):
    return None
    
def get_max(bst):
    return None

def delete_min(bst):
    return None

def delete_max(bst):
    return None
    
def keys(bst, key_initial, key_final):
    return None

def values(bst, key_initial, key_final):
    return None
    
def height(bst):
    return height_tree(bst["root"], 0)

def height_tree(root, contador):
    if root is None:
        return contador
    else:
        contador += 1
        return max(height_tree(root["left"], contador), height_tree(root["right"], contador))