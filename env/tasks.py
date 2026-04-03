TASKS = {
    "easy": [
        {
            "code": "def add(a,b):\n return a+b",
            "issues": ["missing space", "indentation"],
        }
    ],
    "medium": [
        {
            "code": "for i in range(10): print(i)",
            "issues": ["bad formatting", "one-line loop"],
        }
    ],
    "hard": [
        {
            "code": "password = input(); print(password)",
            "issues": ["security risk", "exposing sensitive data"],
        }
    ]
}