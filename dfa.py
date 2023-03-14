from pythomata import SimpleDFA
import os

alphabet = {"a", "b", "c"}
states = {"s1", "s2", "s3", "s4"}
initial_state = "s1"
accepting_states = {"s3", "s4"}
transition_function = {
    "s1": {
        "b" : "s1",
        "a" : "s2"
    },
    "s2": {
        "a" : "s2",
        "b" : "s1",
        "c" : "s3",
    },
    "s3":{
        "c" : "s3",
        "b" : "s4"
    },
    "s4":{
        "c" : "s4"
    }
}
dfa = SimpleDFA(states, alphabet, initial_state, accepting_states, transition_function)

graph = dfa.to_graphviz()
graph.render("path_to_file")
os.startfile("path_to_file.svg")