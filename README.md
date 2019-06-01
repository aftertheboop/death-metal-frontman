# death-metal-frontman

A twitter bot that introduces a new, randomly generated death metal song every hour.
Follow *@dethmetalsinger* on Twitter

## Description

The bot takes an input of song titles, in this case (most of) the discographies of 
notable death metal bands, Cannibal Corpse, The Black Dahlia Murder, Hate and Bloodbath
(also my old band, because why not), chops up the titles preserving a few joiners for
coherence and then creates a whole new song title.

The bot additionally pulls a random song intro line just for a bit of flavour.

## Requirements

* Python
* Tweepy

## Use

1. Run `pip install` to install requirements
2. Run `python nextsong.py` to generate a new song and include it in a phrase