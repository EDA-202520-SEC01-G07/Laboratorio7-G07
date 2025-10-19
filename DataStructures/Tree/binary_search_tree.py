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