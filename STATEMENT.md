This program is a small window app in Python that helps you do basic statistics and error calculation for measurements. It uses Tkinter to show input boxes, a button, and result labels on the screen.realpython​

Main work: calculate() function
It reads what you typed in the “Measured values” box and picks out all the numbers, even if they are separated by spaces, commas, or newlines.realpython​

It turns these numbers into floats and then finds:

Mean (average of all measured values).

Variance (how spread out the values are; uses sample variance if there is more than one value).

Standard deviation (square root of the variance).realpython​

If you also type a correct number in the “True value” box, it finds:

Absolute error = 
∣
mean
−
true value
∣
∣mean−true value∣.

Relative error = absolute error ÷ true value.

Percentage error = relative error × 100.

All these results are then shown in the labels in the window.realpython​

Error checking
If you do not enter any valid numbers in the measured values box, an error message pops up and tells you to fix the input.

If you type something that is not a number in the true value box, you also get an error message.

If some unexpected problem happens, a general error message is shown instead of crashing.stackoverflow​

Parts of the GUI
A text box for measured values where you can paste or type many numbers in any format.

A text box for the true value, which you can leave empty if you only want mean, variance, and standard deviation.

A “Calculate” button that runs the calculate() function.

Labels that show the mean, variance, standard deviation, and (if possible) absolute, relative, and percentage error; if error values cannot be computed, they show “N/A”.realpython​

How to use it
Type or paste your measured values in the first box, separated by spaces, commas, or newlines.

(Optional) Type the known true value in the second box.

Click “Calculate”.

Read the mean, variance, standard deviation, and error values in the labels below; if there is any problem with your input, an error message will tell you what to correct.realpython​
