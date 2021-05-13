def parse_node_parameters(path):
    file = open(path, "r")

    file_as_string = file.read().replace("----------------\n", "").replace("output([", "").replace("]).", "")

    node_array = file_as_string.split("\n")
    node_array.pop(len(node_array)-1)

    node_list = []
    for node in node_array:
        node_list.append(node.split(", "))
        
    return node_list