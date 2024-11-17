# twosum


Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Problem boils down to the time complexity we wanna achieve, in this example I got o(n^2), Think I wanna Improve that as I go along but let it stay like this for now

I mainly started this to improve on my coding consistency and improve my problem solving skills.

The problem is solved with this logic:

We start at the index 0 and we loop through the other numbers and try to see if (it+other indices)=target, if it is true, then we found our pair, if not, we go to the next index

