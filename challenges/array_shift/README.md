# array_shift

**Author**: Max McFarland
**Version**: 0.0.1

## Overview
This application allows for a user put a given value in the center of a given array

## Getting Started
To run this application, you first must pull off of github from this repo: https://github.com/MaxMcF/data_structures_and_algorithms
Python 3.7.0 must be installed. A virtual environment must be created to run, which is done by downloading pip and running the pipenv shell command.
Pytest must also be installed, which can be down using the command pipenv install pytest in the command line


## Architecture
This application was written in python 3.7 using VScode in a virtual environment created by pip.
This program was tested using pytest.

## API
To use this application, open the test_array_shift.py file and create a new function. In this function create a variable called expected, which should be set equal to the array you expect to be returned (with your value in the middle index). Next, make a variable called actual, which should be set equal to the function insert_shift_array(), with the array and value you want to test as the two parameters. Finally, on a new line, write assert expected == acutal. Run pytest from your command line in your pipenv. If your test was entered correctly, you should have all tests passed

## Change Log

08-14-2018 1:30pm - Began whiteboarding with group
08-14-2018 2:00pm - Finished psuedocode, began working on actual python code
08-14-2018 3:00pm - Finished working on whiteboard, began setting up environment to run challenges
08-14-2018 3:30pm - Began writing the actual logic and test
08-14-2018 4:00pm - finsihed all logic and submitted everything to gitHub

