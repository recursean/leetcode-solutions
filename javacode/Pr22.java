import java.util.LinkedList;
import java.util.List;

class Pr22 {
    public List<String> generateParenthesis(int n) {
        List<String> sols = new LinkedList<String>();
        generateParenthesis(n, n, new StringBuilder(), sols); 
        return sols;
    }

    private void generateParenthesis(int left, int right, StringBuilder parenStr, List sols) {
        if(left == 0 && right == 0) {
            sols.add(parenStr.toString());
        }
        else {
            if(left > 0) {
                generateParenthesis(left-1, right, parenStr.append("("), sols); 
            }
            if(left != right && right > 0) {
                generateParenthesis(left, right-1, parenStr.append(")"), sols); 
            }
        }

        if(parenStr.length() > 0)
            parenStr.deleteCharAt(parenStr.length() - 1);
    }

    public static void main(String[] args) {
        Pr22 pr = new Pr22();
        int n = 3;
        List<String> sols = pr.generateParenthesis(n);

        for(String sol: sols) {
            System.out.println(sol);
        }
    }    
}