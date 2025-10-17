def insert_node(root, key, value):
    if root is None:
        return {'key': key, 'value':value, 'left': None, 'right': None}
    else:
        if key < root['key']:
            root['left'] = insert_node(root['left'], key, value)
        else:
            root['right'] = insert_node(root['right'], key, value)
    return root

def put(my_bst, key, value):
    my_bst = insert_node(my_bst, key, value)
    return my_bst
