# Project Overview
Health Tracker allows user to do the following:

- [ ] Display current mental status like a dashboard 
- [ ] Display a calendar for choosing the date to record   
- [X] Record their daily stress level, anxiety level and depression level (mental levels) as well as the symptoms. 
- [ ] Display analysis including mental level graph vs time, statistics of symptons and mental levels.

# How to complete the project : 
The app is made of three pages.

* ## Display the status and calendar
- [ ] Add the functionality to get the status of the user, like a score and quick summary
- [ ] Add a calendar for clicking the date to enter to Recording_Info page
- [ ] Clicking a More button by the score goes to anaysis page 

* ## Record information
- [X] Add the functionality to choose mental levels, symptoms from four categories (phyiscal, whole body, sleep and cognitive)
- [X] Backend store the information into database such as mental levels and symptons that users choose
- [ ] The page can link back to main status page and link to analysis page

* ## Analysis and graphs
- [ ] Report trend like symptoms for example, most common symptons chosen.
- [ ] Display graphs showing stress level vs time, anxiety vs time and depression level vs time 
- [ ] Pie chart showing the percentages of the frequency of each category of symptons 

# Application Organization
Front End:
* Framework: Knockout, AJAX, JQuery 

Back End:
* Framework: Flask 
* File app.py contains all the backend routing and functions. 

Database:
* Sqlite connected to Flask app via sqlalchemy 
* File dataBaseSetUp.py contains database and tables setup and schema. 
