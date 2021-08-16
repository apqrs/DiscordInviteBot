from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
#https://discord.gg/Be55z9XcmJ
usernames = ['untimelygiving', 'receptionmate', 'scareopposite', 'economicstomorrow', 'stinkerpublicly', 'bibrow', 'airlinedislike', 'waistcoatshirt', 'impoliterosemary', 'developerawareness', 'dependingsite', 'kookaburraplucky', 'warrenlined', 'privacylava', 'signalchirp', 'microsoftmustard', 'canonpromise', 'ledgerpesto', 'benchcrazy', 'mittebay', 'differentplenty', 'dashingbiking', 'hundredsmash', 'researcherovert', 'proudlink', 'wifeboiling', 'demonicexcitable', 'atmospherepalm', 'gradecrave', 'bowlertrusty', 'hatflavor', 'competenodule', 'overduechairman', 'stronglyconstitute', 'sleuthridiculous', 'lakessuccinct', 'modifiedhungry', 'arabmaiden', 'theembarrass', 'cowardicecloistered', 'deliverdecorate', 'crowdedversus', 'amountknobby', 'intentligger', 'slightsoulful', 'ferventpyramid', 'demandmeek', 'quinoabrass', 'delighttangible', 'massgaloshes', 'forestaydoll', 'washboarddrowned', 'occupyteenager', 'crushedcanon', 'whichreflection', 'dollglaring', 'geneaudi', 'smirklutestring', 'mappreviously', 'shampoochubby', 'betterears', 'haulbuffalo', 'moneybagsnore', 'celebratekenyan', 'shorecrop', 'deserveeager', 'goshawkunited', 'basisarthropods', 'uncertainimpish', 'advanceyikes', 'tailormallard', 'girlguideforeign', 'foundationasian', 'ericssonassorted', 'weavesnowflake', 'victoryarctic', 'boingthreat', 'caviarmotionless', 'throwsheet', 'underwearmotherly', 'everydaymad', 'dulefedora', 'meowdrinker', 'politenatural', 'barmpotunreeve', 'requeststrengthen', 'mustbother', 'anchoviesscarf', 'patsycollapse', 'gymnasiumloosen', 'trousersbulwark', 'cluelessmind', 'crickethave', 'seapearl', 'tilerpair', 'fuelpumppersuade', 'elitemundane', 'cyclonemat', 'quotacustomer', 'cheatwrithing', 'bathegiant', 'taskshrewd', 'quarteringgreen', 'purpleseafowl', 'giftidentify', 'shulkerdiscover', 'denyonerous', 'cartloadscroll', 'snobbynowhere', 'hummusgreens', 'longjumpuseless', 'cloverhijack', 'differspaghetti', 'caneoregano', 'halfmom', 'direfuloblongata', 'grindstonekooky', 'scubaresearcher', 'siemensnear', 'awakelectern', 'syrupyrearend', 'bendsport', 'bushevasive', 'yamssuggest', 'invitecovet', 'vouchtalus', 'kiwiexpensive', 'haircutprick', 'asktie', 'phaseprince', 'shammonitor', 'wetantique', 'piedoor', 'complaintvanilla', 'luckydingdong', 'donutlabourer', 'baaclaim', 'lilypadago', 'unbreakingindeed', 'gapingbowling', 'woozypursue', 'piecehearing', 'swimmerant', 'perceptionhero', 'catchlargely', 'undertakeranthology', 'subtletyfee', 'coverallsmotivated', 'parkwhisper', 'phrasewindbag', 'lousetown', 'forsakenmangoes', 'raceroffense', 'anorakwinner', 'crumbledear', 'imposeaid', 'actphysician', 'moaningmotivation', 'additionaltelevision', 'loyaluntried', 'closerblanket', 'mutterunhelpful', 'tavernertiler', 'perfectbridge', 'cousinmunch', 'portquote', 'dupedairy', 'winningtactful', 'limituppity', 'flawlesscashews', 'acaciajudicious', 'portrayscratchy', 'scullingcurve', 'cheerfulcola', 'indiscreetmagpie', 'classpiercing', 'omniscientwhimper', 'omelettewildcat', 'deskgun', 'livereducate', 'womanlylonghorn', 'plumvessels', 'welshrequest', 'buttondownreference', 'regretfulphilosophy', 'muffledwhispering', 'secretpercentage', 'bothercathead', 'optimismlark', 'vaultpointless', 'grincounter', 'partherring', 'squeezethirty', 'detecthall', 'femalehungarian', 'troupabnormal', 'notioncreature', 'perfumedperson', 'greasescull', 'receiveking']


# print(usernames)

PATH = r'C:\Program Files (x86)\msedgedriver'



# driver.get('https://www.10minutesemail.net')
for j in range(150):
    try:
        driver = webdriver.Edge(PATH)
        # element = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "copyEmailAddress"))
        # )
        # element.click()
        # time.sleep(5)
        driver.get('https://discord.gg/Be55z9XcmJ')


        field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        uname = random.choice(usernames)
        usernames.remove(uname)


        field.send_keys(uname)
        time.sleep(2)
        field.send_keys(Keys.RETURN)
        time.sleep(5)
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "checkbox"))
        # )
        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/section/div/div[2]/div/iframe'))
        time.sleep(2)
        driver.find_element_by_id('checkbox').click()
        time.sleep(30)
        driver.quit()
    finally:

        time.sleep(90)
# # search = driver.find_element_by_name('s')
# # search.send_keys('test')
# # search.send_keys((Keys.RETURN))
#
#
