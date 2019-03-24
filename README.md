Hosted here: https://sushmitachaudhari.github.io/TechTrio/

Our website proposes different routes for the user to walk to their destination. We take into account the different locations along the itinerary, the time of the day and the crime statistics in these locations in order to evaluate the safety of different route options, and propose the safest route.

Github Link: https://github.com/sushmitachaudhari/TechTrio

How To Use It:
Choose the origin and destination. After your input, the app shows different routes on the map to reach from the source to destination. Each path is colored differently. Please use the key on the top-right to see what each color means. After that scroll down to see more details about the routes. Be Safe :)

Analysis
For the analysis part, first we parse a the Analyze Boston crime database and retrieve all criminal activity that occurred near the path at a similar time in the day. The path is then scored according to how dense the criminal activity is along the way of the specific path.

Results
Results are then overlayed onto Google's Maps Javascript API, allowing the user to see the routes with the estimated time of travel and total distance, color-coded according to their safety rating.
