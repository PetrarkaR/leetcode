# roman to integer 

the algorithm boils down to evaluating each numbers position in the array, if a number is behind a larger number, then  it subracts from the total sum, if it is the same or larger then it adds towards the sum, for example XL would be evaluated as -10 + 50 = 40 which is correct according to our algo, the main problem of this solution is the conversion between types