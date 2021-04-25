# flask-forms
Exercise for familiarization with HTML forms in Flask.

The goal of the exercise was to render a simple HTML form using Flask and to be able to receive and handle the data coming from that form using a "request" object
from the Flask module.

The home route provides a simple form with two fields, one for the user's email and another one for the user's password.

![image](https://user-images.githubusercontent.com/55893421/115976488-a7fe1700-a53c-11eb-8e84-5d8bcfb473d2.png)

The user can then just input his/her data:

![image](https://user-images.githubusercontent.com/55893421/115976507-c6641280-a53c-11eb-8d3d-26f4fec1390e.png)

Then click on the "ok" button.

Once the button is clicked, the data from the two fields is sent to the server through the url generated in the "action" attribute of the form.

![image](https://user-images.githubusercontent.com/55893421/115976543-075c2700-a53d-11eb-9cd9-bfe7b9f33328.png)

This attribute is therefore tied to the route function named "login()" located inside our server.
Once this function is reached, we can into the data received from the form via the "request" object imported from the Flask module.
We tap in the data per se by using the "form" attribute of the object and the value of the HTML "name" attribute we provided in the form.
![image](https://user-images.githubusercontent.com/55893421/115976589-80f41500-a53d-11eb-83f9-f4568d94a52b.png)

Once the data is extracted, it is sent to be rendered into an f-string as an h1 element back to the screen.

![image](https://user-images.githubusercontent.com/55893421/115976607-9bc68980-a53d-11eb-875e-3c52157e2204.png)

The comments in the code provide a bit more details.

To run this program, simply run the "main.py" file and have a "templates" directory ready with the HTML file in the same project.
