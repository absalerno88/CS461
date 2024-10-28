
import random
import json
from scipy.special import softmax

def select_random_room(rooms):
    """Randomly selects a room from a list of rooms for an activity assignment."""
    return random.choice(rooms)


def select_random_time_slot(time_slots):
    """Select a random time slot from the list of time slots."""
    return random.choice(time_slots)

def select_random_facilitator(facilitators):
    """Select a random facilitator from the list of facilitators."""
    return random.choice(facilitators)

def calculate_time_difference(time_slots, slot1, slot2):
    """Calculate the 'distance' between two time slots in terms of their index positions."""
    index1 = time_slots.index(slot1)
    index2 = time_slots.index(slot2)
    return abs(index1 - index2)

def normalize_fitness_scores(fitness_scores):
    """Apply softmax normalization to convert fitness scores to selection probabilities."""
    return softmax(fitness_scores)

def save_schedule_to_file(schedule, filename="best_schedule.json"):
    """Save the best schedule to a JSON file for easy inspection."""
    data = {
        "fitness_score": schedule.fitness_score,
        "assignments": {
            activity_name: {
                "room": assignment[0].name,
                "time_slot": assignment[1],
                "facilitator": assignment[2].name
            }
            for activity_name, assignment in schedule.assignment.items()
        }
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
