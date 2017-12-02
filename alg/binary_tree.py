# coding=utf-8

class Node():
    def __init__(self, value=None, left=None, right=None):
        '''

        :type value: object
        :type left: Node
        :type right: Node
        '''
        self.value = value
        self.left = left
        self.right = right


def inorder_cpu_simulation(root):
    # jump, function call
    pc = 0
    stack = [pc, root]
    # function "def mid_recursive(root):"
    while stack:
        pc += 1
        root = stack[len(stack) - 1]
        if pc == 1:
            if not root:
                # jump, function return
                stack.pop()
                pc = stack.pop()
                continue
        elif pc == 2:
            # jump, function call
            stack.append(pc)
            stack.append(root.left)
            pc = 0
            continue
        elif pc == 3:
            print root.value,
        elif pc == 4:
            # jump, function call
            stack.append(pc)
            stack.append(root.right)
            pc = 0
            continue
        else:
            # jump, function return
            stack.pop()
            pc = stack.pop()
            continue


def preorder_recursive(root):
    if not root:
        return
    print root.value,
    preorder_recursive(root.left)
    preorder_recursive(root.right)


def preorder_iterate(root):
    stack = []
    while root or stack:
        if root:
            print root.value,
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            root = root.right


def inorder_recursive(root):
    if not root:
        return
    inorder_recursive(root.left)
    print root.value,
    inorder_recursive(root.right)


def inorder_iterate(root):
    if not root:
        return
    cur = root
    stack = []
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            print cur.value,
            cur = cur.right


def postorder_recursive(root):
    if not root:
        return
    postorder_recursive(root.left)
    postorder_recursive(root.right)
    print root.value,


def postorder_iterate(root):
    stack = []
    visited = {}
    cur = root
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            if cur.right not in visited:
                stack.append(cur)
                visited[cur.right] = True
                cur = cur.right
            else:
                print cur.value,
                cur = None


def postorder_iterate2(root):
    stack = []
    cur = root
    last_pop = None
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            if cur.right and last_pop != cur.right:
                stack.append(cur)
                cur = cur.right
            else:
                last_pop = cur
                print cur.value,
                cur = None


def create_tree():
    '''
                          1
                2                   3
            4       5           6       7
                  8           9
    :rtype: Node
    '''
    n1 = Node('1')
    n2 = Node('2')
    n3 = Node('3')
    n4 = Node('4')
    n5 = Node('5')
    n6 = Node('6')
    n7 = Node('7')
    n8 = Node('8')
    n9 = Node('9')
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n5.left = n8
    n6.left = n9
    return n1


if __name__ == '__main__':
    root = create_tree()
    preorder_recursive(root)
    print
    preorder_iterate(root)
    print
    print
    #
    inorder_cpu_simulation(root)
    print
    inorder_recursive(root)
    print
    inorder_iterate(root)
    print
    print
    #
    postorder_recursive(root)
    print
    postorder_iterate(root)
    print
    postorder_iterate2(root)
    print
