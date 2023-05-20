# Single Responsiblity Principle
# Separtion of Concerns
import os


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, entry):
        self.count += 1
        self.entries.append(f"{self.count}: {entry}")

    def remove_entry(self, position):
        self.count -= 1
        self.entries.pop(position)

    def __str__(self) -> str:
        return "\n".join(self.entries)


class PersistentManager:
    @staticmethod
    def save_journal_to_file(journal, filename):
        with open(filename, "w") as f:
            f.write(str(journal))

    @staticmethod
    def load(filename):
        with open(filename, "r") as f:
            journal = Journal()
            journal.entries = f.read().splitlines()
            return journal


print("creating journal...")
j = Journal()
print("adding entries...")
j.add_entry("First entry")
j.add_entry("Second entry")
print(f"Journal entries:\n{j}")

print()
print("Saving to file...")
filename = os.path.join(os.path.dirname(__file__), "journal.txt")
PersistentManager.save_journal_to_file(j, filename)
print("Done.")
print("Loading from file...")
j2 = PersistentManager.load(filename)
print(f"Journal entries:\n{j2}")
