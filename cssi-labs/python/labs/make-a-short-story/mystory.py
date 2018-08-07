story = '''Once there was a {0} who was poor, but who had a {1} {2}. Now it happened that he had to go and {3} to the king.'''

noun1 = raw_input("add a singular noun1")
adj = raw_input("add a plural adjective1")
noun2 = raw_input("add a singular noun2")
vrb = raw_input("add a present tense verb1")

print(story.format(noun1, adj, noun2, vrb))
