from abc import abstractmethod


# without ISP
class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        print("Printing document: " + str(document))

    def fax(self, document):
        print("Faxing document: " + str(document))

    def scan(self, document):
        print("Scanning document: " + str(document))


print("Using MultiFunctionPrinter")
printer = MultiFunctionPrinter()
printer.print("Document")
printer.fax("Document")
printer.scan("Document")
print()


class OldFashionedPrinter(Machine):
    def print(self, document):
        print("Printing document: " + str(document))

    def fax(self, document):
        """
        Not Supported!
        """
        raise NotImplementedError

    def scan(self, document):
        """
        Not Supported!
        """
        raise NotImplementedError


print("Using OldFashionedPrinter")
printer = OldFashionedPrinter()
printer.print("Document")
# printer.fax("Document")
# printer.scan("Document")
print()
# with ISP


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print("Printing document: " + str(document))


print("Using MyPrinter")
printer = MyPrinter()
printer.print("Document")
print()


class MyScanner(Scanner):
    def scan(self, document):
        print("Scanning document: " + str(document))


print("Using MyScanner")
scanner = MyScanner()
scanner.scan("Document")
print()


class PhotoCopier(Printer, Scanner):
    def print(self, document):
        print("Printing document: " + str(document))

    def scan(self, document):
        print("Scanning document: " + str(document))


print("Using PhotoCopier")
printer = PhotoCopier()
printer.print("Document")
printer.scan("Document")
print()


class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionPrinter(MultiFunctionDevice):
    def __init__(self, printer, scanner) -> None:
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        print("Printing document: " + str(document))

    def scan(self, document):
        print("Scanning document: " + str(document))


print("Using MultiFunctionPrinter")
printer = MultiFunctionPrinter(MyPrinter(), MyScanner())
printer.print("Document")
printer.scan("Document")
print()
