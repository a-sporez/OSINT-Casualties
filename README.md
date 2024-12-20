# OSINT Content

-Detailed comparison of Palestinian casualties reported by Btselem and Al-Qassam brigades during the events surrounding the 2008-2009 Israeli Defense Force's "Operation Cast Lead"

https://github.com/a-sporez/OSINT---Cast-Lead/blob/main/frontend_database.md

_**Credits**_

-Research: https://www.youtube.com/@lonerboxlive

-Database: https://github.com/giladfrid009

-Sorter/Maintainer: https://github.com/a-sporez

**Original table**: https://docs.google.com/spreadsheets/d/1d91sJVbpa5Lx84bXgCxPaZPABA3tYjIL/

**Bias Comparison**: https://statistics.btselem.org/en/stats/during-cast-lead/by-date-of-death?section=overall&tab=overview

### CSV to Markdown parser

This python script will convert Comma Separated Values format from Microsoft excel files and convert it to Markdown as well as produce sorted tables.
It makes the database less dense and friendly to IDE's like Obsidian as well as make the maintaining more straight forward.

You do not need to use the python sorter or know any programming to use the database.

Simply download the raw file linked above and open it with Obsidian or edit directly on Github.

https://github.com/a-sporez/OSINT---Cast-Lead/blob/main/frontend_database.md

#### To convert excel file into markdown, export from excel or download from google docs as CSV format, rename the file to "data.csv" and put in the "input" folder. Run the sorter or wait for maintainer to run the script. Copy the resulting "database.md" in "output" and replace "frontend_database.md" with it. The archived files allow anyone to do version control without logging in to Github or needing a Github account. I will automate this later but for now it is acceptable graceful handling.

Otherwise if you want to venture into the deep depth of bad life decisions this is how to use the sorter:

_Work in progress_

_**Disclaimer: Do not execute scripts on your computer without reviewing them, if you are feeling lazy use a virtual machine, otherwise ask a maintainer to sort the input for you.**_

- Clone this repository either by downloading the compressed folder or using your favorite esoteric hackerman git method.
- Export excel spreadsheet to CSV format, rename it to data.csv, and put it in the "input" folder of the repository.
- Install Python3 https://packaging.python.org/en/latest/tutorials/installing-packages/
- create and activate python3 virtual environment
  * open the folder with a terminal (right-click dropdown) and type ```python -m venv venv```
  * activate with ```venv\Scripts\activate```
  * import scv parser library with ```pip install pandas```
  * execute directly from terminal with ```python sorter.py```
  * You can also open the folder in VS Code and it will automatically create a virtual environment if you have Python3 extension installed (restart VS Code for extensions to apply).
  * Or use you favorite esoteric hackerman method
- review the output for mistakes, in VS Code you can see a preview and edit directly by clicking on cells and changing the text string
- Find a cozy spot for the front end result, perhaps a folder?

### Statistics aggregator

