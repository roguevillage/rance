`rance` PassSentence Generator
================================

Overview
--------
  
  The passSentence generator `rance` uses lists of words separated by parts of speech to generate random English sentences. In the spirit of [diceware](http://world.std.com/~reinhold/diceware.html), `rance` trades total randomness for a more memorable structure. Rather than a string of random words, `rance` provides an even more memorabe structure--a random sentence--with comparable levels of entropy.

Motivation
----------
  
  [Password strength](https://en.wikipedia.org/wiki/Password_strength) is derived from randomness (entropy). The strongest, shortest-length passwords are random collections of letters, numbers, and symbols. Completely random strings are notoriously difficult for humans to remember, which is why many studies have shown that people [reuse](http://www.dphu.org/uploads/attachements/books/books_3522_0.pdf) [bad passwords](https://www.tandfonline.com/doi/abs/10.1080/01449290903121386) even though they understand what good passwords are. 
  There are benefits and drawbacks to all password management strategies. Even [expert-recommended](http://www.ra.ethz.ch/cdstore/www2005/docs/p471.pdf) strategies like password managers require the user to remember *at least one* "master password" that unlocks all other passwords--which means that the security of *everything* is riding on the strength of that one password. That is where strong, easily memorizable pass sentences come in.
  This work is similar to Aaron Bassett's [pass phrase](https://github.com/aaronbassett/Pass-phrase) generator, though ours provides additional structures, parts of speech, entropy analysis, and a secure memory option.
  
Security
--------

Our security comes from the number of combinations of sentences it is possible to make using our structures and word lists. Random choices are made using Python's built-in secure [secrets](https://docs.python.org/3/library/secrets.html) library. You can find the structures in `Structures.py` and the wordlists in `Wordlists.py` (individual lists are included as `.txt` files), as well as test functions in `rance_secmem.py` and `rance.py` that calculate the bits of entropy for each. There are auxiliary lists in the parts of speech folders. Thanks to [Desi Quintans](http://www.desiquintans.com/nounlist) and [Ashley Bovan](http://www.ashley-bovan.co.uk/words/partsofspeech.html) for their lists. 

`rance` has three password strength settings: basic, extra, and cryptographic.

* Basic Strength (~44 bits entropy): This option provides a fairly strong passphrase for basic online accounts (the number of bits famously used in the diceware [xkcd](https://xkcd.com/936/) comic).

* Extra Strength (~77 bits entropy): This option provides a very strong passphrase for more sensitive accounts.

* Cryptographic Strength (~128 bits entropy): This option provides an extremely strong passphrase with enough entropy to protect [standard cryptographic key material](https://en.wikipedia.org/wiki/Brute-force_attack#Theoretical_limits). Good for use as a master password, or for safeguarding PGP or disk encryption keys.

Using the Generator
-------------------

[Secure memory handling](https://www.sjoerdlangkemper.nl/2016/06/09/clearing-memory-in-python/) in Python is non-trivial. The secure memory version of `rance` employs [SecureString](https://github.com/dnet/pysecstr) to clear your passphrase from memory after it has been generated. If you intend to use the generator for passphrases, we highly recommend the secure memory version. For extra sensitive matters, we recommend using physical randomness (like dice) to choose structures and words from the list without running `rance`.

Secure Memory Version (on the command line): 

    pip install SecureString

Then you can run `rance_secmem.py` however you would normally execute a Python file: open and run it in idle, or execute it from the command line using `./rance_secmem.py`.

Non-Secure Version:

For those using the random sentence generator recreationally, there is a version `rance.py` that does not require any additional installations. As with the secure version, you can run this however you would normally run a `.py` file.

Editing for Sense
------------------

Because our lists are not curated perfectly and we do not use machine learning algorithms, the sentences generated are often grammatically incorrect (for example nouns and verb conjugations disagree, nouns are improperly plural or singular, etc.). We separate the ways you can change the sentences into **DO**s (which will not affect the strength of your password) and **DO NOT**s (which *will* affect the strength of your password, and should be avoided).

Please *DO*:

* Change grammar

* Change, add, or remove punctuation

* Change, add, or remove capitalization

* Add words


Please *DO NOT*:

* Change or remove words

* Change sentence structure


Examples
--------

Basic Strength:

    dead dishwasher decide.
    edited version: Dead dishwashers decide.
    
    fit sensuously.
    edited version: It fits sensuously!

Extra Strength:

    inside the somewhere, soap negotiate.
    edited version: Inside the somewhere, soaps negotiate.
    
    within the convert, unity protect.
    edited version: Within the convert, unity protects.
    
Cryptographic Strength:

    who remote lecture, before bottle and poultry decay round the jellyfish?
    edited version: Who will remote lecture, before bottles and poultry decay round the jellyfish?
    
    uneven  asterisk slide down, if driving button strip seasonally and iridescently.
    edited version: Uneven asterisks slide down if the driving button is stripped seasonally and iridescently.