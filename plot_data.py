import argparse
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from load.database import ViewerDataBase


# This file is to prove that data has been injected
# I created a script which draw a plot with the temperatures of any state
if __name__ == "__main__":
    terminal_parser = argparse.ArgumentParser()
    terminal_parser.add_argument(
        '--state',
        '-s',
        required=True,
        nargs=1,
        help='State to get the data about the min and max temperatures between'
             + ' 1990 and 2000',
        type=str)
    args = terminal_parser.parse_args()
    arg_state = args.state[0]
    with ViewerDataBase() as db:
        result_query = db.query_data_state(arg_state)
    if result_query:
        max_temps = [data['max'] for data in result_query]
        min_temps = [data['min'] for data in result_query]
        dates = [data['date'] for data in result_query]
        all_values = max_temps + min_temps

        plt.title(
            "{0} daily max and min temperatures between 1990-2000".format(
                arg_state
            )
        )
        plt.xlabel("Date")
        plt.ylabel("Temperature")
        plt.plot(dates, max_temps, color='red')
        plt.plot(dates, min_temps, color='blue')
        red_legend = mpatches.Patch(color='red', label='max')
        blue_legend = mpatches.Patch(color='blue', label='min')
        plt.legend(handles=[red_legend, blue_legend])
        plt.axhline(0, color='grey')
        plt.show()

        # http://www.developintelligence.com/blog/2017/08/plotting-climate-data-matplotlib-python/
        # https://matplotlib.org/users/legend_guide.html
