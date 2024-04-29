README.md

Required Functionality:
Data table on the dashboard which shows an unfiltered view of the Austin Animal Center Outcomes data set sourced by the retrieve_all function
limiting the number of rows displayed, enabling pagination (advanced), enabling sorting
developing database queries that match the required filter functionality
Water Rescue
Mountain or Wilderness Rescue
Disaster or Individual Tracking
Reset (returns all widgets to their original, unfiltered state)
Radio buttons to control the filtering
dashboard widgets that receive input from the interactive options and present those dynamic updates to the client

Tools used:
MongoDB
Is a great database that offers flexible schema, scalability, high performance, rich-query language, and automatic failover.
Some of its downsides are above average memory usage, limited transactional capability, strict data integrity, limited join operations, and indexing overhead
For MongoDB and python, MongoDB has libraries available for many programming languages.  So it makes it a nice option for python being one of the most popular languages.
This class specifically probably uses MongoDB because we already took a class based on an SQL database.  So NoSQL as the next database makes sense.  MongoDB was one of the first movers in the NoSQL world and probably has a large market share.
Dash framework
Dash is a great dashboard framework for python that enables interactivity, unified environment, python based syntax, customization, and integration with other python frameworks.
Some disadvantages of using dash are performance overhead, limited deployments, version control and collaboration, dependency management, and limited frontend control.
We are probably using dash in this course because of its easy and well established use case for python dashboards.






Steps taken to complete the project:
Struggle and fight with the apporoto/linux environment to try and get the dashboard to work.  This included:
Trying to download a better IDE (visual studio code) to help with indent errors
Restarts, reloggins, various print statements, etc to try and get the dashboard to work
Try setting everything up locally instead of using the apporoto/linux environment.  Didn’t have time to get the mongodb, python, jupyter notebook, and such installed and working
Email instructor several times asking and receiving help
Once given up trying to get it to work, the next step was to build the dashboard anyway without being able to see it.
Understanding all the requirements.  Mentioned earlier in the README
Learning how to do radio button in dash
Learning which dog breeds are better for certain rescues
Creating filters for those dog breeds in the AnimalShelter class
Attaching the controllers to the radio buttons to then call the correct function in the AnimalShelter class
Try out pagination and how that will turn out in the final viewable product
Write README





Challengers:
Getting the dashboard to run in the linux/apporoto environment.
I generally did not overcome this and tried to write the dashboard anyway
Being able to write python code that wasn't getting errors from trivial things like indent errors
I sent the code to my local machine from the virtual machine to edit the indent errors and then send the code back to the virtual machine each time they appeared
