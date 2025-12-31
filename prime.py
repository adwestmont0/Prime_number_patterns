import matplotlib.pyplot as plt
import math

class PrimePatterns(object):
    def __init__(self, num_primes = 1000000):
        self.prime_numbers = []
        self.gaps = []
        self.num_primes = num_primes
        self.is_prime = [True] * (num_primes + 1)
        self.is_prime[0] = self.is_prime[1] = False


    def run(self):
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
                else:
                    self.gaps.append(num)
                prev_prime = num


    def plot(self):
        plt.plot(self.prime_numbers, self.gaps, marker='o', linestyle='-', markersize=3)
        plt.title('Prime Numbers and Their Gaps')
        plt.xlabel('Prime Numbers')
        plt.ticklabel_format(style='plain', axis='x')
        plt.ylabel('Gaps Between Consecutive Primes')
        plt.grid(True)
        plt.show()
        plt.savefig('prime_gaps.png', dpi=300)
        plt.close()

        plt.hist(self.gaps, bins=30)
        plt.title("Distribution of Prime Gaps")
        plt.xlabel("Gap Size")
        plt.ylabel("Frequency")
        plt.show()
        plt.savefig('prime_gaps_histogram.png', dpi=300)
        plt.close()

class PrimeDensityExperiments(object):
    def __init__(self):
        self.densities = []
        self.num_primes_list = [1000, 10000, 100000, 1000000, 10000000, 100000000]
        self.natural_logs = [1 / math.log(n) for n in self.num_primes_list]

    def run(self):
        
        densities = []
        for num_primes in self.num_primes_list:
            a = PrimePatterns(num_primes)
            a.run()
            density = len(a.prime_numbers) / num_primes
            self.densities.append(density)
    
    def plot(self):
        plt.plot(self.num_primes_list, self.densities, marker='o', linestyle='-', markersize=3)
        plt.plot(self.num_primes_list, self.natural_logs, marker='o', linestyle='-', markersize=3)
        plt.ticklabel_format(style='plain', axis='x')
        plt.legend(['Actual Prime Density', '1 / ln(n) Approximation'])
        plt.title('Prime Number Density vs Natural Log Approximation')          
        plt.xlabel('Range of Numbers')
        plt.ylabel('Density of prime numbers in that range')
        plt.show()
        plt.savefig('prime_density vs natural_log.png', dpi=300)
        plt.close()
    
def main():
    a = PrimePatterns()
    a.run()
    a.plot()
    b = PrimeDensityExperiments()
    b.run()
    b.plot()

if __name__ == "__main__":
    main()