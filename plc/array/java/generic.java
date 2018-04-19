import java.util.*;
import java.lang.*;

class Rextester {
    static class Array<T> {
        private static final int initialCapacity = 4;
        private T[] buffer;
        private int size = 0;
        private int capacity = initialCapacity;
 
        public Array() {
            buffer = (T[]) new Object[initialCapacity];
        }
        
        public void resize() {
            capacity *= 2;
            buffer = Arrays.copyOf(buffer, capacity);
        }
        
        public void add(T element) {
            if (size >= capacity) {
                resize();
            }
            buffer[size] = element;
            ++size;
        }
        
        public int size() {
            return size;
        }
        
        public T get(int index) {
            return buffer[index];
        }
    }
 
    public static void main(String[] args) {
        Array<Integer> arr = new Array<Integer>();
        for (int i = 0; i < 10; ++i) {
            arr.add(i);
        }
        for (int i = 0; i < arr.size(); ++i) {
            System.out.println(arr.get(i));
        }
    }
}