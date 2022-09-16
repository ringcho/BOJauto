def solution(fees, records):
    def cal_time(in_time,out_time):
        hour_in, minute_in = map(int, in_time.split(':'))
        hour_out, minute_out = map(int, out_time.split(':'))
        stay_time = hour_out*60 + minute_out - hour_in*60 - minute_in
        return stay_time
    def cal_fee(stay_time):
        if stay_time <= basic_time:
            return basic_fee
        else:
            add_time = (stay_time-basic_time)/time_per
            if add_time > int(add_time):
                add_time = int(add_time) + 1
            add_fee = add_time*(fee_per)
            return basic_fee + add_fee
    answer = []
    
    basic_time = fees[0]
    basic_fee = fees[1]
    time_per = fees[2]
    fee_per = fees[3]
    
    parking = {}
    stay_time = {}
    for record in records:
        time, number, in_out = record.split()
        if in_out == 'IN':
            parking[number] = time
        elif in_out == 'OUT':
            if number in stay_time:
                stay_time[number] += cal_time(parking[number],time)
            else:
                stay_time[number] = cal_time(parking[number],time)
            del(parking[number])
    for number in parking:
        if number in stay_time:
            stay_time[number] += cal_time(parking[number],'23:59')
        else:
            stay_time[number] = cal_time(parking[number],'23:59')
    s = sorted(stay_time)
    print(s)
    for car in s:
        answer.append(cal_fee(stay_time[car]))

    return answer