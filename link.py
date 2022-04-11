class link_node:
    def __init__(self,item):
        print("__init__")
        self.ele=item
        self.next=None
class linklist:
    def __init__(self):
        self.head=None
    def add(self,n):
        node=link_node(n)
        print(self.head,"add methond \n")
        node.next=self.head
        self.head=node
        # print(str(node),node.next,self.head)
        # print(node.next)
        return self.head
    def append(self, item):
        """尾部添加元素"""
        node = link_node(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            print("This node ")
            self.head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    def is_empty(self):
        """判断链表是否为空"""
        return self.head == None

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self._head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        cur=self.head
        a=[]
        while cur!=None:
            print(type(cur.ele),cur.ele)
            a.append(cur.ele)
            cur=cur.next
        print(a)

a=linklist()
a.add(2132)
a.add(1)
a.add(3)


a.travel()
