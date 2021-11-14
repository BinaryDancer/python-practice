class System():
    def __init__(self, data: list[str]):
        self.name = data[0]
        self.req_names = []
        self.parts = []
        for el in data[1:]:
            if el == el.upper():
                self.req_names = list(el)
            else:
                self.parts = list(el)


class Template:
    TEMPLATE_PARTS = """
class {name}{req_systems}:
    def __init__(self):
        self.parts = set()
        super().__init__()
        self.parts.update([{parts}])

"""
    TEMPLATE_CONSTRUCT = """
class {name}{req_systems}:
    def __init__(self):
        self.req_elements = set({req_elements})
        self.parts = set()
        super().__init__()
        self.parts.update([{parts}])
        for el in self.req_elements:
            if el not in self.parts:
                raise "Can't construct"


{name}()
"""

    def __call__(self, system: System, needed=None):
        if not needed:
            return self.TEMPLATE_PARTS.format(
                name=system.name,
                req_systems="({})".format(", ".join(system.req_names)) if system.req_names else "",
                parts="'{}'".format("','".join(system.parts)) if system.parts else ""
            )
        return self.TEMPLATE_CONSTRUCT.format(
            name=system.name,
            req_systems="({})".format(", ".join(system.req_names)) if system.req_names else "",
            req_elements="['{}']".format("', '".join(needed)) if needed else "",
            parts="'{}'".format("', '".join(system.parts)) if system.parts else ""
        )


if __name__ == "__main__":
    b = B()
    s = input()
    systems = []
    while len(s.split()[0]) == 1:
        data = s.split()
        systems.append(System(data))
        s = input()
    data = ["PepelaC3"] + s.split()
    needed = data[-1]
    final_system = System(data[:-1])
    get_template = Template()
    template = ""
    for system in systems:
        template += get_template(system)

    template += get_template(final_system, needed)
    with open("prog_to_exec.py", "w") as f:
        print(template, file=f)

    try:
        exec(template)
    except Exception as ex:
        print("Incorrect")
    else:
        print("Correct")
