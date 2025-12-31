# Prime Number Patterns

This project explores patterns in prime numbers by generating a list of primes up to a specified limit, calculating the gaps between consecutive primes, and visualizing these gaps using matplotlib plots. Additionally, it compares prime number density with the natural logarithm approximation as per the Prime Number Theorem.

## Overview

Prime numbers are integers greater than 1 that have no positive divisors other than 1 and themselves. The gaps between consecutive primes (prime gaps) reveal interesting mathematical patterns. This script uses the Sieve of Eratosthenes to efficiently find primes and then plots the gaps to illustrate their distribution. Additionally, it explores prime density across different ranges and compares it with the theoretical approximation from the Prime Number Theorem (π(n) ≈ n/ln(n)).

### Key Features
- **Prime Generation**: Implements the Sieve of Eratosthenes to find all primes up to 10,000 (configurable).
- **Gap Calculation**: Computes the difference between each consecutive pair of primes.
- **Gap Visualization**: Creates a plot showing prime gaps vs. prime numbers, saved as a high-resolution PNG image.
- **Density Analysis**: Calculates prime density for various ranges and compares with 1/ln(n) approximation.
- **Density Visualization**: Generates a comparison plot of actual vs. approximated prime densities.

## Requirements

- Python 3.x
- matplotlib library
- math library (built-in)

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
- Display an interactive plot of prime gaps (if running in a GUI environment).
- Save the prime gaps plot as `prime_gaps.png` in the current directory.
- Calculate prime densities for various ranges.
- Display an interactive plot comparing prime density with natural log approximation.
- Save the density comparison plot as `prime_density_vs_natural_log.png` in the current directory.

## Code Structure

- `PrimePatterns` class:
  - `__init__(self, num_primes=10000)`: Initializes the sieve array and sets the limit.
  - `run()`: Executes the sieve to find primes and calculates gaps.
  - `plot()`: Uses matplotlib to create and save the prime gaps visualization.

- `PrimeDensityExperiments` class:
  - `__init__()`: Sets up lists for densities and ranges to test.
  - `run()`: Generates primes for different ranges, calculates actual densities, and computes 1/ln(n) approximations.
  - `plot()`: Creates a comparison plot of actual vs. approximated prime densities.

- `main()`: Instantiates both classes, runs their methods, and generates all plots.

## Output Explanation

### Prime Gaps Plot
The matplotlib plot displays:
- **X-axis**: Prime numbers (e.g., 2, 3, 5, 7, ...).
- **Y-axis**: Gaps between consecutive primes (e.g., gap for 3 is 1, for 5 is 2).
- **Plot Style**: Line plot with circular markers, showing how gaps tend to increase with larger primes.

This visualization helps demonstrate concepts from number theory, such as the Prime Number Theorem, where average gaps grow logarithmically.

### Prime Density Comparison Plot
This plot compares:
- **X-axis**: Upper limits of the ranges tested (1000, 10000, 100000, etc.).
- **Y-axis**: Prime density (fraction of numbers that are prime in each range).
- **Actual Density**: Blue line with circles showing computed prime densities.
- **Approximation**: Orange dashed line with squares showing 1/ln(n) values.

The plot illustrates how prime density decreases with larger numbers and approaches the theoretical approximation from the Prime Number Theorem.

## Example Output

After running, you'll see plots like these (conceptually):

### Prime Gaps Plot
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

### Prime Density Comparison Plot
```
Prime Number Density vs Natural Log Approximation
|
|     s--  (approximation)
|    /
|   o     (actual)
|  /
| o
+-----------------
    Range of Numbers
```

The saved images `prime_gaps.png` and `prime_density_vs_natural_log.png` are high-resolution (300 DPI) files.

## Customization

- To change the number of primes for gap analysis, modify `num_primes` in the `PrimePatterns` constructor (e.g., `PrimePatterns(50000)` for more primes).
- To adjust the ranges for density analysis, modify `self.num_primes_list` in `PrimeDensityExperiments.__init__()`.
- Adjust plot parameters in the `plot()` methods for different styles, colors, or labels.

## License

This project is open-source. Feel free to modify and distribute.

## Observations

I used Python to generate prime numbers efficiently using the Sieve of Eratosthenes and analyzed patterns such as prime gaps and prime density. 

- Prime gaps generally increase as numbers grow larger, though small gaps persist unpredictably
- The empirical density of primes closely follows the theoretical 1 / ln(n) approximation
- Log-scaled plots reveal the slow decay of prime density across increasing ranges

## Future work
The problem with the Eratosthenes sieve algorithm is that it consumes memory that is proportional to the number of prime numbers
that we want to generate. We can do something better by segmenting the range into smaller chunks so that we can constrain the amount
of memory that the program uses. I will follow-up on the changes in a future change.

