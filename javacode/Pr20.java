import java.util.Stack;

class Pr20 {
    public boolean isMatch(char c, char popped) {
        if(c == ')' && popped == '(') {
            return true;
        }

        else if(c == ']' && popped == '[') {
            return true;
        }

        else if(c == '}' && popped == '{') {
            return true;
        }

        else {
            return false;
        }
    }

    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();

        for(char c: s.toCharArray()) {
            if(c == '(' || c == '[' || c == '{') {
                stack.push(Character.valueOf(c));
            }

            else {
                if(stack.isEmpty() || !isMatch(Character.valueOf(c), stack.pop().charValue())) {
                    return false;
                }
            }
        }

        if(stack.isEmpty()) {
            return true;
        }
        
        else {
            return false;
        }
    }

    public static void main(String[] args) {
        System.out.println(new Pr20().isValid("(([]{()}[()]))"));
    }
}