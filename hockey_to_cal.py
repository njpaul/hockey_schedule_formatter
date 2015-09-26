#!/usr/bin/python3

import csv
import sys
import datetime as dt

team_name = sys.argv[1]
csv_name = sys.argv[2]

with open(csv_name, newline='') as infile:
    infields = ["Game #", "Day", "Date", "Time", "Location", "Away Team", "Home Team"]
    outfields = ["Subject", "Start Date", "Start Time", "End Date", "End Time",
                 "All Day Event", "Description", "Location", "Private"]
    reader = csv.DictReader(infile, fieldnames=infields)
    writer = csv.DictWriter(sys.stdout, fieldnames=outfields)
    writer.writeheader()

    for row in reader:
        away = row["Away Team"]
        home = row["Home Team"]

        if team_name != away and team_name != home:
            continue

        start_date = dt.datetime.strptime(row["Date"], "%m/%d/%Y")
        start_time = dt.datetime.strptime(row["Time"], "%I:%M%p")
        duration = dt.timedelta(minutes=90)
        end_date = start_date + duration
        end_time = start_time + duration
        
        if team_name == away:
            desc = "{} at {}".format(team_name, home)
        else:
            desc = "{} vs {}".format(team_name, away)

        outrow = {}
        outrow["Subject"] = "Hockey - {}".format(team_name)
        outrow["Start Date"] = start_date.strftime("%m/%d/%Y")
        outrow["Start Time"] = start_time.strftime("%I:%M %p")
        outrow["End Date"] = end_date.strftime("%m/%d/%Y")
        outrow["End Time"] = end_time.strftime("%I:%M %p")
        outrow["All Day Event"] = "False"
        outrow["Description"] = desc
        outrow["Location"] = row["Location"]
        outrow["Private"] = "False"
        writer.writerow(outrow)

