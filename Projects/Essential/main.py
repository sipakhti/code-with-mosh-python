import requests
# from io import BytesIO
# from PIL import Image

# r = requests.get("https://www.itl.cat/pngfile/big/81-811691_3d-name-wallpapers-hd-desktop-background-epic-pc.jpg")
# stars = requests.get("http://www.aljanh.net/data/archive/img/1293170889.jpeg")
# airport = requests.get("https://effigis.com/wp-content/uploads/2015/02/Airbus_Pleiades_50cm_8bit_RGB_Yogyakarta.jpg")
# print("Status:",r.status_code)

# img = Image.open(BytesIO(airport.content))


# print(img.size,img.format,img.mode,img)
# path = f"airport.{img.format}"
# try:
#     img.save(path), img.format
# except IOError:
#     print("File not saved")
my_data = {"name":"Umer","email":"Umer@example.com"}
r = requests.post("https://tryphp.w3schools.com/showphp.php?filename=demo_form_post",my_data)
print(r.status_code)
print(r.headers)
with open("myfile.html","w+") as f_obj:
    f_obj.write(r.text)
