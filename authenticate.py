# authenticate with name,passcode not empty and passcode matching
def authenticate(yourname,yourpass):
    if yourname:  # display blocks below if yourname is not empty
        if yourpass:  # display blocks below if yourpass is not empty
            if yourpass == -1730865266111383083: # -396666076534335015:display blocks below if yourpass is not equal to hashed code
                return 'authenticated'
            else:
                return "<div>Enter <span class='highlight blue'>matching passcode</span></div>"
        else:
            return "<div>Enter <span class='highlight red'>passcode</span></div>"
    else:
        return "<div>Enter <span class='highlight blue'>your name</span></div>"
