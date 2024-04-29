# function that adds time to specified time 
# and returns the time in a string including dayes later parmeter
# time of day(AM\PM) and optinal day parmeter
def add_time(time, add, w_day=None):
    # time - the current time
    # add - a string of time including only hours and minuts --ex: 123:40

    # splits the input strings to parmeters
    time, day_time = time.split(' ')
    h_add, m_add = add.split(':')
    h_time, m_time = time.split(':')

    # chack if minuts input bigger then 60
    if int(m_add) > 60 or int(m_time) > 60:
        return 'INPUT EROR'
    
    # adds the time 
    r_h = int(h_time) + int(h_add)
    r_m = int(m_time) + int(m_add)
    
    # if the hours are eqale more the 24 hours incramnts the day parmeter
    day1 = 0
    r = r_h
    while r > 24:
        day1 += 1
        r -= 24
    # if the minuts are eqale more the 60 incramnts the hour parmeter
    hour = 0
    r2 = r_m
    while r > 24:
        hour += 1
        r2 -= 60
    r += hour

    # chacks the time of day to the ans
    if len(str(r2)) < 2:
        r2 = '0' + str(r2)
    if r > 24:
        pp = 'PM'
    else:
        pp = 'AM'
    r = r%12
    
    # res == the resolt string
    # adds to the resolt the day if specifaid
    res = f'{r}:{r2} {pp}'
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' ]
    if w_day in days:
        the_day = days.index(w_day)
        the_day += day1
        res += f', {days[the_day]}'
    days_later = None
    
    if day1 == 1:
        days_later = '(next day)'
    elif day1 > 1:
        days_later = f'({day1} days later)'
    if days_later is not None:     
        res += f' {days_later}'

    return res


    



def main():
    print(add_time('3:00 PM', '12:00', 'Sunday'))

if __name__=='__main__':
    main()