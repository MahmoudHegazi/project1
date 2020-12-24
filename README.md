# project1
# Fyyur-Artist-Booking-Site

#### Udacity-First-Project

# programming languages and libraries:
Python3, JavaScript, SQL, jinja2, SQLalchemy,  Relational Database: PostgreSQL

# front-end
HTML5, CSS3, W3.css, JavaScript, ES6, AJAX, grid, flexbox

# Database and connection:
1. ```code app.secret_key = 'S&Djry636qyye21777346%%^&&&#^$^^y___' ```
2. 2 tables Band, Event


# packeges:
1. flask
3. flask_sqlalchemy
4. datetime
5. requests
6. os
7. sys
8. sqlalchemy
9. text
10. string



# What You Need To Start:
1. you have to download virtualbox and vagrant install them and start your server
2. if you are using Linux/Mac, escap this step, else Download GitBash for Windows Users
3. Clone the project, unzip it, run vagrant init, vagrant up, and vagrant ssh
4. make sure to use pip3 and python3, and install all packges 



# app Routes:
```python
@app.route('/search_ajax', methods=['POST'])

@app.route('/golden_arrow', methods=['GET'])

@app.route('/event/<int:event_id>', methods=['GET','POST'])

@app.route('/edit_band/<int:band_id>', methods=['GET','POST'])

@app.route('/submit_edit', methods=['POST'])

@app.route('/edit_event/<int:event_id>', methods=['GET','POST'])

@app.route('/submit_edit/event', methods=['POST'])

@app.route('/band/<int:band_id>', methods=['GET','POST'])

@app.route('/remove_band/<int:band_id>', methods=['GET','POST'])

@app.route('/remove_event/<int:event_id>', methods=['GET','POST'])

@app.route('/bandlist', methods=['GET','POST'])

@app.route('/band_list/page/<int:request_start>', methods=['GET','POST'])

@app.route('/event_list/page/<int:request_start>', methods=['GET','POST'])

@app.route('/home')

@app.route('/')

@app.route('/addevent', methods=['GET', 'POST'])

@app.route('/add_band', methods=['GET','POST'])

```
