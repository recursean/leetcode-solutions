fun tictactoe(moves: Array<IntArray>): String {
    var board = arrayOf<Array<String>>()

    var currentPlayer = "A"

    for (i in 0 until 3) {
        var tmp = arrayOf<String>()
        for (j in 0 until 3) {
            tmp += ""
        }
        board += tmp
    }

    for(move in moves) {
        board[move[0]][move[1]] = currentPlayer 

        if(validateWinner(board, currentPlayer)) {
            return currentPlayer
        }

        else {
            if(currentPlayer == "A") {
                currentPlayer = "B"
            }
            else {
                currentPlayer = "A"
            }  
        }
    }  

    if(moves.size == 9) {
        return "Draw"
    }  
    else {
        return "Pending"
    }
}
    
fun validateWinner(board: Array<Array<String>>, player: String): Boolean {
    if(board[0][0] == player && board[0][1] == player && board[0][2] == player) {
        return true
    }
    else if(board[1][0] == player && board[1][1] == player && board[1][2] == player) {
        return true
    }
    else if(board[2][0] == player && board[2][1] == player && board[2][2] == player) {
        return true
    }
    else if(board[0][0] == player && board[1][0] == player && board[2][0] == player) {
        return true
    }
    else if(board[0][1] == player && board[1][1] == player && board[2][1] == player) {
        return true
    }
    else if(board[0][2] == player && board[1][2] == player && board[2][2] == player) {
        return true
    }
    else if(board[0][0] == player && board[1][1] == player && board[2][2] == player) {
        return true
    }
    else if(board[0][2] == player && board[1][1] == player && board[2][0] == player) {
        return true
    }

    else {
        return false
    }
}

fun main() {
    var moves = arrayOf(intArrayOf(0,0),intArrayOf(1,1),intArrayOf(0,1),intArrayOf(0,2),intArrayOf(1,0),intArrayOf(2,0))
    println(tictactoe(moves))
}