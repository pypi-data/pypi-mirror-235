import builtins


def check(rabbit: str):
    """
    Checks the input for potential issues such as:
     - encoding problems,
     - SQL queries,
     - Python/JS-related issues.

    :param rabbit: The input to be validated.
    """

    try:
        try:
            rabbit.encode('utf-8')
        except UnicodeEncodeError:
            raise ValueError("The encoding should be utf-8!")

        if type(rabbit) is not builtins.str:
            raise ValueError("Bad characters!")

        if " " in rabbit:
            raise ValueError("Using spaces is disallowed!")

        string_to_check = rabbit.strip().lower()

        __py_forbidden_chars = (
            "\'", '\"', '=', 'or', 'in', 'for', 'while', 'true', 'false', '$', '#', ';', '(', ')', '-', '&', '%', '<', '>')

        sql_forbidden_queries = (
            "select",
            "insert",
            "update",
            "delete",
            "drop table",
            "create table",
            "alter table",
            "union"
        )

        forbidden = __py_forbidden_chars + sql_forbidden_queries

        for char in string_to_check:
            if char in forbidden:
                raise ValueError(f"Using {char} is disallowed.")

        return rabbit

    except Exception:
        raise ValueError("Invalid input")
