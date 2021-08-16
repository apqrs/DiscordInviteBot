from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# https://discord.gg/Be55z9XcmJ
usernames = ['untimelygiving', 'receptionmate', 'scareopposite', 'economicstomorrow', 'stinkerpublicly', 'bibrow', 'airlinedislike', 'waistcoatshirt', 'impoliterosemary', 'developerawareness', 'dependingsite', 'kookaburraplucky', 'warrenlined', 'privacylava', 'signalchirp', 'microsoftmustard', 'canonpromise', 'ledgerpesto', 'benchcrazy', 'mittebay', 'differentplenty', 'dashingbiking', 'hundredsmash', 'researcherovert', 'proudlink', 'wifeboiling', 'demonicexcitable', 'atmospherepalm', 'gradecrave', 'bowlertrusty', 'hatflavor', 'competenodule', 'overduechairman', 'stronglyconstitute', 'sleuthridiculous', 'lakessuccinct', 'modifiedhungry', 'arabmaiden', 'theembarrass', 'cowardicecloistered', 'deliverdecorate', 'crowdedversus', 'amountknobby', 'intentligger', 'slightsoulful', 'ferventpyramid', 'demandmeek', 'quinoabrass', 'delighttangible', 'massgaloshes', 'forestaydoll', 'washboarddrowned', 'occupyteenager', 'crushedcanon', 'whichreflection', 'dollglaring', 'geneaudi', 'smirklutestring', 'mappreviously', 'shampoochubby', 'betterears', 'haulbuffalo', 'moneybagsnore', 'celebratekenyan', 'shorecrop', 'deserveeager', 'goshawkunited', 'basisarthropods', 'uncertainimpish', 'advanceyikes', 'tailormallard', 'girlguideforeign', 'foundationasian', 'ericssonassorted', 'weavesnowflake', 'victoryarctic', 'boingthreat', 'caviarmotionless', 'throwsheet', 'underwearmotherly', 'everydaymad', 'dulefedora', 'meowdrinker', 'politenatural', 'barmpotunreeve', 'requeststrengthen', 'mustbother', 'anchoviesscarf', 'patsycollapse', 'gymnasiumloosen', 'trousersbulwark', 'cluelessmind', 'crickethave', 'seapearl', 'tilerpair', 'fuelpumppersuade', 'elitemundane', 'cyclonemat', 'quotacustomer', 'cheatwrithing', 'bathegiant', 'taskshrewd', 'quarteringgreen', 'purpleseafowl', 'giftidentify', 'shulkerdiscover', 'denyonerous', 'cartloadscroll', 'snobbynowhere', 'hummusgreens', 'longjumpuseless', 'cloverhijack', 'differspaghetti', 'caneoregano', 'halfmom', 'direfuloblongata', 'grindstonekooky', 'scubaresearcher', 'siemensnear', 'awakelectern', 'syrupyrearend', 'bendsport', 'bushevasive', 'yamssuggest', 'invitecovet', 'vouchtalus', 'kiwiexpensive', 'haircutprick', 'asktie', 'phaseprince', 'shammonitor', 'wetantique', 'piedoor', 'complaintvanilla', 'luckydingdong', 'donutlabourer', 'baaclaim', 'lilypadago', 'unbreakingindeed', 'gapingbowling', 'woozypursue', 'piecehearing', 'swimmerant', 'perceptionhero', 'catchlargely', 'undertakeranthology', 'subtletyfee', 'coverallsmotivated', 'parkwhisper', 'phrasewindbag', 'lousetown', 'forsakenmangoes', 'raceroffense', 'anorakwinner', 'crumbledear', 'imposeaid', 'actphysician', 'moaningmotivation', 'additionaltelevision', 'loyaluntried', 'closerblanket', 'mutterunhelpful', 'tavernertiler', 'perfectbridge', 'cousinmunch', 'portquote', 'dupedairy', 'winningtactful', 'limituppity', 'flawlesscashews', 'acaciajudicious', 'portrayscratchy', 'scullingcurve', 'cheerfulcola', 'indiscreetmagpie', 'classpiercing', 'omniscientwhimper', 'omelettewildcat', 'deskgun', 'livereducate', 'womanlylonghorn', 'plumvessels', 'welshrequest', 'buttondownreference', 'regretfulphilosophy', 'muffledwhispering', 'secretpercentage', 'bothercathead', 'optimismlark', 'vaultpointless', 'grincounter', 'partherring', 'squeezethirty', 'detecthall', 'femalehungarian', 'troupabnormal', 'notioncreature', 'perfumedperson', 'greasescull', 'receiveking']
usernames = """n7rbh3ufcowcywrk
qcy4pei5fii6ylm3
a0uaf7vxuc9h2ozq
9uh3fts0l9n2trmi
8dof1u3ag98k4a3a
4gior35nro0fbskz
nyagxcprrylsjm8u
fb5gd35uqmosvf5l
moffujz7m1lfv23y
hyuyok4dt16xxtb8
n2b3zug337q444ek
mwj5pa2jlkq9oac8
eif0dn5u0rixowu4
tvg1v4cuih2qky7f
gn0xzpiusferl7ng
t4k52j27h834cn2s
4hylsvlgg09ogsb5
g6s87u7d1qns9m69
kfh2pmve3arg3h22
xicx63b92rhdptmw
qo0cnvajhtpswats
p9iqt3fscg8bx5mx
p7qy5nqzny44ly08
5c0hpqc91i9zjm72
7scq8ad5qpih2toe
pdfie6q6a3fj76q4
1elyv0r8mwztux6k
8g3xinpgq274bf1w
v4mnivkterevl2o9
yp7oozwdw1ootgqi
4pell0movq38idq0
7a1b7djoa64ew6nd
ink31zehws7r7mlo
go248ci8qi2ol6na
1tx2fw92m4r9x9cl
w9izgzgqpl6qpa53
buz3az5acavj00zf
y6uqky95j7iz44d6
aejttw1t661zguz7
0k0oxxk77ccogng4
34g8xguim1myjp1q
cpsmmv41mrjbyanb
aywwr6r2h9hi06x4
y3bqruqscu524gn9
lelfo0hwi8qowbwt
11ovupxgo8ya689q
2agx34s2mz4ibc7t
5j2nq0clu34nw3wp
c4g14r9tsc6dqnje
ndqorx2rj4cs32kw
frv1fglb9l5rkt45
p2q4nqqr1tigt8oe
zr1gti89667gqy86
hjzqf5qsbazik5mj
npxv4om8zia1k8g9
5x0qaplmgu90yros
b0gf6fqaomzrj1in
3lx5gmhkbjjalzu2
qqhvamlwag4821hu
0pk93jdsz625wfnd
oeiqu4uclqsxhwu7
xghxm2fjsbvcu7vx
ni3cmsikegll2rwx
mbs23ljfk8as24cl
q5t2ta8w3lcbmb8o
sbn59zilt0fdhieh
0yabg564ir8wu7h0
we64yvfty6jnqahc
cs2j52dlh1el8fd8
39vyndma1clpv82t
dgfmbxwlymo6xlxq
vidziewd3wsvyjx2
fjntoj9ieglustfo
3vvjg5a7nbonghpb
fgy52cbe63jtczit
73m41v1p1lz5qkk6
30oriss112dfko72
r6v0y9rwa2ojmnrq
9rd8jf62v4uv8675
u0ew2fltfo4rmbnu
bfu5iv5wrulhl1kx
vuorfmdyi3fbicop
2at0yaf3d87j7fs3
g2z94yn6dbbuytj1
1jgjy3xojpspfdfc
63vv6ieuk7qe9jdn
oqq3jtlt4ajc1tb6
6dww14dm0seulqxj
j1ue4d537mux6eku
lq9oenn9rn363qy8
maa4axj52nnxbjs8
sa5y599sakq5kgwi
i5n2llcjaqdhfgo8
10u15d42eczn28cw
01wn0alcpcvogkjp
n8pto2hxot4f9568
qjeh8knfbg56vo7l
m5hjzbhwxu3wj1bz
z9h6cppc99j1tylg
5htu7h5zj2btvvt9
nlvr2rcb0dsumhra
dcw6k35h5pwfdq9y
twpv3ytqjbep3wiv
2cgb02xddua09zfg
1bcd082sn3kpp7jh
wdesywz765zelqxz
whegs27ev4l9sh9e
6y3dn48zk5l764om
sf3ohw1n1j1x8whl
gdhh6at6btdeqmv9
a5hjb2095xpjkopv
fayghq935dzs8ivg
5qf94sis0ed2c52g
mp8a8pg3x1ybtmpv
j7lix5vn8jmr1vif
tx2pq8teygoivrrf
cadj2tao1dmuk2qy
a2tbil7uj754c9f8
wd2txnqr3fhl4852
z6sh9mrg7m0bf2rf
cl431wc4sbg3sgk2
374imy5s494929rs
wi65wuka99fpjit8
xwfe3nfc96rzvbho
b7dgiywrfuue9ujk
ph4wbs8lpicjeqow
4qbh9570j0f62uhv
f0wm9gnw4jput0jn
9pj46ujtb7av3ota
9la610jkfal2h467
7qn3i56oqurlhbp7
duqph9jloce1qrtg
vcx0uc8t8pw3naic
f1yb24ll1mkwjzqc
fn5z82i399qpnmrq
l0sox9fjvo3dijbx
8rprd24yqk6yxk3g
dvox4tgdrkw683wv
8yywnz8um6r60fbl
s6muy2pzj4esq0re
0z3wtqlx7cwvlg0l
sp8hdidrz1bmoujd
3ezjz6zyq0kxbnxb
9kkmcacu5gz7s69a
zyku4xu1elexks7g
37nwamzzmaeo8qj2
74x5zvuj37ncw9p9
bxtprzp27s0vk8ga
0xsbut2vxd2768wn
3sx3qt9cznockhj2
bh1qey0mu7m0i49u
ud4va90x0foja4iu
newfs3tjzq6m0llx
jszi24413zup53ag
o0timb3cau9a67bw
8q9gp24ioezln97z
mzgw9u58k8lvuui2
n2h03pii3p9s0ylh
2e8ln5ujgw2gju2o
khre9m4dvve7g46y
2lx6fhuh7282iqsc
lwqc78dv732gzmeb
wuhdfl2z1k52qoc0
p74061ke2q6asce4
n1sb46zelyrfz12r
bb8m5l3cdi0qdok0
mb2wdhnq43b9b0j9
bz6qa8hcbvwhak06
nz5tiyi0p5cvzont
a3wx9el6ax0vd0dk
wm4qxoj15d9tv00b
xkvm50cnmeuvvwi6
f4pq7x32kesy2n56
9wasgx23v23puo5k
go2fwp14tiu95364
1gcm8yxevlbxsjlj
365sbgy2zvo89e5t
drtksty3hxkh17p5
uaasw8o0q6h6760g
hzeljtvqe2hycfg1
wdiguuz2i3h0v2wh
e2104bg41jrqyxdt
hd7s3g6smvpq5ln8
jkzz7zey3eqqv4rc
f6bj1c9jyqd9tw15
kc4nqm77d8oejroe
asgjtnnxz4isgw17
v7m9vvz9jo0x4gqn
ztmmbi4muu19itbg
nyax51niav3889ap
7mchcgxw7vcl2s7z
sh0szic81fkjmo92
8znq2zd9axg2u76z
npndyqkz78i2jn6r
vowyk74nrl1zeit8
3dngbmp446fmjvcr
sx2bc8jiiso1oht2
rrbdwpwtxljqx5ap
3im1cl1qmitw1rg4
6hyenab6p2moi1n5""".split('\n')

# print(usernames)

PATH = r'C:\Program Files (x86)\msedgedriver'

r=[i.strip(' has accepted') for i in"""q5t2ta8w3lcbmb8o has accepted
mzgw9u58k8lvuui2 has accepted
vcx0uc8t8pw3naic has accepted
1gcm8yxevlbxsjlj has accepted
0k0oxxk77ccogng4 has accepted
6hyenab6p2moi1n5 has accepted
n8pto2hxot4f9568 has accepted
5qf94sis0ed2c52g has accepted
oqq3jtlt4ajc1tb6 has accepted
7a1b7djoa64ew6nd has accepted
o0timb3cau9a67bw has accepted
39vyndma1clpv82t has accepted
fayghq935dzs8ivg has accepted
8g3xinpgq274bf1w has accepted
newfs3tjzq6m0llx has accepted
yp7oozwdw1ootgqi has accepted
74x5zvuj37ncw9p9 has accepted
8znq2zd9axg2u76z has accepted
sbn59zilt0fdhieh has accepted
f0wm9gnw4jput0jn has accepted
2e8ln5ujgw2gju2o has accepted
aywwr6r2h9hi06x4 has accepted
3ezjz6zyq0kxbnxb has accepted
8yywnz8um6r60fbl has accepted
jkzz7zey3eqqv4rc has accepted
uaasw8o0q6h6760g has accepted
go248ci8qi2ol6na has accepted
3dngbmp446fmjvcr has accepted
zyku4xu1elexks7g has accepted
c4g14r9tsc6dqnje has accepted
""".split('\n')]
# print(r)
for i in r:
    if i in usernames:
        usernames.remove(i)

# driver.get('https://www.10minutesemail.net')
for j in range(150):
    try:
        time.sleep(10)
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
        time.sleep(4)
        field.send_keys(Keys.RETURN)
        time.sleep(5)
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "checkbox"))
        # )
        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/section/div/div[2]/div/iframe'))
        time.sleep(2)
        driver.find_element_by_id('checkbox').click()
        time.sleep(30)
        print(f'{uname} has accepted')

    finally:


        time.sleep(120)
        driver.quit()

# # search = driver.find_element_by_name('s')
# # search.send_keys('test')
# # search.send_keys((Keys.RETURN))
#
#
