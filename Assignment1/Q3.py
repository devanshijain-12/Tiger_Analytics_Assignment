words = input("Enter words: ").split()
unique_sorted = sorted(set(words))
print(' '.join(unique_sorted))
