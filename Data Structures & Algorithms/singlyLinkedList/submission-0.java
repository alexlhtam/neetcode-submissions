class LinkedList {
    private Node head;
    private int size;

    class Node {
        public int data;
        public Node next;

        public Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    public LinkedList() {
        this.head = null;
        this.size = 0;
    }

    public int get(int index) {
        if (index + 1 > size) {
           return -1; 
        } else {
            Node walk = head;
            for (int i = 0; i < index; i++) {
                walk = walk.next;
                
            }
            return walk.data;
        } 
    }

    public void insertHead(int val) {
        Node newNode = new Node(val);
        newNode.next = this.head;
        this.head = newNode;
        this.size++;
    }

    public void insertTail(int val) {
        if (head == null) {
            insertHead(val);
            return;
        }
        Node walk = head;
        while (walk.next != null) { walk = walk.next; }
        walk.next = new Node(val);
        this.size++;
    }

    public boolean remove(int index) {
        // check if out of bounds first
        if (index >= size) { return false; }

        // case 1: remove head
        if (index == 0) { 
            this.head = this.head.next; 
        } else {
            // case 2: not removing head
            Node walk = this.head;
            for (int i = 0; i < index - 1; i++) { walk = walk.next; }
            walk.next = walk.next.next;
        }
        this.size--;
        return true;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> returnArray = new ArrayList<>(this.size);
        Node walk = head;
        while (walk != null) {
            returnArray.add(walk.data);
            walk = walk.next;
        }
        return returnArray;
    }
}