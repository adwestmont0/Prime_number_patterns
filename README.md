# Prime Number Patterns

This project explores patterns in prime numbers by generating a list of primes up to a specified limit, calculating the gaps between consecutive primes, and visualizing these gaps using a matplotlib plot.

## Overview

Prime numbers are integers greater than 1 that have no positive divisors other than 1 and themselves. The gaps between consecutive primes (prime gaps) reveal interesting mathematical patterns. This script uses the Sieve of Eratosthenes to efficiently find primes and then plots the gaps to illustrate their distribution.

### Key Features
- **Prime Generation**: Implements the Sieve of Eratosthenes to find all primes up to 10,000 (configurable).
- **Gap Calculation**: Computes the difference between each consecutive pair of primes.
- **Visualization**: Creates a plot showing prime gaps vs. prime numbers, saved as a high-resolution PNG image.

## Requirements

- Python 3.x
- matplotlib library

## Installation

1. Ensure Python 3 is installed on your system.
2. Install the required library:
   ```
   pip install matplotlib
   ```

## Usage

1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the script:
   ```
   python prime.py
   ```

The script will:
- Generate prime numbers and their gaps.
- Display an interactive plot (if running in a GUI environment).
- Save the plot as `prime_gaps.png` in the current directory.

## Code Structure

- `PrimePatterns` class:
  - `__init__(self, num_primes=10000)`: Initializes the sieve array and sets the limit.
  - `run()`: Executes the sieve to find primes and calculates gaps.
  - `plot()`: Uses matplotlib to create and save the visualization.

- `main()`: Instantiates the class, runs the sieve, and generates the plot.

## Output Explanation

The matplotlib plot displays:
- **X-axis**: Prime numbers (e.g., 2, 3, 5, 7, ...).
- **Y-axis**: Gaps between consecutive primes (e.g., gap for 3 is 1, for 5 is 2).
- **Plot Style**: Line plot with circular markers, showing how gaps tend to increase with larger primes.

This visualization helps demonstrate concepts from number theory, such as the Prime Number Theorem, where average gaps grow logarithmically.

## Example Output

After running, you'll see a plot like this (conceptually):

```
Prime Numbers and Their Gaps
|
|     o
|    / \
|   o   o
|  /     \
| o       o
+-----------------
    Primes
```


The saved `prime_gaps.png` is a high-resolution (300 DPI image)

## Customization

- To change the number of primes, modify `num_primes` in the `PrimePatterns` constructor (e.g., `PrimePatterns(50000)` for more primes).
- Adjust plot parameters in the `plot()` method for different styles or labels.

## License

This project is open-source. Feel free to modify and distribute.

## Observations

I used Python to generate prime numbers efficiently using the Sieve of Eratosthenes and analyzed patterns such as prime gaps and prime density. By visualizing these properties, I observed that while primes become less frequent as numbers grow, small gaps remain common and larger gaps appear sporadically. This project demonstrated how computation can be used to explore deep mathematical patterns.

## Future work
The problem with the Eratosthenes sieve algorithm is that it consumes memory that is proportional to the number of prime numbers
that we want to generate. We can do something better by segmenting the range into smaller chunks so that we can constrain the amount
of memory that the program uses. I will follow-up on the changes in a future change.

