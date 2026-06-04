# Assignment: Shutdown
# Write a program to define the shutdown function.

def shut_down(s):
    # This function is used to shut down or abort depending on the input s
    if s.lower() == "yes":
        return "Shutting down"
    elif s.lower() == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

# Test the function with different cases
print(shut_down("yes"))
print(shut_down("no"))
print(shut_down("maybe"))
