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

    1.Deployed to: http://qianqianq.pythonanywhere.com/, and you can visit it directly 

    Example:
    
    http://qianqianq.pythonanywhere.com/restaurants/search?q=sushi&lat=60.17045&lon=24.93147
    
    2.Run from the source code 
    
    unzip the project zip file somewhere you want, then
        
        cd restaurants_search
        # in your virtual environment (>=python3.5)
        pip install -r requirements.txt
        # or maybe you need
        pip3 install -r requirements.txt
        
    run in a development mode
        
        export FLASK_ENV=development
        python app.py
        # or
        python3 app.py
    
    or run in a production mode
   
        uwsgi app.ini 
    
    Then visit http://localhost:5000/
    
    Example:
    
    http://localhost:5000/restaurants/search?q=sushi&lat=60.17045&lon=24.93147
   
    