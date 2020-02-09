**Restaurant Searching API**
----
  API allows searching restaurants
 
* **Method:**
   
  `GET /restaurants/search` - Search restaurants based on three parameters
  
  `GET /` - List all the restaurants
  
* **Data Params**
    - _q_: query string. Full or partial match for the string is searched from _name_, _description_ and _tags_ fields. A minimum length for the query string is one character.
    - _lat_: latitude coordinate (customer's location)
    - _lon_ : longitude coordinate (customer's location)
    
    Example:

    `/restaurants/search?q=sushi&lat=60.1704,,5&lon=24.93147`

  
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ "matched_restaurants": a list of matched restaurants(objects)}`

* **Error Response:**

  * **Code:** 400 <br />
  
* **How to Run**

    Unzip the project zip file somewhere you want, then
    
        cd restaurants_search
        pip install -r requirements.txt
        # or
        pip3 install -r requirements.txt

	1.run in a development mode
	    
        export FLASK_ENV=development
        flask run
        
    2.or run in a production mode
   
        uwsgi app.ini 
   
    3.Also deploy to: 
    http://qianqianq.pythonanywhere.com/

    Example:
    
    http://qianqianq.pythonanywhere.com/restaurants/search?q=sushi&lat=60.17045&lon=24.93147
    
 

