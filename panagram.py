def panagram(x):
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in x:
            return False
    return True

def main():
    print "Enter a string "
    x=raw_input()
    true=panagram(x)
    print  true        


if __name__ == '__main__':
    main()

