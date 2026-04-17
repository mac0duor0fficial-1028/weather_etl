from etl_mod.extract_weather_mod import get_weather_data
from etl_mod.transform_weather_mod import transform_weather_data
from etl_mod.load_weather_mod import load_weather_data

def run_weather_pipeline():
    try:
        hourly = get_weather_data()

        if not hourly:
            print("No data extracted — check API key or network connection")
            return

        transformed_weather_data = transform_weather_data(hourly)

        if not transformed_weather_data:
            print("No data after transformation")
            return

        load_weather_data(transformed_weather_data)

        print("Weather ETL pipeline completed successfully")

    except Exception as e:
        print(f"Weather ETL pipeline failed: {e}")
