import pendulum
from lab_01.app import get_wu_forecast_hourly, str_format_wu
from lab_01.helper import LineNotify
from config import LINE_ACCESS_TOKEN

FORECAST_STEPS = 3

if __name__ == "__main__":
    linenotify = LineNotify(LINE_ACCESS_TOKEN=LINE_ACCESS_TOKEN)
    datetime_now = pendulum.now("Asia/Bangkok").to_datetime_string()
    data_forecast = get_wu_forecast_hourly(forecast_steps=FORECAST_STEPS)

    str_forecast = str_format_wu(data_forecast)
    str_forecast = "\n".join(str_forecast)

    noti_text = f"""
        NOW: {datetime_now}

        FORECAST:{str_forecast}    
    """

    linenotify.line_text(noti_text)