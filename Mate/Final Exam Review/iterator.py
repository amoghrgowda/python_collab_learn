class NumberIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # return itself

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # Signal the end of iteration
        value = self.current
        self.current += 1
        return value

num_iter = NumberIterator(1, 5)
for num in num_iter:
    print(num)  


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
        chunk = self.data[self.index: self.index + self.chunk_size]
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

def prime_numbers(num_stop):
    primes = [2]
    print(2)
    candidate = 3 

    while len(primes) < num_stop:
        if all(candidate % p != 0 for p in primes):
            primes.append(candidate)
            print(candidate)
        candidate += 2  # we can skip even numbers, since they can't be prime

# Generate the first 10 prime numbers
# prime_numbers(10)

'''
Now, we would like make a change: Instead of printing each number on a different line, we would like to iterate over the prime numbers and concatenate them as a comma-separated string. i.e. "2,3,5,...". 

One bad choice is to change the prime_numbers function to handle string formatting. If we expect more changes to formatting, we would be prone to introducing errors because modifications have to made to multiple locations.

Instead, let's refactor the code such that prime_numbers becomes a python generator. Fill in the ??? holes.
'''
def prime_numbers_generator():
    primes = [2]
    yield 2
    candidate = 3 

    while True:
        if all(candidate % p != 0 for p in primes):
            primes.append(candidate)
            yield candidate
        candidate += 2  # Skip even numbers

# Generate the first 10 prime numbers using the generator
prime_gen = prime_numbers_generator()
sep = ", "
primes = []
for _ in range(10):
    primes.append(next(prime_gen))
print(sep.join(map(str, primes)))