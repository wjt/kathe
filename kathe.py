#!/usr/bin/env python
# vim: set fileencoding=utf-8
from __future__ import print_function
import codecs
import itertools
import os.path

def scan(f, alphabet, normalise, forbid_repetition=True):
    # TODO: Garuda's songs weren't written in alphabetical order
    assert alphabet == u''.join(sorted(alphabet))

    for word in itertools.imap(unicode.strip, f):
        chars = sorted(map(lambda c: normalise.get(c, c), word))

        if chars[0] < alphabet[0] or chars[-1] > alphabet[-1]:
            yield (None, word)
        elif forbid_repetition and len(set(chars)) != len(chars):
            yield (None, word)
        else:
            i = alphabet.index(chars[-1])
            yield (i, word)

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

def main():
    alphabet = u'αβγδεζηθικλμνξοπρστυφχψω'
    garuda_songs = u'αβδεγηζθ'
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
        scanner = scan(f, alphabet, normalise, forbid_repetition=False)
        write(scanner, alphabet, directory='alphabet-with-duplicates')

if __name__ == '__main__':
    main()
