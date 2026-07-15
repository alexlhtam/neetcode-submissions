class DynamicArray {
    private ArrayList<Integer> data;
    private int capacity;
    private int size;

    public DynamicArray(int capacity) {
        this.data = new ArrayList<>();
        this.capacity = capacity;
        this.size = 0;
    }

    public int get(int i) {
        return this.data.get(i);
    }

    public void set(int i, int n) {
        this.data.set(i, n);
    }

    public void pushback(int n) {
        if (this.size == this.capacity) { this.resize(); }

        this.data.add(n);
        this.size++;
   }

    public int popback() {
        this.size--;
        return this.data.remove(this.size);
    }

    public void resize() {
        this.capacity *= 2;
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.capacity;
    }
}