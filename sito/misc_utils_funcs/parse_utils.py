def insert_underscore_name(nominativo: str) -> str:
    return "_".join(nominativo.split())


def remove_underscore_name(nominativo: str) -> str:
    return " ".join(nominativo.split("_"))


def capitalize_all(nominativo: str) -> str:
    nominativo = nominativo.split()
    nominativo = [parola.capitalize() for parola in nominativo]
    nominativo = " ".join(nominativo)
    return nominativo