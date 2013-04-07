from app.models import *
# Create your views here.
def populate_db(request):
    matt = Grabber(username="mbuech", venmo_key="null")
    clara = Grabber(username="clara", venmo_key="null")
    mano = Grabber(username="mano", venmo_key="null")
    shek = Grabber(username="shek", venmo_key="null")
    matt.save()
    clara.save()
    mano.save()
    shek.save()
    grocery_store = Tasks(task_id=1, task_title="Grocery Store", task_description="Grab an enlightened protein popsickle.",
                          date="2013-04-05 12:12:12", price=5, assigner=matt, executor="null", status="open", location=


