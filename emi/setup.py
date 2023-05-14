from setuptools import setup, find_packages
setup(
    name='emi_calculator',
    version='1.0.1',
    author='Lalit Rajbanshi',
    author_email='lalitrajbanshi45@gmail.com',
    description='The EMI Library is a Python library that provides a convenient way to calculate the Equated Monthly Installment (EMI) for loans. The library implements the EMI formula, which takes into account the principal loan amount, interest rate, and tenure in months.',
    long_description="""
            EMI Calculator Library
            =====================

            The EMI Calculator Library is a Python library that provides a simple and efficient way to calculate the Equated Monthly Installment (EMI) for loans. It enables developers to incorporate EMI calculations into their applications, making it easier to determine the fixed monthly payment amount that borrowers need to make towards a loan.

            Features
            --------

            - Calculates the Equated Monthly Installment (EMI) based on the principal loan amount, interest rate, and tenure.
            - Handles both the principal amount and the interest in the EMI calculation, providing accurate results.
            - Flexible and easy to use, allowing developers to integrate EMI calculations seamlessly into their applications.
            - Provides configurable options to handle different compounding frequencies and interest calculation methods.
            - Includes error handling and validation to ensure accurate input and calculations.

            Usage
            -----

            To use the EMI Calculator Library, follow these simple steps:

            1. Install the library using pip:

                ```shell
                pip install emi_calculator
                ```

            2. Import the `emi_calculator` function from the library:

                ```python
                from emi_calculator import emi_calculator
                ```

            3. Call the `emi_calculator` function with the loan details to calculate the EMI:

                ```python
                loan_amount = 100000  # Replace with the principal loan amount
                interest_rate = 12  # Replace with the monthly interest rate
                tenure_months = 36  # Replace with the number of monthly installments

                emi = emi_calculator(loan_amount, interest_rate, tenure_months)
                print(f"The Equated Monthly Installment (EMI) is: {emi:.2f}")
                ```

            For more advanced usage and customization options, please refer to the documentation.

            License
            -------

            The EMI Calculator Library is released under the MIT License. See the LICENSE file for more details.

            Contributing
            ------------

            Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request on the GitHub repository.

            """,
    long_description_content_type='text/markdown',
    url='https://github.com/Zack1o1/emi-calculator',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.7',
)
