tree=[None]*10

def root(key):
    if tree[0] is None:
        tree[0]=key
    else:
        print('root already exists')

def set_left(key,parent):
    if tree[parent] is None:
        print('cant allow orphans')
    else:
        tree[parent*2+1]=key

def set_right(key,parent):
    if tree[parent] is None:
        print('cant allow orphans')
    else:
        tree[parent*2+2]=key

def print_tree():
    for i in tree:
        if i:
            print(i,end='')
        else:
            print('-',end='')
    print()
    
root('A')
set_right('C', 0)
set_left('D', 1)
set_right('E', 1)
set_right('F', 2)
print_tree()
print(tree)