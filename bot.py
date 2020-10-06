from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os, time
import random

# Definir parametros
usuario = "User"
contrasena = "Password"

followers  = []

driver = webdriver.Chrome(executable_path=os.getcwd() + "/chromedriver.exe" )

driver.get("https://www.instagram.com/")
time.sleep(random.uniform(6.0, 10.0))

username = driver.find_element_by_name("username")
username.clear()
username.send_keys(usuario)

password = driver.find_element_by_name("password")
password.clear()
password.send_keys(contrasena)

# Bonton ingresar
print("Se está iniciando sesión")
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
time.sleep(random.uniform(4.0, 6.0))

# Boton no recordar información
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(random.uniform(4.0, 6.0))

# Boton no activar notificaciones
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
time.sleep(random.uniform(4.0, 6.0))

# ir al perfil
print("Yendo al perfil: " + usuario)
driver.get("https://www.instagram.com/" + usuario + "/")
time.sleep(random.uniform(4.0, 6.0))

# href seguidores click
print("Observando los seguidores...")
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
time.sleep(random.uniform(4.0, 6.0))

#Scroll followers
scr1 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')

# Get scroll height
last_height = driver.execute_script("return arguments[0].scrollHeight", scr1)

while True:
    # Scroll down to bottom
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)

    # Wait to load page
    time.sleep(random.uniform(3.0, 4.0))

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return arguments[0].scrollHeight", scr1)
    if new_height == last_height:
        break
    last_height = new_height

print("Procesando los seguidores...")
followers_elements = driver.find_elements_by_class_name('wo9IH')
index = 1
for follower in followers_elements:
    user_name   = follower.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li['+ str(index) +']/div/div[1]/div[2]/div[1]/span/a').text
    followers.append(user_name)
    index += 1

# Cerrar seguidores popup windows
print("Fin del procesamiento de seguidores...")
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
time.sleep(random.uniform(2.0, 3.0))



# href seguidos click
print("Observando a los que sigo...")
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
time.sleep(random.uniform(4.0, 6.0))

#Scroll following
scr2 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')

# Get scroll height
last_height = driver.execute_script("return arguments[0].scrollHeight", scr2)

while True:
    # Scroll down to bottom
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr2)

    # Wait to load page
    time.sleep(random.uniform(3.0, 4.0))

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return arguments[0].scrollHeight", scr2)
    if new_height == last_height:
        break
    last_height = new_height


following_elements = driver.find_elements_by_class_name('wo9IH')
index = 1
print("Comienza la eliminación de las personas que no me siguen...")
for following in following_elements:
    user_name   = following.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li['+ str(index) +']/div/div[1]/div[2]/div[1]/span/a').text
    if not user_name in followers:
        # click en siguiendo
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li['+ str(index)+']/div/div[2]/button').click()
        time.sleep(random.uniform(1.0, 1.5))
        # Click en dejar de seguir
        print("Se dejó de seguir a: " + user_name)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
        print("Esperando 20 segundos prevenir Ban...")
        time.sleep(random.uniform(20.0, 21.0))
    
    index += 1









