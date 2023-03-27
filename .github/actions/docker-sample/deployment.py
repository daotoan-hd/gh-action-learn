import os
import mimetypes

def run():
    print(os.environ)
    who_to_greet = os.environ['INPUT_WHO-TO-GREET']
    

if __name__ == '__main__':
    run()
