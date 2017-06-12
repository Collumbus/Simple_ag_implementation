import random

target = [1,1,1,1,1,1] # Goal to reach
gen_size = 6 # The length of the genetic material of each individual
pop = 10 # The number of individuals in the population
pressure = 3 # How many individuals are selected for reproduction. Necessarily greater than 2
mutation = 0.2 # The probability that an individual will mute

print("\n\nModel: %s\n"%(target)) # Show the model, with a little spacing

def individual(min, max):
    """
        Create an individual
    """
    return[random.randint(min, max) for i in range(gen_size)]

def createPopulation():
    """
        Creates a new population of individuals
    """
    return [individual(1,9) for i in range(pop)]

def calculateFitness(individual):
    """
        Calculate the fitness of a particular individual.
    """
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == target[i]:
            fitness += 1

    return fitness

def selection_and_reproduction(population):
    """
        Punctuate all the elements of the population and keep the best ones kept
         within 'selected'.
        Then mix the genetic material of the chosen ones to create new individuals
        and fill the population (also keeping a copy of the selected individuals
        without modifying).

        Finally, it mutates the individuals.

    """
    Scored = [ (calculateFitness(i), i) for i in population] # Calculates the fitness of each individual, and stores it in ordered pairs of the form (5, [1,2,1,1,4,1,8,9,4,1])
    Scored = [i[1] for i in sorted(Scored)] # Order the ordered pairs and stay only with the array of values
    population = Scored



    selected =  Scored[(len(Scored)-pressure):] # This line select the 'n' individuals at the end, where we are given by 'pressure'



    # The genetic material is mixed to create new individuals
    for i in range(len(population)-pressure):
        cut_point = random.randint(1,gen_size-1) # A point is chosen to make the exchange
        parents = random.sample(selected, 2) # Two parents are chosen

        population[i][:cut_point] = parents[0][:cut_point] # The genetic material of the parents is mixed in each new individual
        population[i][cut_point:] = parents[1][cut_point:]

    return population # The array 'population' now has a new population of individuals, which are returned

def mutation(population):
    """
        Individuals are randomly mutated. Without the mutation of new genes,
        the solution could never be reached.
    """
    for i in range(len(population)-pressure):
        if random.random() <= mutation: # Each individual of the population (minus the parents) has a probability of mutating
            cut_point = random.randint(0,gen_size-1) # A random cut point is chosen
            nuevo_valor = random.randint(1,9) #A nd a new value for this point

            # It is important to see that the new value is not the same as the old one
            while nuevo_valor == population[i][cut_point]:
                nuevo_valor = random.randint(1,9)

            # Mutation is applied
            population[i][cut_point] = nuevo_valor

    return population



population = createPopulation()# Initialize a population
print("Initial Population:\n%s"%(population)) # The initial population is shown

ger = 0

# Evolution of the population
for i in range(500):
    population = selection_and_reproduction(population)
    population = mutation(population)
    ger += 1
    print '\Generation: %i'% ger
    print("Population in generation\n%s"%(population))

print("\nFinal Population:\n%s"%(population)) # The evolved population is shown
print("\n\n")
