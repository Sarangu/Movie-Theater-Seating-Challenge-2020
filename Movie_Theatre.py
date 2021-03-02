import re
import argparse
import pathlib

num_of_rows = 10
num_of_columns = 20
buffer = 3
max_seats = num_of_columns * num_of_rows
avail_seats = max_seats
rows = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    
def canBeAccomodated(req_seats, occupied_seats):
    if (occupied_seats == 0):
        return True
    else:
        if ( (20 - occupied_seats) >= req_seats ):
            return True
        else:
            return False
            
def getRow(idx):
    switcher = { 
        0: "J", 
        1: "I", 
        2: "H",
        3: "G",        
        4: "F",        
        5: "E",        
        6: "D",        
        7: "C",        
        8: "B",        
        9: "A"
    } 
  
    return switcher.get(idx, "X")
    

def updateAvailableSeats(idx, req_seats):
    global avail_seats
    if rows[idx] + req_seats + buffer >= num_of_columns:
        avail_seats = avail_seats - (num_of_columns - rows[idx])
        rows[idx] = num_of_columns
    else:    
        rows[idx] = rows[idx] + req_seats + buffer
        avail_seats = avail_seats - (req_seats + buffer)
        
        
def breakAndAccomodate(req_seats):
    seat_list = []
    current_req_seats = req_seats
    
    for idx, val in enumerate(rows):
        remaining_seats = num_of_columns - val
        row_name = getRow(idx)
        if (remaining_seats > 0):
            if (current_req_seats <= remaining_seats):
                for i in range(val+1, current_req_seats + val + 1):
                    seat_list.append("{row_name}{seat_no}".format(row_name=row_name, seat_no=i))
                
                updateAvailableSeats(idx, current_req_seats)
            
            else:
                for i in range(val+1, remaining_seats + val + 1):
                    seat_list.append("{row_name}{seat_no}".format(row_name=row_name, seat_no=i))
                
                updateAvailableSeats(idx, remaining_seats)
                current_req_seats = current_req_seats - remaining_seats
                
        if (current_req_seats == 0):
            break
            
    return seat_list
    
def fill(req_seats):
    seat_list = [ ]
    
    while True:
        if (req_seats > num_of_columns):
            current_req_seats = num_of_columns
        else:
            current_req_seats = req_seats
            
        accomodated = False
        
        for idx, val in enumerate(rows):
            if (canBeAccomodated(current_req_seats, val)):
                accomodated = True
                row_name = getRow(idx)
                for i in range(val+1, current_req_seats + val + 1):
                    seat_list.append("{row_name}{seat_no}".format(row_name=row_name, seat_no=i))
                
                updateAvailableSeats(idx, current_req_seats)
                
                break
                
        if (accomodated == False):
            seat_list = seat_list + breakAndAccomodate(current_req_seats)
                
        if (req_seats <= num_of_columns):
            break
        else:
            req_seats -= current_req_seats
            
    return seat_list
            



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='input', required=True, help='Full path to the input file')
    args = parser.parse_args()
    
    try:
        input_file = open(args.input, 'r')
        output_file_name = args.input.replace('.txt', '_output.txt')
        output_file = open(output_file_name, 'w')
        
        requests = input_file.readlines()
        
        for request in requests:
            request_split = request.strip().split()
            res_id = request_split[0]
            req_seats = int(request_split[1])
            
            output_file.write(("{res_id} ".format(res_id = res_id)).rstrip('\n'))
            if (avail_seats == 0):
                output_file.write("Seats full!".rstrip('\n'))
                break
            elif (req_seats > avail_seats):
                output_file.write("Not enough seats available".rstrip('\n'))
            else:
                seat_list = fill(req_seats)
                for idx, seat in enumerate(seat_list):
                    if (idx == 0):
                        output_file.write(("{seat}".format(seat = seat)).rstrip('\n'))
                    else:
                        output_file.write((", {seat}".format(seat = seat)).rstrip('\n'))
            
            output_file.write('\n')
        
        print("Output saved to: {output_file}".format(output_file = output_file_name))
            
    except FileNotFoundError as err:
        print(err) 