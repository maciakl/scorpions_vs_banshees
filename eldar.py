import random
import sys

TESTS = 1000

if(len(sys.argv) > 2):
	tests = int(sys.argv[2])

ELDAR_TOHIT = 4

BANSHEE_TOWOUND = 5
BANSHEE_ATTACKS = 2
MARINE_SAVE_AGAINST_BANSHEE = 7

SCORPION_TOWOUND = 4
SCORPION_ATTACKS = 3
MARINE_SAVE_AGAINST_SCORPION = 3

MARINE_TOHIT = 4
MARINE_TOWOUND = 3

BANSHEE_SAVE = 4
SCORPION_SAVE = 3


def roll(over):
	i = random.randint(1,6)
	return (i>=over)



def resolve_combat(eldar_tohit, eldar_towound, eldar_save, eldar_attacks, marine_tohit, marine_towound, marine_save):

	eldar_hits_scored = 0
	eldar_wounds_scored = 0
	eldar_saves = 0
	eldar_deaths = 0

	eldars_alive = 10

	marine_hits_scored = 0
	marine_wounds_scored = 0
	marine_saves = 0
	marine_deaths = 0

	marines_alive = 10


	# eldar roll to hit

	for i in range(eldars_alive*eldar_attacks):
		if(roll(eldar_tohit)): 
			eldar_hits_scored+=1
	 	 
	# eldar roll to wound

	for i in range(eldar_hits_scored):
		if(roll(eldar_towound)): 
			eldar_wounds_scored+=1

	# marines save

	for i in range(eldar_wounds_scored):
		if(not roll(marine_save)):
			marine_deaths+=1
			marines_alive-=1

	# marines strike back

	for i in range(marines_alive):
		if(roll(marine_tohit)):
			marine_hits_scored+=1

	# marines wound

	for i in range(marine_hits_scored):
		if(roll(marine_towound)):
			marine_wounds_scored+=1

	# eldar save

	for i in range(marine_wounds_scored):
		if(not roll(eldar_save)):
			eldar_deaths+=1
			eldars_alive+=1


	result = "\t" + str(eldar_hits_scored) + "\t" +str(eldar_wounds_scored)
	result += "\t" + str(marine_hits_scored) + "\t" + str(marine_wounds_scored)
	result += "\t" + str(marine_deaths) + "\t" + str(eldar_deaths)

	print result

	return eldar_deaths-marine_deaths
	

	

def print_head():
	head = "\t" + "eh" + "\t" + "ew"
	head += "\t" + "mh" + "\t" + "mw"
	head += "\t" + "dm" + "\t" + "de"

	print head


def print_summary(ties, eldar, marines):
	
	print "\n"
	print "ties\t\t\t\t\t\t\t\t" + str(ties)
	print "eldar\t\t\t\t\t\t\t\t" + str(eldar)
	print "marines\t\t\t\t\t\t\t\t" + str(marines)


def print_results(what):
	
	print_head()

	marine_wins = 0
	eldar_wins = 0
	ties = 0

	if(what=="ban"):
		eldar_towound = BANSHEE_TOWOUND
		eldar_save = BANSHEE_SAVE
		marine_save = MARINE_SAVE_AGAINST_BANSHEE
		eldar_attacks = BANSHEE_ATTACKS

	if(what=="scor"):
		eldar_towound = SCORPION_TOWOUND
		eldar_save = SCORPION_SAVE
		marine_save = MARINE_SAVE_AGAINST_SCORPION
		eldar_attacks = SCORPION_ATTACKS

	for i in range(tests):
		random.seed()
		r = resolve_combat(ELDAR_TOHIT, eldar_towound, eldar_save, eldar_attacks, MARINE_TOHIT, MARINE_TOWOUND, marine_save)

		if(r == 0): 
			ties+=1
		elif(r<0):
			eldar_wins+=1
		else:
			marine_wins+=1

	print_summary(ties, eldar_wins, marine_wins)



what = "ban"

if(len(sys.argv) > 1):
	what = sys.argv[1]
	print_results(what)





	
