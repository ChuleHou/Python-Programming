#This program displays the contents of a file
def main():
    try:
        #Open the file
        infile = open('/Users/chulehou/Desktop/randomnum.txt', 'r')
        print("List of random numbers in randomnum.txt:")
        count = 0
        for line in infile:
            num = int(line)
            count +=1
            print(num)
        print("Random number count: ", count)
        #Close the file
        infile.close
    except:
        print("An error occurred.")
#Call the main function

main()
