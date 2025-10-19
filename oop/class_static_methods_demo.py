class Calculator:
    calculation_type = "Arithmetic Operations" 


    @staticmethod
    def add(a , b):
        return a + b

   
    @classmethod
    def multiply(cls, a, b):
        print(f"calculation_type: {cls.calculation_type}")
        return a * b





