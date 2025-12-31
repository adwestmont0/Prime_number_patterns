import matplotlib.pyplot as plt
import math

'''
This module analyzes prime numbers up to a specified limit, computes the gaps between consecutive primes,
and visualizes both the gaps and the histogram of these gaps.
'''
class PrimePatterns:
    def __init__(self, num_primes = 1000000):
        
        self.prime_numbers = []
        self.gaps = []
        self.num_primes = num_primes
        self.is_prime = [True] * (num_primes + 1)
        self.is_prime[0] = self.is_prime[1] = False


    def compute_prime_gaps(self, log_mean_max = False):
        # This is a simple Sieve of Eratosthenes implementation to find all prime numbers up to self.num_primes
        for i in range(2, int(self.num_primes**0.5) + 1):
            if self.is_prime[i]:
                for j in range(i*i, self.num_primes + 1, i):
                    self.is_prime[j] = False

        prev_prime = None
        for num in range(2, self.num_primes + 1):
            if self.is_prime[num]:
                self.prime_numbers.append(num)
                if prev_prime is not None:
                    self.gaps.append(num - prev_prime)
                prev_prime = num
        if log_mean_max:
            print((f"Total primes found: {len(self.prime_numbers)} in range up to {self.num_primes}"))
            print(f"Mean prime gap: {sum(self.gaps)/len(self.gaps):.2f}")
            print(f"Max prime gap: {max(self.gaps)}")

    def plot_prime_gaps(self):
        plt.plot(self.prime_numbers[1:], self.gaps, marker='o', linestyle='-', markersize=3)
        plt.title('Prime Numbers and Their Gaps')
        plt.xlabel('Prime Numbers')
        plt.ticklabel_format(style='plain', axis='x')
        plt.ylabel('Gaps Between Consecutive Primes')
        plt.grid(True)
        plt.savefig('prime_gaps.png', dpi=300)
        plt.show()
        plt.close()

        plt.hist(self.gaps, bins=30)
        plt.title("Distribution of Prime Gaps")
        plt.xlabel("Gap Size")
        plt.ylabel("Frequency")
        plt.yscale('log')
        plt.savefig('prime_gaps_histogram.png', dpi=300)
        plt.show()
        plt.close()


'''
This module conducts experiments to compare the actual density of prime numbers
with the theoretical approximation of 1 / ln(n). It used the PrimePatterns class to gather prime data
up to various limits and then plots the results. The class visualizes upto 1,000,000 primes to constrain
the computation and memory load. Extending it to handle higher numbers would require a segmented sieve approach
that can be more memory efficient.
'''

class PrimeDensityExperiments:
    def __init__(self):
        self.densities = []
        self.num_primes_list = [1000, 10000, 100000, 1000000]
        self.natural_logs = [1 / math.log(n) for n in self.num_primes_list]

    def compute_prime_densities(self):
        for num_primes in self.num_primes_list:
            a = PrimePatterns(num_primes)
            a.compute_prime_gaps()
            density = len(a.prime_numbers) / num_primes
            self.densities.append(density)
    
    def plot_prime_densities(self):
        plt.plot(self.num_primes_list, self.densities, linestyle='-', marker='*', markersize=3)
        plt.plot(self.num_primes_list, self.natural_logs, linestyle='-', marker='*', markersize=3)
        plt.ticklabel_format(style='plain', axis='x')
        plt.xscale('log')
        plt.legend(['Actual Prime Density', '1 / ln(n) Approximation'])
        plt.title('Prime Number Density vs Natural Log Approximation')          
        plt.xlabel('Range of Numbers')
        plt.ylabel('Density of prime numbers in that range')
        plt.savefig('prime_density vs natural_log.png', dpi=300)
        plt.show()
        plt.close()
    
def main():
    a = PrimePatterns()
    a.compute_prime_gaps(True)
    a.plot_prime_gaps()
    b = PrimeDensityExperiments()
    b.compute_prime_densities()
    b.plot_prime_densities()

if __name__ == "__main__":
    main()