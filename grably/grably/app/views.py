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
                          date="2013-04-05 12:12:12", price=25, assigner=matt, executor="null", 
                          status="open", location='44780b6cf964a520c3331fe3')

    textbook = Tasks(task_id=2, task_title="Stat textbook", task_description = "Can you kindly bring my stat textbook from Gregory to Huntsman?",
                          date="2013-04-02 12:10:34", price=5, assigner=clara, executor=mano, status="closed",location="46f6d742f964a520f94a1fe3")


    nike = Tasks(task_id=3, task_title="Running Shoes", task_description="Please deliver some nice running shoes to Hamco",
                    date="2013-04-01 10:10:34", price=80, assigner=shek, executor=matt,status="in_progress", location="4adb6fdff964a520742721e3")


    chickenrice = Tasks(task_id=4,task_title="Food delivery",task_description="Please deliver some chicken and rice to engineering",
                date="2013-03-21 13:10:34", price=15, assigner=mano, executor="null",status="open",location="4b7c4814f964a52070892fe3")

    grocery_store.save()
    textbook.save()
    nike.save()
    chickenrice.save()

    a1 = Friends(friender_id=shek,friendee_id=mano,status="confirmed")
    a2 = Friends(friender_id=shek,friendee_id=matt,status="confirmed")
    a3 = Friends(friender_id=shek,friendee_id=clara,status="confirmed")

    a1.save()
    a2.save()
    a3.save()

    m1 = Friends(friender_id=mano,friendee_id=shek,status="confirmed")
    m2 = Friends(friender_id=mano,friendee_id=matt,status="confirmed")
    m3 = Friends(friender_id=mano,friendee_id=clara,status="confirmed")

    m1.save()
    m2.save()
    m3.save()

    c1 = Friends(friender_id=clara,friendee_id=shek,status="confirmed")
    c2 = Friends(friender_id=clara,friendee_id=matt,status="confirmed")
    c3 = Friends(friender_id=clara,friendee_id=mano,status="confirmed")

    c1.save()
    c2.save()
    c3.save()

    f1 = Friends(friender_id=matt,friendee_id=shek,status="confirmed")
    f2 = Friends(friender_id=matt,friendee_id=clara,status="confirmed")
    f3 = Friends(friender_id=matt,friendee_id=mano,status="confirmed")

    f1.save()
    f2.save()
    f3.save()











