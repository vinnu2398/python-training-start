# ==========================================
# Name: Vishal Vasudev
# Date: 17-11-2026
# Module 2: Core Fundamentals
# ==========================================

# 1. Memory Mapping
x = 256
y = 256

# 2. Cache Limit
a = 257
b = 257

# 3. Boolean Identity
is_same_identity = a is b
is_same_value = a == b

# 4. NoneType Check
status = None

# 5. Output
print(
    f"x id: {id(x)} \n"
    f"y id: {id(y)} \n"
    f"a id: {id(a)} \n"
    f"b id: {id(b)} \n"
    f"Identity (a is b): {is_same_identity} \n"
    f"Equality (a == b): {is_same_value} \n"
    f"Status type: {type(status)} \n"
    f"Status id: {id(status)}"
)

# output :
# x id: 140722237408344 
# y id: 140722237408344 
# a id: 1395300282832 
# b id: 1395300282832 
# Identity (a is b): True 
# Equality (a == b): True 
# Status type: <class 'NoneType'> 
# Status id: 140722236500800
