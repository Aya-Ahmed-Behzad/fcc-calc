# Mean-Variance-Standard Deviation Calculator

## Project Description
This **python** project is a solution to this [FreeCodeCamp project](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator).
This project implements a Python function `calculate()` that uses **NumPy** library to compute basic statistical operations on a 3x3 matrix. The function takes a list of 9 numerical values, converts it into a 3x3 matrix, and calculates the **mean**, **variance**, **standard deviation**, **max**, **min**, and **sum** along both the rows, columns, and flattened matrix.

The result is returned as a dictionary containing these statistical measures for each axis (rows, columns) as well as the flattened matrix. If the input list does not contain exactly 9 elements, a `ValueError` is raised.

## Project Structure

- `mean_var_std.py`: The main Python file that contains the `calculate()` function.
- `main.py`: A script for testing the `calculate()` function.
- `test_module.py`: Unit tests for the `calculate()` function. To check for valid inputs, edge cases, and invalid inputs.
- `README.md`: Project documentation (this file).

## Function Description

### `calculate()`

The function `calculate()` accepts a list of 9 numbers, which is then converted into a 3x3 Numpy array. It calculates the following statistical metrics:

- **mean**: Mean of the rows, columns, and the flattened matrix.
- **variance**: Variance of the rows, columns, and the flattened matrix.
- **standard deviation**: Standard deviation of the rows, columns, and the flattened matrix.
- **max**: Maximum values of the rows, columns, and the flattened matrix.
- **min**: Minimum values of the rows, columns, and the flattened matrix.
- **sum**: Sum of the rows, columns, and the flattened matrix.

The function returns a dictionary with the following structure:

```python
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
```

## Example:
```python
calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
```
Returns:

```python
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```
## Error Handling
If the input list contains fewer or more than 9 elements, the function will raise a ValueError with the message:

```text
"List must contain nine numbers."
```
To test the calculate( ) function, run the main.py script:

```bash
python3 main.py
```
## Requirements
- Python 3.x: The project is designed to run with Python 3.
- NumPy: The NumPy library is used for numerical calculations.
