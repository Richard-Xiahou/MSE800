from Matrix import Matrix


def menu():

    print()
    print("======================================")
    print("      Matrix Multiplication System")
    print("======================================")
    print("1. Create Empty Matrix")
    print("2. Run Default Example")
    print("3. Fill Matrix with One Value")
    print("4. Input Matrix")
    print("0. Exit")
    print()


def run_default_example():
    matrixA = Matrix(2, 3)
    matrixA.set_matrix(
        [
            [1, 2, 3],
            [4, 5, 6]
        ]
    )

    matrixB = Matrix(3, 2)
    matrixB.set_matrix(
        [
            [10, 11],
            [20, 21],
            [30, 31]
        ]
    )

    print()
    print("Matrix A")
    matrixA.print_matrix()

    print()
    print("Matrix B")
    matrixB.print_matrix()

    matrixC = matrixA.multiply(matrixB)
    print()
    print("Matrix C = A x B")
    matrixC.print_matrix()


def create_empty_matrix():
    rows = int(input("Rows: "))
    cols = int(input("Columns: "))

    matrix = Matrix(rows, cols)
    matrix.display_info()
    matrix.print_matrix()


def fill_matrix():

    rows = int(input("Rows: "))
    cols = int(input("Columns: "))
    matrix = Matrix(rows, cols)
    value = int(input("Fill Value: "))

    matrix.fill(value)
    matrix.display_info()
    matrix.print_matrix()


def input_matrix():
    rows = int(input("Rows: "))
    cols = int(input("Columns: "))

    matrix = Matrix(rows, cols)

    matrix.input_matrix()

    matrix.display_info()
    matrix.print_matrix()


def main():
    while True:
        menu()
        choice = input("Choose: ")
        if choice == "1":
            create_empty_matrix()

        elif choice == "2":
            run_default_example()

        elif choice == "3":
            fill_matrix()

        elif choice == "4":
            input_matrix()

        elif choice == "0":
            print()
            print("Thank you.")
            print("Program Finished.")
            break

        else:
            print()
            print("Invalid choice.")


if __name__ == "__main__":
    main()