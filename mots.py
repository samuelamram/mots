from random import choice, seed
import multiprocessing as mp
import argparse

WORD_PATTERNS = {
                    # Basic word shapes
                    'W': ('CDF', 'CVnAX', 'CVnAU', 'CVnAT', 'CVMT', 'CDMU', 'CVMU', 'IVMT', 'ECT', 'CVZX', ),
                    # Prefixes
                    'I': ('in', 'ad', 'con', 'des', 'mal', 'pour', 'sous', ),
                    # V Prefixes
                    'E': ('entre', 're', ),
                    # Ends of words
                    'T': ('VF', ),
                    # Medial consonants
                    'M': ('l', 'll', 't', 'ss', 'n', 'm', ),
                    # Affixes
                    'U': ('eur', 'ien', 'ant', 'esse', 'ent', 'able', 'oir', 'eau', 'aire', 'erie', 'e', 'er', 'ir', 'ain', 'age', 'ule', 'on', 'ade', ),
                    # Consonants
                    'C': ('b', 'c', 'ch', 'd', 'f', 'g', 'j', 'l', 'm', 'n', 'p', 'qu', 'r', 's', 't', 'v', 'sP', 'Rr', 'Ll', ),
                    # Finals
                    'F': ('c', 'f', 'gne', 'm', 'n', 'nt', 'p', 'r', 'sse', 't', 's', 'l', ),
                    # Other finals
                    'Z': ('c', 'f', 'gn', 'm', 'n', 'nt', 'p', 'r', 't', 's', 'l', ),
                    # Finals after nasals
                    'A': ('c', 'p', 's', 't', ),
                    # Voiceless stops
                    'P': ('p', 't', ),
                    # Voiced stops
                    'Q': ('b', 'd', 'g', ),
                    # Can be next to L
                    'L': ('b', 'f', 'p', 'c', ),
                    # Can be next to R
                    'R': ('P', 'Q', 'f', ),
                    # Simple vowels
                    'V': ('a', 'e', 'i', 'o', 'u', ),
                    # Diphthongs
                    'D': ('au', 'ai', 'oi', 'ou', 'ie', 'eau', 'oeu', ),
                    # Final vowels or diphthongs
                    'X': ('ee', 'e', 'ou', 'ie', 'eau', 'oi', )
                }

def mot(phonemes):
    """
    Recursive algorithm to generate a pseudo-french word
    """
    if phonemes.islower() or phonemes == '':
        return phonemes
    else:
        return mot(choice(WORD_PATTERNS.get(phonemes[0], (phonemes[0],)))) + mot(phonemes[1:])

def liste_de_mots(nombre):
    l = []
    for i in range(nombre):
        word_pattern = choice(WORD_PATTERNS['W'])
        l.append('{0}: {1}'.format(word_pattern, mot(word_pattern).capitalize()))
    return l

def main(num):
  
  pool = mp.Pool(mp.cpu_count())
  result = pool.map(liste_de_mots, [num//mp.cpu_count() for i in range(mp.cpu_count())])

  return result


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='A simple pseudo-french word generator')
    parser.add_argument('num', type=int, help='the number of words to generate')

    args = parser.parse_args()

    seed()
    l = main(args.num)
    for i in l:
        print(f'{i}')
