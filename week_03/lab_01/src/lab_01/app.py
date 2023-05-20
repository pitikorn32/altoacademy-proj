import requests
import pendulum

from config import URL_WU_FORECAST


def get_wu_forecast_hourly(forecast_steps: int = 3):
    assert 1 <= forecast_steps <= 24, " `forecast_steps` must between 1 and 24"

    res = requests.get(URL_WU_FORECAST)
    data = res.json()

    forecast_list = []
    for i in range(forecast_steps):
        forecast_list.append(
            {
                "datetime": pendulum.parse(
                    data["validTimeLocal"][i]
                ).to_datetime_string(),
                "status": data["wxPhraseLong"][i],
                "uv_status": data["uvDescription"][i],
                "temperature": data["temperature"][i],
            }
        )

    return forecast_list


def str_format_wu(forecast_list: list):
    all_text = []
    for e in forecast_list:
        temp_text = f"""
        datetime: {e['datetime']}
        status: {e['status']}
        uv_status: {e['uv_status']}
        temperature: {e['temperature']} F
        """
        all_text.append(temp_text)
    return all_text
