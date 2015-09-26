# hockey_schedule_formatter
Format my hockey schedule into CSV format for Google Calendar

## Instructions
1. Export the league schedule into a CSV file
2. Strip the first line of the CSV file to get rid of misc header junk
3. Run `./hockey_schedule_formatter "<team name>" <csv file> > <team name>.csv`
4. Create a temporary Google calendar
5. Import the CSV into this calendar
6. Export the temporary calendar to iCal
7. Delete the temporary calendar
