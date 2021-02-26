from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import winsound
import logging
import threading

safety=input('Safety on?')

#log
logging.basicConfig(filename="websitelog.txt", format='%(asctime)s %(message)s', filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.INFO) 

localtime = time.asctime( time.localtime(time.time()) )
firefoxwebdriver0=webdriver.Firefox(executable_path="C:\\Users\\stink\\OneDrive\\Documents\\webdrivers\\geckodriver")
firefoxwebdriver1=webdriver.Firefox(executable_path="C:\\Users\\stink\\OneDrive\\Documents\\webdrivers\\geckodriver")
firefoxwebdriver2=webdriver.Firefox(executable_path="C:\\Users\\stink\\OneDrive\\Documents\\webdrivers\\geckodriver")
firefoxwebdriver3=webdriver.Firefox(executable_path="C:\\Users\\stink\\OneDrive\\Documents\\webdrivers\\geckodriver")
firefoxwebdriver4=webdriver.Firefox(executable_path="C:\\Users\\stink\\OneDrive\\Documents\\webdrivers\\geckodriver")
firefoxwebdriver5=webdriver.Firefox(executable_path="C:\\Users\\stink\\OneDrive\\Documents\\webdrivers\\geckodriver")
firefoxwebdriver6=webdriver.Firefox(executable_path="C:\\Users\\stink\\OneDrive\\Documents\\webdrivers\\geckodriver")
firefoxwebdriver7=webdriver.Firefox(executable_path="C:\\Users\\stink\\OneDrive\\Documents\\webdrivers\\geckodriver")
firefoxwebdriver8=webdriver.Firefox(executable_path="C:\\Users\\stink\\OneDrive\\Documents\\webdrivers\\geckodriver")
firefoxwebdriver9=webdriver.Firefox(executable_path="C:\\Users\\stink\\OneDrive\\Documents\\webdrivers\\geckodriver")
firefoxwebdriver10=webdriver.Firefox(executable_path="C:\\Users\\stink\\OneDrive\\Documents\\webdrivers\\geckodriver")
#firefoxwebdrivertest=webdriver.Firefox(executable_path="C:\\Users\\stink\\OneDrive\\Documents\\webdrivers\\geckodriver")    #test


firefoxtimeoutlist=[firefoxwebdriver0,firefoxwebdriver1,
firefoxwebdriver2,firefoxwebdriver3,
firefoxwebdriver4,firefoxwebdriver5,
firefoxwebdriver6,firefoxwebdriver7,
firefoxwebdriver8,firefoxwebdriver9,
firefoxwebdriver10]
for yee in firefoxtimeoutlist:
    yee.set_page_load_timeout(7)


#firefoxwebdrivertest.set_page_load_timeout(30) #test


#amazonsocks=firefoxwebdrivertest    #test
amazonmsi3060ti=firefoxwebdriver0
amazonasus3070=firefoxwebdriver1
amazonmsi3070=firefoxwebdriver2
amazonevga3070=firefoxwebdriver3
amazonevga3070XC3=firefoxwebdriver4
amazonevga3070XC3BLACK=firefoxwebdriver5
amazonmsi3070ventus=firefoxwebdriver6
amazonmsi3070ventus2=firefoxwebdriver7
amazonasusTUF3070=firefoxwebdriver8
amazonasus3070gaming=firefoxwebdriver9
amazonasus3070gamingOC=firefoxwebdriver10

checkthread=[] #used for checking if bought

def checkamazoncart(id, budget, website, websiteprintname, url):
        try:
            website.get(url)
            try: #captcha test
                captcha=website.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/form/div[2]/div/span/span/button')
                localtime = time.asctime( time.localtime(time.time()) )
                print('CAPTCHA '+websiteprintname+' '+localtime)
                logging.info('CAPTCHA '+websiteprintname+' '+localtime)
                captcha.click()
                time.sleep(1)
                checkthread.append(0)
                success=0
                return success
            except:
                try:
                    elem=website.find_element_by_xpath(id) #finds buy button
                    localtime = time.asctime( time.localtime(time.time()) )
                    print(websiteprintname+ ' '+ 'In stock, time: '+localtime) 
                    logging.info(websiteprintname+' In stock')
                    if pricecheck('priceblock_ourprice',budget, website)==1: #checks if price good, checks id and budget
                        print(websiteprintname+ ' Price good, moving on to buying')
                        logging.info('Price good, moving on to buying')
                    else:
                        success=0
                        checkthread.append(0)
                        return success  #this stops code and says that item not bought
                    
                    elem.click()  #click buy button
                    print(websiteprintname+' Buy button pressed')
                    logging.info('Buy button pressed')
                    time.sleep(1)#wait for page to load
                    try:
                        nothanksbutton=website.find_element_by_id('siNoCoverage-announce', website) #this is for pop-up 
                        nothanksbutton.click()
                        time.sleep(1)
                    except:
                        print('No thanks button not found')
                    textbox('//*[@id="ap_email"]','EMAIL', website) #send email
                    buyconfirm('continue', website)  #press continue after username sent
                    textbox('//*[@id="ap_password"]','PASSWORD', website) #send password
                    buyconfirm('signInSubmit', website) #press sign in
                    buyconfirm('/html/body/div[5]/div/div[2]/form/div/div/div/div[2]/div/div[1]/div/div[1]/div/span/span/input', website)#the button for place order -----------------------------------------------------------------------------------------------------------
                    success=1
                    checkthread.append(1)
                    return success
                        
                except NoSuchElementException:
                    print(websiteprintname+' Not in stock',end='. ')
                    localtime = time.asctime( time.localtime(time.time()) )
                    print (" Time:", localtime)
                    print('')
                    logging.info(websiteprintname+' Not in stock')
                    logging.info('')
                    success=0
                    checkthread.append(0)
                    return success      
        except:
            localtime = time.asctime( time.localtime(time.time()) )
            print('TIMEOUT '+websiteprintname+' '+localtime)
            print('')
            logging.info('TIMEOUT '+websiteprintname+' '+localtime)
            logging.info('')
            success=0
            checkthread.append(0)
            return success
# find button, buy now xpath: //*[@id="buy-now-button"]
def buyconfirm(buttonname, website):
    try:
        continuebutton=website.find_element_by_id(buttonname)
        continuebutton.click()
        time.sleep(1)
        print(buttonname+' pressed by id')
        logging.info(buttonname+' pressed by id')
    except:
        try:
            continuebutton=website.find_element_by_xpath(buttonname)
            continuebutton.click()
            time.sleep(1)
            print(buttonname+' pressed by xpath')
            logging.info(buttonname+' pressed by xpath')
        except:
            print(buttonname+' not found')
            logging.info(buttonname+ ' not found')

def textbox(xpath, text, website):
    try:
        box=website.find_element_by_xpath(xpath)
        box.send_keys(text)
        time.sleep(1)
        print('sent keys')
        logging.info('sent keys')
    except:
        print('textbox not found')
        logging.info('textbok not found')
        
#amazon price id: 'priceblock_ourprice'
def pricecheck(id, budget, website):
    pricegood=0
    try:
        price=website.find_element_by_id(id).text #finds price element
        price=price[1:] #remove 1st letter ($)
        print('Price is '+price, end=', ')
        logging.info('Price: '+price)
        price=int(float(price))
    except:
        print('Price not found') #when price not found, pricegood=0
        print('')
        logging.info('Price not found')
        logging.info('')
        pricegood=0
        return pricegood
    if price<=budget and price>0: #check if price under budget and over 0
        pricegood=1
        return pricegood #if price good, pricegood=1
    else:  
        pricegood=0  #if price not under budget and over 0, pricegood=0
        stringbudget=str(budget)
        print('over budget('+stringbudget+')')
        print('')
        logging.info('over budget('+stringbudget+')')
        logging.info('')
        return pricegood

def beepsound(): 
    x=0
    while not x:
        winsound.Beep(1000, 1000) #(hz, milliseconds)
        time.sleep(.75)

def checkdumbthreads():
    dumb=0
    for i in checkthread:
        if i==1:
            checkthread.clear()
            dumb=1
            print('Bought confirmed')
            logging.info('Bought confirmed')
            return dumb
    checkthread.clear()
    print('Nothing bought')
    logging.info('Nothing bought')

#add firefoxwebdriver, timeout, websitedriver, new thread, thread.start(), thread.join()
bought=0
while not bought:
    a=threading.Thread(target=checkamazoncart, args=('//*[@id="buy-now-button"]',900,amazonasus3070, 'Amazon ASUS 3070', 'https://www.amazon.com/dp/B08L8JNTXQ/?coliid=I1OENF2HS0ML2S&colid=3W3AF0E9E85S7&psc=0&ref_=lv_vv_lig_dp_it'))
    a.start()
    
    #test=threading.Thread(target=checkamazoncart, args=('//*[@id="buy-now-button"]', 20, amazonsocks, 'AMAZON SOCKS','https://www.amazon.com/Hanes-ComfortBlend-Cushion-Socks-6-Pack/dp/B01FRBTPHK/ref=pd_ybh_a_1?_encoding=UTF8&psc=1&refRID=EQS7H8480HTWTHNQDVDC'))
    #test.start()

    b=threading.Thread(target=checkamazoncart, args=('//*[@id="buy-now-button"]',500, amazonmsi3060ti, 'Amazon MSI 3060ti','https://www.amazon.com/dp/B08P2DQ28S/?coliid=I3R1LYMT0TLQOZ&colid=1DCPV6WQLQDDO&psc=0&ref_=lv_vv_lig_dp_it')) # xpath for buy button, budget, website, printname, url
    b.start()

    c=threading.Thread(target=checkamazoncart,args=('//*[@id="buy-now-button"]',900, amazonmsi3070, 'Amazon MSI 3070','https://www.amazon.com/dp/B08KWN2LZG/?coliid=I1RFW641IAGB5U&colid=3W3AF0E9E85S7&psc=0&ref_=lv_vv_lig_dp_it'))
    c.start()
    
    d=threading.Thread(target=checkamazoncart,args=('//*[@id="buy-now-button"]',900, amazonevga3070, 'Amazon EVGA 3070','https://www.amazon.com/dp/B08L8L9TCZ/?coliid=I21SHUR8BDW489&colid=3W3AF0E9E85S7&psc=0&ref_=lv_vv_lig_dp_it'))
    d.start()
    
    e=threading.Thread(target=checkamazoncart,args=('//*[@id="buy-now-button"]',900, amazonevga3070XC3, 'Amazon EVGA 3070 XC3','https://www.amazon.com/dp/B08L8L71SM/?coliid=IKTK8U3Z5CVFS&colid=3W3AF0E9E85S7&psc=0&ref_=lv_vv_lig_dp_it'))
    e.start()
    
    f=threading.Thread(target=checkamazoncart,args=('//*[@id="buy-now-button"]',900, amazonevga3070XC3BLACK, 'Amazon EVGA 3070 XC3 BLACK','https://www.amazon.com/dp/B08LW46GH2/?coliid=I2M8SB6COYW0VV&colid=3W3AF0E9E85S7&psc=0&ref_=lv_vv_lig_dp_it'))
    f.start()
    
    g=threading.Thread(target=checkamazoncart,args=('//*[@id="buy-now-button"]',900, amazonmsi3070ventus, 'Amazon MSI 3070 Ventus','https://www.amazon.com/dp/B08KWLMZV4/?coliid=I38JZJCXJGIXJR&colid=3W3AF0E9E85S7&psc=0&ref_=lv_vv_lig_dp_it'))
    g.start()
    
    h=threading.Thread(target=checkamazoncart,args=('//*[@id="buy-now-button"]',900, amazonmsi3070ventus2, 'Amazon MSI 3070 Ventus 2', 'https://www.amazon.com/dp/B08KWPDXJZ/?coliid=I1U3OY0GKI85MB&colid=3W3AF0E9E85S7&psc=0&ref_=lv_vv_lig_dp_it'))
    h.start()
    
    i=threading.Thread(target=checkamazoncart,args=('//*[@id="buy-now-button"]',900, amazonasusTUF3070, 'Amazon ASUS TUF 3070','https://www.amazon.com/dp/B08L8KC1J7/?coliid=IAM2WPBNNQG1&colid=3W3AF0E9E85S7&psc=0&ref_=lv_vv_lig_dp_it'))
    i.start()
    
    j=threading.Thread(target=checkamazoncart,args=('//*[@id="buy-now-button"]',900, amazonasus3070gaming, 'Amazon ASUS 3070 Gaming','https://www.amazon.com/dp/B08L8HPKR6/?coliid=I1S8VJ7YV332GU&colid=3W3AF0E9E85S7&psc=0&ref_=lv_vv_lig_dp_it'))
    j.start()

    k=threading.Thread(target=checkamazoncart,args=('//*[@id="buy-now-button"]',900, amazonasus3070gamingOC, 'Amazon ASUS 3070 Gaming OC','https://www.amazon.com/dp/B08L8LG4M3/?coliid=I13DQG4BKTJR02&colid=3W3AF0E9E85S7&psc=0&ref_=lv_vv_lig_dp_it'))
    k.start()
    
    threadlist=[a,b,c,d,e,f,g,h,i,j,k] #add new thread name here
    for bro in threadlist:
        bro.join()
    #test.join() #test
    print(checkthread)
    logging.info(checkthread)
    if checkdumbthreads()==1:
        bought=1
        break
#time stamp when finish    
localtime = time.asctime( time.localtime(time.time()) )
print ("Finished at :", localtime)
logging.info('Finished')
beepsound() #play sound