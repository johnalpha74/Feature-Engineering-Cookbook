# Load the KDDTrain+ and KDDTest+ datasets using pandas,
# assign correct column names, and print the first 10 rows

import pandas as pd

columns = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
    'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in',
    'num_compromised', 'root_shell', 'su_attempted', 'num_root',
    'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds',
    'is_host_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate',
    'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',
    'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count',
    'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate',
    'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
    'dst_host_srv_rerror_rate', 'label', 'difficulty'
]

# Load training data
train_path = "KDDTrain+.txt"
test_path  = "KDDTest+.txt"

df_train = pd.read_csv(train_path, header=None, names=columns)
df_test  = pd.read_csv(test_path,  header=None, names=columns)

print("Training set shape:", df_train.shape)
print("Test set shape:", df_test.shape)

# Print the first 10 rows of each dataset
print("\nFirst 10 rows of TRAIN set:")
print(df_train.head(10))

print("\nFirst 10 rows of TEST set:")
print(df_test.head(10))

# Check the number of unique attack labels
print("Unique labels in TRAIN set:")
print(df_train['label'].unique())

print("\nUnique labels in TEST set:")
print(df_test['label'].unique())

# Count how many rows belong to each label
print("\nLabel distribution in TRAIN set:")
print(df_train['label'].value_counts())

# Check the first few rows of specific important columns
df_train[['protocol_type', 'service', 'flag']].head(10)

# Check for missing values
print("\nMissing values in TRAIN set:")
print(df_train.isna().sum())

print("\nMissing values in TEST set:")
print(df_test.isna().sum())

# Display dataset info
df_train.info()
