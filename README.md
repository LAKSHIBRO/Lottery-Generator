## What it does

"Lottery Generator" is a Python-based lottery number generator that creates unique sets of numbers for lottery enthusiasts. It leverages the unpredictability of the current time down to microseconds to simulate the randomness of a lottery draw, providing users with a fresh set of numbers every time they run the program.

## How I built it

The generator was built using Python, without the reliance on external libraries, to ensure simplicity and ease of use. The core of the program hinges on the current system time, which provides a constantly changing seed for generating random numbers.

## Challenges I ran into

A significant challenge was ensuring the uniqueness of each number in a set, as duplicates would not be valid in an actual lottery. I addressed this by implementing a loop that checks for and excludes any repeats, ensuring every number in the set is unique.

## What I learned

Through this project, I learned more about the intricacies of random number generation and the importance of creating a user-friendly interface, even in a simple command-line program.
