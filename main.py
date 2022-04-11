class link_node:
    def __init__(self,item):

        self.ele=item
        self.next=None
class linklist:
    def __init__(self):
        self.head=None


        
    def add (self,s):
        node=link_node(s)
        node.next=self.head
        self.head=node
    def em(self):
        return self.head==None
    def travel(self):
        cur = self.head
        a = []
        while cur != None:
            print(type(cur.ele), cur.ele)
            a.append(cur.ele)
            cur = cur.next

    def append(self, item):
        node = link_node(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.em():
            self.head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    def Po(self, s):
        Node = link_node(s)
        if self.em():
            print(123)
            self.head = Node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = Node




a=linklist()
# a.add(2132)
a.add(1)
# a.add(3)
# a.append(2)
# a.Po(34)
a.Po(3445)
a.Po(3445)
a.travel()