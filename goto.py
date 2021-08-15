import inspect

FILENAME = inspect.stack()[-1].filename
depth = 0
labels = {}


class GotoError(Exception):
    def __init__(self):
        self.message = "maximum goto depth exceeded"
        super().__init__(self.message)


def goto_(line):
    global depth
    caller = inspect.stack()[-1]
    with open(FILENAME, "r") as f:
        contents = "".join(f.readlines()[line - 1 :])
    depth += 1
    if depth > 1000:
        raise GotoError()
    exec(contents, caller.frame.f_globals)
    depth = 0
    exit()


class Label:
    def __getattr__(self, name: str):
        global labels
        caller = inspect.stack()[-1]
        labels[name] = caller.lineno
        return True


class Goto:
    def __getattr__(self, name: str):
        global labels
        try:
            goto_(labels[name] + 1)
        except KeyError:
            with open(FILENAME, "r") as f:
                for index, line in enumerate(f.readlines()):
                    if f'label .{name}' in line:
                        goto_(index+2)
            raise Exception('label not defined')       
                

label = Label()
goto = Goto()
