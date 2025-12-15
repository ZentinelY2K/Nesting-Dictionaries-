
robot_config = {
    # Main Dictionary Key: Category
    "motors": {
        # Nested Dictionary Keys: Settings for the category
        "left_wheel": {"pin": 10, "speed": 150},
        "right_wheel": {"pin": 11, "speed": 150}
    },
    "sensors": {
        "proximity": {"type": "ultrasonic", "port": "A1"},
        "camera": {"resolution": "1080p", "fps": 30}
    }
}
print(robot_config['motors']['right_wheel']['speed']) #should be 150
#List inside fictionaries
user_profile = {
    "username": "Lol123",
    "level": "Intermediate",
    "skills": ["Python", "Java", "WebDev", "Cybersecurity"], # <-- The list is here
    "last_login": "2025-12-10"
}
user_skills = user_profile['skills'][1]
print(user_skills)
upd = user_profile['skills'][1] = "updated"
print(upd)
print(user_profile['skills'])
#Dictionaries inside a list
sensor_readings = [
    # Item 0 (a dictionary)
    {"sensor_id": "P-45", "time": "14:00:01", "pressure": 10.2},
    # Item 1 (a dictionary)
    {"sensor_id": "T-12", "time": "14:00:02", "temperature": 28.5},
    # Item 2 (a dictionary)
    {"sensor_id": "P-45", "time": "14:00:03", "pressure": 10.1}
]
get_pressure_third = sensor_readings[2]['pressure'] + 1

print(get_pressure_third)
