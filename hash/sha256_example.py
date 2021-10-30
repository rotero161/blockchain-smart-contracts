"""
In this script we set a function for calculating the SHA256 hash for any string introduced.
"""

# Import the library
import hashlib

# Encode the message to bytes
message = "Poker de Hashes is the best group".encode()

# Example with SHA-256

print("SHA-256:", hashlib.sha256(message).hexdigest())