# 获取天气数据的模块
import requests

# 用于城市code转换的字典
CITY_CODE = {
    "北京": "110000",
    "上海": "310000",
    "广州": "440100",
    "深圳": "440300",
    "杭州": "330100",
    "南京": "320100",
    "成都": "510100",
    "重庆": "500000",
    # 可以继续添加更多城市和对应的代码
}

# 转化城市名称为城市代码的函数
def get_city_code(city_name):
    return CITY_CODE.get(city_name, None)

# 获取天气数据的函数
def get_weather(city, extensions="base"):
    # 使用requests库获取天气数据-返还json格式的数据
    city_code_value = get_city_code(city)
    if not city_code_value:
        raise ValueError("城市代码未找到")
    weather_api_url = f"https://restapi.amap.com/v3/weather/weatherInfo?key=889f83713bf96b006f1b57d78c53771e&city={city_code_value}&extensions={extensions}"
    response = requests.get(weather_api_url)
    print(f"请求URL: {weather_api_url}")
    return response.json()

# 格式化返还的天气json数据的函数
def format_weather_data(weather_json):
    if weather_json.get("status") != "1":
        raise ValueError("天气数据获取失败")
    lives = weather_json.get("lives", [])
    if not lives:
        raise ValueError("没有天气数据")
    live = lives[0]
    formatted_data = {
        "城市": live.get("city"),
        "天气": live.get("weather"),
        "温度": live.get("temperature"),
        "风向": live.get("winddirection"),
        "风力": live.get("windpower"),
        "湿度": live.get("humidity"),
    }
    return formatted_data

def main():
    city = input("请输入城市名称：")
    try:
        weather_data = get_weather(city)
        formatted_data = format_weather_data(weather_data)
        print(f"{formatted_data['城市']}的天气：{formatted_data['天气']}，温度：{formatted_data['温度']}℃，风力：{formatted_data['风力']}级，湿度：{formatted_data['湿度']}%")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
