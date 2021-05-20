#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from tortoisebot_flexbe_states.go_state import GoState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue May 18 2021
@author: Shubham Takbhagte
'''
class GotogoalSM(Behavior):
	'''
	Enter the coordinates
	'''


	def __init__(self):
		super(GotogoalSM, self).__init__()
		self.name = 'Gotogoal'

		# parameters of this behavior
		self.add_parameter('x_goal', 2)
		self.add_parameter('y_goal', 3)

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:275, x:130 y:275
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:306 y:67
			OperatableStateMachine.add('Go to goal',
										GoState(xgoal=self.x_goal, ygoal=self.y_goal),
										transitions={'done': 'second goal', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off})

			# x:30 y:97
			OperatableStateMachine.add('second goal',
										GoState(xgoal=4, ygoal=5),
										transitions={'done': 'finished', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
