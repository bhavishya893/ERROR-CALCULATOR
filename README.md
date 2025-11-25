# Error Calculator

This Python program provides a graphical user interface (GUI) to calculate statistical values and error metrics based on measured data and an optional true value. It uses Tkinter for the GUI and supports flexible inputs for measured values. The main processing logic is contained in the `calculate()` function.


## Functions and Their Uses

### `calculate()`

- **Purpose:**  
  This function processes the user inputs from the GUI, computes statistical properties of the measured values, and calculates error metrics if a true value is provided.

- **Input:**  
  - `Measured values`: A string input containing one or more numerical values separated by any delimiters (spaces, commas, newlines, etc). The function extracts valid numbers using regular expressions.  
  - `True value`: An optional string input representing the true or accepted value for error calculations.

- **Processing Steps:**  
  1. Extract valid numerical values from the measured values input string.  
  2. Convert these extracted strings to floats.  
  3. Calculate the mean of the measured values.  
  4. Calculate the variance (using sample variance formula if more than one value exists).  
  5. Calculate the standard deviation from the variance.  
  6. If a true value is provided and valid:  
     - Calculate the absolute error (difference between mean and true value).  
     - Calculate the relative error (absolute error divided by true value).  
     - Calculate the percentage error (relative error multiplied by 100).  
  7. Update the GUI labels to display these computed values.

- **Error Handling:**  
  - Shows error dialogs if the measured values input is empty or contains no valid numbers.  
  - Shows error if the true value is provided but invalid (non-numeric).  
  - Catches unexpected exceptions and shows a generic error message dialog.

- **Output:**  
  The calculated values are displayed in the GUI labels for:  
  - Mean  
  - Variance  
  - Standard deviation  
  - Absolute error  
  - Relative error  
  - Percentage error


## GUI Components and Their Uses

- **Measured values input (`entry_values`)**: Entry field where users input the measured numerical data. Supports flexible delimiters.

- **True value input (`entry_true`)**: Entry field for the known true value used in error calculations. Optional input.

- **Calculate button**: Triggers the `calculate()` function to process inputs and update results.

- **Result labels**: Display the computed values for mean, variance, standard deviation, and errors. If errors are not calculable (e.g., no true value), they show "N/A".


## How to Use

1. Enter the measured values into the first input box. You may separate numbers by spaces, commas, or other characters.  
2. (Optional) Enter the true value in the second input box for error calculations.  
3. Click the "Calculate" button. The statistical and error results will be shown in the labels below.  
4. If invalid inputs are detected, error dialogs will prompt you to correct them.

This tool is useful for scientific and engineering measurements where error analysis and statistics of repeated measurements are needed.
