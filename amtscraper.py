# Enter Lotto Numebrs on lotto24.de
from selenium import webdriver
import time
import random

waiter = random.randrange(20,40)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome() 


# OPTIONS:
terminwunsch   = "03"
dienstleistung = "120686"



driver.get('https://service.berlin.de/dienstleistung/'+dienstleistung+'/')
time.sleep(5)
# -> go to terminbuchung page 
driver.execute_script('document.querySelector("div.zmstermin-multi > p > a").click()')
time.sleep(5)

buchen = 0 

while buchen != 1:
    time.sleep(waiter)
    buchen = driver.execute_script('''
    (
        function(){
            for (val of document.querySelector("table > tbody").rows) {
                for (var x = 0; x <= val.cells.length; x++) {
                    var cellItem = val.cells.item(x)
                    if(cellItem){
                        console.log(cellItem)
                        if (cellItem.innerText === '''+terminwunsch+''' && cellItem.classList.value.replace(' heutemarkierung','') != "nichtbuchbar") {
                            alert("JETZT BUCHEN!!!");
                            return 1;
                        };
                    };
                };
            };
        }
    ());
    ''')
    driver.refresh()
    
print("JETZT BUCHEN!")


