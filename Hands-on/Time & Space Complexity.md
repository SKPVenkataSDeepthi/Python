# SPACE & TIME COMPLEXITY
Ex: Waiting in a line at a coffee shop. 

## O(1) 
Grabbing a pre-made cookie and walking out no matter how many are in the line

## O(LogN)
Is like asking if your order is in first half or 2nd half of the line -- They keep cutting the group in half until they find you. 

## O(N)
Imagine we are in a line, the time it takes depends on how many people are ahead of us. (More people = longer wait time)

## O(NLogN)
Sorting To-go's, regulars and newbies and then serving them. Sorting takes time. but is faster then serving everyone one-by-one in a random order. 

## O(N^2)
Say like every customer not only orders for themselves but also for their friends and for their families (5*5).

## O(2^N)
Shop will be indecisive that for every customer they try every possible drink combination - (5 customers - 2,4,6,8....) line gets slow and customer might leave shop before getting their order.

## O(N!)
Shop is trying every possible combination of drinks & serving orders in every possible sequence for all customers -- (3 people - 6(3*2*1)ways) -- (More people = more waiting)

# Big-O, Big-Omega, Big-Theta
Ex: Searching your friend in a party

## Big-O - Upper Bound 
* Worst Case
* Max time it might take to search for your friend  
* Suppose there are 500 people and you are checking each person one-by-one until you find your friend (max time O(n)).

## Big-Omega - Lower Bound
* Best and Worst Case
* Exact time it takes to search for your friend 
* Whether the part has 100 or 500 it always takes same amount of time to find your friend. 

## Big-Theta - Both(Big-O, Big-Omega) - Tight bound on runtime
* Best Case 
* Minimum time it takes to search for your friend
* If you already know where your friend is, you can walk straight to them. 


