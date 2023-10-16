class Calculator:
    """A calculator class for basic arithmetic operations."""
    def __init__(self): 
        """Initialize the calculator with a result of 0."""
        self.result = 0

    def addition(self, input_number):
        """
        Add the input number to the current result.

        Args:
            input_number (float or int): The number to add to the result.

        Returns:
            float: The updated result after addition.
        """
        self.result += input_number
        return self.result
    
    def substraction(self, input_number):
        """
        Substract the input number from the current result.

        Args:
            input_number (float or int): The number to substract from the result.

        Returns:
            float: The updated result after substraction.
        """
        self.result -= input_number
        return self.result
    
    def multiplication(self, input_number):
        """
        Multiply the current result by the input number.

        Args:
            input_number (float): The number to multiply the result by.

        Returns:
            float: The updated result after multiplication.
        """
        self.result *= input_number
        return self.result
    
    def division(self, input_number):
        """
        Divide the current result by the input number.

        Args:
            input_number (float): The number to divide the result by.

        Returns:
            float: The updated result after division.

        Raises:
            ValueError: If the input_number is 0 (division by zero is not allowed).
        """
        if input == 0:
            raise ValueError("Division by zero is not allowed. Please enter another number.")
        self.result /= input_number
        return self.result
    
    def take_n_root(self, n):
        """
        Calculate the nth root of the current result.

        Args:
            n (int): The root to calculate.

        Returns:
            float: The updated result after taking the nth root.

        Raises:
            ValueError: If the result is negative and n is even (even-root of a negative number is not allowed).
        """
        if self.result < 0 and n % 2 ==0:
            raise ValueError("It is not allowed to calculate even-root of a negative number. Please enter another number.")
        self.result **= (1 / n)
        return self.result
    
    def reset_memory(self):
        """Reset the result to 0."""
        self.result = 0
        return self.result
    


