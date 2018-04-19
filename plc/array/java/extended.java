import java.util.*;
import java.lang.*;

class Rextester {
    interface ITextHandler {
        String Process(String text);
    };

    static class LowercaseHandler implements ITextHandler {
        public String Process(String token) {
            return token.toLowerCase();
        }
    };
    
    static class Array<T extends ITextHandler> {
        private static final int initialCapacity = 4;
        private T[] buffer;
        private int size = 0;
        private int capacity = initialCapacity;
 
        public Array() {
            buffer = (T[]) new ITextHandler[initialCapacity];
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
        
        public String apply(String text) {
            for (int i = 0; i < size; ++i) {
                text = buffer[i].Process(text);
            }
            return text;
        }
    }
 
    public static void main(String[] args) {
        Array<ITextHandler> handlers = new Array<ITextHandler>();
        handlers.add(new LowercaseHandler());
        System.out.println(handlers.apply("SamplE tEXt"));
    }
}