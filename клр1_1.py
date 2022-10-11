def main():
    
    s=input()
    
    n=s.split()
    s1=n[::-1]
    s1=" ".join(s1)
    
    print(s1.capitalize())
            
if __name__ == "__main__":
    main()
