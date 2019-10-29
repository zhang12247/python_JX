import textwrap

if __name__ == "__main__":
    s = "THE prairie lay that afternoon as it had lain for centuries of September afternoons, vast as an ocean; motionless as an ocean coaxed into very little ripples by languid breezes; silent as an ocean where only very little waves slip back into their element. One might have walked for hours without hearing anything louder than high white clouds casting shadows over the distances, or the tall slough grass bending lazily into waves. One might have gone on startled only by the falling of scarlet swamp-lily seeds, by sudden goldfinches, or the scratching of young prairie chickens in the shorter grasses. For years now not even a baby buffalo had called to its mother in those stretches, or an old "
    print(textwrap.fill(s, 70))
    print(textwrap.fill(s, 40))
    print(textwrap.fill(s, 40, initial_indent=" "))
    print(textwrap.fill(s, 40, subsequent_indent=" "))
