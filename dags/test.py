from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
import socket
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import socket
import os
import time
import requests 
def test():
        url = "https://jo.opensooq.com/ar"
            # resp = requests.get('https://www.google.com', stream=True)
            # print(resp.raw._connection.sock.getsockname())

        # Use headless mode
   
        options = webdriver.FirefoxOptions()
        options.headless = True        
        #create profile for proxy
        profile = webdriver.FirefoxProfile()
        myProxy = "127.0.0.1:9050 "
        ip, port = myProxy.split(':')
        profile.set_preference('network.proxy.type', 1)
        profile.set_preference('network.proxy.socks', ip)
        profile.set_preference('network.proxy.socks_port', int(port))
        profile.set_preference('permissions.default.image', 2)
        options.profile = profile # added profile to option
        driver = webdriver.Firefox(options=options)
            # Set the path of the Firefox binary
        firefox_binary_path = "/usr/bin/firefox-esr"
        options.binary_location = firefox_binary_path
            # Set the display port as an environment variable
        display_port = os.environ.get("DISPLAY_PORT", "99")
        display = f":{display_port}"
        os.environ["DISPLAY"] = display
            # Start the Xvfb server
        xvfb_cmd = f"Xvfb {display} -screen 0 1024x768x24 -nolisten tcp &"
        os.system(xvfb_cmd)
            # Start the Firefox driver
            #driver = webdriver.Firefox(options=options)
            # Go to Google.com
           # driver.get(url)
        # driver.get('https://ifconfig.me')  # Navigate to the IP check site
        #     time.sleep(2)  # Wait for the page to load
        #     current_ip = driver.find_element("tag name", "body").text  # Get the text content (IP address)
        #     print(f"Current IP address: {current_ip}")
        # # Print the page source
            #print(driver.page_source)

        # Close the browser
        driver.quit()

        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        print(f"Local IP address: {local_ip}")


default_args = {
    'owner': 'moayad',
    'email': ['altlawy19@gmail.com'],
    'email_on_failure': True
}
with DAG(
        dag_id='test',
        schedule_interval=timedelta(days=100),
        # start_date=datetime(2023,12,30,10,0)
        start_date=datetime(2024, 1, 1, 21, 5),
        default_args=default_args,
        catchup=False
) as dag:
    connection_task = PythonOperator(
        task_id='print',
        python_callable=test,
    )
connection_task
