def decorate_file_name(file_name: str, suffix="_reduced_summary") -> str:
    name, extension = file_name.split(".")

    return f"{name}{suffix}.{extension}"
