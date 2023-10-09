def pencocokanString(pattern, text):
    n = len(pattern)
    m = len(text)

    i = 0
    found = False

    while(i <= n-m) and (found == False):
        j = 0
        while (j < m) and (pattern[i+j] == text[j]):
            j += 1

        if (j == m):
            found = True
        else:
            i += 1

    if (found == True):
        idx = i  # Adjusted to 0-based indexing
    else:
        idx = -1

    return found, idx

a = "Universitas Pembangunan Jaya"
b = "Pembangunan"

print(pencocokanString(a, b))
