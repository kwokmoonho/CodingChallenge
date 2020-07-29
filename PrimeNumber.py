#Find the prime number
#

def getPrimeFactors(N):
    factors = []
    divisor = 2
    while (divisor <= N):
        if (N % divisor == 0):
            factors.append(divisor)
            N /= divisor
        else:
            divisor += 1
    print(factors)

def main():
    getPrimeFactors(360) #[2,3,3,5,7]
    getPrimeFactors(13) #[13]


if __name__ == "__main__":
    main()