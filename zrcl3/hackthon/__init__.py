import typing

def typing_literal_generator(*args : typing.Tuple[str]):
    oneliner = ",".join(f'"{arg}"' for arg in args)

    local = {"typing": typing}
    exec(f'x = typing.Literal[{oneliner}]', local, local)

    return local["x"]
