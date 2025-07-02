# run.py

import hupper
from weather_app import main

if __name__ == "__main__":
    reloader = hupper.start_reloader('run.main')
    main()

