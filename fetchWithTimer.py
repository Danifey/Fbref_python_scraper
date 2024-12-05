import requests
import csv
import time
import datetime

# # https://httpstat.us/200 test site for url add the number to the end of the url to generate that code
# # https://httpstat.us/N where N is the error code you want to produce

# # put the fetcher class initialization at the top of the main function
# # then call the function in the loop 
class Fetcher:
    def __init__(self):
        self.start = time.time()
        self.__prevTime = self.start#holds time last time ensureMinimumInterval was called

    @property
    def previous(self):
        return self.__prevTime
    @previous.setter
    def previous(self, now):
        self.__prevTime = now
    # check last request time to ensure gap
    def ensureMinimumInterval(self,interval = 4.0): #Changed from 2.1
    # If less than `interval` seconds have elapsed, sleeps the remainder of the interval.
        now = time.time()
        prev = self.previous
        elapsed = now - prev
        remaining = interval - elapsed
        if remaining > 0:
            time.sleep(remaining)
        self.previous = time.time() # Update the previous time after sleeping

    # url = https://youtu.be/xMo7ugWudCA?si=21O2NRUUlx84P_82
        
    def fetchUrlContent(self, url):

        ## here the wait occurs unless 
        ## if applicable after waiting the function 
        ## will reset itself
        self.ensureMinimumInterval()

        # Send request
        response = requests.get(url, timeout = 10.0)
        status = response.status_code
        # # sets file path and prints to csv with the url and the status code
        file_path = 'bad_url_eCode.csv'
        # # creates list with the information relevant to the error 
        info = [url, datetime.datetime.now(), status]
        #print(errorInfo)
        # mode ='a' means it will append and close after
        with open(file_path, mode='a', newline='')as errorFile:
                writer = csv.writer(errorFile)
                writer.writerow(info)
                # when the indent ends the file is closed
        
        # Check if the request was successful
        if status == 200:
            print('fetch success')
            # Output text could also return response.content or response.text
            return response.text  # Return the response content as .text
        else:    
            # # if the page does not load then the function will return false
            # # and print error messages with url
            # print('Error: Unable to fetch URL. Status code:' +  str(status))
            print('fetch failure')
        
            # pass False back when called for branch in other code
            # and have them skip the current url 
            return False  
        
        
#     Example usage:
#     url = "https://www.example.com"
#     response_content = fetchUrlContent(url)
#     print(response.text)






