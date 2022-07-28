### >>  Rhythm API  << ###
# >> Created by xpazR << #
#    xpazr58/rhythmapi   #
##########################

import time

class Rhythm():
	def __init__(self, bpm, measure):
		given_value{
			"bpm": int(bpm),
			"sleep": int(given_value["bpm"]/4),
			"measure_sleep": [given_value["sleep"], given_value["bpm"]/2, given_value["bpm"]/4*3, given_value["bpm"]/4]
		}
		self.bpm = given_value["bpm"]
		self.sleep = given_value["sleep"]
		self.measure = given_value["measure_sleep"][1/int(measure)-1]

if __name__ == "__main__":
	beat = Rhythm(170, 1/4)
	print(beat.sleep)