# Caching Algorithms

This project explores different caching algorithms implemented in Python. Caching is a technique used to store frequently accessed data in a faster access medium (cache) to improve system performance. This project covers various cache replacement policies including FIFO, LIFO, LRU, MRU, and LFU.

## Table of Contents

- [Background](#background)
- [Requirements](#requirements)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Background

In this project, we implement caching algorithms to understand how different strategies affect cache performance and efficiency. Each caching algorithm has its own approach to deciding which items to keep in the cache and which ones to evict when the cache is full.

### Cache Replacement Policies Explored:

- **FIFO**: First In, First Out
- **LIFO**: Last In, First Out
- **LRU**: Least Recently Used
- **MRU**: Most Recently Used
- **LFU**: Least Frequently Used

## Requirements

- Python 3.7 or later
- `pycodestyle` for code style enforcement

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/caching-algorithms.git

```
2. Navigate to the project directory:

```bash
cd caching-algorithms
```
  3. Execute the test scripts to run individual caching algorithms:

```bash

./0-main.py
./1-main.py
# Continue with other test scripts as needed
```

## Project Structure

    base_caching.py: Contains the BaseCaching class, the parent class for all caching algorithms.
    0-basic_cache.py: Implementation of the basic cache class without any limit on cache size.
    1-fifo_cache.py: Implementation of FIFO caching algorithm.
    2-lifo_cache.py: Implementation of LIFO caching algorithm.
    3-lru_cache.py: Implementation of LRU caching algorithm.
    4-mru_cache.py: Implementation of MRU caching algorithm.
    100-lfu_cache.py: Implementation of LFU caching algorithm.

## Testing

The project includes test scripts (e.g., 0-main.py, 1-main.py, ..., 100-main.py) to evaluate the correctness and functionality of each caching algorithm. Run these test scripts to see the algorithms in action and verify their behavior.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
