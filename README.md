This project contains the instructions to run the dashboard for the rocket.


The Data Visualization has three parts:
1. The python script that listens for data from a socket and streams the data to the DB
2. The InfluxDB, a metric Database good with streaming data
3. The Grafana, a visualization tool that connects to the InfluxDB and displays the data in the desired format


To get things started you need to:
1. Download Grafana - download the installer from https://grafana.com/grafana/download?platform=windows and run it
   1. Add the custom.ini file from the grafana folder in this project into the C:\Program Files\GrafanaLabs\grafana\conf\ folder on your computer
2. Install InfluxDB - run the following commands in order:
   ```batch
   wget https://dl.influxdata.com/influxdb/releases/influxdb2-2.7.7-windows.zip -UseBasicParsing -OutFile influxdb2-2.7.7-windows.zip
   Expand-Archive .\influxdb2-2.7.7-windows.zip -DestinationPath 'C:\Program Files\InfluxData\influxdb\'
   ```


To get things running you need to:
1. Run InflexDB
   1. Run the influxd.exe in a CMD or powershell
      1. Located at C:\Program Files\InfluxData\influxdb\
   2. Go to http://localhost:8086/ 
   3. Create and remember your username and password
   4. Enter the API Tokens page under the Load Data
   5. Create a token with privileges to do everything
2. Run Grafana
   1. Run the grafana-server.exe in a CMD or PowerShell **As Administrator**
      1. Located at C:\Program Files\GrafanaLabs\grafana\bin\
   2. Go to http://localhost:3000/ 
   3. Create username and password 
   4. Connect the InfluxDB as a DataSource 
      1. Pictures in the grafana folder 
      2. Use the token generated in step 1.v.
      3. Click "Save & Test" to validate the connection
   5. Import the dashboard file from the grafana folder to create a new dashboard
   6. Edit time range to view Last 15 minutes
3. Run the listener 
   1. Update the token in the listen.py file to the token generated in step 1.v.
   2. Run as a normal python file (works with python3.6 should work for all python3)
4. Generate data and watch everything work 
   1. Use the generate_fake_data.py to validate everything