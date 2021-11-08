# test

from __future__ import annotations
from typing import List, Union

# States
class State(object):
	__slots__ = ("gc", "finished", "failure", "soc", "load", "c", "nee", "preheat", "available", "not_available", "pa", "a", "sun_c", "heating", "slewing", "insolation", "ac_lock", "bUpdate", "new_time", "old_time", "JobProvider_location_2", "JobProvider_location_3", "Job_location_2", "temptime", "Job_location_3", "temptime_1", "Terminate_location_1", "Battery_location_1", "Sun_location_1")
	
	def copy_to(self, other: State):
		other.gc = self.gc
		other.finished = self.finished
		other.failure = self.failure
		other.soc = self.soc
		other.load = self.load
		other.c = list(self.c)
		other.nee = list(self.nee)
		other.preheat = list(self.preheat)
		other.available = list(self.available)
		other.not_available = list(self.not_available)
		other.pa = list(self.pa)
		other.a = self.a
		other.sun_c = self.sun_c
		other.heating = self.heating
		other.slewing = self.slewing
		other.insolation = self.insolation
		other.ac_lock = self.ac_lock
		other.bUpdate = self.bUpdate
		other.new_time = self.new_time
		other.old_time = self.old_time
		other.JobProvider_location_2 = self.JobProvider_location_2
		other.JobProvider_location_3 = self.JobProvider_location_3
		other.Job_location_2 = self.Job_location_2
		other.temptime = self.temptime
		other.Job_location_3 = self.Job_location_3
		other.temptime_1 = self.temptime_1
		other.Terminate_location_1 = self.Terminate_location_1
		other.Battery_location_1 = self.Battery_location_1
		other.Sun_location_1 = self.Sun_location_1
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.gc == other.gc and self.finished == other.finished and self.failure == other.failure and self.soc == other.soc and self.load == other.load and self.c == other.c and self.nee == other.nee and self.preheat == other.preheat and self.available == other.available and self.not_available == other.not_available and self.pa == other.pa and self.a == other.a and self.sun_c == other.sun_c and self.heating == other.heating and self.slewing == other.slewing and self.insolation == other.insolation and self.ac_lock == other.ac_lock and self.bUpdate == other.bUpdate and self.new_time == other.new_time and self.old_time == other.old_time and self.JobProvider_location_2 == other.JobProvider_location_2 and self.JobProvider_location_3 == other.JobProvider_location_3 and self.Job_location_2 == other.Job_location_2 and self.temptime == other.temptime and self.Job_location_3 == other.Job_location_3 and self.temptime_1 == other.temptime_1 and self.Terminate_location_1 == other.Terminate_location_1 and self.Battery_location_1 == other.Battery_location_1 and self.Sun_location_1 == other.Sun_location_1
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.gc)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.finished)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.failure)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.soc)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.load)) & 0xFFFFFFFF
		for x in self.c:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.nee:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.preheat:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.available:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.not_available:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.pa:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.a)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.sun_c)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.heating)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.slewing)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.insolation)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.ac_lock)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.bUpdate)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.new_time)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.old_time)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.JobProvider_location_2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.JobProvider_location_3)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Job_location_2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.temptime)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Job_location_3)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.temptime_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Terminate_location_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Battery_location_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Sun_location_1)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "gc = " + str(self.gc)
		result += ", finished = " + str(self.finished)
		result += ", failure = " + str(self.failure)
		result += ", soc = " + str(self.soc)
		result += ", load = " + str(self.load)
		result += ", c = " + str(self.c)
		result += ", nee = " + str(self.nee)
		result += ", preheat = " + str(self.preheat)
		result += ", available = " + str(self.available)
		result += ", not_available = " + str(self.not_available)
		result += ", pa = " + str(self.pa)
		result += ", a = " + str(self.a)
		result += ", sun_c = " + str(self.sun_c)
		result += ", heating = " + str(self.heating)
		result += ", slewing = " + str(self.slewing)
		result += ", insolation = " + str(self.insolation)
		result += ", ac_lock = " + str(self.ac_lock)
		result += ", bUpdate = " + str(self.bUpdate)
		result += ", new_time = " + str(self.new_time)
		result += ", old_time = " + str(self.old_time)
		result += ", JobProvider_location_2 = " + str(self.JobProvider_location_2)
		result += ", JobProvider_location_3 = " + str(self.JobProvider_location_3)
		result += ", Job_location_2 = " + str(self.Job_location_2)
		result += ", temptime = " + str(self.temptime)
		result += ", Job_location_3 = " + str(self.Job_location_3)
		result += ", temptime_1 = " + str(self.temptime_1)
		result += ", Terminate_location_1 = " + str(self.Terminate_location_1)
		result += ", Battery_location_1 = " + str(self.Battery_location_1)
		result += ", Sun_location_1 = " + str(self.Sun_location_1)
		result += ")"
		return result

# Transients
class Transient(object):
	__slots__ = ("R_Succ_Rate_edge_reward", "cost", "sun_start", "sun_stop", "gom_start", "gom_stop", "kourou_start", "kourou_stop", "toulouse_start", "toulouse_stop", "ftwo_start", "ftwo_stop", "fthree_start", "fthree_stop", "cost_rate", "a_nfe", "power_g", "power_p", "JobProvider_location", "JobProvider_location_1", "Job_location", "Job_location_1", "Terminate_location", "Battery_location", "Sun_location")
	
	def copy_to(self, other: Transient):
		other.R_Succ_Rate_edge_reward = self.R_Succ_Rate_edge_reward
		other.cost = self.cost
		other.sun_start = list(self.sun_start)
		other.sun_stop = list(self.sun_stop)
		other.gom_start = list(self.gom_start)
		other.gom_stop = list(self.gom_stop)
		other.kourou_start = list(self.kourou_start)
		other.kourou_stop = list(self.kourou_stop)
		other.toulouse_start = list(self.toulouse_start)
		other.toulouse_stop = list(self.toulouse_stop)
		other.ftwo_start = list(self.ftwo_start)
		other.ftwo_stop = list(self.ftwo_stop)
		other.fthree_start = list(self.fthree_start)
		other.fthree_stop = list(self.fthree_stop)
		other.cost_rate = list(self.cost_rate)
		other.a_nfe = list(self.a_nfe)
		other.power_g = list(self.power_g)
		other.power_p = list(self.power_p)
		other.JobProvider_location = self.JobProvider_location
		other.JobProvider_location_1 = self.JobProvider_location_1
		other.Job_location = self.Job_location
		other.Job_location_1 = self.Job_location_1
		other.Terminate_location = self.Terminate_location
		other.Battery_location = self.Battery_location
		other.Sun_location = self.Sun_location
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.R_Succ_Rate_edge_reward == other.R_Succ_Rate_edge_reward and self.cost == other.cost and self.sun_start == other.sun_start and self.sun_stop == other.sun_stop and self.gom_start == other.gom_start and self.gom_stop == other.gom_stop and self.kourou_start == other.kourou_start and self.kourou_stop == other.kourou_stop and self.toulouse_start == other.toulouse_start and self.toulouse_stop == other.toulouse_stop and self.ftwo_start == other.ftwo_start and self.ftwo_stop == other.ftwo_stop and self.fthree_start == other.fthree_start and self.fthree_stop == other.fthree_stop and self.cost_rate == other.cost_rate and self.a_nfe == other.a_nfe and self.power_g == other.power_g and self.power_p == other.power_p and self.JobProvider_location == other.JobProvider_location and self.JobProvider_location_1 == other.JobProvider_location_1 and self.Job_location == other.Job_location and self.Job_location_1 == other.Job_location_1 and self.Terminate_location == other.Terminate_location and self.Battery_location == other.Battery_location and self.Sun_location == other.Sun_location
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.R_Succ_Rate_edge_reward)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.cost)) & 0xFFFFFFFF
		for x in self.sun_start:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.sun_stop:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.gom_start:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.gom_stop:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.kourou_start:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.kourou_stop:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.toulouse_start:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.toulouse_stop:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.ftwo_start:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.ftwo_stop:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.fthree_start:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.fthree_stop:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.cost_rate:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.a_nfe:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.power_g:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.power_p:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.JobProvider_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.JobProvider_location_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Job_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Job_location_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Terminate_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Battery_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Sun_location)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "R_Succ_Rate_edge_reward = " + str(self.R_Succ_Rate_edge_reward)
		result += ", cost = " + str(self.cost)
		result += ", sun_start = " + str(self.sun_start)
		result += ", sun_stop = " + str(self.sun_stop)
		result += ", gom_start = " + str(self.gom_start)
		result += ", gom_stop = " + str(self.gom_stop)
		result += ", kourou_start = " + str(self.kourou_start)
		result += ", kourou_stop = " + str(self.kourou_stop)
		result += ", toulouse_start = " + str(self.toulouse_start)
		result += ", toulouse_stop = " + str(self.toulouse_stop)
		result += ", ftwo_start = " + str(self.ftwo_start)
		result += ", ftwo_stop = " + str(self.ftwo_stop)
		result += ", fthree_start = " + str(self.fthree_start)
		result += ", fthree_stop = " + str(self.fthree_stop)
		result += ", cost_rate = " + str(self.cost_rate)
		result += ", a_nfe = " + str(self.a_nfe)
		result += ", power_g = " + str(self.power_g)
		result += ", power_p = " + str(self.power_p)
		result += ", JobProvider_location = " + str(self.JobProvider_location)
		result += ", JobProvider_location_1 = " + str(self.JobProvider_location_1)
		result += ", Job_location = " + str(self.Job_location)
		result += ", Job_location_1 = " + str(self.Job_location_1)
		result += ", Terminate_location = " + str(self.Terminate_location)
		result += ", Battery_location = " + str(self.Battery_location)
		result += ", Sun_location = " + str(self.Sun_location)
		result += ")"
		return result

# Automaton: JobProvider
class JobProviderAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 2, 2]
		self.transition_labels = [[1, 61], [2, 61], [3, 61], [1, 61]]
		self.branch_counts = [[1, 1], [1, 1], [1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.JobProvider_location_2 = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.JobProvider_location_2
		if location == 0:
			if transient_variable == "JobProvider_location":
				return 0
		elif location == 1:
			if transient_variable == "JobProvider_location":
				return 1
		elif location == 2:
			if transient_variable == "JobProvider_location":
				return 2
		elif location == 3:
			if transient_variable == "JobProvider_location":
				return 3
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.JobProvider_location_2]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.JobProvider_location_2][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.JobProvider_location_2
		if location == 0:
			if transition == 0:
				return (state.gc == ((self.network._get_transient_value(state, "ftwo_start"))[(state.c)[3]] - 1200))
			elif transition == 1:
				return (state.gc < ((self.network._get_transient_value(state, "ftwo_start"))[(state.c)[3]] - 1200))
		elif location == 1:
			if transition == 0:
				return (state.gc == (self.network._get_transient_value(state, "ftwo_start"))[(state.c)[3]])
			elif transition == 1:
				return (state.gc < (self.network._get_transient_value(state, "ftwo_start"))[(state.c)[3]])
		elif location == 2:
			if transition == 0:
				return (state.gc == (self.network._get_transient_value(state, "ftwo_stop"))[(state.c)[3]])
			elif transition == 1:
				return (state.gc < (self.network._get_transient_value(state, "ftwo_stop"))[(state.c)[3]])
		elif location == 3:
			if transition == 0:
				return (state.gc == ((self.network._get_transient_value(state, "ftwo_start"))[(state.c)[3]] - 1200))
			elif transition == 1:
				return (state.gc < ((self.network._get_transient_value(state, "ftwo_start"))[(state.c)[3]] - 1200))
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.JobProvider_location_2][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.JobProvider_location_2
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
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.JobProvider_location_2
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.heating = True
						target_state.preheat[3] = True
						target_state.new_time = ((transient.ftwo_start)[(state.c)[3]] - 1200)
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.heating = False
						target_state.available[3] = True
						target_state.new_time = (transient.ftwo_start)[(state.c)[3]]
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.not_available[3] = True
						target_state.new_time = (transient.ftwo_stop)[(state.c)[3]]
						target_state.c[3] = ((state.c)[3] + 1)
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.heating = True
						target_state.preheat[3] = True
						target_state.new_time = ((transient.ftwo_start)[(state.c)[3]] - 1200)
		elif assignment_index == 1:
			location = state.JobProvider_location_2
			if location == 0:
				if transition == 1:
					if branch == 0:
						target_transient.JobProvider_location = 0
			elif location == 1:
				if transition == 1:
					if branch == 0:
						target_transient.JobProvider_location = 1
			elif location == 2:
				if transition == 1:
					if branch == 0:
						target_transient.JobProvider_location = 2
			elif location == 3:
				if transition == 1:
					if branch == 0:
						target_transient.JobProvider_location = 3
		elif assignment_index == 3:
			location = state.JobProvider_location_2
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.JobProvider_location_2 = 1
				elif transition == 1:
					if branch == 0:
						target_state.JobProvider_location_2 = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.JobProvider_location_2 = 2
				elif transition == 1:
					if branch == 0:
						target_state.JobProvider_location_2 = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.JobProvider_location_2 = 3
				elif transition == 1:
					if branch == 0:
						target_state.JobProvider_location_2 = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.JobProvider_location_2 = 1
				elif transition == 1:
					if branch == 0:
						target_state.JobProvider_location_2 = 3

# Automaton: JobProvider
class JobProviderAutomaton_1(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 2, 2]
		self.transition_labels = [[1, 61], [2, 61], [3, 61], [1, 61]]
		self.branch_counts = [[1, 1], [1, 1], [1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.JobProvider_location_3 = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.JobProvider_location_3
		if location == 0:
			if transient_variable == "JobProvider_location_1":
				return 0
		elif location == 1:
			if transient_variable == "JobProvider_location_1":
				return 1
		elif location == 2:
			if transient_variable == "JobProvider_location_1":
				return 2
		elif location == 3:
			if transient_variable == "JobProvider_location_1":
				return 3
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.JobProvider_location_3]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.JobProvider_location_3][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.JobProvider_location_3
		if location == 0:
			if transition == 0:
				return (state.gc == ((self.network._get_transient_value(state, "fthree_start"))[(state.c)[4]] - 1200))
			elif transition == 1:
				return (state.gc < ((self.network._get_transient_value(state, "fthree_start"))[(state.c)[4]] - 1200))
		elif location == 1:
			if transition == 0:
				return (state.gc == (self.network._get_transient_value(state, "fthree_start"))[(state.c)[4]])
			elif transition == 1:
				return (state.gc < (self.network._get_transient_value(state, "fthree_start"))[(state.c)[4]])
		elif location == 2:
			if transition == 0:
				return (state.gc == (self.network._get_transient_value(state, "fthree_stop"))[(state.c)[4]])
			elif transition == 1:
				return (state.gc < (self.network._get_transient_value(state, "fthree_stop"))[(state.c)[4]])
		elif location == 3:
			if transition == 0:
				return (state.gc == ((self.network._get_transient_value(state, "fthree_start"))[(state.c)[4]] - 1200))
			elif transition == 1:
				return (state.gc < ((self.network._get_transient_value(state, "fthree_start"))[(state.c)[4]] - 1200))
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.JobProvider_location_3][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.JobProvider_location_3
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
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.JobProvider_location_3
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.heating = True
						target_state.preheat[4] = True
						target_state.new_time = ((transient.fthree_start)[(state.c)[4]] - 1200)
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.heating = False
						target_state.available[4] = True
						target_state.new_time = (transient.fthree_start)[(state.c)[4]]
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.not_available[4] = True
						target_state.new_time = (transient.fthree_stop)[(state.c)[4]]
						target_state.c[4] = ((state.c)[4] + 1)
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.heating = True
						target_state.preheat[4] = True
						target_state.new_time = ((transient.fthree_start)[(state.c)[4]] - 1200)
		elif assignment_index == 1:
			location = state.JobProvider_location_3
			if location == 0:
				if transition == 1:
					if branch == 0:
						target_transient.JobProvider_location_1 = 0
			elif location == 1:
				if transition == 1:
					if branch == 0:
						target_transient.JobProvider_location_1 = 1
			elif location == 2:
				if transition == 1:
					if branch == 0:
						target_transient.JobProvider_location_1 = 2
			elif location == 3:
				if transition == 1:
					if branch == 0:
						target_transient.JobProvider_location_1 = 3
		elif assignment_index == 3:
			location = state.JobProvider_location_3
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.JobProvider_location_3 = 1
				elif transition == 1:
					if branch == 0:
						target_state.JobProvider_location_3 = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.JobProvider_location_3 = 2
				elif transition == 1:
					if branch == 0:
						target_state.JobProvider_location_3 = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.JobProvider_location_3 = 3
				elif transition == 1:
					if branch == 0:
						target_state.JobProvider_location_3 = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.JobProvider_location_3 = 1
				elif transition == 1:
					if branch == 0:
						target_state.JobProvider_location_3 = 3

# Automaton: Job
class JobAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [3, 3, 2, 2, 2, 2, 3, 2, 2, 2, 3, 2, 2, 2, 2, 2]
		self.transition_labels = [[4, 5, 61], [6, 7, 61], [8, 61], [9, 61], [10, 61], [11, 61], [12, 13, 61], [14, 61], [15, 61], [14, 61], [4, 5, 61], [16, 61], [17, 61], [14, 61], [18, 61], [14, 61]]
		self.branch_counts = [[1, 1, 1], [1, 1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1, 1], [1, 1], [1, 1], [1, 1], [1, 1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Job_location_2 = 0
		state.temptime = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Job_location_2
		if location == 0:
			if transient_variable == "Job_location":
				return 0
		elif location == 1:
			if transient_variable == "Job_location":
				return 1
		elif location == 2:
			if transient_variable == "Job_location":
				return 2
		elif location == 3:
			if transient_variable == "Job_location":
				return 3
		elif location == 4:
			if transient_variable == "Job_location":
				return 4
		elif location == 5:
			if transient_variable == "Job_location":
				return 5
		elif location == 6:
			if transient_variable == "Job_location":
				return 6
		elif location == 7:
			if transient_variable == "Job_location":
				return 7
		elif location == 8:
			if transient_variable == "Job_location":
				return 8
		elif location == 9:
			if transient_variable == "Job_location":
				return 9
		elif location == 10:
			if transient_variable == "Job_location":
				return 10
		elif location == 11:
			if transient_variable == "Job_location":
				return 11
		elif location == 12:
			if transient_variable == "Job_location":
				return 12
		elif location == 13:
			if transient_variable == "Job_location":
				return 13
		elif location == 14:
			if transient_variable == "Job_location":
				return 14
		elif location == 15:
			if transient_variable == "Job_location":
				return 15
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Job_location_2]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Job_location_2][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Job_location_2
		if location == 0:
			if transition >= 0 and transition < 2:
				return (state.preheat)[3]
			elif transition == 2:
				return ((not (state.preheat)[3]) and (((state.soc >= 90000000) and (not state.ac_lock)) or ((self.network._get_transient_value(state, "cost_rate"))[3] != -1)))
		elif location == 1:
			if transition == 0:
				return (((self.network._get_transient_value(state, "a_nfe"))[3] != 0) and (state.a != (self.network._get_transient_value(state, "a_nfe"))[3]))
			elif transition == 1:
				return (((self.network._get_transient_value(state, "a_nfe"))[3] == 0) or (state.a == (self.network._get_transient_value(state, "a_nfe"))[3]))
			elif transition == 2:
				return True
		elif location == 2:
			if transition == 0:
				return (state.available)[3]
			elif transition == 1:
				return True
		elif location == 3:
			if transition >= 0 and transition < 2:
				return True
		elif location == 4:
			if transition == 0:
				return (state.not_available)[3]
			elif transition == 1:
				return True
		elif location == 5:
			if transition >= 0 and transition < 2:
				return True
		elif location == 6:
			if transition == 0:
				return (((self.network._get_transient_value(state, "a_nfe"))[3] == 0) or (state.a == 1))
			elif transition == 1:
				return (((self.network._get_transient_value(state, "a_nfe"))[3] != 0) and (state.a != 1))
			elif transition == 2:
				return True
		elif location == 7:
			if transition >= 0 and transition < 2:
				return True
		elif location == 8:
			if transition == 0:
				return (state.gc == state.temptime)
			elif transition == 1:
				return True
		elif location == 9:
			if transition >= 0 and transition < 2:
				return True
		elif location == 10:
			if transition >= 0 and transition < 2:
				return (state.preheat)[3]
			elif transition == 2:
				return ((not (state.preheat)[3]) and (((state.soc >= 90000000) and (not state.ac_lock)) or ((self.network._get_transient_value(state, "cost_rate"))[3] != -1)))
		elif location == 11:
			if transition == 0:
				return (state.available)[3]
			elif transition == 1:
				return True
		elif location == 12:
			if transition == 0:
				return (state.not_available)[3]
			elif transition == 1:
				return True
		elif location == 13:
			if transition >= 0 and transition < 2:
				return True
		elif location == 14:
			if transition == 0:
				return (state.gc == state.temptime)
			elif transition == 1:
				return True
		elif location == 15:
			if transition >= 0 and transition < 2:
				return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Job_location_2][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Job_location_2
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
		elif location == 1:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
		elif location == 2:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 4:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 5:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 6:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
		elif location == 7:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 8:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 9:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 10:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
		elif location == 11:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 12:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 13:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 14:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 15:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Job_location_2
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.preheat[3] = False
				elif transition == 1:
					if branch == 0:
						target_state.ac_lock = ((transient.a_nfe)[3] != 0)
						target_state.preheat[3] = False
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.slewing = True
						target_state.temptime = (state.new_time + 600)
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.pa[3] = True
						target_state.available[3] = False
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.bUpdate = True
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.not_available[3] = False
						target_state.pa[3] = False
						target_state.nee[3] = ((state.nee)[3] + 1)
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.bUpdate = True
			elif location == 6:
				if transition == 1:
					if branch == 0:
						target_state.slewing = True
						target_state.temptime = (state.new_time + 600)
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.bUpdate = True
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.slewing = False
						target_state.new_time = state.temptime
						target_state.a = 1
						target_state.ac_lock = False
						target_state.temptime = 0
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.bUpdate = True
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.preheat[3] = False
				elif transition == 1:
					if branch == 0:
						target_state.ac_lock = ((transient.a_nfe)[3] != 0)
						target_state.preheat[3] = False
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_state.available[3] = False
			elif location == 12:
				if transition == 0:
					if branch == 0:
						target_state.not_available[3] = False
						target_transient.cost = (transient.cost_rate)[3]
			elif location == 13:
				if transition == 0:
					if branch == 0:
						target_state.bUpdate = True
			elif location == 14:
				if transition == 0:
					if branch == 0:
						target_state.slewing = False
						target_state.new_time = state.temptime
						target_state.a = (transient.a_nfe)[3]
						target_state.temptime = 0
			elif location == 15:
				if transition == 0:
					if branch == 0:
						target_state.bUpdate = True
		elif assignment_index == 1:
			location = state.Job_location_2
			if location == 0:
				if transition == 2:
					if branch == 0:
						target_transient.Job_location = 0
			elif location == 1:
				if transition == 2:
					if branch == 0:
						target_transient.Job_location = 1
			elif location == 2:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location = 2
			elif location == 3:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location = 3
			elif location == 4:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location = 4
			elif location == 5:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location = 5
			elif location == 6:
				if transition == 2:
					if branch == 0:
						target_transient.Job_location = 6
			elif location == 7:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location = 7
			elif location == 8:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location = 8
			elif location == 9:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location = 9
			elif location == 10:
				if transition == 2:
					if branch == 0:
						target_transient.Job_location = 10
			elif location == 11:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location = 11
			elif location == 12:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location = 12
			elif location == 13:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location = 13
			elif location == 14:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location = 14
			elif location == 15:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location = 15
		elif assignment_index == 3:
			location = state.Job_location_2
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_2 = 11
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_2 = 1
				elif transition == 2:
					if branch == 0:
						target_state.Job_location_2 = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_2 = 13
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_2 = 2
				elif transition == 2:
					if branch == 0:
						target_state.Job_location_2 = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_2 = 3
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_2 = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_2 = 4
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_2 = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_2 = 5
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_2 = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_2 = 6
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_2 = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_2 = 10
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_2 = 7
				elif transition == 2:
					if branch == 0:
						target_state.Job_location_2 = 6
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_2 = 8
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_2 = 7
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_2 = 9
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_2 = 8
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_2 = 10
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_2 = 9
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_2 = 11
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_2 = 1
				elif transition == 2:
					if branch == 0:
						target_state.Job_location_2 = 10
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_2 = 12
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_2 = 11
			elif location == 12:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_2 = 10
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_2 = 12
			elif location == 13:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_2 = 14
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_2 = 13
			elif location == 14:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_2 = 15
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_2 = 14
			elif location == 15:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_2 = 2
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_2 = 15

# Automaton: Job
class JobAutomaton_1(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [3, 3, 2, 2, 2, 2, 3, 2, 2, 2, 3, 2, 2, 2, 2, 2]
		self.transition_labels = [[4, 5, 61], [6, 7, 61], [8, 61], [9, 61], [10, 61], [11, 61], [12, 13, 61], [14, 61], [15, 61], [14, 61], [4, 5, 61], [16, 61], [17, 61], [14, 61], [18, 61], [14, 61]]
		self.branch_counts = [[1, 1, 1], [1, 1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1, 1], [1, 1], [1, 1], [1, 1], [1, 1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Job_location_3 = 0
		state.temptime_1 = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Job_location_3
		if location == 0:
			if transient_variable == "Job_location_1":
				return 0
		elif location == 1:
			if transient_variable == "Job_location_1":
				return 1
		elif location == 2:
			if transient_variable == "Job_location_1":
				return 2
		elif location == 3:
			if transient_variable == "Job_location_1":
				return 3
		elif location == 4:
			if transient_variable == "Job_location_1":
				return 4
		elif location == 5:
			if transient_variable == "Job_location_1":
				return 5
		elif location == 6:
			if transient_variable == "Job_location_1":
				return 6
		elif location == 7:
			if transient_variable == "Job_location_1":
				return 7
		elif location == 8:
			if transient_variable == "Job_location_1":
				return 8
		elif location == 9:
			if transient_variable == "Job_location_1":
				return 9
		elif location == 10:
			if transient_variable == "Job_location_1":
				return 10
		elif location == 11:
			if transient_variable == "Job_location_1":
				return 11
		elif location == 12:
			if transient_variable == "Job_location_1":
				return 12
		elif location == 13:
			if transient_variable == "Job_location_1":
				return 13
		elif location == 14:
			if transient_variable == "Job_location_1":
				return 14
		elif location == 15:
			if transient_variable == "Job_location_1":
				return 15
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Job_location_3]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Job_location_3][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Job_location_3
		if location == 0:
			if transition >= 0 and transition < 2:
				return (state.preheat)[4]
			elif transition == 2:
				return ((not (state.preheat)[4]) and (((state.soc >= 90000000) and (not state.ac_lock)) or ((self.network._get_transient_value(state, "cost_rate"))[4] != -1)))
		elif location == 1:
			if transition == 0:
				return (((self.network._get_transient_value(state, "a_nfe"))[4] != 0) and (state.a != (self.network._get_transient_value(state, "a_nfe"))[4]))
			elif transition == 1:
				return (((self.network._get_transient_value(state, "a_nfe"))[4] == 0) or (state.a == (self.network._get_transient_value(state, "a_nfe"))[4]))
			elif transition == 2:
				return True
		elif location == 2:
			if transition == 0:
				return (state.available)[4]
			elif transition == 1:
				return True
		elif location == 3:
			if transition >= 0 and transition < 2:
				return True
		elif location == 4:
			if transition == 0:
				return (state.not_available)[4]
			elif transition == 1:
				return True
		elif location == 5:
			if transition >= 0 and transition < 2:
				return True
		elif location == 6:
			if transition == 0:
				return (((self.network._get_transient_value(state, "a_nfe"))[4] == 0) or (state.a == 1))
			elif transition == 1:
				return (((self.network._get_transient_value(state, "a_nfe"))[4] != 0) and (state.a != 1))
			elif transition == 2:
				return True
		elif location == 7:
			if transition >= 0 and transition < 2:
				return True
		elif location == 8:
			if transition == 0:
				return (state.gc == state.temptime_1)
			elif transition == 1:
				return True
		elif location == 9:
			if transition >= 0 and transition < 2:
				return True
		elif location == 10:
			if transition >= 0 and transition < 2:
				return (state.preheat)[4]
			elif transition == 2:
				return ((not (state.preheat)[4]) and (((state.soc >= 90000000) and (not state.ac_lock)) or ((self.network._get_transient_value(state, "cost_rate"))[4] != -1)))
		elif location == 11:
			if transition == 0:
				return (state.available)[4]
			elif transition == 1:
				return True
		elif location == 12:
			if transition == 0:
				return (state.not_available)[4]
			elif transition == 1:
				return True
		elif location == 13:
			if transition >= 0 and transition < 2:
				return True
		elif location == 14:
			if transition == 0:
				return (state.gc == state.temptime_1)
			elif transition == 1:
				return True
		elif location == 15:
			if transition >= 0 and transition < 2:
				return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Job_location_3][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Job_location_3
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
		elif location == 1:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
		elif location == 2:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 4:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 5:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 6:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
		elif location == 7:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 8:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 9:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 10:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
		elif location == 11:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 12:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 13:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 14:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 15:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Job_location_3
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.preheat[4] = False
				elif transition == 1:
					if branch == 0:
						target_state.ac_lock = ((transient.a_nfe)[4] != 0)
						target_state.preheat[4] = False
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.slewing = True
						target_state.temptime_1 = (state.new_time + 600)
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.pa[4] = True
						target_state.available[4] = False
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.bUpdate = True
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.not_available[4] = False
						target_state.pa[4] = False
						target_state.nee[4] = ((state.nee)[4] + 1)
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.bUpdate = True
			elif location == 6:
				if transition == 1:
					if branch == 0:
						target_state.slewing = True
						target_state.temptime_1 = (state.new_time + 600)
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.bUpdate = True
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.slewing = False
						target_state.new_time = state.temptime_1
						target_state.a = 1
						target_state.ac_lock = False
						target_state.temptime_1 = 0
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.bUpdate = True
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.preheat[4] = False
				elif transition == 1:
					if branch == 0:
						target_state.ac_lock = ((transient.a_nfe)[4] != 0)
						target_state.preheat[4] = False
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_state.available[4] = False
			elif location == 12:
				if transition == 0:
					if branch == 0:
						target_state.not_available[4] = False
						target_transient.cost = (transient.cost_rate)[4]
			elif location == 13:
				if transition == 0:
					if branch == 0:
						target_state.bUpdate = True
			elif location == 14:
				if transition == 0:
					if branch == 0:
						target_state.slewing = False
						target_state.new_time = state.temptime_1
						target_state.a = (transient.a_nfe)[4]
						target_state.temptime_1 = 0
			elif location == 15:
				if transition == 0:
					if branch == 0:
						target_state.bUpdate = True
		elif assignment_index == 1:
			location = state.Job_location_3
			if location == 0:
				if transition == 2:
					if branch == 0:
						target_transient.Job_location_1 = 0
			elif location == 1:
				if transition == 2:
					if branch == 0:
						target_transient.Job_location_1 = 1
			elif location == 2:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location_1 = 2
			elif location == 3:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location_1 = 3
			elif location == 4:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location_1 = 4
			elif location == 5:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location_1 = 5
			elif location == 6:
				if transition == 2:
					if branch == 0:
						target_transient.Job_location_1 = 6
			elif location == 7:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location_1 = 7
			elif location == 8:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location_1 = 8
			elif location == 9:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location_1 = 9
			elif location == 10:
				if transition == 2:
					if branch == 0:
						target_transient.Job_location_1 = 10
			elif location == 11:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location_1 = 11
			elif location == 12:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location_1 = 12
			elif location == 13:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location_1 = 13
			elif location == 14:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location_1 = 14
			elif location == 15:
				if transition == 1:
					if branch == 0:
						target_transient.Job_location_1 = 15
		elif assignment_index == 3:
			location = state.Job_location_3
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_3 = 11
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_3 = 1
				elif transition == 2:
					if branch == 0:
						target_state.Job_location_3 = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_3 = 13
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_3 = 2
				elif transition == 2:
					if branch == 0:
						target_state.Job_location_3 = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_3 = 3
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_3 = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_3 = 4
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_3 = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_3 = 5
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_3 = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_3 = 6
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_3 = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_3 = 10
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_3 = 7
				elif transition == 2:
					if branch == 0:
						target_state.Job_location_3 = 6
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_3 = 8
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_3 = 7
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_3 = 9
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_3 = 8
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_3 = 10
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_3 = 9
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_3 = 11
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_3 = 1
				elif transition == 2:
					if branch == 0:
						target_state.Job_location_3 = 10
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_3 = 12
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_3 = 11
			elif location == 12:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_3 = 10
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_3 = 12
			elif location == 13:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_3 = 14
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_3 = 13
			elif location == 14:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_3 = 15
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_3 = 14
			elif location == 15:
				if transition == 0:
					if branch == 0:
						target_state.Job_location_3 = 2
				elif transition == 1:
					if branch == 0:
						target_state.Job_location_3 = 15

# Automaton: Terminate
class TerminateAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 1]
		self.transition_labels = [[19, 61], [20, 61], [61]]
		self.branch_counts = [[1, 1], [1, 1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Terminate_location_1 = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Terminate_location_1
		if location == 0:
			if transient_variable == "Terminate_location":
				return 0
		elif location == 1:
			if transient_variable == "Terminate_location":
				return 1
		elif location == 2:
			if transient_variable == "Terminate_location":
				return 2
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Terminate_location_1]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Terminate_location_1][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Terminate_location_1
		if location == 0:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.gc < 10000)
		elif location == 1:
			if transition == 0:
				return (state.gc == 10000)
			elif transition == 1:
				return True
		elif location == 2:
			return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Terminate_location_1][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Terminate_location_1
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
			location = state.Terminate_location_1
			if location == 1:
				if transition == 0:
					if branch == 0:
						target_state.finished = True
		elif assignment_index == 1:
			location = state.Terminate_location_1
			if location == 0:
				if transition == 1:
					if branch == 0:
						target_transient.Terminate_location = 0
			elif location == 1:
				if transition == 1:
					if branch == 0:
						target_transient.Terminate_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_transient.Terminate_location = 2
		elif assignment_index == 3:
			location = state.Terminate_location_1
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Terminate_location_1 = 1
				elif transition == 1:
					if branch == 0:
						target_state.Terminate_location_1 = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Terminate_location_1 = 2
				elif transition == 1:
					if branch == 0:
						target_state.Terminate_location_1 = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Terminate_location_1 = 2

# Automaton: Battery
class BatteryAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 2, 3, 1]
		self.transition_labels = [[21, 61], [14, 61], [22, 61], [23, 24, 61], [61]]
		self.branch_counts = [[1, 1], [1, 1], [1, 1], [1, 1, 1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Battery_location_1 = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Battery_location_1
		if location == 0:
			if transient_variable == "Battery_location":
				return 0
		elif location == 1:
			if transient_variable == "Battery_location":
				return 1
		elif location == 2:
			if transient_variable == "Battery_location":
				return 2
		elif location == 3:
			if transient_variable == "Battery_location":
				return 3
		elif location == 4:
			if transient_variable == "Battery_location":
				return 4
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Battery_location_1]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Battery_location_1][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Battery_location_1
		if location == 0:
			if transition >= 0 and transition < 2:
				return True
		elif location == 1:
			if transition == 0:
				return state.bUpdate
			elif transition == 1:
				return True
		elif location == 2:
			if transition >= 0 and transition < 2:
				return True
		elif location == 3:
			if transition == 0:
				return (state.soc > 59904000)
			elif transition == 1:
				return (state.soc <= 59904000)
			elif transition == 2:
				return True
		elif location == 4:
			return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Battery_location_1][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Battery_location_1
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
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
		elif location == 4:
			if transition == 0:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Battery_location_1
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.soc = (state.soc - (state.load * (state.new_time - state.old_time)))
						target_state.old_time = state.new_time
						target_state.load = 2989
						target_state.load = (state.load + ((transient.power_p)[1] if (state.pa)[1] else 0))
						target_state.load = (state.load + ((transient.power_p)[2] if (state.pa)[2] else 0))
						target_state.load = (state.load + ((transient.power_p)[3] if (state.pa)[3] else 0))
						target_state.load = (state.load + ((transient.power_p)[4] if (state.pa)[4] else 0))
						target_state.load = (state.load + (414 if state.slewing else 0))
						target_state.load = (state.load - ((transient.power_g)[state.a] if state.insolation else 0))
						target_state.load = (state.load + (414 if state.heating else 0))
						target_state.load = (0 if (state.load > 15000) else state.load)
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.soc = (state.soc - (state.load * (state.new_time - state.old_time)))
						target_state.old_time = state.new_time
						target_state.load = 2989
						target_state.bUpdate = False
						target_state.load = (state.load + ((transient.power_p)[1] if (state.pa)[1] else 0))
						target_state.load = (state.load + ((transient.power_p)[2] if (state.pa)[2] else 0))
						target_state.load = (state.load + ((transient.power_p)[3] if (state.pa)[3] else 0))
						target_state.load = (state.load + ((transient.power_p)[4] if (state.pa)[4] else 0))
						target_state.load = (state.load + (414 if state.slewing else 0))
						target_state.load = (state.load - ((transient.power_g)[state.a] if state.insolation else 0))
						target_state.load = (state.load + (414 if state.heating else 0))
						target_state.load = (0 if (state.load > 15000) else state.load)
			elif location == 3:
				if transition == 1:
					if branch == 0:
						target_state.failure = True
		elif assignment_index == 1:
			location = state.Battery_location_1
			if location == 0:
				if transition == 1:
					if branch == 0:
						target_transient.Battery_location = 0
			elif location == 1:
				if transition == 1:
					if branch == 0:
						target_transient.Battery_location = 1
			elif location == 2:
				if transition == 1:
					if branch == 0:
						target_transient.Battery_location = 2
			elif location == 3:
				if transition == 2:
					if branch == 0:
						target_transient.Battery_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_transient.Battery_location = 4
		elif assignment_index == 3:
			location = state.Battery_location_1
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Battery_location_1 = 1
				elif transition == 1:
					if branch == 0:
						target_state.Battery_location_1 = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Battery_location_1 = 2
				elif transition == 1:
					if branch == 0:
						target_state.Battery_location_1 = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Battery_location_1 = 3
				elif transition == 1:
					if branch == 0:
						target_state.Battery_location_1 = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Battery_location_1 = 1
				elif transition == 1:
					if branch == 0:
						target_state.Battery_location_1 = 4
				elif transition == 2:
					if branch == 0:
						target_state.Battery_location_1 = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.Battery_location_1 = 4

# Automaton: Sun
class SunAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [3, 2, 2, 2, 2, 2, 2, 2, 2]
		self.transition_labels = [[25, 26, 61], [27, 61], [14, 61], [28, 61], [14, 61], [28, 61], [14, 61], [27, 61], [14, 61]]
		self.branch_counts = [[1, 1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Sun_location_1 = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Sun_location_1
		if location == 0:
			if transient_variable == "Sun_location":
				return 0
		elif location == 1:
			if transient_variable == "Sun_location":
				return 1
		elif location == 2:
			if transient_variable == "Sun_location":
				return 2
		elif location == 3:
			if transient_variable == "Sun_location":
				return 3
		elif location == 4:
			if transient_variable == "Sun_location":
				return 4
		elif location == 5:
			if transient_variable == "Sun_location":
				return 5
		elif location == 6:
			if transient_variable == "Sun_location":
				return 6
		elif location == 7:
			if transient_variable == "Sun_location":
				return 7
		elif location == 8:
			if transient_variable == "Sun_location":
				return 8
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Sun_location_1]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Sun_location_1][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Sun_location_1
		if location == 0:
			if transition == 0:
				return ((self.network._get_transient_value(state, "sun_start"))[state.sun_c] <= (self.network._get_transient_value(state, "sun_stop"))[state.sun_c])
			elif transition == 1:
				return ((self.network._get_transient_value(state, "sun_start"))[state.sun_c] > (self.network._get_transient_value(state, "sun_stop"))[state.sun_c])
			elif transition == 2:
				return True
		elif location == 1:
			if transition == 0:
				return (state.gc == (self.network._get_transient_value(state, "sun_stop"))[state.sun_c])
			elif transition == 1:
				return (state.gc < (self.network._get_transient_value(state, "sun_stop"))[state.sun_c])
		elif location == 2:
			if transition >= 0 and transition < 2:
				return True
		elif location == 3:
			if transition == 0:
				return (state.gc == (self.network._get_transient_value(state, "sun_start"))[state.sun_c])
			elif transition == 1:
				return (state.gc < (self.network._get_transient_value(state, "sun_start"))[state.sun_c])
		elif location == 4:
			if transition >= 0 and transition < 2:
				return True
		elif location == 5:
			if transition == 0:
				return (state.gc == (self.network._get_transient_value(state, "sun_start"))[state.sun_c])
			elif transition == 1:
				return (state.gc < (self.network._get_transient_value(state, "sun_start"))[state.sun_c])
		elif location == 6:
			if transition >= 0 and transition < 2:
				return True
		elif location == 7:
			if transition == 0:
				return (state.gc == (self.network._get_transient_value(state, "sun_stop"))[state.sun_c])
			elif transition == 1:
				return (state.gc < (self.network._get_transient_value(state, "sun_stop"))[state.sun_c])
		elif location == 8:
			if transition >= 0 and transition < 2:
				return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Sun_location_1][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Sun_location_1
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
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
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 4:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 5:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 6:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 7:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 8:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Sun_location_1
			if location == 0:
				if transition == 1:
					if branch == 0:
						target_state.insolation = True
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.insolation = False
						target_state.new_time = (transient.sun_stop)[state.sun_c]
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.bUpdate = True
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.sun_c = (state.sun_c + 1)
						target_state.insolation = True
						target_state.new_time = (transient.sun_start)[state.sun_c]
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.bUpdate = True
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.insolation = True
						target_state.new_time = (transient.sun_start)[state.sun_c]
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.bUpdate = True
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.sun_c = (state.sun_c + 1)
						target_state.insolation = True
						target_state.new_time = (transient.sun_stop)[state.sun_c]
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.bUpdate = True
		elif assignment_index == 1:
			location = state.Sun_location_1
			if location == 0:
				if transition == 2:
					if branch == 0:
						target_transient.Sun_location = 0
			elif location == 1:
				if transition == 1:
					if branch == 0:
						target_transient.Sun_location = 1
			elif location == 2:
				if transition == 1:
					if branch == 0:
						target_transient.Sun_location = 2
			elif location == 3:
				if transition == 1:
					if branch == 0:
						target_transient.Sun_location = 3
			elif location == 4:
				if transition == 1:
					if branch == 0:
						target_transient.Sun_location = 4
			elif location == 5:
				if transition == 1:
					if branch == 0:
						target_transient.Sun_location = 5
			elif location == 6:
				if transition == 1:
					if branch == 0:
						target_transient.Sun_location = 6
			elif location == 7:
				if transition == 1:
					if branch == 0:
						target_transient.Sun_location = 7
			elif location == 8:
				if transition == 1:
					if branch == 0:
						target_transient.Sun_location = 8
		elif assignment_index == 3:
			location = state.Sun_location_1
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Sun_location_1 = 5
				elif transition == 1:
					if branch == 0:
						target_state.Sun_location_1 = 1
				elif transition == 2:
					if branch == 0:
						target_state.Sun_location_1 = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Sun_location_1 = 2
				elif transition == 1:
					if branch == 0:
						target_state.Sun_location_1 = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Sun_location_1 = 3
				elif transition == 1:
					if branch == 0:
						target_state.Sun_location_1 = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Sun_location_1 = 4
				elif transition == 1:
					if branch == 0:
						target_state.Sun_location_1 = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.Sun_location_1 = 1
				elif transition == 1:
					if branch == 0:
						target_state.Sun_location_1 = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.Sun_location_1 = 6
				elif transition == 1:
					if branch == 0:
						target_state.Sun_location_1 = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.Sun_location_1 = 7
				elif transition == 1:
					if branch == 0:
						target_state.Sun_location_1 = 6
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.Sun_location_1 = 8
				elif transition == 1:
					if branch == 0:
						target_state.Sun_location_1 = 7
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.Sun_location_1 = 5
				elif transition == 1:
					if branch == 0:
						target_state.Sun_location_1 = 8

# Automaton: GlobalInvariant
class GlobalInvariantAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [1]
		self.transition_labels = [[61]]
		self.branch_counts = [[1]]
	
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
			return (self.network._get_transient_value(state, "Sun_location") != 0)
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[0][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = 0
		if location == 0:
			if transition == 0:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 3:
			location = 0
			if location == 0:
				if transition == 0:
					if branch == 0:
						pass

# Automaton: GlobalSync
class GlobalSyncAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2]
		self.transition_labels = [[61, 62]]
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
						target_state.gc = min((state.gc + 1), 250001)
		elif assignment_index == 3:
			location = 0
			if location == 0:
				if transition == 0:
					if branch == 0:
						pass
				elif transition == 1:
					if branch == 0:
						target_transient.R_Succ_Rate_edge_reward = transient.cost

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
	
	def __init__(self, label = 0, transitions = [-1, -1, -1, -1, -1, -1, -1, -1, -1]):
		self.label = label
		self.transitions = transitions

class Branch(object):
	__slots__ = ("probability", "branches")
	
	def __init__(self, probability = 0.0, branches = [0, 0, 0, 0, 0, 0, 0, 0, 0]):
		self.probability = probability
		self.branches = branches

class Network(object):
	__slots__ = ("network", "transition_labels", "sync_vectors", "properties", "aut_JobProvider", "aut_JobProvider_1", "aut_Job", "aut_Job_1", "aut_Terminate", "aut_Battery", "aut_Sun", "aut_GlobalInvariant", "aut_GlobalSync")
	
	def __init__(self):
		self.network = self
		self.transition_labels = { 0: "τ", 1: "gotjob", 2: "preheated", 3: "jobended", 4: "checkskip", 5: "beginjob", 6: "notcorrect", 7: "alreadycorrect", 8: "jobavailable", 9: "startjob", 10: "jobdone", 11: "checkaltitude", 12: "altitudecorrect", 13: "back_notcorrect", 14: "bUpdate_action", 15: "back_reached", 16: "applypenalty", 17: "endskip", 18: "reached", 19: "start", 20: "finish", 21: "init", 22: "update", 23: "backtoidle", 24: "batterylow", 25: "earliereclipse", 26: "earlierinsolation", 27: "toeclipse", 28: "toinsolation", 29: "gotjob3", 30: "preheated3", 31: "jobended3", 32: "gotjob4", 33: "preheated4", 34: "jobended4", 35: "checkskip3", 36: "beginjob3", 37: "notcorrect3", 38: "altitudecorrect3", 39: "jobavailable3", 40: "startjob3", 41: "jobdone3", 42: "checkaltitude3", 43: "back_notcorrect3", 44: "back_reached3", 45: "applypenalty3", 46: "endskip3", 47: "reached3", 48: "checkskip4", 49: "beginjob4", 50: "notcorrect4", 51: "altitudecorrect4", 52: "jobavailable4", 53: "startjob4", 54: "jobdone4", 55: "checkaltitude4", 56: "back_notcorrect4", 57: "back_reached4", 58: "applypenalty4", 59: "endskip4", 60: "reached4", 61: "tick", 62: "tau" }
		self.sync_vectors = [[0, -1, -1, -1, -1, -1, -1, -1, -1, 0], [-1, 0, -1, -1, -1, -1, -1, -1, -1, 0], [-1, -1, 0, -1, -1, -1, -1, -1, -1, 0], [-1, -1, -1, 0, -1, -1, -1, -1, -1, 0], [-1, -1, -1, -1, 0, -1, -1, -1, -1, 0], [-1, -1, -1, -1, -1, 0, -1, -1, -1, 0], [-1, -1, -1, -1, -1, -1, 0, -1, -1, 0], [-1, -1, -1, -1, -1, -1, -1, 0, -1, 0], [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0], [1, -1, -1, -1, -1, -1, -1, -1, 62, 29], [2, -1, -1, -1, -1, -1, -1, -1, 62, 30], [3, -1, -1, -1, -1, -1, -1, -1, 62, 31], [-1, 1, -1, -1, -1, -1, -1, -1, 62, 32], [-1, 2, -1, -1, -1, -1, -1, -1, 62, 33], [-1, 3, -1, -1, -1, -1, -1, -1, 62, 34], [-1, -1, 4, -1, -1, -1, -1, -1, 62, 35], [-1, -1, 5, -1, -1, -1, -1, -1, 62, 36], [-1, -1, 6, -1, -1, -1, -1, -1, 62, 37], [-1, -1, 7, -1, -1, -1, -1, -1, 62, 38], [-1, -1, 8, -1, -1, -1, -1, -1, 62, 39], [-1, -1, 9, -1, -1, -1, -1, -1, 62, 40], [-1, -1, 10, -1, -1, -1, -1, -1, 62, 41], [-1, -1, 11, -1, -1, -1, -1, -1, 62, 42], [-1, -1, 12, -1, -1, -1, -1, -1, 62, 38], [-1, -1, 13, -1, -1, -1, -1, -1, 62, 43], [-1, -1, 15, -1, -1, -1, -1, -1, 62, 44], [-1, -1, 16, -1, -1, -1, -1, -1, 62, 45], [-1, -1, 17, -1, -1, -1, -1, -1, 62, 46], [-1, -1, 18, -1, -1, -1, -1, -1, 62, 47], [-1, -1, -1, 4, -1, -1, -1, -1, 62, 48], [-1, -1, -1, 5, -1, -1, -1, -1, 62, 49], [-1, -1, -1, 6, -1, -1, -1, -1, 62, 50], [-1, -1, -1, 7, -1, -1, -1, -1, 62, 51], [-1, -1, -1, 8, -1, -1, -1, -1, 62, 52], [-1, -1, -1, 9, -1, -1, -1, -1, 62, 53], [-1, -1, -1, 10, -1, -1, -1, -1, 62, 54], [-1, -1, -1, 11, -1, -1, -1, -1, 62, 55], [-1, -1, -1, 12, -1, -1, -1, -1, 62, 51], [-1, -1, -1, 13, -1, -1, -1, -1, 62, 56], [-1, -1, -1, 15, -1, -1, -1, -1, 62, 57], [-1, -1, -1, 16, -1, -1, -1, -1, 62, 58], [-1, -1, -1, 17, -1, -1, -1, -1, 62, 59], [-1, -1, -1, 18, -1, -1, -1, -1, 62, 60], [-1, -1, -1, -1, 19, -1, -1, -1, 62, 19], [-1, -1, -1, -1, 20, -1, -1, -1, 62, 20], [-1, -1, -1, -1, -1, 21, -1, -1, 62, 21], [-1, -1, -1, -1, -1, 22, -1, -1, 62, 22], [-1, -1, -1, -1, -1, 23, -1, -1, 62, 23], [-1, -1, -1, -1, -1, 24, -1, -1, 62, 24], [-1, -1, -1, -1, -1, -1, 25, -1, 62, 25], [-1, -1, -1, -1, -1, -1, 26, -1, 62, 26], [-1, -1, -1, -1, -1, -1, 27, -1, 62, 27], [-1, -1, -1, -1, -1, -1, 28, -1, 62, 28], [-1, -1, 14, 14, -1, 14, 14, -1, 62, 14], [61, 61, 61, 61, 61, 61, 61, 61, 61, 61]]
		self.properties = [Property("R_Succ_Rate", PropertyExpression("xmin", [0, PropertyExpression("ap", [1])]))]
		self.aut_JobProvider = JobProviderAutomaton(self)
		self.aut_JobProvider_1 = JobProviderAutomaton_1(self)
		self.aut_Job = JobAutomaton(self)
		self.aut_Job_1 = JobAutomaton_1(self)
		self.aut_Terminate = TerminateAutomaton(self)
		self.aut_Battery = BatteryAutomaton(self)
		self.aut_Sun = SunAutomaton(self)
		self.aut_GlobalInvariant = GlobalInvariantAutomaton(self)
		self.aut_GlobalSync = GlobalSyncAutomaton(self)
	
	def get_initial_state(self) -> State:
		state = State()
		state.gc = 0
		state.finished = False
		state.failure = False
		state.soc = 119808000
		state.load = 0
		state.c = [0, 0, 0, 0, 0, 0, 0]
		state.nee = [0, 0, 0, 0, 0, 0, 0]
		state.preheat = [False, False, False, False, False, False, False]
		state.available = [False, False, False, False, False, False, False]
		state.not_available = [False, False, False, False, False, False, False]
		state.pa = [False, False, False, False, False, False, False]
		state.a = 0
		state.sun_c = 0
		state.heating = False
		state.slewing = False
		state.insolation = False
		state.ac_lock = False
		state.bUpdate = False
		state.new_time = 0
		state.old_time = 0
		self.aut_JobProvider.set_initial_values(state)
		self.aut_JobProvider_1.set_initial_values(state)
		self.aut_Job.set_initial_values(state)
		self.aut_Job_1.set_initial_values(state)
		self.aut_Terminate.set_initial_values(state)
		self.aut_Battery.set_initial_values(state)
		self.aut_Sun.set_initial_values(state)
		self.aut_GlobalInvariant.set_initial_values(state)
		self.aut_GlobalSync.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		transient.R_Succ_Rate_edge_reward = 0
		transient.cost = 0
		transient.sun_start = [1151, 6655, 12159, 17663, 23168, 28672, 34176, 39680, 45184, 50688, 56192, 61696, 67200, 72705, 78209, 83713, 89217, 94721, 100226, 105730, 111234, 116738, 122242, 127747, 133251, 138755, 144260, 149764, 155268, 160773, 166277, 171781, 177286, 182790, 188295, 193799, 199304, 204808, 210313, 215818, 221322, 226827, 232332]
		transient.sun_stop = [4620, 10127, 15633, 21140, 26646, 32153, 37660, 43167, 48673, 54180, 59687, 65194, 70701, 76208, 81715, 87222, 92729, 98236, 103743, 109250, 114757, 120265, 125772, 131279, 136786, 142294, 147801, 153309, 158816, 164324, 169831, 175339, 180846, 186354, 191862, 197369, 202877, 208385, 213893, 219401, 224909, 230417]
		transient.gom_start = [60917, 66429, 72087, 77787, 83507, 89317, 148887, 154504, 160190, 165900, 171645]
		transient.gom_stop = [61141, 66947, 72667, 78366, 84023, 89530, 149330, 155067, 160775, 166457, 172058]
		transient.kourou_start = [23916, 29751, 65340, 70973, 106372, 112047, 153366, 159207, 194425, 200321]
		transient.kourou_stop = [24504, 30099, 65751, 71549, 106842, 112605, 153954, 159559, 195021, 200556]
		transient.toulouse_start = [6837, 60592, 66202, 71954, 77737, 83484, 89215, 95054, 148622, 154327, 160108, 165873, 171604, 177362]
		transient.toulouse_stop = [7354, 61025, 66803, 72532, 78291, 84075, 89800, 95322, 149188, 154924, 160664, 166444, 172208, 177852]
		transient.ftwo_start = [5367, 11204, 16951, 22674, 28430, 34307, 40374, 46421, 52289, 58049, 63772, 69513, 75349, 81376, 87459, 93369, 99149, 104876, 110608, 116414, 122392, 128487, 134437, 140238, 145971, 151696, 157475, 163402, 169496, 175495, 181325, 187070, 192792, 198552, 204435, 210504, 216541, 222402]
		transient.ftwo_stop = [10937, 16774, 22521, 28244, 34000, 39877, 45944, 51991, 57859, 63619, 69342, 75083, 80919, 86946, 93029, 98939, 104719, 110446, 116178, 121984, 127962, 134057, 140007, 145808, 151541, 157266, 163045, 168972, 175066, 181065, 186895, 192640, 198362, 204122, 210005, 216074, 222111, 227972]
		transient.fthree_start = [2707, 8521, 14261, 19986, 25756, 31664, 37749, 43768, 49614, 55366, 61090, 66845, 72711, 78765, 84817, 90695, 96462, 102187, 107928, 113757, 119768, 125851, 131771, 137558, 143288, 149021, 154821, 160786, 166875, 172835, 178644, 184381, 190108, 195884, 201800, 207883, 213889, 219727, 225477]
		transient.fthree_stop = [8277, 14091, 19831, 25556, 31326, 37234, 43319, 49338, 55184, 60936, 66660, 72415, 78281, 84335, 90387, 96265, 102032, 107757, 113498, 119327, 125338, 131421, 137341, 143128, 148858, 154591, 160391, 166356, 172445, 178405, 184214, 189951, 195678, 201454, 207370, 213453, 219459, 225297, 231047]
		transient.cost_rate = [-1, 23, 22, 1, 1, 1, 1]
		transient.a_nfe = [0, 3, 3, 4, 4, 4, 4]
		transient.power_g = [0, 5700, 6100, 570, 6100]
		transient.power_p = [2630, 11945, 11945, 3863, 3863, 3863, 3863]
		transient.JobProvider_location = 0
		transient.JobProvider_location_1 = 0
		transient.Job_location = 0
		transient.Job_location_1 = 0
		transient.Terminate_location = 0
		transient.Battery_location = 0
		transient.Sun_location = 0
		self.aut_JobProvider.set_initial_transient_values(transient)
		self.aut_JobProvider_1.set_initial_transient_values(transient)
		self.aut_Job.set_initial_transient_values(transient)
		self.aut_Job_1.set_initial_transient_values(transient)
		self.aut_Terminate.set_initial_transient_values(transient)
		self.aut_Battery.set_initial_transient_values(transient)
		self.aut_Sun.set_initial_transient_values(transient)
		self.aut_GlobalInvariant.set_initial_transient_values(transient)
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
		result = self.aut_JobProvider.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self.aut_JobProvider_1.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self.aut_Job.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self.aut_Job_1.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self.aut_Terminate.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self.aut_Battery.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self.aut_Sun.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self.aut_GlobalInvariant.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self.aut_GlobalSync.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		if transient_variable == "R_Succ_Rate_edge_reward":
			return 0
		elif transient_variable == "cost":
			return 0
		elif transient_variable == "sun_start":
			return [1151, 6655, 12159, 17663, 23168, 28672, 34176, 39680, 45184, 50688, 56192, 61696, 67200, 72705, 78209, 83713, 89217, 94721, 100226, 105730, 111234, 116738, 122242, 127747, 133251, 138755, 144260, 149764, 155268, 160773, 166277, 171781, 177286, 182790, 188295, 193799, 199304, 204808, 210313, 215818, 221322, 226827, 232332]
		elif transient_variable == "sun_stop":
			return [4620, 10127, 15633, 21140, 26646, 32153, 37660, 43167, 48673, 54180, 59687, 65194, 70701, 76208, 81715, 87222, 92729, 98236, 103743, 109250, 114757, 120265, 125772, 131279, 136786, 142294, 147801, 153309, 158816, 164324, 169831, 175339, 180846, 186354, 191862, 197369, 202877, 208385, 213893, 219401, 224909, 230417]
		elif transient_variable == "gom_start":
			return [60917, 66429, 72087, 77787, 83507, 89317, 148887, 154504, 160190, 165900, 171645]
		elif transient_variable == "gom_stop":
			return [61141, 66947, 72667, 78366, 84023, 89530, 149330, 155067, 160775, 166457, 172058]
		elif transient_variable == "kourou_start":
			return [23916, 29751, 65340, 70973, 106372, 112047, 153366, 159207, 194425, 200321]
		elif transient_variable == "kourou_stop":
			return [24504, 30099, 65751, 71549, 106842, 112605, 153954, 159559, 195021, 200556]
		elif transient_variable == "toulouse_start":
			return [6837, 60592, 66202, 71954, 77737, 83484, 89215, 95054, 148622, 154327, 160108, 165873, 171604, 177362]
		elif transient_variable == "toulouse_stop":
			return [7354, 61025, 66803, 72532, 78291, 84075, 89800, 95322, 149188, 154924, 160664, 166444, 172208, 177852]
		elif transient_variable == "ftwo_start":
			return [5367, 11204, 16951, 22674, 28430, 34307, 40374, 46421, 52289, 58049, 63772, 69513, 75349, 81376, 87459, 93369, 99149, 104876, 110608, 116414, 122392, 128487, 134437, 140238, 145971, 151696, 157475, 163402, 169496, 175495, 181325, 187070, 192792, 198552, 204435, 210504, 216541, 222402]
		elif transient_variable == "ftwo_stop":
			return [10937, 16774, 22521, 28244, 34000, 39877, 45944, 51991, 57859, 63619, 69342, 75083, 80919, 86946, 93029, 98939, 104719, 110446, 116178, 121984, 127962, 134057, 140007, 145808, 151541, 157266, 163045, 168972, 175066, 181065, 186895, 192640, 198362, 204122, 210005, 216074, 222111, 227972]
		elif transient_variable == "fthree_start":
			return [2707, 8521, 14261, 19986, 25756, 31664, 37749, 43768, 49614, 55366, 61090, 66845, 72711, 78765, 84817, 90695, 96462, 102187, 107928, 113757, 119768, 125851, 131771, 137558, 143288, 149021, 154821, 160786, 166875, 172835, 178644, 184381, 190108, 195884, 201800, 207883, 213889, 219727, 225477]
		elif transient_variable == "fthree_stop":
			return [8277, 14091, 19831, 25556, 31326, 37234, 43319, 49338, 55184, 60936, 66660, 72415, 78281, 84335, 90387, 96265, 102032, 107757, 113498, 119327, 125338, 131421, 137341, 143128, 148858, 154591, 160391, 166356, 172445, 178405, 184214, 189951, 195678, 201454, 207370, 213453, 219459, 225297, 231047]
		elif transient_variable == "cost_rate":
			return [-1, 23, 22, 1, 1, 1, 1]
		elif transient_variable == "a_nfe":
			return [0, 3, 3, 4, 4, 4, 4]
		elif transient_variable == "power_g":
			return [0, 5700, 6100, 570, 6100]
		elif transient_variable == "power_p":
			return [2630, 11945, 11945, 3863, 3863, 3863, 3863]
		elif transient_variable == "JobProvider_location":
			return 0
		elif transient_variable == "JobProvider_location_1":
			return 0
		elif transient_variable == "Job_location":
			return 0
		elif transient_variable == "Job_location_1":
			return 0
		elif transient_variable == "Terminate_location":
			return 0
		elif transient_variable == "Battery_location":
			return 0
		elif transient_variable == "Sun_location":
			return 0
		return None
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_JobProvider = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_JobProvider.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_JobProvider.get_guard_value(state, i):
				trans_JobProvider[self.aut_JobProvider.get_transition_label(state, i)].append(i)
		trans_JobProvider_1 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_JobProvider_1.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_JobProvider_1.get_guard_value(state, i):
				trans_JobProvider_1[self.aut_JobProvider_1.get_transition_label(state, i)].append(i)
		trans_Job = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_Job.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_Job.get_guard_value(state, i):
				trans_Job[self.aut_Job.get_transition_label(state, i)].append(i)
		trans_Job_1 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_Job_1.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_Job_1.get_guard_value(state, i):
				trans_Job_1[self.aut_Job_1.get_transition_label(state, i)].append(i)
		trans_Terminate = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_Terminate.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_Terminate.get_guard_value(state, i):
				trans_Terminate[self.aut_Terminate.get_transition_label(state, i)].append(i)
		trans_Battery = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_Battery.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_Battery.get_guard_value(state, i):
				trans_Battery[self.aut_Battery.get_transition_label(state, i)].append(i)
		trans_Sun = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_Sun.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_Sun.get_guard_value(state, i):
				trans_Sun[self.aut_Sun.get_transition_label(state, i)].append(i)
		trans_GlobalInvariant = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_GlobalInvariant.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_GlobalInvariant.get_guard_value(state, i):
				trans_GlobalInvariant[self.aut_GlobalInvariant.get_transition_label(state, i)].append(i)
		trans_GlobalSync = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self.aut_GlobalSync.get_transition_count(state)
		for i in range(transition_count):
			if self.aut_GlobalSync.get_guard_value(state, i):
				trans_GlobalSync[self.aut_GlobalSync.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for sv in self.sync_vectors:
			synced = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
			# JobProvider
			if synced is not None:
				if sv[0] != -1:
					if len(trans_JobProvider[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_JobProvider[sv[0]][0]
						for i in range(1, len(trans_JobProvider[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_JobProvider[sv[0]][i]
			# JobProvider
			if synced is not None:
				if sv[1] != -1:
					if len(trans_JobProvider_1[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_JobProvider_1[sv[1]][0]
						for i in range(1, len(trans_JobProvider_1[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_JobProvider_1[sv[1]][i]
			# Job
			if synced is not None:
				if sv[2] != -1:
					if len(trans_Job[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_Job[sv[2]][0]
						for i in range(1, len(trans_Job[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_Job[sv[2]][i]
			# Job
			if synced is not None:
				if sv[3] != -1:
					if len(trans_Job_1[sv[3]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][3] = trans_Job_1[sv[3]][0]
						for i in range(1, len(trans_Job_1[sv[3]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][3] = trans_Job_1[sv[3]][i]
			# Terminate
			if synced is not None:
				if sv[4] != -1:
					if len(trans_Terminate[sv[4]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][4] = trans_Terminate[sv[4]][0]
						for i in range(1, len(trans_Terminate[sv[4]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][4] = trans_Terminate[sv[4]][i]
			# Battery
			if synced is not None:
				if sv[5] != -1:
					if len(trans_Battery[sv[5]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][5] = trans_Battery[sv[5]][0]
						for i in range(1, len(trans_Battery[sv[5]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][5] = trans_Battery[sv[5]][i]
			# Sun
			if synced is not None:
				if sv[6] != -1:
					if len(trans_Sun[sv[6]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][6] = trans_Sun[sv[6]][0]
						for i in range(1, len(trans_Sun[sv[6]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][6] = trans_Sun[sv[6]][i]
			# GlobalInvariant
			if synced is not None:
				if sv[7] != -1:
					if len(trans_GlobalInvariant[sv[7]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][7] = trans_GlobalInvariant[sv[7]][0]
						for i in range(1, len(trans_GlobalInvariant[sv[7]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][7] = trans_GlobalInvariant[sv[7]][i]
			# GlobalSync
			if synced is not None:
				if sv[8] != -1:
					if len(trans_GlobalSync[sv[8]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][8] = trans_GlobalSync[sv[8]][0]
						for i in range(1, len(trans_GlobalSync[sv[8]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][8] = trans_GlobalSync[sv[8]][i]
			if synced is not None:
				for sync in synced:
					sync[9] = sv[9]
				transitions.extend(filter(lambda s: s[-1] != -1, synced))
		# Convert to Transition instances
		for i in range(len(transitions)):
			transitions[i] = Transition(transitions[i][9], transitions[i])
			del transitions[i].transitions[9]
		# Done
		return transitions
	
	def get_branches(self, state: State, transition: Transition) -> List[Branch]:
		combs = [[-1, -1, -1, -1, -1, -1, -1, -1, -1]]
		probs = [1.0]
		if transition.transitions[0] != -1:
			existing = len(combs)
			branch_count = self.aut_JobProvider.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self.aut_JobProvider.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self.aut_JobProvider.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		if transition.transitions[1] != -1:
			existing = len(combs)
			branch_count = self.aut_JobProvider_1.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self.aut_JobProvider_1.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self.aut_JobProvider_1.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self.aut_Job.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self.aut_Job.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self.aut_Job.get_probability_value(state, transition.transitions[2], 0)
			for i in range(existing):
				combs[i][2] = 0
				probs[i] *= probability
		if transition.transitions[3] != -1:
			existing = len(combs)
			branch_count = self.aut_Job_1.get_branch_count(state, transition.transitions[3])
			for i in range(1, branch_count):
				probability = self.aut_Job_1.get_probability_value(state, transition.transitions[3], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][3] = i
					probs.append(probs[j] * probability)
			probability = self.aut_Job_1.get_probability_value(state, transition.transitions[3], 0)
			for i in range(existing):
				combs[i][3] = 0
				probs[i] *= probability
		if transition.transitions[4] != -1:
			existing = len(combs)
			branch_count = self.aut_Terminate.get_branch_count(state, transition.transitions[4])
			for i in range(1, branch_count):
				probability = self.aut_Terminate.get_probability_value(state, transition.transitions[4], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][4] = i
					probs.append(probs[j] * probability)
			probability = self.aut_Terminate.get_probability_value(state, transition.transitions[4], 0)
			for i in range(existing):
				combs[i][4] = 0
				probs[i] *= probability
		if transition.transitions[5] != -1:
			existing = len(combs)
			branch_count = self.aut_Battery.get_branch_count(state, transition.transitions[5])
			for i in range(1, branch_count):
				probability = self.aut_Battery.get_probability_value(state, transition.transitions[5], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][5] = i
					probs.append(probs[j] * probability)
			probability = self.aut_Battery.get_probability_value(state, transition.transitions[5], 0)
			for i in range(existing):
				combs[i][5] = 0
				probs[i] *= probability
		if transition.transitions[6] != -1:
			existing = len(combs)
			branch_count = self.aut_Sun.get_branch_count(state, transition.transitions[6])
			for i in range(1, branch_count):
				probability = self.aut_Sun.get_probability_value(state, transition.transitions[6], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][6] = i
					probs.append(probs[j] * probability)
			probability = self.aut_Sun.get_probability_value(state, transition.transitions[6], 0)
			for i in range(existing):
				combs[i][6] = 0
				probs[i] *= probability
		if transition.transitions[7] != -1:
			existing = len(combs)
			branch_count = self.aut_GlobalInvariant.get_branch_count(state, transition.transitions[7])
			for i in range(1, branch_count):
				probability = self.aut_GlobalInvariant.get_probability_value(state, transition.transitions[7], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][7] = i
					probs.append(probs[j] * probability)
			probability = self.aut_GlobalInvariant.get_probability_value(state, transition.transitions[7], 0)
			for i in range(existing):
				combs[i][7] = 0
				probs[i] *= probability
		if transition.transitions[8] != -1:
			existing = len(combs)
			branch_count = self.aut_GlobalSync.get_branch_count(state, transition.transitions[8])
			for i in range(1, branch_count):
				probability = self.aut_GlobalSync.get_probability_value(state, transition.transitions[8], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][8] = i
					probs.append(probs[j] * probability)
			probability = self.aut_GlobalSync.get_probability_value(state, transition.transitions[8], 0)
			for i in range(existing):
				combs[i][8] = 0
				probs[i] *= probability
		# Convert to Branch instances
		for i in range(len(combs)):
			combs[i] = Branch(probs[i], combs[i])
		# Done
		return list(filter(lambda b: b.probability > 0.0, combs))
	
	def jump(self, state: State, transition: Transition, branch: Branch, expressions: List[int] = []) -> State:
		transient = self._get_initial_transient()
		for i in range(0, 4):
			target_state = State()
			state.copy_to(target_state)
			target_transient = Transient()
			transient.copy_to(target_transient)
			if transition.transitions[0] != -1:
				self.aut_JobProvider.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self.aut_JobProvider_1.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self.aut_Job.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			if transition.transitions[3] != -1:
				self.aut_Job_1.jump(state, transient, transition.transitions[3], branch.branches[3], i, target_state, target_transient)
			if transition.transitions[4] != -1:
				self.aut_Terminate.jump(state, transient, transition.transitions[4], branch.branches[4], i, target_state, target_transient)
			if transition.transitions[5] != -1:
				self.aut_Battery.jump(state, transient, transition.transitions[5], branch.branches[5], i, target_state, target_transient)
			if transition.transitions[6] != -1:
				self.aut_Sun.jump(state, transient, transition.transitions[6], branch.branches[6], i, target_state, target_transient)
			if transition.transitions[7] != -1:
				self.aut_GlobalInvariant.jump(state, transient, transition.transitions[7], branch.branches[7], i, target_state, target_transient)
			if transition.transitions[8] != -1:
				self.aut_GlobalSync.jump(state, transient, transition.transitions[8], branch.branches[8], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)