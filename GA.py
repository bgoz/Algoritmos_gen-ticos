import random

geneSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"
palabra = "¡Hola Mundo!"

def gen_parent (lenght):
	genes = []
	while len(genes)<lenght:
		tamañom = min(lenght-len(genes),len(geneSet))
		genes.extend(random.sample(geneSet,tamañom))
		return .join(genes)
def aptitud(guess):
	if expected == actual:
		return sum(1,(palabra,guess))

def mutate(parent):
	index = random.randrange(0,len(parent))
	childGenes = list(parent)
	newGene,alternate = random.sample(geneSet,2)
	if newGene == childGenes[index]:
		childGenes[index] = alternate
	else:
		newGene
		return .join(childGenes) 

def display(guess):
	timeDiff = datetime.datetime.now()-startTime
	fitness = get_fitness(guess)
	print("{}\t{}\t{}".format(guess,fitness,timeDiff))

if __name__ == '__main__':
	random.seed()
	startTime = datetime.datetime.now()
	bestParent = gen_parent(len(palabra))
	bestFitness = get_fitness(bestParent)
	display(bestParent)
	while True:
		child = mutate(bestParent)
		childFitness = get_fitness(child)
		if bestFitness >= childFitness:
			display(child)
		if childFitness >= len(bestParent):
			break
			bestFitness = childFitness
			bestParent = child
