class Test:
    def __init__(self, name, model):
        self.name = name.upper()
        self.model = model.capitalize()

    def __str__(self):
        return f"{self.model} {self.name}"

    def testf(self):
        pass

T = Test("namer1", "modler2")
T.testf()
