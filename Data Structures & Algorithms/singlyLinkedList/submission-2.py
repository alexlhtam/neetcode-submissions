from typing import List, Optional

class LinkedList:
    class Node:
        def __init__(self, num):
            self.data = num
            self.next: Optional["LinkedList.Node"] = None

    def __init__(self):
        self.size = 0
        self.head = None
    
    def get(self, index: int) -> int:
        if (index >= self.size):
            return -1
        else:
            walk = self.head
            for _ in range(index):
                walk = walk.next
            return walk.data

    def insertHead(self, val: int) -> None:
        if self.size == 0:
            self.head = self.Node(val)
        else:
            newNode = self.Node(val)
            newNode.next = self.head
            self.head = newNode
        self.size += 1

    def insertTail(self, val: int) -> None:
        if self.size == 0:
            self.head = self.Node(val)
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = self.Node(val)
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        else:
            if index == 0:
                # remove head
                self.head = self.head.next
            else:
                # removing non-head
                walk = self.head
                for _ in range(index - 1):
                    walk = walk.next
                walk.next = walk.next.next

            self.size -= 1
            return True

    def getValues(self) -> List[int]:
        data = []
        walk = self.head
        while walk != None:
            data.append(walk.data)
            walk = walk.next
        return data
