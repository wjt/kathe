κάθε
----

This script partitions a word list into lists of words which can be spelled
using only progressively-larger leading subsets of the alphabet. For example,
consider a list of English words and the Roman alphabet
(*abcdefghijklmnopqrstuvwxyz*). This script would find words that can be
spelled using only *a*, then only *ab*, then only *abc* (such as "cab"), then
only *abcd* ("ad", "bad", "cad"), then only *abcde* ("ace", "aced", "bed",
"bead"), and so on.

Why?
----

My band, [Garuda][], names [its songs][bc] using letters from the Greek
alphabet, roughly in order. So, this script can be used to find Greek words you
could spell with our song titles as we use each new letter of the Greek
alphabet. I then [tweet][kathegaruda] these words using [Adam Parrish's
Everyword Bot][ew]. Perhaps one day we'll play a set that spells out a
meaningful word!

[garuda]: https://twitter.com/garudacbg
[bc]: http://garudacbg.bandcamp.com/
[kathegaruda]: https://twitter.com/kathegaruda
[ew]: https://github.com/aparrish/everywordbot

Okay, this sounds great, but where do I get the word list?
----------------------------------------------------------

I used a Greek word list published by [the elspell project][elspell]. It is not
included here because it is enormous.

[elspell]: http://elspell.math.upatras.gr/

License
-------

This program is provided under the MIT license. See `LICENSE.md` for more
information.
