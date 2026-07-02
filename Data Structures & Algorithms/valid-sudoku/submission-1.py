class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check hàng
        for row in range (9):
            saw=set()
            for col in range (9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in saw:
                    return False
                saw.add(val)

        # check cột
        for col in range (9):
            saw=set()
            for row in range (9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in saw:
                    return False
                saw.add(val)

        # (start,stop,step)
        for startRow in range (0,9,3):
            for startCol in range (0,9,3):
                seen = set()
                for r in range (startRow, startRow+3,1):
                    for c in range (startCol, startCol+3,1):
                        value = board[r][c]
                        if value == ".":
                            continue
                        if value in seen:
                            return False
                        seen.add(value)
        return True




        

        