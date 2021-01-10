import readdata
userdf = readdata.read_user()

# authenticate with name,passcode not empty and passcode matching
def authenticate(yourname, yourpass):
    if yourname:  # display blocks below if yourname is not empty
        if yourpass:  # display blocks below if yourpass is not empty
            if userdf[userdf.name == yourname].pswd.values == yourpass:
            # if yourpass == 'MIT@123': #display blocks below if yourpass is not equal to hashed code
                return 'authenticated'
            else:
                return "<div>Enter <span class='highlight blue'>matching name/passcode</span></div>"
        else:
            return "<div>Enter <span class='highlight red'>passcode</span></div>"
    else:
        return "<div>Enter <span class='highlight blue'>your name</span></div>"
