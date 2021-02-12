from datetime import datetime

def get_server_side_cookie(request, cookie, default_val=None):
    """Return the value of requested cookie"""
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    """Update visitors count."""
    # Get the number of visits to the site, 1 if doesn't exist
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    # If it's been longer then time_to_update (day by default)
    if (datetime.now() - last_visit_time).days > 0:
        print(last_visit_time)

        visits += 1
        # Update the last visit cookie now that we have updated the count
        request.session['last_visit'] = str(datetime.now())
    else:
        # Set the last visit cookie
        request.session['last_visit'] = last_visit_cookie
        
    # Update/set the visits cookie
    request.session['visits'] = visits

