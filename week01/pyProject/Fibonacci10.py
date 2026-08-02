if __name__ == "__main__":
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    print "Fibonacci sequence (10 iterations):"
    
    # Iterate 10 times
    for _ in range(10):
        print a,  # Adding a comma at the end keeps the print job on the same line
        a, b = b, a + b
    
    print ""