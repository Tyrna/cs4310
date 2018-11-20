Program must run using: Python3.

The following program solves the stablished Equalizing problem in linear time.

The premise of my solution consists of:

> Get the summation of all the cards on each pile, to know what we're equalizing to
> Starting from the first pile of cards, find out how many cards you need to equalize yourself
> Steal from next neighbour how many cards you need
> By the end, they will all have the piles equalized

Following this logic, the amount of movements will never be more than (n-1).

This solution at worst always looks at all elements of our list once, and does movements of the cards at worst (n-1). So it's a O(n) solution.