from flask import Flask, app
from colorama import Fore

app = Flask(__name__) # create a flask app instance

def start_server(): # func to start the fake server - from your video lol
    print(f"{Fore.RESET}[{Fore.CYAN}*{Fore.RESET}] Starting fake server...") # log the server start

    @app.route("/check") # route to handle license check
    def check(): # check keys func
        return "works" # always return valid license response

    app.run(port=1337) # run the Flask app on localhost:1337
