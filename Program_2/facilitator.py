
class Facilitator:
    def __init__(self, name):
        self.name = name
        self.assignments = []

    def add_assignment(self, activity_name, time_slot):
        """Adds an assignment to the facilitator's schedule."""
        self.assignments.append((activity_name, time_slot))

    def clear_assignments(self):
        """Clears all assignments, used when starting a new generation."""
        self.assignments = []
