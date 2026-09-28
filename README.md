# Weather Station

Python application that retrieves current weather measurements from the Institute of Meteorology and Water Management (IMGW) API, processes the data, and stores it in a MySQL database.

## How It Works

The application retrieves XML weather data from the IMGW API and processes measurements for stations across Poland. The processed records are stored in the `POGODA_W_POLSCE` table.

Duplicate measurements are skipped based on station ID, measurement date, and measurement hour.

The application also calculates the difference between the measured atmospheric pressure and the standard pressure of 1013.25 hPa.

## Architecture

```text
IMGW API
   ↓
Python
   ↓
XML parsing
   ↓
Data transformation
   ↓
MySQL
```

## Tech Stack

- Python
- MySQL
- Docker
- IMGW API
- XML
- Environment variables

## What I Implemented

- Retrieval of weather measurements from the IMGW API
- XML parsing and data transformation
- MySQL database integration
- Automatic table creation
- Duplicate-record prevention
- Environment-based configuration
- Basic error handling for API and database failures
- Local MySQL environment using Docker Compose

## Data Stored

For each weather station, the application stores:

- Station ID and name
- Measurement date and hour
- Temperature
- Wind speed and direction
- Relative humidity
- Precipitation
- Atmospheric pressure
- Difference from the standard pressure of 1013.25 hPa

## Setup

### 1. Clone the repository

```shell
git clone https://github.com/bkulpa/weather-station-program-operation.git
cd weather-station-program-operation
```

### 2. Create the environment file

Copy the example configuration:

```shell
cp .env.example .env
```

The default example values are ready to work with the included Docker Compose configuration.

### 3. Start MySQL with Docker

```shell
docker compose up -d
```

### 4. Install Python dependencies

```shell
pip install -r requirements.txt
```

### 5. Run the application

```shell
python createAndPopulateWeatherMeasurement.py
```

## Configuration

The application uses the following environment variables:

```text
DB_HOST
DB_USER
DB_PASSWORD
DB_DATABASE
API_URL
```

See `.env.example` for a working local-development example.

## Project Structure

```text
.
├── createAndPopulateWeatherMeasurement.py
├── services
│   ├── apiClientService.py
│   └── dbClientService.py
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```
