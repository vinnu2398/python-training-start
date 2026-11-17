# ==========================================
# Name: Vishal Vasudev
# Date: 17-11-2026
# Module 2: Core Fundamentals
# ==========================================

# 1. Define Flags
GUEST = 1       # 0001
USER = 2        # 0010
ADMIN = 4       # 0100
SUPERUSER = 8   # 1000

# 2. Operations

# Combine using OR (|)
current_access = GUEST | USER

# Elevate using Left Shift (<<)
NEW_SECURE_LEVEL = ADMIN << 1

# Check USER permission using AND (&)
has_user_permission = current_access & USER

# Toggle GUEST permission using XOR (^)
updated_access = current_access ^ GUEST

# 3. Binary output in Decimal and Binary
print("\n----- Bitwise Permissions & Flag Manipulation -----")

print("\n--- Original Security Flags ---")

print(f"GUEST: {GUEST} | Binary: {bin(GUEST)}")
print(f"USER: {USER} | Binary: {bin(USER)}")
print(f"ADMIN: {ADMIN} | Binary: {bin(ADMIN)}")
print(f"SUPERUSER: {SUPERUSER} | Binary: {bin(SUPERUSER)}")

print("\n--- Bitwise Operations ---")

print(f"Current Access: {current_access} | Binary: {bin(current_access)}")
print(f"New Secure Level: {NEW_SECURE_LEVEL} | Binary: {bin(NEW_SECURE_LEVEL)}")
print(f"USER Permission Check: {has_user_permission} | Binary: {bin(has_user_permission)}")
print(f"Updated Access: {updated_access} | Binary: {bin(updated_access)}")

# output : 
# ----- Bitwise Permissions & Flag Manipulation -----

# --- Original Security Flags ---
# GUEST: 1 | Binary: 0b1
# USER: 2 | Binary: 0b10
# ADMIN: 4 | Binary: 0b100
# SUPERUSER: 8 | Binary: 0b1000

# --- Bitwise Operations ---
# Current Access: 3 | Binary: 0b11
# New Secure Level: 8 | Binary: 0b1000
# USER Permission Check: 2 | Binary: 0b10
# Updated Access: 2 | Binary: 0b10
