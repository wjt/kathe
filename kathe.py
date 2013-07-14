#!/usr/bin/env python
# vim: set fileencoding=utf-8
from __future__ import print_function
import codecs
import itertools
import os.path
import collections
import argparse

def scan(f, alphabet, normalise, allow_repetition=False):
    alphabet_set = set(alphabet)
    alphabet_indices = list(enumerate(alphabet))
    alphabet_indices.reverse()

    for word in itertools.imap(unicode.strip, f):
        chars = set(map(lambda c: normalise.get(c, c), word))

        if not chars <= alphabet_set:
            yield (None, word)
        elif not allow_repetition and len(chars) != len(word):
            yield (None, word)
        else:
            for i, a in alphabet_indices:
                if a in chars:
                    yield (i, word)
                    break

def count(scanner, alphabet):
    n = len(alphabet)
    ks = [0] * n
    skipped = 0

    for i, word in scanner:
        if i is None:
            skipped += 1
        else:
            ks[i] += 1

    for i, k in enumerate(ks):
        print("%s: %d" % (alphabet[i], k))

    print("skipped: %d" % skipped)

def write(scanner, alphabet, directory='.'):
    fs = []
    skipped_filename = os.path.join(directory, 'skipped.txt')
    skipped = codecs.open(skipped_filename, 'w', 'utf-8')

    for i, letter in enumerate(alphabet):
        filename = os.path.join(directory, '%02d-%s.txt' % (i, letter))
        fs.append(codecs.open(filename, 'w', 'utf-8'))

    for i, word in scanner:
        if i is None:
            print(word, file=skipped)
        else:
            print(word, file=fs[i])

    skipped.close()
    for f in fs:
        f.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''Partitions a word list into lists of words which can be
                       spelled using only progressively-larger leading subsets
                       of the alphabet.''',
        epilog='''By default, the size of each partition will be printed, but
                  nothing will be saved.''')
    parser.add_argument('-s', '--save', metavar='DIRECTORY',
                        help='save partitioned word lists to DIRECTORY')
    parser.add_argument('-r', '--allow-repetition', action='store_true',
                        help='''allow a letter of the alphabet to be used more
                                than once in a word''')
    args = parser.parse_args()

    alphabet = u'αβγδεζηθικλμνξοπρστυφχψω'
    garuda_songs = u'αβδεγηζθικλμνξοπρστυφχψω'
    normalise = {
        # tonos and dialytika
        u'ά': u'α',
        u'έ': u'ε',
        u'ή': u'η',
        u'ί': u'ι',
        u'ΰ': u'υ',
        u'ϊ': u'ι',
        u'ϋ': u'υ',
        u'ό': u'ο',
        u'ύ': u'υ',
        u'ώ': u'ω',

        # final sigma
        u'ς': u'σ',
    }

    wordlist = 'el.wl.iso-8859-7'
    encoding = 'iso-8859-7'

    with codecs.open(wordlist, mode='r', encoding=encoding) as f:
        scanner = scan(f, garuda_songs, normalise, allow_repetition=args.allow_repetition)

        if args.save is not None:
            write(scanner, garuda_songs, directory=args.save)
        else:
            count(scanner, garuda_songs)
