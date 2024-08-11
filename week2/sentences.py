import random

def main():
    print(make_sentence(1,'past'))
    print(make_sentence(1,'present'))
    print(make_sentence(1,'future'))
    print(make_sentence(2,'past'))
    print(make_sentence(2,'present'))
    print(make_sentence(2,'future'))
    
def make_sentence(quantity, tense):
    return str.capitalize(f"{get_determiner(quantity)} {get_noun(quantity)} {get_verb(quantity, tense)} {get_adverb()} {get_prepositional_phrase(quantity)} {get_prepositional_phrase(quantity)}")

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
            words = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    else:
            words = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]
    word = random.choice(words)
    return word
    
def get_verb(quantity, tense):
    if tense == 'past':
         verbs = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    elif tense == 'present' and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"] 
    elif tense == 'present' and quantity != 1:
         verbs =["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    elif tense == 'future':
         verbs = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
    
    verbs = random.choice(verbs)
    return verbs

def get_preposition():
    prepositions = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition


def get_prepositional_phrase(quantity):
    return (f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)} {get_adjetive()}")

def get_adjetive():
     adjetives = ["happy","sad","angry","excited","tired","energetic","beautiful","ugly","smart","brave","strong"]
     adjetive = random.choice(adjetives)
     return adjetive

def get_adverb():
    adverbs = ["quickly","slowly","carefully","loudly","quietly","well","badly","easily","hard","softly","suddenly","always","never","sometimes","often","rarely","soon","late","early","now","here","there","everywhere","nowhere","upstairs","downstairs","inside","outside","almost","really"]
    adverb = random.choice(adverbs)
    return adverb

main()



