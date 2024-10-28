
import random
from utils import calculate_time_difference

class Schedule:
    def __init__(self, activities, rooms, facilitators, time_slots):
        self.activities = activities
        self.rooms = rooms
        self.facilitators = facilitators
        self.time_slots = time_slots
        self.assignment = self._generate_initial_assignment()
        self.fitness_score = 0  # Initial fitness score

    def _generate_initial_assignment(self):
        """Randomly assign each activity to a room, time, and facilitator."""
        assignment = {}
        for activity in self.activities:
            room = random.choice(self.rooms)
            time_slot = random.choice(self.time_slots)
            facilitator = random.choice(self.facilitators)
            assignment[activity.name] = (room, time_slot, facilitator)
        return assignment

    def calculate_fitness(self):
        """Calculate the fitness score based on assignment criteria."""
        # Reset fitness score for recalculations
        self.fitness_score = 0
        facilitator_load = {f.name: 0 for f in self.facilitators}
        room_time_allocations = {room.name: {} for room in self.rooms}

        for activity in self.activities:
            room, time_slot, facilitator = self.assignment[activity.name]
            activity_fitness = 0

            # Room size fitness adjustments
            if room.capacity < activity.expected_enrollment:
                activity_fitness -= 0.5
            elif room.capacity > 6 * activity.expected_enrollment:
                activity_fitness -= 0.4
            elif room.capacity > 3 * activity.expected_enrollment:
                activity_fitness -= 0.2
            else:
                activity_fitness += 0.3

            # Facilitator preference fitness adjustments
            if facilitator in activity.preferred_facilitators:
                activity_fitness += 0.5
            elif facilitator in activity.other_facilitators:
                activity_fitness += 0.2
            else:
                activity_fitness -= 0.1

            # Track facilitator load and check for overload penalties
            facilitator_load[facilitator.name] += 1
            if facilitator_load[facilitator.name] == 1:
                activity_fitness += 0.2
            elif facilitator_load[facilitator.name] > 1:
                activity_fitness -= 0.2

            # Room-time conflicts
            if time_slot in room_time_allocations[room.name]:
                activity_fitness -= 0.5
            else:
                room_time_allocations[room.name][time_slot] = activity.name

            # Add the individual activity fitness to total fitness
            self.fitness_score += activity_fitness

        # Facilitator load penalties after all activities
        for facilitator, count in facilitator_load.items():
            if count > 4:
                self.fitness_score -= 0.5
            elif count in [1, 2] and facilitator != "Dr. Tyler":
                self.fitness_score -= 0.4

        # Apply any additional SLA-specific fitness adjustments
        self._apply_activity_specific_adjustments()

        return self.fitness_score

    def _apply_activity_specific_adjustments(self):
        """Apply specific fitness rules for SLA 101 and SLA 191 activities directly on fitness score."""
        
        sla_101_times = []
        sla_191_times = []

        for activity in self.activities:
            room, time_slot, facilitator = self.assignment[activity.name]
            
            if activity.name in ["SLA101A", "SLA101B"]:
                sla_101_times.append(time_slot)
            elif activity.name in ["SLA191A", "SLA191B"]:
                sla_191_times.append(time_slot)

        # Rules for SLA 101
        if len(sla_101_times) == 2:
            time_diff_101 = calculate_time_difference(self.time_slots, sla_101_times[0], sla_101_times[1])
            if time_diff_101 >= 4:
                self.fitness_score += 0.5
            elif time_diff_101 == 0:
                self.fitness_score -= 0.5

        # Rules for SLA 191
        if len(sla_191_times) == 2:
            time_diff_191 = calculate_time_difference(self.time_slots, sla_191_times[0], sla_191_times[1])
            if time_diff_191 >= 4:
                self.fitness_score += 0.5
            elif time_diff_191 == 0:
                self.fitness_score -= 0.5

        # Rules for SLA 101 and SLA 191 consecutive time slots
        if len(sla_101_times) == 2 and len(sla_191_times) == 2:
            for t101 in sla_101_times:
                for t191 in sla_191_times:
                    time_diff = calculate_time_difference(self.time_slots, t101, t191)
                    if time_diff == 1:
                        self.fitness_score += 0.5
                    elif time_diff == 2:
                        self.fitness_score += 0.25
                    elif time_diff == 0:
                        self.fitness_score -= 0.25

    def mutate(self, mutation_rate=0.1):
        """Randomly mutate the schedule by changing room, time, or facilitator independently."""
        for activity_name in self.assignment:
            room, time_slot, facilitator = self.assignment[activity_name]

            # Independently mutate each component
            if random.random() < mutation_rate:
                room = random.choice(self.rooms)
            if random.random() < mutation_rate:
                time_slot = random.choice(self.time_slots)
            if random.random() < mutation_rate:
                facilitator = random.choice(self.facilitators)

            self.assignment[activity_name] = (room, time_slot, facilitator)

    @staticmethod
    def random_assignment(rooms, facilitators, time_slots):
        """Generates a random assignment for a room, time slot, and facilitator."""
        room = random.choice(rooms)
        time_slot = random.choice(time_slots)
        facilitator = random.choice(facilitators)
        return room, time_slot, facilitator