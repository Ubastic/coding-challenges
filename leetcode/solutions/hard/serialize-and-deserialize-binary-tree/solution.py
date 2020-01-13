def serialize(node, arr):
    if not node:
        arr.append('*')
    else:
        arr.append(node.val)
        serialize(node.left, arr)
        serialize(node.right, arr)

    return arr


def deserialize(arr: list):
    if not arr:
        return

    val = arr.pop(0)
    if val == '*':
        return

    node = TreeNode(int(val))
    node.left = deserialize(arr)
    node.right = deserialize(arr)

    return node


class Codec:
    def serialize(self, root) -> str:
        return ' '.join(map(str, serialize(root, [])))

    def deserialize(self, data):
        return deserialize(data.split())