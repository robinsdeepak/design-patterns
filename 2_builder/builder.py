class HTMLElement:
    intent_size = 2

    def __init__(self, name="", text=None):
        self.name = name
        self.text = text
        self.elements: list[HTMLElement] = []

    def __str__(self, indent=0):
        i1 = " " * indent * self.intent_size
        i2 = i1 + " " * self.intent_size

        lines = [f"{i1}<{self.name}>"]

        if self.text:
            lines.append(i2 + self.text)

        for e in self.elements:
            lines.append(e.__str__(indent + 1))

        lines.append(f"{i1}</{self.name}>")

        return "\n".join(lines)

    @staticmethod
    def create(name):
        return HTMLBuilder(name)


class HTMLBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.root = HTMLElement(root_name)

    def add_child(self, name="", text=""):
        self.root.elements.append(HTMLElement(name, text))
        return self


root = HTMLElement.create("ul")
root.add_child("li", "element 1").add_child("li", "element 2")
print(root.root)
