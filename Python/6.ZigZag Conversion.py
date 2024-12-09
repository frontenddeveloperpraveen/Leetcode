def convert( s:str, numRows):
        seter = numRows - 1
        n_mat = numRows // len(s)
        n_mat += n_mat//2
        mat = [[0]*numRows]*n_mat
        Col = 0
        row_set = 0
        s_index = 0
        setter_map = 0
        joiner = numRows -seter
        for i in range((numRows*n_mat)):
            if(i % numRows -1 == 0):
                row_set = 0 if row_set == 1 else 1
                counter += 1
            if(row_set == 1):
                if(setter_map == joiner and joiner != 0):
                    mat[counter][i] = s[s_index]
                    s_index += 1
                    setter_map = 0
                    joiner -= 1
                else:
                    mat[counter][i] = None
            mat[counter][i] = s[s_index]
            s_index += 1

        print(mat)

convert("PAYPALISHIRING",3)