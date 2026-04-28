class ChunkIterator:
    def __init__(self, data, chunk_size):
        self.data = data
        self.chunk_size = chunk_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        
        chunk = self.data[self.index:self.index + self.chunk_size]
        self.index += self.chunk_size
        return chunk

data = list(range(1, 21))  
chunk_size = 5

chunk_iter = ChunkIterator(data, chunk_size)
for chunk in chunk_iter:
    print(chunk)
# It should print:
# [1, 2, 3, 4, 5]
# [6, 7, 8, 9, 10]
# [11, 12, 13, 14, 15]
# [16, 17, 18, 19, 20]


'''
EXERCISE 2
'''

def prime_numbers_generator():
    primes = [2]
    yield 2 # first prime 
    
    candidate = 3 

    # keeps going truing to find new prime
    while True:
        if all(candidate % p != 0 for p in primes):
            primes.append(candidate)
            yield candidate
        candidate += 2  # Skip even numbers

# Generate the first 10 prime numbers using the generator
prime_gen = prime_numbers_generator()
#for _ in range(10):
#    print(next(prime_gen))

primes = []
for _ in range(10):
    primes.append(next(prime_gen))
separator = ", "
result_string = separator.join(map(str, primes))
print(result_string)