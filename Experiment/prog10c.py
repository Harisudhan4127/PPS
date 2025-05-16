def main():
    try:
        mark=int(input("Enter your mark : "))
        if mark>=35 and mark<101:
            print("Pass and your mark is valid")
        else:
            print("Fail and your mark is valid")
    except ValueError: 
        print("Mark must be avalid number") 
    except IOError:
        print("Enter correct valid mark")
    except:
        print("An error occurred") 
main()
