from MarkovChain import MarkovChain
from PoetryGenerator import PoetryGenerator

if __name__ == "__main__":
    #mc = MarkovChain()
    #mc.add_state(("Hello", "world"), "Hello")
    #mc.add_state(("Hello", "world"), "Hello")
    #mc.add_state(("world,", "hello"), "Universe")
    #mc.add_state(("world,", "hello"), "Pincopallino")
    #mc.add_state(("hello", "universe!"), "\n")
    #print(mc.states)

    #for _ in range(0, 5):
    #   print(mc.get_state(("world,", "hello")))

    pg = PoetryGenerator(3, 50)
    pg.train("poems.txt")
    pg.generate()
