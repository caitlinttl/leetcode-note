// binarySearch
// TC: O(log n)
// SC: O(1)


public int binarySearch(int array[], int target) {
    int left = 0;
    int right = array.length - 1;
    while(left <= right) {  
        int mid = left + (right - left) / 2;
        if (array[mid] == target) { 
            return mid;
        } else if (target < array[mid]) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return -1;



    
}


// insert the element to the specific position, position starts from index 0
public void insert(int position, int number) {
    if (position > size) {
        return;
    }
    ListNode newNode = new ListNode(number);
    if (position == 0) {
        newNode.next = head;
        head = newNode;
        if(tail == null) {
            tail = newNode;
        }
        size++;
    } else if (position == size) {
        this.append(number);
    } else {
        ListNode prev = head;
        for (int i = 0; i < position - 1; i++) {
            prev = prev.next;
        }
        ListNode next = prev.next;
        newNode.next = next;
        prev.next = newNode;
        size++;
    }
}
// append the new element to the end of the list
public void append(int number) { 
    ListNode newNode = new ListNode(number);
    if(tail == null) {
        tail = newNode;
    } else {
        tail.next = newNode;
        tail = newNode;
    }
    size++;
}

public void delete(int number) {
    if(head != null && head.val == number) { // delete the head node
        head = head.next;
        size--;
        if(size == 0) { // corner case: no element is left
            tail = head;
        }
    } else {
        ListNode prev = head;
        ListNode cur = head;
        while (prev != null && cur != null) {
            if (cur.val == number) {
                if(cur == tail) { // corner case: delete the last element
                    tail = prev;
                }
                prev.next = cur.next;
                size--;
                return;
            }
            prev = cur;
            cur = cur.next;
        }
    }
}


public int search(int number) {
    ListNode cur = head;
    for(int index = 0; cur != null; index++) {
        if(cur.val == number) {
            return index;
        }
        cur = cur.next;
    }
    return -1;
}


public int update(int oldValue, int newValue) {
    ListNode cur = head;
    for(int index = 0; cur != null; index++) {
        if(cur.val == oldValue) {
            cur.val = newValue;
            return index;
        }
        cur = cur.next;
    }
    return -1;
}


// Stack (array) --------------------------------
public class Stack {
    static final int CAPACITY = 1000;
    int top;
    int stack[];

    public Stack() {
        top = -1;
        stack = new int[CAPACITY];
    }
}

// Push
public boolean push(int val) {
    if (top >= (CAPACITY - 1)) {
        System.out.println("Stack Overflow.");
        return false;
    }
    stack[++top] = val;
    return true;
}

//Pop
public int pop() {
    if (top < 0) {
        System.out.println("Stack Underflow."); // 沒有東西可以拿
        return 0;
    }
    int element = stack[top--];
    return element;
}

// peak
public int peek() {
    if (top < 0) {
        System.out.println("Stack Underflow");
        return 0;
    }
    int element = stack[top];
    return element;
}

// isEmpty
public boolean isEmpty() {
    return top < 0;
}

// Stack (linkedList) --------------------------------

public class ListStack {

    static class StackNode {
        int val;
        StackNode next;
        StackNode(int val) {
            this.val = val;
        }
    }

    StackNode top;

    public ListStack() {
        top = null;
    }
}

public void push(int val) {
    StackNode newNode = new StackNode(val);
    if (top == null) {
        top = newNode;
    } else {
        StackNode temp = top;
        top = newNode;
        newNode.next = temp;
    }
    System.out.println(val + " is pushed to stack.");
}

public int pop() {
    if (top == null) {
        System.out.println("Stack is Empty.");
        return Integer.MIN_VALUE;
    }
    int popped = top.val;
    top = top.next;
    return popped;
}

public int peek() {
    if (top == null) {
        System.out.println("Stack is empty.");
        return Integer.MIN_VALUE;
    }
    return top.val;
}

public boolean isEmpty() {
    return top == null;
}



// Queue (array) --------------------------------

// 循環對列
public class ArrayQueue {
    int front, rear, size; // 前端, 後端, 多少元素
    int capacity;
    int array[];

    public ArrayQueue(int capacity) {
        this.capacity = capacity;
        front = rear = size = 0;
        array = new int[capacity];
    }
}

public void enqueue(int item) {
    if (isFull()) return;
    array[rear] = item;
    rear = (rear + 1) % capacity;
    size++;
    System.out.println(item + " is enqueued.");
}

public int dequeue() {
    if (isEmpty()) return Integer.MIN_VALUE;
    int item = array[front];
    front = (front + 1) % capacity;
    size --;
    return item;
}

public int peek() {
    if (isEmpty()) return Integer.MIN_VALUE;
    return array[front];
}

public boolean isFull() {
    return size == capacity;
}

public boolean isEmpty() {
    return size == 0;
}


// Queue (linkedList) --------------------------------

public class ListQueue {

    QueueNode front;
    QueueNode rear;

    static class QueueNode {
        int value;
        QueueNode next;
        public QueueNode(int value) {
            this.value = value;
        }
    }
}

public void enqueue(int value) {
    QueueNode newNode = new QueueNode(value);
    if (this.rear == null) { // Queue is empty
        this.front = this.rear = newNode;
        return;
    }
    this.rear.next = newNode;
    this.rear = newNode;
}

public int dequeue() {
    if (this.front == null) {
        System.out.println("The queue is empty.");
        return Integer.MIN_VALUE;
    }
    QueueNode frontNode = this.front;
    this.front = this.front.next;
    if (this.front == null) {
        this.rear = null;
    }
    return frontNode.value;
}