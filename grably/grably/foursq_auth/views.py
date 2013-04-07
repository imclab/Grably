import urllib
import urllib2
import json

from django.http import *
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.db.models import Q
from django.http import HttpResponseRedirect

from app.models import *
from foursq_auth.models import *

CLIENT_ID = 'DCRBNKLOZCARX3SR3QEA1HTQMW4KUYZZGRHCAABO5SUDLVRI'
CLIENT_SECRET = '2RHBQCXC2VF1UUSWZTDBYIAJ5VOKJ2OLVZP0JDS5NKY4K4GP'

request_token_url = 'https://foursquare.com/oauth2/authenticate'
access_token_url = 'https://foursquare.com/oauth2/access_token'
redirect_url = 'http://127.0.0.1:8000/foursq_auth/callback'

def main( request ):
    if request.session.get('access_token'):
        return HttpResponseRedirect('done')
    else:
        return render_to_response( 'foursq_auth/login.html' )

def callback( request ):
    # get the code returned from foursquare
    code = request.GET.get('code')

    # build the url to request the access_token
    params = { 'client_id' : CLIENT_ID,
               'client_secret' : CLIENT_SECRET,
               'grant_type' : 'authorization_code',
               'redirect_uri' : redirect_url,
               'code' : code}
    data = urllib.urlencode( params )
    req = urllib2.Request( access_token_url, data )

    # request the access_token
    response = urllib2.urlopen( req )
    access_token = json.loads( response.read( ) )
    access_token = access_token['access_token']

    # store the access_token for later use
    request.session['access_token'] = access_token

    # redirect the user to show we're done
    return HttpResponseRedirect(reverse( 'oauth_done' ) )

def unauth( request ):
    # clear any tokens and logout
    request.session.clear( )
    logout( request )
    return HttpResponseRedirect( reverse( 'main' ) )

def auth( request ):
    # build the url to request
    params = {'client_id' : CLIENT_ID,
            'response_type' : 'code',
            'redirect_uri' : redirect_url }
    data = urllib.urlencode( params )
    # redirect the user to the url to confirm access for the app
    return HttpResponseRedirect( '%s?%s' % ( request_token_url, data  ) )

def done( request ):
    # get the access_token
    access_token = request.session.get('access_token')

    # request user details from foursquare
    params = { 'oauth_token' : access_token }
    data = urllib.urlencode( params )
    url = 'https://api.foursquare.com/v2/users/self'
    full_url = url + '?' + data
    print full_url
    response = urllib2.urlopen( full_url )
    response = response.read( )
    user = json.loads( response )['response']['user']
    name = user['firstName']
    user_id = user['id']
    username = Grabber(username=user_id)
    username.save()
    # show the page with the user's name to show they've logged in
    return render_to_response( 'foursq_auth/done.html', { 'name' : name } )

def get_auth(request):
    if request.is_ajax():
        access_token = request.session.get('access_token')
        return HttpResponse(access_token)
    else:
        return HttpResponse(0)

def create_checkin(request):
    if request.is_ajax():
        access_token = request.session.get('access_token')
        venue = request.POST['id']
        url= 'https://api.foursquare.com/v2/checkins/add'
        values = {
            'oauth_token' : access_token,
            'venueId' : venue,
        }
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        tasks = Tasks.objects.filter(location = venue).values()
        return HttpResponse(json.dumps(tasks))
    else:
        return HttpResponse("Did not work")

def create_task(request):
    if request.is_ajax():
        venue = request.POST['venue']
        title = request.POST['title']
        description = request.POST['description']
        task_id = request.POST['id']
        price = request.POST['price']
        params = { 'oauth_token' : access_token }
        data = urllib.urlencode( params )
        url = 'https://api.foursquare.com/v2/users/self'
        full_url = url + '?' + data
        response = urllib2.urlopen( full_url )
        response = response.read( )
        user = json.loads( response )['response']['user']
        user_id = user['id']
        assigner = Grabber.objects.get(username = user_id)
        if task_id == "empty":
            new_task = Tasks(task_id = task_id, task_title = title,
                             task_description=description, price = price,
                             assigner = assigner, status = "Open",
                             location = venue)
            new_task.save()
        else:
            new_task = Tasks.objects.get(task_id = task_id)
            new_task.update(task_title = title, task_description=description,
                            price = price, location = venue)
            new_task.save()
        tasks = Tasks.objects.filter(assigner = user_id).values()
        return HttpResponse(json.dumps(tasks))
    else:
        return HttpResponse("Error")

def accept_task(request):
    if request.is_ajax():
        task_id = request.POST['task_id']
        access_token = request.session.get('access_token')
        tasks = Tasks.objects.get(task_id = task_id)
        #gets user info from api
        params = { 'oauth_token' : access_token }
        data = urllib.urlencode( params )
        url = 'https://api.foursquare.com/v2/users/self'
        full_url = url + '?' + data
        response = urllib2.urlopen( full_url )
        response = response.read( )
        user = json.loads( response )['response']['user']
        user_id = user['id']
        executor = Grabber.objects.get(user_id = user_id)
        tasks.update(executer = executor, status="Pending")
        tasks.save()
        return HttpResponse("Success")
    else:
        return HttpResponse("")

def delete_task(request):
    if request_is_ajax():
        task_id = request.POST['task_id']
        tasks = Tasks.objects.get(task_id=task_id)
        tasks.delete()
        return HttpResponse("")

def finish_task(request):
    if request.is_ajax():
        #CHANGE STATUS OF TASK AND MAKE THE VENMO CALL HERE
        return HttpResponse("")
    else:
        return HttpResponse("")

def edit_form (request):
    return render_to_response( 'foursq_auth/checkin.html' )
