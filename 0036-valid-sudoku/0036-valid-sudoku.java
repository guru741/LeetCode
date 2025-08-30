class Solution {
    public boolean isValidSudoku(char[][] board) {
        int [] row = new int[9],col = new int[9],sub = new int[9];

        for (int i = 0;i < 9;i++){
            for(int j = 0;j < 9;j++){

                if (board[i][j] == '.') continue;

                int val = board[i][j] - '1';
                int mask = 1 << val;
                int idx = (i / 3) * 3 + (j / 3);
                if ((row[i] & mask) != 0 || (col[j] & mask) != 0 || (sub[idx] & mask) != 0) return false;

                row[i] |= mask;
                col[j] |= mask;
                sub[idx] |= mask;
            }
        }
        return true;
    }
}