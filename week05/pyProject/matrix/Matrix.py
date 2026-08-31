class Matrix:

    # Constructor
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # Create a matrix with all values = 0
        self.data = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(0)
            self.data.append(row)


    # Print the matrix
    def print_matrix(self):
        print()
        print("Matrix ({} x {})".format(self.rows, self.cols))
        print("----------------------")
        for row in self.data:
            for value in row:
                print(value, end=" ")
            print()
        print("----------------------")
    # Set one value
    def set_value(self, row, col, value):
        if row < 0 or row >= self.rows:
            print("Invalid row index.")
            return

        if col < 0 or col >= self.cols:
            print("Invalid column index.")
            return
        self.data[row][col] = value

    # Get one value
    def get_value(self, row, col):
        if row < 0 or row >= self.rows:
            print("Invalid row index.")
            return None

        if col < 0 or col >= self.cols:
            print("Invalid column index.")
            return None

        return self.data[row][col]

    # Set the whole matrix
    def set_matrix(self, matrix):
        if len(matrix) != self.rows:
            print("Invalid number of rows.")
            return

        for row in matrix:
            if len(row) != self.cols:
                print("Invalid number of columns.")
                return

        self.data = matrix


    # Matrix multiplication
    def multiply(self, other):
        # Check matrix size
        if self.cols != other.rows:
            raise ValueError(
                "Matrix dimensions do not match for multiplication."
            )

        # Create result matrix
        result = Matrix(self.rows, other.cols)

        # Matrix multiplication
        for i in range(self.rows):
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.data[i][k] * other.data[k][j]
                result.data[i][j] = total
        return result

    # Input matrix values
    def input_matrix(self):
        print()
        print("Please enter the matrix values:")

        for i in range(self.rows):
            for j in range(self.cols):
                value = int(
                    input("Enter value [{0}][{1}]: ".format(i, j))
                )
                self.data[i][j] = value

    # Fill the matrix with one value
    def fill(self, value):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = value

    # Display matrix information
    def display_info(self):
        print()
        print("Rows    :", self.rows)
        print("Columns :", self.cols)