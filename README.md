# Weather Station

## Program Operation Concept

The aim of the program is to populate the `WEATHER_IN_POLAND` table with data regarding weather measurements provided by the Institute of Meteorology and Water Management (IMGW). The program is developed in Python using MySQL queries.</br>
</br>
Upon execution, the program communicates with the IMGW API, retrieves data from the moment of invocation, processes it accordingly, and then populates the database. The program's functionality has been tested on a MySQL database within a Docker environment.

## Program Execution

To execute the program, run the file `createAndPopulateWeatherMeasurement.py`.

## Installation of Necessary Libraries

To install the necessary libraries, use the command:

```shell
pip install -r requirements.txt

```

or optionally

```shell
pip3 install -r requirements.txt

```

## Environmental Variables

To configure the database connection, you should:

- Copy the .env.example file and save it as .env.
- Set the appropriate database access details.

## Tech Stack

- Python
- MySQL
- Docker
- IMGW API
- Environment variables

## Architecture

IMGW API → Python data processing → MySQL database

## What I Implemented

- API data retrieval from IMGW
- Data processing and database insertion
- MySQL integration
- Environment-based configuration
- Testing with MySQL running in Docker
