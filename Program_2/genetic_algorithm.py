
import random
from schedule import Schedule
from utils import normalize_fitness_scores, save_schedule_to_file

def initialize_population(activities, rooms, facilitators, time_slots, population_size=500):
    """Creates an initial population of random schedules."""
    population = []
    for _ in range(population_size):
        schedule = Schedule(activities, rooms, facilitators, time_slots)
        schedule.calculate_fitness()
        population.append(schedule)
    return population

def select_parents(population, fitness_probs, tournament_size=5):
    tournament = random.sample(population, tournament_size)
    parent1 = max(tournament, key=lambda s: s.fitness_score)
    tournament = random.sample(population, tournament_size)
    parent2 = max(tournament, key=lambda s: s.fitness_score)
    return parent1, parent2


def crossover(parent1, parent2):
    offspring = Schedule(parent1.activities, parent1.rooms, parent1.facilitators, parent1.time_slots)
    offspring.assignment = {}
    
    for activity_name in parent1.assignment:
        if random.random() < 0.1:
            # Pass the necessary arguments to `random_assignment`
            offspring.assignment[activity_name] = Schedule.random_assignment(
                parent1.rooms, parent1.facilitators, parent1.time_slots
            )
        else:
            if random.random() < 0.5:
                offspring.assignment[activity_name] = parent1.assignment[activity_name]
            else:
                offspring.assignment[activity_name] = parent2.assignment[activity_name]

    offspring.calculate_fitness()
    return offspring

def mutate_population(population, mutation_rate=0.1):
    """Applies mutation to the entire population based on the mutation rate."""
    for schedule in population:
        if schedule.fitness_score < 1.0:  # Apply higher mutation for low fitness
            schedule.mutate(mutation_rate * 1.5)
        else:
            schedule.mutate(mutation_rate)

def write_best_schedule_to_file(best_schedule, file_path="output_schedule.txt"):
    """Writes the best schedule's fitness and assignments to an output file."""
    with open(file_path, "w") as file:
        file.write(f"Best schedule fitness: {best_schedule.fitness_score}\n")
        file.write("Assignments:\n")
        for activity_name, assignment in best_schedule.assignment.items():
            room, time_slot, facilitator = assignment
            file.write(f"{activity_name} -> Room: {room.name}, Time: {time_slot}, Facilitator: {facilitator.name}\n")


def run_genetic_algorithm(activities, rooms, facilitators, time_slots, generations=50, population_size=100, mutation_rate=0.1):
    """Main loop for running the genetic algorithm, creating two offspring per pairing."""

    population = initialize_population(activities, rooms, facilitators, time_slots, population_size)
    best_schedule = None

    for generation in range(generations):
        # Calculate fitness for each schedule and normalize probabilities
        fitness_scores = [schedule.fitness_score for schedule in population]
        fitness_probs = normalize_fitness_scores(fitness_scores)

        # Create the next generation as a new, separate pool
        next_generation = []
        while len(next_generation) < population_size:
            parent1, parent2 = select_parents(population, fitness_probs)
            
            # Produce two offspring per pairing
            offspring1 = crossover(parent1, parent2)
            offspring2 = crossover(parent1, parent2)
            
            # Mutate both offspring
            offspring1.mutate(mutation_rate)
            offspring2.mutate(mutation_rate)
            
            # Add offspring to the next generation pool
            next_generation.extend([offspring1, offspring2])

        # Reinitialize a small portion of the population every 10 generations for diversity
        if generation % 10 == 0:
            for i in range(int(0.1 * len(next_generation))):  # 10% of the population
                next_generation[i] = Schedule(activities, rooms, facilitators, time_slots)
                next_generation[i].calculate_fitness()

        # Elitism: Keep the top 5% of the population
        num_elites = int(0.03 * population_size)
        elites = sorted(population, key=lambda s: s.fitness_score, reverse=True)[:num_elites]
        next_generation = elites + next_generation[:population_size - num_elites]

        # Mutate the entire next generation after it's built
        mutate_population(next_generation, mutation_rate)

        # Trim next generation to the population size if it exceeds
        population = next_generation[:population_size]
        
        # Track the best schedule so far
        best_schedule = max(population, key=lambda s: s.fitness_score)
        print(f"Generation {generation + 1}: Best Fitness = {best_schedule.fitness_score}")

        # Adjust mutation rate adaptively
        mutation_rate = max(0.1, mutation_rate * 0.98)

    write_best_schedule_to_file(best_schedule)
    return best_schedule
