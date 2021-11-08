# test2

from __future__ import annotations
from typing import List, Union

# States
class State(object):
	__slots__ = ("finished", "c", "bool1", "bool2", "bool3", "gc", "clocked_location", "check_location", "finish_location")
	
	def copy_to(self, other: State):
		other.finished = self.finished
		other.c = self.c
		other.bool1 = self.bool1
		other.bool2 = self.bool2
		other.bool3 = self.bool3
		other.gc = self.gc
		other.clocked_location = self.clocked_location
		other.check_location = self.check_location
		other.finish_location = self.finish_location
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.finished == other.finished and self.c == other.c and self.bool1 == other.bool1 and self.bool2 == other.bool2 and self.bool3 == other.bool3 and self.gc == other.gc and self.clocked_location == other.clocked_location and self.check_location == other.check_location and self.finish_location == other.finish_location
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.finished)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.c)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.bool1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.bool2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.bool3)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.gc)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.clocked_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.check_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.finish_location)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "finished = " + str(self.finished)
		result += ", c = " + str(self.c)
		result += ", bool1 = " + str(self.bool1)
		result += ", bool2 = " + str(self.bool2)
		result += ", bool3 = " + str(self.bool3)
		result += ", gc = " + str(self.gc)
		result += ", clocked_location = " + str(self.clocked_location)
		result += ", check_location = " + str(self.check_location)
		result += ", finish_location = " + str(self.finish_location)
		result += ")"
		return result

# Transients
class Transient(object):
	__slots__ = ("R_Succ_Rate_edge_reward", "it", "time1", "time2", "time3")
	
	def copy_to(self, other: Transient):
		other.R_Succ_Rate_edge_reward = self.R_Succ_Rate_edge_reward
		other.it = self.it
		other.time1 = list(self.time1)
		other.time2 = list(self.time2)
		other.time3 = list(self.time3)
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.R_Succ_Rate_edge_reward == other.R_Succ_Rate_edge_reward and self.it == other.it and self.time1 == other.time1 and self.time2 == other.time2 and self.time3 == other.time3
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.R_Succ_Rate_edge_reward)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.it)) & 0xFFFFFFFF
		for x in self.time1:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.time2:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.time3:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "R_Succ_Rate_edge_reward = " + str(self.R_Succ_Rate_edge_reward)
		result += ", it = " + str(self.it)
		result += ", time1 = " + str(self.time1)
		result += ", time2 = " + str(self.time2)
		result += ", time3 = " + str(self.time3)
		result += ")"
		return result

# Automaton: clocked
class clockedAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 2]
		self.transition_labels = [[1, 9], [2, 9], [3, 9]]
		self.branch_counts = [[1, 1], [1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.clocked_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.clocked_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.clocked_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.clocked_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.clocked_location
		if location == 0:
			if transition == 0:
				return (state.gc == (self.network._get_transient_value(state, "time1"))[state.c])
			elif transition == 1:
				return (state.gc < (self.network._get_transient_value(state, "time1"))[state.c])
		elif location == 1:
			if transition == 0:
				return (state.gc == (self.network._get_transient_value(state, "time2"))[state.c])
			elif transition == 1:
				return (state.c <= (self.network._get_transient_value(state, "time1"))[state.c])
		elif location == 2:
			if transition == 0:
				return (state.gc == (self.network._get_transient_value(state, "time3"))[state.c])
			elif transition == 1:
				return (state.c <= (self.network._get_transient_value(state, "time1"))[state.c])
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.clocked_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.clocked_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 1:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 2:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.clocked_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.bool1 = True
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.bool2 = True
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.c = (state.c + 1)
						target_state.bool3 = True
		elif assignment_index == 2:
			location = state.clocked_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.clocked_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.clocked_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.clocked_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.clocked_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.clocked_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.clocked_location = 2

# Automaton: check
class checkAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 2]
		self.transition_labels = [[4, 9], [5, 9], [6, 9]]
		self.branch_counts = [[1, 1], [1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.check_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.check_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.check_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.check_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.check_location
		if location == 0:
			if transition == 0:
				return state.bool1
			elif transition == 1:
				return True
		elif location == 1:
			if transition == 0:
				return state.bool2
			elif transition == 1:
				return True
		elif location == 2:
			if transition == 0:
				return state.bool3
			elif transition == 1:
				return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.check_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.check_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 1:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 2:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.check_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.bool1 = False
						target_transient.it = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.bool2 = False
						target_transient.it = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.bool3 = False
						target_transient.it = 1
		elif assignment_index == 2:
			location = state.check_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.check_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.check_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.check_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.check_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.check_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.check_location = 2

# Automaton: finish
class finishAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 1]
		self.transition_labels = [[7, 9], [8, 9], [9]]
		self.branch_counts = [[1, 1], [1, 1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.finish_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.finish_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.finish_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.finish_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.finish_location
		if location == 0:
			if transition >= 0 and transition < 2:
				return True
		elif location == 1:
			if transition == 0:
				return ((state.gc == 90) and (state.c == 3))
			elif transition == 1:
				return (state.gc < 90)
		elif location == 2:
			return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.finish_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.finish_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 1:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 2:
			if transition == 0:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.finish_location
			if location == 1:
				if transition == 0:
					if branch == 0:
						target_state.finished = True
		elif assignment_index == 2:
			location = state.finish_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.finish_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.finish_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.finish_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.finish_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.finish_location = 2

# Automaton: GlobalSync
class GlobalSyncAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2]
		self.transition_labels = [[9, 10]]
		self.branch_counts = [[1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		pass
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = 0
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[0]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[0][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = 0
		if location == 0:
			if transition >= 0 and transition < 2:
				return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[0][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = 0
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = 0
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.gc = min((state.gc + 1), 91)
		elif assignment_index == 2:
			location = 0
			if location == 0:
				if transition == 0:
					if branch == 0:
						pass
				elif transition == 1:
					if branch == 0:
						target_transient.R_Succ_Rate_edge_reward = transient.it

class PropertyExpression(object):
	__slots__ = ("op", "args")
	
	def __init__(self, op: str, args: List[Union[int, PropertyExpression]]):
		self.op = op
		self.args = args
	
	def __str__(self):
		result = self.op + "("
		needComma = False
		for arg in self.args:
			if needComma:
				result += ", "
			else:
				needComma = True
			result += str(arg)
		return result + ")"

class Property(object):
	__slots__ = ("name", "exp")
	
	def __init__(self, name: str, exp: PropertyExpression):
		self.name = name
		self.exp = exp
	
	def __str__(self):
		return self.name + ": " + str(self.exp)

class Transition(object):
	__slots__ = ("label", "transitions")
	
	def __init__(self, label = 0, transitions = [-1, -1, -1, -1]):
		self.label = label
		self.transitions = transitions

class Branch(object):
	__slots__ = ("probability", "branches")
	
	def __init__(self, probability = 0.0, branches = [0, 0, 0, 0]):
		self.probability = probability
		self.branches = branches

class Network(object):
	__slots__ = ("network", "transition_labels", "sync_vectors", "properties", "aut_clocked", "aut_check", "aut_finish", "aut_GlobalSync")
	
	def __init__(self):
		self.network = self
		self.transition_labels = { 0: "τ", 1: "trans1", 2: "trans2", 3: "trans3", 4: "check1", 5: "check2", 6: "check3", 7: "a", 8: "b", 9: "tick", 10: "tau" }
		self.sync_vectors = [[0, -1, -1, -1, 0], [-1, 0, -1, -1, 0], [-1, -1, 0, -1, 0], [-1, -1, -1, 0, 0], [1, -1, -1, 10, 1], [2, -1, -1, 10, 2], [3, -1, -1, 10, 3], [-1, 4, -1, 10, 4], [-1, 5, -1, 10, 5], [-1, 6, -1, 10, 6], [-1, -1, 7, 10, 7], [-1, -1, 8, 10, 8], [9, 9, 9, 9, 9]]
		self.properties = [Property("R_Succ_Rate", PropertyExpression("xmin", [0, PropertyExpression("ap", [1])]))]
		self.aut_clocked = clockedAutomaton(self)
		self.aut_check = checkAutomaton(self)
		self.aut_finish = finishAutomaton(self)
		self.aut_GlobalSync = GlobalSyncAutomaton(self)
	
	def get_initial_state(self) -> State:
		state = State()
		state.finished = False
		state.c = 0
		state.bool1 = False
		state.bool2 = False
		state.bool3 = False
		state.gc = 0
		self.aut_clocked.set_initial_values(state)
		self.aut_check.set_initial_values(state)
		self.aut_finish.set_initial_values(state)
		self.aut_GlobalSync.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		transient.R_Succ_Rate_edge_reward = 0
		transient.it = 0
		transient.time1 = [10, 40, 70]
		transient.time2 = [20, 50, 80]
		transient.time3 = [30, 60, 90]
		self.aut_clocked.set_initial_transient_values(transient)
		self.aut_check.set_initial_transient_values(transient)
		self.aut_finish.set_initial_transient_values(transient)
		self.aut_GlobalSync.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return self.network._get_transient_value(state, "R_Succ_Rate_edge_reward")
		elif expression == 1:
			return state.finished
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return transient.R_Succ_Rate_edge_reward
		elif expression == 1:
			return state.finished
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		result = self.aut_clocked.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self.aut_check.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self.aut_finish.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self.aut_GlobalSync.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		if transient_variable == "R_Succ_Rate_edge_reward":
			return 0
		elif transient_variable == "it":
			return 0
		elif transient_variable == "time1":
			return [10, 40, 70]
		elif transient_variable == "time2":
			return [20, 50, 80]
		elif transient_variable == "time3":
			return [30, 60, 90]
		return None
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_clocked = [[], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_clocked.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_clocked.get_guard_value(state, i):
				trans_clocked[self.aut_clocked.get_transition_label(state, i)].append(i)
		trans_check = [[], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_check.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_check.get_guard_value(state, i):
				trans_check[self.aut_check.get_transition_label(state, i)].append(i)
		trans_finish = [[], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_finish.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_finish.get_guard_value(state, i):
				trans_finish[self.aut_finish.get_transition_label(state, i)].append(i)
		trans_GlobalSync = [[], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_GlobalSync.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_GlobalSync.get_guard_value(state, i):
				trans_GlobalSync[self.aut_GlobalSync.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for sv in self.sync_vectors:
			synced = [[-1, -1, -1, -1, -1]]
			# clocked
			if synced is not None:
				if sv[0] != -1:
					if len(trans_clocked[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_clocked[sv[0]][0]
						for i in range(1, len(trans_clocked[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_clocked[sv[0]][i]
			# check
			if synced is not None:
				if sv[1] != -1:
					if len(trans_check[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_check[sv[1]][0]
						for i in range(1, len(trans_check[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_check[sv[1]][i]
			# finish
			if synced is not None:
				if sv[2] != -1:
					if len(trans_finish[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_finish[sv[2]][0]
						for i in range(1, len(trans_finish[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_finish[sv[2]][i]
			# GlobalSync
			if synced is not None:
				if sv[3] != -1:
					if len(trans_GlobalSync[sv[3]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][3] = trans_GlobalSync[sv[3]][0]
						for i in range(1, len(trans_GlobalSync[sv[3]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][3] = trans_GlobalSync[sv[3]][i]
			if synced is not None:
				for sync in synced:
					sync[4] = sv[4]
				transitions.extend(filter(lambda s: s[-1] != -1, synced))
		# Convert to Transition instances
		for i in range(len(transitions)):
			transitions[i] = Transition(transitions[i][4], transitions[i])
			del transitions[i].transitions[4]
		# Done
		return transitions
	
	def get_branches(self, state: State, transition: Transition) -> List[Branch]:
		combs = [[-1, -1, -1, -1]]
		probs = [1.0]
		if transition.transitions[0] != -1:
			existing = len(combs)
			branch_count = self.aut_clocked.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self.aut_clocked.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self.aut_clocked.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		if transition.transitions[1] != -1:
			existing = len(combs)
			branch_count = self.aut_check.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self.aut_check.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self.aut_check.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self.aut_finish.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self.aut_finish.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self.aut_finish.get_probability_value(state, transition.transitions[2], 0)
			for i in range(existing):
				combs[i][2] = 0
				probs[i] *= probability
		if transition.transitions[3] != -1:
			existing = len(combs)
			branch_count = self.aut_GlobalSync.get_branch_count(state, transition.transitions[3])
			for i in range(1, branch_count):
				probability = self.aut_GlobalSync.get_probability_value(state, transition.transitions[3], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][3] = i
					probs.append(probs[j] * probability)
			probability = self.aut_GlobalSync.get_probability_value(state, transition.transitions[3], 0)
			for i in range(existing):
				combs[i][3] = 0
				probs[i] *= probability
		# Convert to Branch instances
		for i in range(len(combs)):
			combs[i] = Branch(probs[i], combs[i])
		# Done
		return list(filter(lambda b: b.probability > 0.0, combs))
	
	def jump(self, state: State, transition: Transition, branch: Branch, expressions: List[int] = []) -> State:
		transient = self._get_initial_transient()
		for i in range(0, 3):
			target_state = State()
			state.copy_to(target_state)
			target_transient = Transient()
			transient.copy_to(target_transient)
			if transition.transitions[0] != -1:
				self.aut_clocked.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self.aut_check.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self.aut_finish.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			if transition.transitions[3] != -1:
				self.aut_GlobalSync.jump(state, transient, transition.transitions[3], branch.branches[3], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
