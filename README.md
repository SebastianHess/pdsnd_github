## Project: Explore US Bikeshare Data
**Creation Date:**	Saturday, 5th December 2020

Hello! Let's explore some US bikeshare data! :bike:


### Project Data

**Contributors:** Sebastian Hess

**Tags:** bikes, share

**Requires:** Your attention & brain

**Tested up to:** 369.000 brain cells


### Description

In this project, you will make use of Python to explore data related to bike share systems for three major cities in the United States — Chicago, New York City, and Washington. You will write code to import the data and answer interesting questions about it by computing descriptive statistics. You will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

#### The Datasets

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

>* Start Time (e.g., 2017-01-01 00:07:57)
>* End Time (e.g., 2017-01-01 00:20:53)
>* Trip Duration (in seconds - e.g., 776)
>* Start Station (e.g., Broadway & Barry Ave)
>* End Station (e.g., Sedgwick St & North Ave)
>* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

>* Gender
>* Birth Year

#### Statistics Computed

You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:

1. Popular times of travel (i.e., occurs most often in the start time)

* most common month
* most common day of week
* most common hour of day

2. Popular stations and trip

* most common start station
* most common end station
* most common trip from start to end (i.e., most frequent combination of start station and end station)

3. Trip duration

* total travel time
* average travel time

4. User info

* counts of each user type
* counts of each gender (only available for NYC and Chicago)
* earliest, most recent, most common year of birth (only available for NYC and Chicago)

#### Code Quality

Criteria | Meets Specifications
------------ | -------------
Functionality of code | All code cells can be run without error.
Choice of data types and structures | Appropriate data types (e.g. strings, floats) and data structures (e.g. lists, dictionaries) are chosen to carry out the required analysis tasks.
Use of loops and conditional statements | Loops and conditional statements are used to process the data correctly.
Use of packages | Packages are used to carry out advanced tasks.
Use of functions | Functions are used to reduce repetitive code.
Use of good coding practices | Docstrings, comments, and variable names enable readability of the code.

#### Script And Questions

Criteria | Meets Specifications
------------ | -------------
Solicit and handle raw user input | Raw input is solicited and handled correctly to guide the interactive question-answering experience; no errors are thrown when unexpected input is entered.
Use descriptive statistics to answer questions about the data. Raw data is displayed upon request by the user. | Descriptive statistics are correctly computed and used to answer the questions posed about the data. Raw data is displayed upon request by the user in this manner: Script should prompt the user if they want to see 5 lines of raw data, display that data if the answer is 'yes', and continue these prompts and displays until the user says 'no'.

### Software needed

To complete this project, the following software requirements apply:

> You should have Python 3, NumPy, and pandas installed using Anaconda
> A text editor, like Sublime or Atom.
> A terminal application (Terminal on Mac and Linux or Cygwin on Windows).

### Installation Instructions
Run the bikeshare.py file within your terminal witch "python 3 bikeshare.py"

### Files used

* *chicago.csv*
* *new_york_city.csv*
* *washington.csv*

### Copyright and licensing information
:copyright: Sebastian Hess

### Credits
It's important to give proper credit. Add links to any repo that inspired you or blogposts you consulted.

1. [Udacity Knowledge](https://knowledge.udacity.com/questions/193900 "link1")

2. [Mastering Markdown](https://guides.github.com/features/mastering-markdown/ "link2")

3. [About READMEs](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/about-readmes "link3")

### Update Log
* **Update 1 - 05.12.2020:** docs: Update README.md with Project Infos
* **Update 2 - 08.12.2020:** docs: Include "Update Log" in README.md
* **Update 3 - 08.12.2020:** ddocs: Include "Installation Instructions" in README.md