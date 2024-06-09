# School Training Document: Regex Examples for Exam Preparation

This document is designed to help students practice and understand regular expressions (Regex) in preparation for their exams. It includes key symbols, simple explanations, and practical examples.

## Key Regex Symbols

### Special Characters

- `.` : Any character except newline.
- `^` : Start of a string.
- `$` : End of a string.
- `*` : Zero or more of the previous character.
- `+` : One or more of the previous character.
- `?` : Zero or one of the previous character.
- `\` : Escape special characters.
- `|` : OR operator.

### Quantifiers

- `{n}` : Exactly `n` occurrences.
- `{n,}` : `n` or more occurrences.
- `{n,m}` : Between `n` and `m` occurrences.

### Character Classes

- `[]` : Any one of the characters inside.
- `[^]` : Any character not inside.
- `\d` : Any digit (0-9).
- `\D` : Any non-digit.
- `\w` : Any word character (alphanumeric + underscore).
- `\W` : Any non-word character.
- `\s` : Any whitespace character.
- `\S` : Any non-whitespace character.

### Groups and References

- `()` : Capture group.
- `(?:...)` : Non-capturing group.
- `\n` : Backreference to the nth capture group.

### Practical Examples

- Matching Numbers: \d+
- Matching Words: \w+
- Matching Emails: \w+@\w+\.\w+

### Find more examples inside the code ! Have fun :)
