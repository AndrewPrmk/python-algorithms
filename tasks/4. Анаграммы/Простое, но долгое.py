def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)

print(is_anagram("кино", "кони"))          # True
print(is_anagram("кот", "ток"))            # True
print(is_anagram("апельсин", "спаниель"))  # True
print(is_anagram("сон", "нос"))            # True

print(is_anagram("кот", "кит"))            # False
print(is_anagram("дом", "мода"))           # False
print(is_anagram("abc", "ab"))             # False
print(is_anagram("a", "aa"))               # False

print(is_anagram("", ""))                  # True
print(is_anagram("а", "а"))                # True
print(is_anagram("а", "б"))                # False

print(is_anagram("Listen", "Silent"))      # False
print(is_anagram("listen", "silent"))      # True