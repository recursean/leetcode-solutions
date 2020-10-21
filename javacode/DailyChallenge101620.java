public class DailyChallenge101620 {
    public boolean searchMatrix(int[][] matrix, int target) {
        boolean targetFound = false;

        // loop thru each row
        for(int i = 0; i < matrix.length; i++) {
            // if target is greater than last element in row, go to next row
            if(matrix[i].length != 0 && target > matrix[i][matrix[i].length - 1]) {
                continue;
            }
            // target has to be in this row if it exists
            else {
                // could do binary search for efficiency
                for(int j = 0; j < matrix[i].length; j++) {
                    if(matrix[i][j] == target) {
                        targetFound = true;
                        break;
                    }
                }
            }

            if(targetFound) {
                break;
            }
        }        

        return targetFound;
    }

    public static void main(String[] args) {
        int[][] matrix = {
            {1,3,5,7},
            {10,11,16,20},
            {23,30,34,50}
        };

        int target = 16;

        System.out.println(new DailyChallenge101620().searchMatrix(matrix, target));
    }
}