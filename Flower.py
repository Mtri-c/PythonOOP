print("Miles, 10-30-2024. This code is describing a flower lifecycle")
class Flower:
    def __init__(self, name):
        self.name = name

    def grow(self):
        print("The " +self.name + " is growing.")

    def bloom(self):
        print("The " + self.name + " is blooming.")

def main():
    flower1 = Flower("Rose")
    flower1.grow()
    flower1.bloom()
    flower2 = Flower("Daisy")
    flower2.grow()
    flower2.bloom()
    flower3 = Flower("Sunflower")
    flower3.grow()
    flower3.bloom()
    
    

if __name__ == "__main__":
  main()