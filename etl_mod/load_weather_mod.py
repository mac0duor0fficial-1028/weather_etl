import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

def load_weather_data(transformed_weather_data):
    conn = psycopg2.connect(
        dbname= DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    cursor = conn.cursor()

    insert_query = '''
    INSERT INTO weather_schema.weather_measurements_data(
        altimeter_Setting, cloud_Cover, dew_Point, precipitation_Intensity, precipitation_Probability,
        precipitation_Type, pressure_SurfaceLevel, relative_Humidity, temperature, wind_Direction,
        wind_Speed, wind_Gust, wind_Chill, heat_Index, uv_Index, visibility, moon_Phase, moonrise,
        moonset, sunrise, sunset, timestamp
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    columns_for_insertion = [
        "altimeterSetting", "cloudCover", "dewPoint", "precipitationIntensity", "precipitationProbability",
        "precipitationType", "pressureSurfaceLevel", "relativeHumidity", "temperature", "windDirection",
        "windSpeed", "windGust", "windChill", "heatIndex", "uvIndex", "visibility",
        "moonPhase", "moonrise", "moonset", "sunrise", "sunset", "timestamp"
    ]

    data_to_insert = []

    for row_dict in transformed_weather_data:

        row_values = []

        for col_key in columns_for_insertion:
            row_values.append(row_dict.get(col_key))

        data_to_insert.append(tuple(row_values))


    cursor.executemany(insert_query, data_to_insert)
    conn.commit()

    cursor.close()
    conn.close()