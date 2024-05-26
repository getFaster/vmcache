import pandas as pd
import os

# Define file paths
random_files = [
    './data/result_rnd_o.txt', './data/result_rnd_m.txt', './data/result_rnd_me.txt', 
    './data/result_rnd_f.txt', './data/result_rnd_y.txt', './data/result_rnd_bm.txt'
]
tpc_files = [
    './data/result_o.txt', './data/result_m.txt', './data/result_me.txt', 
    './data/result_f.txt', './data/result_y.txt', './data/result_bm.txt'
]

methods_names = ['Original', 'Mutex', 'Merge', 'Futex', 'Yield-Opt', 'Bitmap']

# Define column names
columns = ['tx', 'rmb', 'wmb']

# Function to read data from files
def read_data(files):
    data = {}
    i = 0
    for file in files:
        method_name = methods_names[i]
        i += 1
        if os.path.exists(file):
            df = pd.read_csv(file, sep=',', header=None, names=columns)
            data[method_name] = df
        else:
            print(f"File not found: {file}")
    return data

# Read data
random_data = read_data(random_files)
tpc_data = read_data(tpc_files)

# Add Data Size column
data_sizes = list(range(5, 90, 5))
for df in random_data.values():
    df['Data Size'] = data_sizes
for df in tpc_data.values():
    df['Data Size'] = data_sizes

# Function to calculate improvement percentage
def calculate_improvement(original, modified):
    improvement = ((modified - original) / original) * 100
    return improvement

# Function to calculate overall improvement
def overall_improvement(data):
    improvements = {}
    for method, df in data.items():
        if method != 'Original':  # Skip original
            original_sum = data['Original'].sum()
            modified_sum = df.sum()
            improvements[method] = {
                'tx': calculate_improvement(original_sum['tx'], modified_sum['tx']).mean(),
                'rmb': calculate_improvement(original_sum['rmb'], modified_sum['rmb']).mean(),
                'wmb': calculate_improvement(original_sum['wmb'], modified_sum['wmb']).mean()
            }
    return improvements

# Calculate improvements
random_improvements = overall_improvement(random_data)
tpc_improvements = overall_improvement(tpc_data)

# Convert to DataFrame for better display
random_improvements_df = pd.DataFrame(random_improvements).T
tpc_improvements_df = pd.DataFrame(tpc_improvements).T

# Save to text files
random_improvements_df.to_csv('random_lookup_improvements.txt', sep='\t')
tpc_improvements_df.to_csv('tpc_c_improvements.txt', sep='\t')

print("Random Lookup Improvements:")
print(random_improvements_df)
print("\nTPC-C Improvements:")
print(tpc_improvements_df)