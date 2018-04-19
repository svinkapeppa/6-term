import java.util.*;
import java.lang.*;

class Rextester {
    static class Array {
        private static final int initialCapacity = 4;
        private Integer[] buffer;
        private int size = 0;
        private int capacity = initialCapacity;
 
        public Array() {
            buffer = new Integer[initialCapacity];
        }
        
        public void resize() {
            capacity *= 2;
            buffer = Arrays.copyOf(buffer, capacity);
        }
        
        public void add(Integer element) {
            if (size >= capacity) {
                resize();
            }
            buffer[size] = element;
            ++size;
        }
        
        public int size() {
            return size;
        }
        
        public Integer get(int index) {
            return buffer[index];
        }
    }
 
    public static void main(String[] args) {
        Array arr = new Array();
        for (int i = 0; i < 10; ++i) {
            arr.add(i);
        }
        for (int i = 0; i < arr.size(); ++i) {
            System.out.println(arr.get(i));
        }
    }
}