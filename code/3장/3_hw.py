# Create a dictionary to store sensor information
# 센서 정보를 저장하는 딕셔너리 생성

sensors = {
    'dht11': {  # First sensor
        # 첫 번째 센서
        'temperature': 23,      # Temperature value / 온도 값
        'humidity': 47,         # Humidity value / 습도 값
        'unit': 'celsius'       # Temperature unit / 온도 단위
    },
    'bh1750': {  # Second sensor
        # 두 번째 센서
        'illuminance': 450,     # Light intensity / 조도 값
        'unit': 'lux'           # Unit of measurement / 측정 단위
    }
}

# Print the dictionary
# 딕셔너리 출력
print(sensors)
