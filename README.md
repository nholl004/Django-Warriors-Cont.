# cs180project-022-django-data-warriors
cs180project-022-django-data-warriors created by GitHub Classroom
***We did not do regression testing or Continuous Integration.***

**Instructions:**
The link provided by Django gives a step by step instruction of how to install the necessary components for Django.
[Django Install Instructions](https://docs.djangoproject.com/en/3.2/topics/install/)

**Necessary Technologies: python, Django, Javascript, Html, CSS** 

For more information, he has a YouTube video link that provides a visual description on how to install Django. (Sections 3 and 4 goes over the necessary installations)
[Youtube Visual Refrence](https://youtu.be/F5mRW0jo-U4?t=302) 

**Source Code:** 
The UML diagram below displays the key components of our webpage.

**Templates:**
This holds our html for each webpage url. Within our html we are able to access the static file that holds our css as well as img (images) we may want to implement.
**initClass:**
initClass is where the classes initList and initTop10 are created to reduce globals and prevent “smelly code”. initList is where we store the data from the database into memory. initTop10 is used for our views Top10 request function to store the many values explained later.


**Urls:**
Urls.py is used to direct the path of each URL to each views request functions.

**viewsFunction:**
viewsFunction is a python file we used to carry all our external functions that will be utilized from all of our views request functions. 

**Views:**
Django has a file system that uses the python file views to obtain the user requests. Due to this, ‘views’ has access to our initClass and viewsFunctions. Each request returns data directly to the html so it can be displayed. 

**The views Request functions consists of:**
To start, we have our daily stats by month, which measures the growth rate of that month while displaying the data in that month to give a better visual. (it's based off selection it shows Confirms, deaths, and recoveries) 
	
Next we have Top 10s, this gives a visual representation of the top 10 confirms, deaths, and recoveries by displaying the data upon a graph. For more information on the data, you can look beside the graph to see a table of the data. To see how much of an impact these top 10s have we provide an impact rate vs the total of all the top states or provinces globally.

Then we have our 1v1 comparison, where we get the highest values of two specific cities or provinces and compare their confirms, deaths, and recoveries by displaying a visual graph representation of it.	

Confirm to death analytic feature is a calculation based on a specific date input. Given the day, month, and year, as well as the Province or state, it will go to that specific date, gather the confirmed and death case numbers and divide with confirmed over death. This will create the death ratio for the analytic.

Peak days is more specifically, an analytic that finds the peak rate of change between each day and records the date where that rate of change occurs. Peak days are implemented by creating a separate sub data structure that only contains the corresponding state and country. Then the output will say the number of cases and the date to when peak rate occurred.
