"""
find the velocity of a balloon
Yoav Bierkatz - September 2026
"""

def main() -> None:
  v,a,t = input().split(" ")
  v = int(v)
  a = int(a)
  t = int(t)
  print(f"{v*t + (1/2)*(a*(t**2))}")

if __name__ == "__main__":
  main()
    
