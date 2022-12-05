def bug_catcher(func):

    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except ValueError as exc:
            return exc.args[0]
        except KeyError as exc:
            return f"Wrong information: {exc.args[0]}"
        except IndexError:
            return f"Not enough information for this command."
        except TypeError as exc:
            return exc.args[0]
        except FileExistsError as exc:
            return exc.args[0]
        except AttributeError as exc:
            return exc.args[0]

    return inner

# def bug_catcher(func):
#
#     def inner(*args, **kwargs):
#
#         result = func(*args, **kwargs)
#         return result
#
#
#     return inner
