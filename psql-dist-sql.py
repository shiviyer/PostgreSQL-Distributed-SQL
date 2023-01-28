import psycopg2
import time

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)

# Create a cursor object
cur = conn.cursor()

# Run the script in an infinite loop
while True:
    # Execute the pg_stat_activity query to retrieve the query arrival rate, service time, and wait time
    cur.execute("SELECT datname, usename, query, state, waiting, query_start, now() - query_start AS duration FROM pg_stat_activity WHERE state = 'active'")

    # Fetch the results
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print("Database: ", row[0])
        print("User: ", row[1])
        print("Query: ", row[2])
        print("State: ", row[3])
        print("Waiting: ", row[4])
        print("Start Time: ", row[5])
        print("Duration: ", row[6])
        print("-------------------")

    # Sleep for 2 seconds
    time.sleep(2)

# Close the cursor and connection
cur.close()
conn.close()
