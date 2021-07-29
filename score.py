def cal_score(details):
    points=0
    runs=details[1]
    balls_faced=details[2]
    fours=details[3]
    sixes=details[4]
    balls_bowled=details[5]
    maidens=details[6]
    runs_given=details[7]
    wkts=details[8]
    catches=details[9]
    stumping=details[10]
    RO=details[11]
    points+=runs
    points+=catches*6
    points+=stumping*8
    points+=RO*6
    if runs>50:
        points+=2
    if runs>100:
        points+=4
    if balls_faced!=0:
        strike_rate=(runs/balls_faced)*100
        if (strike_rate>=80) and (strike_rate<=100):
            points+=2
        elif strike_rate >100:
            points+=4
        elif strike_rate<40:
            points-=4
        elif strike_rate<60:
            points-=2
    points+=fours*1
    points+=sixes*2
    points+=wkts*25
    if wkts>=3:
        points+=8
    if wkts>=5:
        points+=15
    points+=maidens*8
    overs=balls_bowled/6
    if overs!=0:
        er=runs_given/overs
        if er<=2:
            points+=12
        elif (er>2) and (er<=3.5):
            points+=7
        elif (er>3.5) and (er<=4.5):
            points+=4
        elif er>9:
            points-=3
            
    return points

    

