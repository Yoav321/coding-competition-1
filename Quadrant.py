"""
Finds the quadrant of a certain coordinate
Yoav Bierkatz - September 2026
"""

def main() -> None:
  x: int = int(input(""))
  y: int = int(input(""))
  if x > 0 and y > 0:
    print("1")
  elif x < 0 and y > 0:
    print("2")
  elif x < 0 and y < 0:
    print("3")
  elif x > 0 and y < 0:
    print("4")
if __name__ == "__main__":
  main()
    
