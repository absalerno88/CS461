from genetic_algorithm import run_genetic_algorithm
from activity import Activity
from room import Room
from facilitator import Facilitator

# Full list of activities with expected enrollment, preferred, and other facilitators
activities = [
    Activity("SLA100A", 50, ["Glen", "Lock", "Banks", "Zeldin"], ["Numen", "Richards"]),
    Activity("SLA100B", 50, ["Glen", "Lock", "Banks", "Zeldin"], ["Numen", "Richards"]),
    Activity("SLA191A", 50, ["Glen", "Lock", "Banks", "Zeldin"], ["Numen", "Richards"]),
    Activity("SLA191B", 50, ["Glen", "Lock", "Banks", "Zeldin"], ["Numen", "Richards"]),
    Activity("SLA201", 50, ["Glen", "Banks", "Zeldin", "Shaw"], ["Numen", "Richards", "Singer"]),
    Activity("SLA291", 50, ["Lock", "Banks", "Zeldin", "Singer"], ["Numen", "Richards", "Shaw", "Tyler"]),
    Activity("SLA303", 60, ["Glen", "Zeldin", "Banks"], ["Numen", "Singer", "Shaw"]),
    Activity("SLA304", 25, ["Glen", "Banks", "Tyler"], ["Numen", "Singer", "Shaw", "Richards", "Uther", "Zeldin"]),
    Activity("SLA394", 20, ["Tyler", "Singer"], ["Richards", "Zeldin"]),
    Activity("SLA449", 60, ["Tyler", "Singer", "Shaw"], ["Zeldin", "Uther"]),
    Activity("SLA451", 100, ["Tyler", "Singer", "Shaw"], ["Zeldin", "Uther", "Richards", "Banks"]),
]

# Full list of rooms with capacities
rooms = [
    Room("Slater 003", 45),
    Room("Roman 216", 30),
    Room("Loft 206", 75),
    Room("Roman 201", 50),
    Room("Loft 310", 108),
    Room("Beach 201", 60),
    Room("Beach 301", 75),
    Room("Logos 325", 450),
    Room("Frank 119", 60),
]

# Full list of facilitators
facilitators = [
    Facilitator("Lock"),
    Facilitator("Glen"),
    Facilitator("Banks"),
    Facilitator("Richards"),
    Facilitator("Shaw"),
    Facilitator("Singer"),
    Facilitator("Uther"),
    Facilitator("Tyler"),
    Facilitator("Numen"),
    Facilitator("Zeldin"),
]

# Available time slots
time_slots = ["10 AM", "11 AM", "12 PM", "1 PM", "2 PM", "3 PM"]

# Run the genetic algorithm with the full set of data
best_schedule = run_genetic_algorithm(activities, rooms, facilitators, time_slots, generations=100, population_size=1000)

# Print the best schedule's fitness and assignments
print(f"Best schedule fitness: {best_schedule.fitness_score}")
print("Assignments:")
for activity_name, assignment in best_schedule.assignment.items():
    room, time_slot, facilitator = assignment
    print(f"{activity_name} -> Room: {room.name}, Time: {time_slot}, Facilitator: {facilitator.name}")
