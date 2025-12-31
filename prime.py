import matplotlib.pyplot as plt

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


def main():
    a = PrimePatterns()
    a.run()
    a.plot()

if __name__ == "__main__":
    main()