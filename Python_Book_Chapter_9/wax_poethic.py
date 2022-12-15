"""
Challenge 9.5
Generate a poem with the following structure using words randomly selected from the word lists given:
{A/An} {adj1} {noun1}

{A/An} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
{adv1}, the {noun1} {verb2}
the {noun2} {verb3} {prep2} a {adj3} {noun3}
"""
import random

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adj = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prep = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adv = ["curiously, extravagantly", "tantalizingly", "furiously", "sensuously"]

generate_nouns = [random.choice(nouns) for i in range(0, 3)]
generate_verbs = [random.choice(verbs) for i in range(0, 3)]
generate_adj = [random.choice(adj) for i in range(0, 3)]
generate_prep = [random.choice(prep) for i in range(0,2)]
generate_adv = random.choice(adv)

vowels = ['a', 'e', 'i', 'o', 'u']

if generate_adj[0][0] in vowels:
    print(f"An {generate_adj[0]} {generate_nouns[0]}\n")
    print(f"An {generate_adj[0]} {generate_nouns[0]} {generate_verbs[0]} {generate_prep[0]} the {generate_adj[1]} "
          f"{generate_nouns[1]}")
    print(f"{generate_adv}, the {generate_nouns[0]} {generate_verbs[1]}")
    print(f"the {generate_nouns[1]} {generate_verbs[2]} {generate_prep[1]} a {generate_adj[2]} {generate_nouns[2]}")
else:
    print(f"A {generate_adj[0]} {generate_nouns[0]}\n")
    print(f"A {generate_adj[0]} {generate_nouns[0]} {generate_verbs[0]} {generate_prep[0]} the {generate_adj[1]} "
          f"{generate_nouns[1]}")
    print(f"{generate_adv}, the {generate_nouns[0]} {generate_verbs[1]}")
    print(f"the {generate_nouns[1]} {generate_verbs[2]} {generate_prep[1]} a {generate_adj[2]} {generate_nouns[2]}")


