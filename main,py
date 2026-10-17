# ==========================================
# PHASE 2: Identity-Based Computational Seed
# ==========================================

# ===== STUDENT IDENTITY =====
LAST_NAME = "Viana"
STUDENT_ID = "TUPM-26-1953"

# ===== DERIVE PARAMETERS =====
seed_digit = int(STUDENT_ID[-1])
id_checksum = sum(int(d) for d in STUDENT_ID if d.isdigit())
vector_dim = len(LAST_NAME)

# ===== ENCAPSULATE IN DICTIONARY =====
sys_config = {
    "operator": LAST_NAME,
    "auth_id": STUDENT_ID,
    "base_seed": seed_digit,
    "checksum": id_checksum,
    "status": "INITIALIZED",
    "vector_dim": vector_dim
}

# ===== DISPLAY OUTPUT =====
print("=== SYSTEM CONFIGURATION ===")
for key, value in sys_config.items():
    print(f"{key.upper()}: {value}")
    print("\n" + "="*50)
print("PHASE 3: MUTABLE SEQUENCES")
print("="*50)

base_val = sys_config["base_seed"]

# --- Task 5: Dynamic List Operations ---
number_sequence = [base_val, base_val + 15, sys_config["checksum"]]
print(f"Initial Sequence: {number_sequence}")

number_sequence.append(base_val + 20)
print(f"After Append: {number_sequence}")

# --- Task 6: Sequential Operations ---
new_numbers = [base_val + 5, sys_config["vector_dim"], base_val]
number_sequence.extend(new_numbers)
print(f"After Extend: {number_sequence}")

base_count = number_sequence.count(base_val)
print(f"Occurrences of {base_val}: {base_count}")

number_sequence.sort()
print(f"Sorted Sequence: {number_sequence}")
print("\n" + "="*50)
print("TASK 7: IMMUTABLE TUPLES")
print("="*50)

# Define an immutable tuple using system parameters
fixed_coordinates = (sys_config["vector_dim"], sys_config["base_seed"], 0)
print(f"Fixed Coordinates: {fixed_coordinates}")

# Unpack the tuple into individual variables
x_val, y_val, z_val = fixed_coordinates
print(f"Unpacked Values -> X: {x_val}, Y: {y_val}, Z: {z_val}")

# Attempt to modify the tuple (Expected to fail)
print("\nAttempting modification...")
try:
    fixed_coordinates[0] = 99
except TypeError as error_msg:
    print(f"Modification Error: {error_msg}")
    print("\n" + "="*50)
print("TASK 8: KEY-VALUE MAPPINGS")
print("="*50)

# Create a dictionary representing a structured data payload
data_payload = {
    "identifier": sys_config["auth_id"],
    "dimension": sys_config["vector_dim"],
    "status": "active"
}

# Iterate and display key-value pairs
print("--- Payload Data ---")
for key, value in data_payload.items():
    print(f"{key.capitalize()}: {value}")

# Add a new key-value pair dynamically
data_payload["efficiency_rating"] = 98.5
print(f"\nUpdated Payload: {data_payload}")
print("\n" + "="*50)
print("TASK 9: DATA DE-DUPLICATION")
print("="*50)

base_val = sys_config["base_seed"]

# Initialize a list with deliberate duplicate values
raw_data = [base_val, base_val + 5, base_val, sys_config["vector_dim"], base_val + 5]
print(f"Raw List (with duplicates): {raw_data}")

# Convert the list to a set to remove duplicates
unique_data = set(raw_data)
print(f"Unique Set: {unique_data}")
print("\n" + "="*50)
print("TASK 10: MATHEMATICAL SET OPERATIONS")
print("="*50)

# Define a secondary reference set for comparison
reference_set = {base_val, base_val + 10, base_val + 20}
print(f"Reference Set: {reference_set}")

# Perform intersections and unions
common_elements = unique_data.intersection(reference_set)
combined_elements = unique_data.union(reference_set)

print(f"Intersection (Common): {common_elements}")
print(f"Union (Combined): {combined_elements}")
print("\n" + "="*50)
print("TASK 11: HOMOGENEOUS ARRAYS")
print("="*50)

import array

# Initialize an integer array using type code 'i'
number_array = array.array('i', [sys_config["base_seed"],
                                  sys_config["vector_dim"],
                                  100])
print(f"Integer Array: {number_array}")

# Attempt to append a non-integer data type (Expected to fail)
print("\nAttempting to append a string...")
try:
    number_array.append("invalid")
except TypeError as error_msg:
    print(f"Type Error: {error_msg}")
    print("\n" + "="*50)
print("TASK 12: LIST COMPREHENSIONS")
print("="*50)

base_val = sys_config["base_seed"]

# Generate a sequence dynamically
generated_list = [(x * base_val) for x in range(1, 6)]
print(f"Generated Comprehension: {generated_list}")

# Filter the generated sequence
filtered_list = [x for x in generated_list if x > 15]
print(f"Filtered Comprehension (Values > 15): {filtered_list}")
print("\n" + "="*50)
print("TASK 13: DOUBLE-ENDED QUEUES (DEQUE)")
print("="*50)

from collections import deque

# Initialize a double-ended queue
data_queue = deque([sys_config["base_seed"], sys_config["vector_dim"]])
print(f"Initial Deque: {data_queue}")

# Append to both ends
data_queue.append(100)
data_queue.appendleft(200)
print(f"After Appends: {data_queue}")

# Remove from the left side
data_queue.popleft()
print(f"Final Deque (After Popleft): {data_queue}")
print("\n" + "="*50)
print("TASK 14: FAULT-TOLERANT KEY MAPPINGS (DEFAULTDICT)")
print("="*50)

from collections import defaultdict

# Initialize with a default integer factory (creates 0 for missing keys)
default_data = defaultdict(int)

# Assign a known key
default_data['active_key'] = sys_config["vector_dim"]
print(f"Existing Key Value: {default_data['active_key']}")

# Accessing an uninitialized key will NOT throw a KeyError
print(f"Missing Key Value (Auto-generated): {default_data['unknown_key']}")