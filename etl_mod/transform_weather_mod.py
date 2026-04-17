def transform_weather_data(hourly):

    transformed_weather_data = []

    for t in hourly:

        values = t.get("values", {})

        transformed_weather_data.append({
            "altimeterSetting":        values.get("altimeterSetting", None),
            "cloudCover":              values.get("cloudCover", None),
            "dewPoint":                values.get("dewPoint", None),
            "precipitationIntensity":  values.get("precipitationIntensity", None),
            "precipitationProbability":values.get("precipitationProbability", None),
            "precipitationType":       values.get("precipitationType", None),
            "pressureSurfaceLevel":    values.get("pressureSurfaceLevel", None),
            "relativeHumidity":        values.get("relativeHumidity", None),
            "temperature":             values.get("temperature", None),
            "windDirection":           values.get("windDirection", None),
            "windSpeed":               values.get("windSpeed", None),
            "windGust":                values.get("windGust", None),
            "windChill":               values.get("windChill", None),
            "heatIndex":               values.get("heatIndex", None),
            "uvIndex":                 values.get("uvIndex", None),
            "visibility":              values.get("visibility", None),
            "moonPhase":               values.get("moonPhase", None),
            "moonrise":                values.get("moonrise", None),
            "moonset":                 values.get("moonset", None),
            "sunrise":                 values.get("sunrise", None),
            "sunset":                  values.get("sunset", None),
            "timestamp":               t.get("time", None),
        })

    return transformed_weather_data