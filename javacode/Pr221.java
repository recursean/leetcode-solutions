public class Pr221 {
    public int maximalSquare(char[][] matrix) {
        int maxSquare = 0, rowCount, tmpRow, colCount, tmpCol, squareSize, actualSize;
        
        for(int row = 0; row < matrix.length; row++) {
            for(int col = 0; col < matrix[0].length; col++) {
                if(matrix[row][col] == '1') {
                    if(maxSquare == 0) {
                        maxSquare = 1;
                    }

                    rowCount = 1;
                    tmpRow = row + 1;
                    while(tmpRow < matrix.length && matrix[tmpRow][col] == '1') {
                        tmpRow++;
                        rowCount++;
                    }

                    if(rowCount > 1) {
                        colCount = 1;
                        tmpCol = col + 1;
                        while(tmpCol < matrix[0].length && matrix[row][tmpCol] == '1') {
                            tmpCol++;
                            colCount++;
                        }

                        if(colCount > 1) {                    
                            squareSize = rowCount < colCount ? rowCount : colCount;
                            actualSize = checkSquare(row, col, squareSize, matrix);
                            if(actualSize > 1) {
                                maxSquare = maxSquare < actualSize ? actualSize : maxSquare;

                                if(actualSize == 6)
                                    System.out.println(row + " : " + col);
                            }
                        }
                    }
                }
            }
        }
        
        return maxSquare * maxSquare;
    }
    
    int checkSquare(int row, int col, int squareSize, char[][] matrix) {
        int maxSquare = 1;
        int maxY = col + squareSize;

        for(int x = row + 1; x < row + squareSize; x++) {
            for(int y = col + 1; y < maxY; y++) {
                if(matrix[x][y] == '0') {
                    if(y - col - 1 > maxSquare) {
                        maxY = y;
                    }
                    else {
                        return maxSquare;
                    }
                }
                else if(x - row == y - col) {
                    maxSquare++;
                }
            }            
        }
        
        return maxSquare;
    }

    public static void main(String[] args)  {
        char[][] matrix = {
            {'0','1','1','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0'},
            {'1','0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'},
            {'1','1','0','1','1','1','1','1','1','1','1','1','0','1','1','1','1','1','1'},
            {'1','1','1','1','1','1','1','1','1','1','1','1','1','0','1','1','1','1','1'},
            {'1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','1','1','1','1'},
            {'1','1','1','0','1','1','1','0','1','1','1','1','1','1','1','1','1','0','1'},
            {'1','0','1','1','1','1','1','1','1','1','1','1','1','1','0','1','1','1','1'},
            {'1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','1','1','0'},
            {'0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','0','1','1','1'},
            {'1','1','0','1','1','1','1','1','1','1','0','1','1','1','1','1','1','1','1'},
            {'1','1','1','1','1','1','1','1','1','0','1','1','1','1','1','1','1','1','1'},
            {'0','1','1','0','1','1','1','0','1','1','1','1','1','1','1','1','1','1','1'},
            {'1','1','1','1','0','1','1','1','1','1','1','1','1','1','0','1','1','1','1'},
            {'1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'},
            {'1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'},
            {'1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','1'},
            {'1','1','1','1','1','1','1','1','0','1','1','0','1','1','0','1','1','1','1'},
            {'1','1','1','1','1','1','0','1','1','1','1','1','1','1','1','0','1','1','1'}
        };

        System.out.println(new Pr221().maximalSquare(matrix));
    }
}