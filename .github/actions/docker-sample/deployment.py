import os
import mimetypes

def run():
    # print(os.environ)
    who_to_greet = os.environ['INPUT_WHO-TO-GREET']
    print("Welcome {}!".format(who_to_greet))
    os.system("output=\"This is sample output\" >> $GITHUB_OUTPUT")
    

if __name__ == '__main__':
    run()
