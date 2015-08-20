#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle

def load_pickle():
    """De-serialize dictionary using pickle."""
    fav_color = pickle.load(open("pickle-file", "rb"))
    print fav_color


def dump_pickle():
    """Serialize dictionary using pickle."""
    fav_color = {"lion": "yellow", "kitty": "black"}
    pickle.dump(fav_color, open("pickle-file", "wb"))

def main():
    load_pickle()
    dump_pickle()

if __name__ == "__main__":
    main()
