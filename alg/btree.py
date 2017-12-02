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


def mid_cpu_simulation(root):
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


def mid_recursive(root):
    if not root:
        return
    mid_recursive(root.left)
    print root.value,
    mid_recursive(root.right)


def mid_iterate(root):
    '''

    :type root: Node
    '''
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


def create_tree():
    '''

    :rtype: Node
    '''
    n1 = Node('a')
    n2 = Node('b')
    n3 = Node('c')
    n4 = Node('d')
    n5 = Node('e')
    n6 = Node('f')
    n7 = Node('g')
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n6
    n4.right = n5
    n6.left = n7
    return n1


if __name__ == '__main__':
    root = create_tree()
    mid_cpu_simulation(root)
    print
    mid_recursive(root)
    print
    mid_iterate(root)
    print
