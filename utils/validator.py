FORBIDDEN = [
    "DROP",
    "DELETE",
    "UPDATE",
    "INSERT",
    "ALTER",
    "TRUNCATE"
]


def validate(sql):

    upper = sql.upper()

    for word in FORBIDDEN:

        if word in upper:
            return False

    return True