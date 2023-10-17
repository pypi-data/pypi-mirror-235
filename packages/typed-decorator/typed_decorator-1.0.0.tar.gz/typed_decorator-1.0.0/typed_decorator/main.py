def typed(types_: list):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                with_type = False
                for type_ in types_:
                    if isinstance(arg, type_):
                        with_type = True
                if not with_type:
                    raise TypeError("Error")
            return func(*args)
        return wrapper
    return decorator
