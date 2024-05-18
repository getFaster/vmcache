# vmcache

For a detailed introduction, please refer to the original author's code [vmcache](https://github.com/viktorleis/vmcache). This document focuses on our modifications.

## Code Overview

vmcache is an implementation of an efficient buffer manager and B-tree data structure designed for managing and accessing large-scale data. The programs in the `./src` directory are based on the original version but have been modified in various ways to enhance the performance of vmcache. The modifications include bitmap, futex, merge, mutex, and yopt approaches. Besides completing the author's TODOs, the aim is to improve the overall efficiency of vmcache.

- **bitmap**: Implements free space management for storage.
- **futex** and **mutex**: Handle mutual exclusion locks.
- **merge**: Completes the unfinished B-tree inner node merge by the original author.
- **yopt**: Dynamically adjusts the waiting strategy of the original spinlock based on the duration.

Additional files:

- `colab_example.ipynb`: An example of how to execute the program, intended to be run on Google Colab.
- `test.sh`: A script for automated testing.
- `test_analysis.py`: Calculates the average from each program execution's output and writes the results to a file.
- `plot_data.py`: Visualizes the data from the results file.
- `plot_cmp.py`: Compares multiple data sets using line charts, with results available in `./pic`.
- `plot_cmp_sub.py`: Creates five subplots to compare each of the five methods with the original implementation for clearer presentation, with results available in `./pic_sub`.

## Comparison Data

- **tx**: Transaction throughput.
- **rmb** and **wmb**: Read and write throughput, respectively.
- **Data size**: Ranges from 5 to 85, in increments of 5.
- **Benchmarks**: Includes Random read benchmark and TPC-C.

There are six data sets in total, including the original version. All data sets are presented in a line chart available in `./pic`. Comparisons between each method and the original version are available in `./pic_sub`.

## Environment

The code is executed using Google Colab. For detailed instructions, please refer to `colab_example.ipynb`. The code requires an environment running Ubuntu 22.04 or later, with GCC version 10.0 or higher. The program uses a Loop Device to simulate storage access.

- **Colab CPU**: Intel(R) Xeon(R) CPU @ 2.20GHz, 2 cores, 4 threads.

**Note**: When running `test.sh`, if the data size exceeds 30, a `structure needs cleaning` issue might occur. In such cases, you must manually execute the commands one by one.
