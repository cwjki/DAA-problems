class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.heigth = 1
        self.desc = 0

def heigth(node):
    if node == None:
        return 0
    return node.heigth

def rightRotate(y):
    x = y.left
    T2 = x.right
    # Rotar
    x.right = y
    y.left = T2
    # Actualizar alturas
    y.heigth = max(heigth(y.left),heigth(y.right)) + 1
    x.heigth = max(heigth(x.left),heigth(x.right)) + 1
    # Actualizar descendencia
    val = -1
    if not T2 == None:
        val = T2.desc
    y.desc = y.desc - (x.desc + 1) + (val + 1)
    x.desc = x.desc - (val + 1) + (y.desc + 1)
    return x

def leftRotate(x):
    y = x.right
    T2 = y.left
    # Rotar
    y.left = x
    x.right = T2
    # Actualizar alturas
    x.heigth = max(heigth(x.left),heigth(x.right)) + 1
    y.heigth = max(heigth(y.left),heigth(y.right)) + 1
    # Actualizar descendencia
    val = -1
    if not T2 == None:
        val = T2.desc
    x.desc = x.desc - (y.desc + 1) + (val + 1)
    y.desc = y.desc - (val + 1) + (x.desc + 1)
    return y

def getBalance(node):
    if node == None:
        return 0
    return heigth(node.left) - heigth(node.right)

def insert(node,key):
    if node == None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left,key)
        node.desc += 1
    elif key > node.key:
        node.right = insert(node.right,key)
        node.desc += 1
    else:
        return node
    # Actualizando alturas
    node.heigth = 1 + max(heigth(node.left),heigth(node.right))
    
    balance = getBalance(node)
    # Left Left Case
    if balance > 1 and key < node.left.key:
        return rightRotate(node)
    # Right right case
    if balance < -1 and key > node.right.key:
        return leftRotate(node)
    # Left right case
    if balance > 1 and key > node.left.key:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    # Right left case
    if balance < -1 and key < node.right.key:
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node

def minValueNode(node):
    while node.left != None:
        node = node.left
    return node

def deleteNode(root,key):
    if root == None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left,key)
        root.desc -= 1
    elif key > root.key:
        root.right = deleteNode(root.right,key)
        root.desc -= 1
    else:
        if root.left == None or root.right == None:
            temp = root.left
            if root.left == None:
                temp = root.right
            if temp == None:
                root = None
            else:
                root = temp
        else:
            temp = minValueNode(root.right)
            root.key = temp.key
            root.right = deleteNode(root.right,temp.key)
            root.desc -= 1
    if root == None:
        return root
    # Actualizar altura
    root.heigth = 1 + max(heigth(root.left),heigth(root.right))
    # Actualizar balance
    balance = getBalance(root)
    # Left left case
    if balance > 1 and getBalance(root.left) >= 0:
        return rightRotate(root)
    # Left right case
    if balance > 1 and getBalance(root.left) < 0:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    # Right right case
    if balance < -1 and getBalance(root.right) <= 0:
        return leftRotate(root)
    # Right left case
    if balance < -1 and getBalance(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)
    return root

def countSmallers(root:Node,x):
    res = 0
    while root != None:
        desc = -1
        if root.left != None:
            desc = root.left.desc
        if root.key < x:
            res = res + desc + 2
            root = root.right
        elif root.key > x:
            root = root.left
        else:
            res += desc + 1
            break
    return res