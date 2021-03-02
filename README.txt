Problem Statement:
To implement an algorithm for assigning seats within a movie theater to fulfill reservation requests. 

Seating Capacity of the hall:
The movie theater has the seating arrangement of 10 rows x 20 seats

Input format:
Text file that contains one line of input for each reservation request. 
The order of the lines in the file reflects the order in which the reservation requests were received. 
Each line in the file will be comprised of a reservation identifier, followed by a space, and then the number of seats requested.

Example:
R001 2
R002 4
R003 4
R004 3

Output format:
Each row in the file includes the reservation number followed by a space, and then a comma-delimited list of the assigned seats.

Example:
R001 J1, J2
R002 J6, J7, J8, J9
R003 J13, J14, J15, J16
R004 I1, I2, I3


Constraints/Goals to satisfy:
1. Maximum customer satisfaction
2. Maximum customer safety

Assumptions made:
1. In order to maximize customer satisfaction, we assume that a customer is happiest when seated as far away from the screen as possible, i.e., Row 'J' would be the most satisfactory, and Row 'A' would be least satisfactory.
2. In order to ensure/maximize customer safety, there  is a buffer of 3 seats left between every unique reservation request.
3. Allocation of seats starts from the left end and progressively moves towards the right. It is assumed that within a single row, all seats are equally satisfactory.
4. There is no limit on the number of seats that can be booked under a single reservation, as long as it is within the capacity of the hall. 
5. Reservation is made on a First-come First-serve (FCFS) basis, and customers with early reservations will be more satisfied than those with later reservations. 
6. Regardless of reservation time, a buffer of 3 seats is always maintained for safety purposes.
7. Customers value satisfaction in this order:
        Seated together at the best seats > Seated together in any seats > Seated separately > No booking > Partial booking (only part of the reservations are made).
Thus, the last situation (partial booking) is avoided at all costs.
8. If there are still seats available and there are two reservations, first with required seats > Remaining seats and second with required seats <= Remaining seats, the earlier reservation is bypassed and later reservation is made.


Approach and implementation details:
1. Algorithm uses Greedy approach to maximize customer satisfaction and safety
2. An array of size 10 (number of rows in the hall) is used to keep track of the number of seats occupied per row (including buffer) until that reservation point.
3. Total number of available seats (initially 200) are updated reguarly, as reservations are made
4. Program terminates once maximum capapcity is reached or input file is completely read and all reservations are made.
5. Reservations are made either continously (if possible) or split to accommodate customers in the remaining seats.

Scope for improvement:
1. Instead of allocating seats on a FCFS basis, the program can use a threshold for each reservation to maximize Customer Satisfaction to a greater extent. Reservations with greater number of people should be given more priority than small bookings, so that number of satisfied people are more.

Running the program:
1. Open Command prompt or terminal.
2. Move into the directory where the program is stored.
3. Type the following command: python greedySeatAllocation.py --input *full_path_to_input_file*
4. The full path to the output file is displayed in the terminal. The naming convention is : "input_file_path\"+"_"+output.txt