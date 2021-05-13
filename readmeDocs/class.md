Create super User and log in to see what the admin site looks like
Shut server back down and start creating a class


makemigrations
migrate
Use shell to add animals

python3 manage.py shell
zooApp.models import *

Animals.objects.create(enter key value here)

To Read in Shell
Animals.objects.all()

View in Admin panel
exit shell
start server

notice there is no difference
shut server down
register class

admin.py = from .models import Animals
admin.site.register(Animals)

Now restart server and view. 