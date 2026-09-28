from dotenv import load_dotenv

import services.apiClientService as api_client_service
import services.dbClientService as db_client_service

load_dotenv()


def parse_measurement(measurement):
    """Convert one IMGW XML measurement into values ready for MySQL."""
    pressure = measurement.find("cisnienie").text

    pressure_difference = 1013.25 - float(pressure) if pressure else None

    return [
        measurement.find("id_stacji").text,
        measurement.find("stacja").text,
        measurement.find("data_pomiaru").text,
        measurement.find("godzina_pomiaru").text,
        measurement.find("temperatura").text,
        measurement.find("predkosc_wiatru").text,
        measurement.find("kierunek_wiatru").text,
        measurement.find("wilgotnosc_wzgledna").text,
        measurement.find("suma_opadu").text,
        pressure,
        pressure_difference,
    ]


CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS POGODA_W_POLSCE (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_stacji INT,
    stacja VARCHAR(255),
    data_pomiaru DATE,
    godzina_pomiaru VARCHAR(10),
    temperatura FLOAT,
    predkosc_wiatru FLOAT,
    kierunek_wiatru INT,
    wilgotnosc_wzgledna FLOAT,
    suma_opadu FLOAT,
    cisnienie FLOAT,
    roznica_cisnien FLOAT
);
"""

INSERT_QUERY = """
INSERT INTO POGODA_W_POLSCE (
    id_stacji,
    stacja,
    data_pomiaru,
    godzina_pomiaru,
    temperatura,
    predkosc_wiatru,
    kierunek_wiatru,
    wilgotnosc_wzgledna,
    suma_opadu,
    cisnienie,
    roznica_cisnien
)
SELECT * FROM (
    SELECT
        %s AS id_stacji,
        %s AS stacja,
        %s AS data_pomiaru,
        %s AS godzina_pomiaru,
        %s AS temperatura,
        %s AS predkosc_wiatru,
        %s AS kierunek_wiatru,
        %s AS wilgotnosc_wzgledna,
        %s AS suma_opadu,
        %s AS cisnienie,
        %s AS roznica_cisnien
) AS tmp
WHERE NOT EXISTS (
    SELECT 1
    FROM POGODA_W_POLSCE
    WHERE
        id_stacji = tmp.id_stacji
        AND data_pomiaru = tmp.data_pomiaru
        AND godzina_pomiaru = tmp.godzina_pomiaru
);
"""


def main():
    database = db_client_service.get_database_instance()

    if database is None:
        return

    cursor = None

    try:
        cursor = database.cursor()
        cursor.execute(CREATE_TABLE_QUERY)

        measurements = api_client_service.get_and_parse_xml_data(
            "/data/synop/format/xml"
        )

        for measurement in measurements:
            try:
                cursor.execute(INSERT_QUERY, parse_measurement(measurement))
            except Exception as error:
                print(f"Error while processing measurement: {error}")

        database.commit()

    except Exception as error:
        print(f"Application error: {error}")

        if database.is_connected():
            database.rollback()

    finally:
        if cursor is not None:
            cursor.close()

        if database.is_connected():
            database.close()


if __name__ == "__main__":
    main()
