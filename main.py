from MarkovChain import MarkovChain


if __name__ == "__main__":
    mc = MarkovChain()
    mc.add_state(("Hello", "world"), "Hello")
    mc.add_state(("Hello", "world"), "Hello")
    mc.add_state(("world,", "hello"), "Universe")
    mc.add_state(("world,", "hello"), "Pincopallino")
    mc.add_state(("hello", "universe!"), "\n")

    print(mc.states)