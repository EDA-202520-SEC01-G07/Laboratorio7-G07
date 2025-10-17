def new_map():
    return {"root": None}
def size(m):
    def size_helper(node):
        if node is None:
            return 0
        return 1 + size_helper(node["left"]) + size_helper(node["right"])
    return size_helper(m["root"])