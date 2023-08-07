import sys
import asyncio

from os import execle, getenv, environ

from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from pyrogram.errors import FloodWait


# ------------- SESSIONS -------------

SESSION1 = getenv('SESSION1', default=None)
SESSION2 = getenv('SESSION2', default=None)
SESSION3 = getenv('SESSION3', default=None)
SESSION4 = getenv('SESSION4', default=None)
SESSION5 = getenv('SESSION5', default=None)


# ------------- CLIENTS -------------

if SESSION1:
    M1 = Client(SESSION1, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M1 = None

if SESSION2:
    M2 = Client(SESSION2, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M2 = None

if SESSION3:
    M3 = Client(SESSION3, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M3 = None

if SESSION4:
    M4 = Client(SESSION4, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M4 = None

if SESSION5:
    M5 = Client(SESSION5, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M5 = None


# ONE_WORDS = ["MADARCHOD", "BHOSDIKE", "LAAAWEEE KE BAAAAAL", "MAAAAR KI JHAAAAT KE BBBBBAAAAALLLLL", "MADRCHOD..", 
#     "TERI MA KI CHUT..", "LWDE KE BAAALLL.", "MACHAR KI JHAAT KE BAAALLLL", "TERI MA KI CHUT M DU TAPA TAP?", 
#     "TERI MA KA BHOSDAA", "TERI BHN SBSBE BDI RANDI.", "TERI MA OSSE BADI RANDDDDD", "TERA BAAP CHKAAAA", 
#     "KITNI CHODU TERI MA AB OR..", "TERI MA CHOD DI HM NE", "MIGHTY !!  BAAP BOLTE", 
#     "TERI MA KE STH REELS BNEGA ROAD PEE", "TERI MA KI CHUT EK DAM TOP SEXY", 
#     "MALUM NA PHR KESE LETA HU M TERI MA KI CHUT TAPA TAPPPPP", "LUND KE CHODE TU KEREGA TYPIN", "SPEED PKD LWDEEEE", 
#     "BAAP KI SPEED MTCH KRRR", "LWDEEE", "PAPA KI SPEED MTCH NHI HO RHI KYA", "ALE ALE MELA BCHAAAA", 
#     "[AADARSH](t.me/JAADUGARXD) TERA BAAP !!", "CHUD GYA PAPA SEEE", "KISAN KO KHODNA OR", "SALE RAPEKL KRDKA TERA", 
#     "HAHAHAAAAA", "KIDSSSS", "BACHHE TERI MAA KI CHUTT", "TERI BHEN KI CHUTT BHOSDIWALE", 
#     "TERI MA CHUD GYI AB FRAR MT HONA", "YE LDNGE BAPP SE", "KIDSSS FRAR HAHAHH", "BHEN KE LWDE SHRM KR", 
#     "KITNI GLIYA PDWEGA APNI MA KO", "NALLEE", "SUAR KE PILLE TERI MAAKO SADAK PR LITAKE CHOD DUNGA 😂😆🤤", 
#     "ABE TERI MAAKA BHOSDA MADERCHOOD KR PILLE PAPA SE LADEGA TU 😼😂🤤", 
#     "GALI GALI NE SHOR HE TERI MAA RANDI CHOR HE 💋💋💦", "ABE TERI BEHEN KO CHODU RANDIKE PILLE KUTTE KE CHODE 😂👻🔥", 
#     "TERI MAAKO AISE CHODA AISE CHODA TERI MAAA BED PEHI MUTH DIA 💦💦💦💦", 
#     "TERI BEHEN KE BHOSDE ME AAAG LAGADIA MERA MOTA LUND DALKE 🔥🔥💦😆😆", "RANDIKE BACHHE TERI MAAKO CHODU CHAL NIKAL", 
#     "KITNA CHODU TERI RANDI MAAKI CHUTH ABB APNI BEHEN KO BHEJ 😆👻🤤", 
#     "TERI BEHEN KOTO CHOD CHODKE PURA FAAD DIA CHUTH ABB TERI GF KO BHEJ 😆💦🤤", 
#     "TERI GF KO ETNA CHODA BEHEN KE LODE TERI GF TO MERI RANDI BANGAYI ABB CHAL TERI MAAKO CHODTA FIRSE ♥️💦😆😆😆😆", 
#     "HARI HARI GHAAS ME JHOPDA TERI MAAKA BHOSDA 🤣🤣💋💦", "CHAL TERE BAAP KO BHEJ TERA BASKA NHI HE PAPA SE LADEGA TU", 
#     "TERI BEHEN KI CHUTH ME BOMB DALKE UDA DUNGA MAAKE LAWDE", 
#     "TERI MAAKO TRAIN ME LEJAKE TOP BED PE LITAKE CHOD DUNGA SUAR KE PILLE 🤣🤣💋💋",  
#     "TERI MAAAKE NUDES GOOGLE PE UPLOAD KARDUNGA BEHEN KE LAEWDE 👻🔥",
#     "TERI MAAAKE NUDES GOOGLE PE UPLOAD KARDUNGA BEHEN KE LAEWDE 👻🔥", 
#     "TERI BEHEN KO CHOD CHODKE VIDEO BANAKE XNXX.COM PE NEELAM KARDUNGA KUTTE KE PILLE 💦💋", 
#     "TERI MAAAKI CHUDAI KO PORNHUB.COM PE UPLOAD KARDUNGA SUAR KE CHODE 🤣💋💦", 
#     "ABE TERI BEHEN KO CHODU RANDIKE BACHHE TEREKO CHAKKO SE PILWAVUNGA RANDIKE BACHHE 🤣🤣", 
#     "TERI MAAKI CHUTH FAADKE RAKDIA MAAKE LODE JAA ABB SILWALE 👄👄", "TERI BEHEN KI CHUTH ME MERA LUND KAALA", 
#     "TERI BEHEN LETI MERI LUND BADE MASTI SE TERI BEHEN KO MENE CHOD DALA BOHOT SASTE SE",  
#     "BETE TU BAAP SE LEGA PANGA TERI MAAA KO CHOD DUNGA KARKE NANGA 💦💋", 
#     "HAHAHAH MERE BETE AGLI BAAR APNI MAAKO LEKE AAYA MATH KAT OR MERE MOTE LUND SE CHUDWAYA MATH KAR", 
#     "CHAL BETA TUJHE MAAF KIA 🤣 ABB APNI GF KO BHEJ", 
#     "SHARAM KAR TERI BEHEN KA BHOSDA KITNA GAALIA SUNWAYEGA APNI MAAA BEHEN KE UPER", 
#     "ABE RANDIKE BACHHE AUKAT NHI HETO APNI RANDI MAAKO LEKE AAYA MATH KAR HAHAHAHA",  
#     "KIDZ MADARCHOD TERI MAAKO CHOD CHODKE TERR LIYE BHAI DEDIYA", 
#     "JUNGLE ME NACHTA HE MORE TERI MAAKI CHUDAI DEKKE SAB BOLTE ONCE MORE ONCE MORE 🤣🤣💦💋", 
#     "GALI GALI ME REHTA HE SAND TERI MAAKO CHOD DALA OR BANA DIA RAND 🤤🤣", 
#     "SAB BOLTE MUJHKO PAPA KYOUNKI MENE BANADIA TERI MAAKO PREGNENT 🤣🤣", 
#     "SUAR KE PILLE TERI MAAKI CHUTH ME SUAR KA LOUDA OR TERI BEHEN KI CHUTH ME MERA LODA", 
#     "CHAL CHAL APNI MAAKI CHUCHIYA DIKA", "HAHAHAHA BACHHE TERI MAAAKO CHOD DIA NANGA KARKE", 
#     "TERI GF HE BADI SEXY USKO PILAKE CHOODENGE PEPSI", "2 RUPAY KI PEPSI TERI MUMMY SABSE SEXY 💋💦", 
#     "TERI MAAKO CHEEMS SE CHUDWAVUNGA MADERCHOOD KE PILLE 💦🤣", 
#     "TERI BEHEN KI CHUTH ME MUTHKE FARAR HOJAVUNGA HUI HUI HUI", "SPEED LAAA TERI BEHEN CHODU RANDIKE PILLE 💋💦🤣", 
#     "ARE RE MERE BETE KYOUN SPEED PAKAD NA PAAA RAHA APNE BAAP KA HAHAH🤣🤣", 
#     "SUN SUN SUAR KE PILLE JHANTO KE SOUDAGAR APNI MUMMY KI NUDES BHEJ", "ABE SUN LODE TERI BEHEN KA BHOSDA FAAD DUNGA", 
#     "TERI MAAKO KHULE BAJAR ME CHOD DALA 🤣🤣💋", "SHRM KR", "MERE LUND KE BAAAAALLLLL", 
#     "KITNI GLIYA PDWYGA APNI MA BHEN KO", "RNDI KE LDKEEEEEEEEE", "KIDSSSSSSSSSSSS", "Apni gaand mein muthi daal", 
#     "Apni lund choos", "Apni ma ko ja choos", "Bhen ke laude", "Bhen ke takke", "Abla TERA KHAN DAN CHODNE KI BARIII", 
#     "BETE TERI MA SBSE BDI RAND", "LUND KE BAAAL JHAT KE PISSSUUUUUUU", "LUND PE LTKIT MAAALLLL KI BOND H TUUU", 
#     "KASH OS DIN MUTH MRKE SOJTA M TUN PAIDA NA HOTAA", "GLTI KRDI TUJW PAIDA KRKE", "SPEED PKDDD", 
#     "Gaand main LWDA DAL LE APNI MERAAA", "Gaand mein bambu DEDUNGAAAAAA", "GAND FTI KE BALKKK", 
#     "Gote kitne bhi bade ho, lund ke niche hi rehte hai", "Hazaar lund teri gaand main", "Jhaant ke pissu-", 
#     "TERI MA KI KALI CHUT", "Khotey ki aulad", "Kutte ka awlad", "Kutte ki jat", "Kutte ke tatte", 
#     "TETI MA KI.CHUT , tERI MA RNDIIIIIIIIIIIIIIIIIIII", "Lavde ke bal", "muh mei lele", "Lund Ke Pasine", 
#     "MERE LWDE KE BAAAAALLL", "HAHAHAAAAAA", "CHUD GYAAAAA", "Randi khanE KI ULADDD", "Sadi hui gaand", 
#     "Teri gaand main kute ka lund", "Teri maa ka bhosda", "Teri maa ki chut", "Tere gaand mein keede paday", 
#     "Ullu ke pathe", "SUNN MADERCHOD", "TERI MAA KA BHOSDA", "BEHEN K LUND", "TERI MAA KA CHUT KI CHTNIIII", 
#     "MERA LAWDA LELE TU AGAR CHAIYE TOH", "GAANDU", "CHUTIYA", "TERI MAA KI CHUT PE JCB CHADHAA DUNGA", "SAMJHAA LAWDE", 
#     "YA DU TERE GAAND ME TAPAA TAP��", "TERI BEHEN MERA ROZ LETI HAI", "TERI GF K SAATH MMS BANAA CHUKA HU���不�不", 
#     "TU CHUTIYA TERA KHANDAAN CHUTIYA", "AUR KITNA BOLU BEY MANN BHAR GAYA MERA�不", 
#     "TERIIIIII MAAAA KI CHUTTT ME ABCD LIKH DUNGA MAA KE LODE", "TERI MAA KO LEKAR MAI FARAR", "RANIDIII", "BACHEE", 
#     "CHODU", "RANDI", "RANDI KE PILLE", "TERIIIII MAAA KO BHEJJJ", "TERAA BAAAAP HU",  
#     "teri MAA KI CHUT ME HAAT DAALLKE BHAAG JAANUGA", "Teri maa KO SARAK PE LETAA DUNGA", 
#     "TERI MAA KO GB ROAD PE LEJAKE BECH DUNGA", "Teri maa KI CHUT MÉ KAALI MITCH", "TERI MAA SASTI RANDI HAI", 
#     "TERI MAA KI CHUT ME KABUTAR DAAL KE SOUP BANAUNGA MADARCHOD", "TERI MAAA RANDI HAI", 
#     "TERI MAAA KI CHUT ME DETOL DAAL DUNGA MADARCHOD", "TERI MAA KAAA BHOSDAA", "TERI MAA KI CHUT ME LAPTOP", 
#     "Teri maa RANDI HAI", "TERI MAA KO BISTAR PE LETAAKE CHODUNGA", "TERI MAA KO AMERICA GHUMAAUNGA MADARCHOD", 
#     "TERI MAA KI CHUT ME NAARIYAL PHOR DUNGA", "TERI MAA KE GAND ME DETOL DAAL DUNGA", 
#     "TERI MAAA KO HORLICKS PILAUNGA MADARCHOD", "TERI MAA KO SARAK PE LETAAA DUNGAAA", "TERI MAA KAA BHOSDA", 
#     "MERAAA LUND PAKAD LE MADARCHOD", "CHUP TERI MAA AKAA BHOSDAA", "TERIII MAA CHUF GEYII KYAAA LAWDEEE", 
#     "TERIII MAA KAA BJSODAAA", "MADARXHODDD", "TERIUUI MAAA KAA BHSODAAA", 
#     "TERIIIIII BEHENNNN KO CHODDDUUUU MADARXHODDDD", "NIKAL MADARCHOD", "RANDI KE BACHE", "TERA MAA MERI FAN", 
#     "TERI SEXY BAHEN KI CHUT OP"]
ONE_WORDS = ["/fban 1174082349",
"/fban 1105302551",
"/fban 1088205007",
"/fban 1076671561",
"/fban 1076231274",
"/fban 1074683045",
"/fban 1061950022",
"/fban 912518634",
"/fban 905401222",
"/fban 857561955",
"/fban 832386375",
"/fban 662241828",
"/fban 576600352",
"/fban 306823997",
"/fban 168380039",
"/fban 1547855169",
"/fban 5602002072",
"/fban 6123537331",
"/fban 2010013044",
"/fban 1667867553",
"/fban 6038466362",
"/fban 5955565028",
"/fban 5675142036",
"/fban 5476016029",
"/fban 1428255748",
"/fban 1275899361",
"/fban 5801654254",
"/fban 6115961238",
"/fban 5252734823",
"/fban 5706889082",
"/fban 5790995164",
"/fban 1085349789",
"/fban 892442290" ,
"/fban 5516805780",
"/fban 6075151090",
"/fban 6079406392",
"/fban 5809398638",
"/fban 2069074084",
"/fban 2119437351",
"/fban 5188267105",
"/fban 1580347307",
"/fban 5093283564",
"/fban 6069038275",
"/fban 1359542875",
"/fban 6381813208",
"/fban 833037841" ,
"/fban 6120177109",
"/fban 5910032563",
"/fban 5793924559",
"/fban 5036910196",
"/fban 1993587896",
"/fban 1926530831",
"/fban 1846743956",
"/fban 1831469990",
"/fban 1524243273",
"/fban 1235746024",
"/fban 1164400251",
"/fban 1157992840",
"/fban 1043417575",
"/fban 892159802" ,
"/fban 812035202" ,
"/fban 5700728871",
"/fban 5073080837",
"/fban 1979889511",
"/fban 1977893267",
"/fban 6385799001",
"/fban 6038125874",
"/fban 5861404990",
"/fban 5594691760",
"/fban 5479905326",
"/fban 5053040426",
"/fban 2134212022",
"/fban 1873576192",
"/fban 1843239146",
"/fban 6075470695",
"/fban 5498766283",
"/fban 1663273429",
"/fban 6044087928",
"/fban 1933125883",
"/fban 5282475045",
"/fban 5221447062",
"/fban 5125909462",
"/fban 2108125070",
"/fban 2071766794",
"/fban 2070510074",
"/fban 1948920671",
"/fban 1790031608",
"/fban 1740546936",
"/fban 1421991770",
"/fban 1285075462",
"/fban 1077496177",
"/fban 934585985" ,
"/fban 870591320" ,
"/fban 6173426329",
"/fban 5846798067",
"/fban 1850010873",
"/fban 1656858564",
"/fban 1174605406",
"/fban 1122698911",
"/fban 1113833651",
"/fban 1112752054",
"/fban 1084380257",
"/fban 1071558564",
"/fban 818542725" ,
"/fban 699303800" ,
"/fban 6081940121",
"/fban 1315833045",
"/fban 5968451943",
"/fban 6243067734",
"/fban 5701631091",
"/fban 5136495401",
"/fban 5928108898",
"/fban 5785873942",
"/fban 6164028677",
"/fban 6163718923",
"/fban 6123692768",
"/fban 638481251" ,
"/fban 5458321804",
"/fban 5345226997",
"/fban 6207312492",
"/fban 6011268225",
"/fban 2075185519",
"/fban 5830269064",
"/fban 5838372129",
"/fban 5472165864",
"/fban 5406523927",
"/fban 6078879275",
"/fban 6027193850",
"/fban 6228366263",
"/fban 6098229520",
"/fban 1373953448",
"/fban 1327218663",
"/fban 6268204144",
"/fban 5259098096",
"/fban 5081187646",
"/fban 5064724980",
"/fban 1662936718",
"/fban 733842228",
"/fban 720161250",
"/fban 719535978",
"/fban 706386062",
"/fban 672213246",
"/fban 670522506",
"/fban 668475194",
"/fban 661828902",
"/fban 647276403",
"/fban 645059352",
"/fban 640594195",
"/fban 605385315",
"/fban 589272363",
"/fban 568991050",
"/fban 532340129",
"/fban 1823249265",
"/fban 6265787325",
"/fban 5704133749",
"/fban 5013045477",
"/fban 1868548541",
"/fban 1656888593",
"/fban 5431818393",
"/fban 5754764800",
"/fban 5936079504",
"/fban 1216476517",
"/fban 6166048092",
"/fban 5885870313",
"/fban 6126463673",
"/fban 6069711972",
"/fban 5831226605",
"/fban 5819822687",
"/fban 5803319700",
"/fban 5742647031",
"/fban 5383986905",
"/fban 5201542548",
"/fban 5173031228",
"/fban 1717080357",
"/fban 1297894055",
"/fban 1159301161",
"/fban 962257542" ,
"/fban 5450262135",
"/fban 6020109500",
"/fban 5926624824",
"/fban 5659625818",
"/fban 6070415603",
"/fban 1778092759",
"/fban 6051484797",
"/fban 5474244823",
"/fban 6152082091",
"/fban 6009037284",
"/fban 5439867530",
"/fban 6143054275",
"/fban 5927662633",
"/fban 5549440853",
"/fban 5527165598",
"/fban 5434979740",
"/fban 5396110442",
"/fban 5346267017",
"/fban 5324851562",
"/fban 5305549178",
"/fban 5280860308",
"/fban 5279423249",
"/fban 5084822828",
"/fban 2123191108",
"/fban 2073450183",
"/fban 1952193532",
"/fban 1935222211",
"/fban 1896502867",
"/fban 1825104065",
"/fban 1758734619",
"/fban 1555884559",
"/fban 1478861926",
"/fban 1430783443",
"/fban 1372781369",
"/fban 1089591396",
"/fban 975570879",
"/fban 857505519",
"/fban 649434794",
"/fban 5308427194",
"/fban 5185334281",
"/fban 5298331196",
"/fban 6141688985",
"/fban 5985557752",
"/fban 5585667769",
"/fban 6036400999",
"/fban 1222195908",
"/fban 5461980358",
"/fban 5826481560",
"/fban 6271887872",
"/fban 5918548652",
"/fban 5563659709",
"/fban 5802227956",
"/fban 1794957243",
"/fban 6255922217",
"/fban 5242019471",
"/fban 6272583933",
"/fban 6146249682",
"/fban 6244546172",
"/fban 6022783859",
"/fban 6060846996",
"/fban 2104787479",
"/fban 936900172",
"/fban 5262123309",
"/fban 1031952739",
"/fban 5748306836",
"/fban 6282779846",
"/fban 5985396610",
"/fban 5889207854",
"/fban 5745078511",
"/fban 5586314327",
"/fban 5483901724",
"/fban 5232298981",
"/fban 1495884885",
"/fban 1123031731",
"/fban 5351913016",
"/fban 1958393484",
"/fban 1141238023",
"/fban 2052264722",
"/fban 759243797",
"/fban 6194199092",
"/fban 6043746756",
"/fban 5949865806",
"/fban 5852316495",
"/fban 5085185716",
"/fban 1983705698",
"/fban 1325692003",
"/fban 1308379413",
"/fban 815474344" ,
"/fban 5019250771",
"/fban 5851550785",
"/fban 6111950429",
"/fban 6111774325",
"/fban 6046907643",
"/fban 5993827628",
"/fban 5963433546",
"/fban 5952111867",
"/fban 5927196923",
"/fban 5855701825",
"/fban 5827760394",
"/fban 5727205258",
"/fban 5672928996",
"/fban 5502456760",
"/fban 5401752616",
"/fban 5378395876",
"/fban 2146890164",
"/fban 1932415258",
"/fban 1852880709",
"/fban 1339745656",
"/fban 1239599484",
"/fban 6254586851",
"/fban 6028753740",
"/fban 5935599092",
"/fban 5840225648",
"/fban 5607197851",
"/fban 5584153402",
"/fban 5531201227",
"/fban 1985598437",
"/fban 856607793" ,
"/fban 6179983916",
"/fban 6089586306",
"/fban 6192974944",
"/fban 5664419650",
"/fban 6098287888",
"/fban 5757767309",
"/fban 6100578840",
"/fban 5944633902",
"/fban 5454724546",
"/fban 6032202619",
"/fban 5912346294",
"/fban 6023258942",
"/fban 5018213971",
"/fban 5537346938",
"/fban 2015103215",
"/fban 5633273578",
"/fban 6179161919",
"/fban 6056431473",
"/fban 5637601187",
"/fban 5635774431",
"/fban 5510801382",
"/fban 5100614931",
"/fban 5098445234",
"/fban 1860839445",
"/fban 1353715681",
"/fban 1301322970",
"/fban 1160579777",
"/fban 1054267993",
"/fban 6215891301",
"/fban 5865182872",
"/fban 5393140463",
"/fban 5075268996",
"/fban 2141998552",
"/fban 1766424551",
"/fban 995196737" ,
"/fban 6086457603",
"/fban 5362644534",
"/fban 6155338215",
"/fban 5941996918",
"/fban 5620806809",
"/fban 5600444420",
"/fban 5459450150",
"/fban 5168092721",
"/fban 6129801307",
"/fban 6103499498",
"/fban 5953933176",
"/fban 6097635751",
"/fban 6125556203",
"/fban 6037430359",
"/fban 1582784547",
"/fban 5618750629",
"/fban 6242265870",
"/fban 5920476737",
"/fban 5959211397",
"/fban 1354741776",
"/fban 5729979422",
"/fban 5639033197",
"/fban 1832163509",
"/fban 5720548079",
"/fban 6285200517",
"/fban 300860929" ,
"/fban 6241319519",
"/fban 6165275476",
"/fban 6080707746",
"/fban 6061063768",
"/fban 5997082834",
"/fban 5871282974",
"/fban 5521108844",
"/fban 1038780772",
"/fban 1037168099",
"/fban 870329398" ,
"/fban 866131353" ,
"/fban 856953648" ,
"/fban 810349902" ,
"/fban 566168080" ,
"/fban 5664730041",
"/fban 5365172293",
"/fban 6249997139",
"/fban 6223976707",
"/fban 6140099803",
"/fban 6036919256",
"/fban 5635508238",
"/fban 1811225628",
"/fban 1441110541",
"/fban 5653065626",
"/fban 1974019607",
"/fban 6211701274",
"/fban 5851777736",
"/fban 5647316202",
"/fban 5956020573",
"/fban 1484619259",
"/fban 6138538817",
"/fban 1376057344",
"/fban 1134627757",
"/fban 1759030390",
"/fban 5421273241",
"/fban 6067657437",
"/fban 6248188104",
"/fban 5911068893",
"/fban 5611098596",
"/fban 6172534923",
"/fban 6059899702",
"/fban 5071778304",
"/fban 5993104795",
"/fban 5124430502",
"/fban 1907934084",
"/fban 1609733249",
"/fban 5254468548",
"/fban 2053086040",
"/fban 6007868906",
"/fban 6110650434",
"/fban 6019932382",
"/fban 6019022097",
"/fban 5944356260",
"/fban 5559823685",
"/fban 1887182335",
"/fban 1792533741",
"/fban 1762186707",
"/fban 1106164064",
"/fban 5975281577",
"/fban 5962498307",
"/fban 5925137686",
"/fban 5900226806",
"/fban 5473023883",
"/fban 5266978603",
"/fban 1327629097",
"/fban 532200178" ,
"/fban 6229911709",
"/fban 6051665347",
"/fban 5402265247",
"/fban 6091758079",
"/fban 5226523167",
"/fban 5649009129",
"/fban 5660913846",
"/fban 5572915371",
"/fban 5026539382",
"/fban 5367619129",
"/fban 1616918160",
"/fban 6100756410",
"/fban 6019931743",
"/fban 5756261664",
"/fban 5798740925",
"/fban 6118782307",
"/fban 5657076385",
"/fban 5027744664",
"/fban 6184912650",
"/fban 6105955010",
"/fban 6087947803",
"/fban 6242112498",
"/fban 6083167915",
"/fban 6005357605",
"/fban 5913471745",
"/fban 5416525472",
"/fban 5289750389",
"/fban 5745074845",
"/fban 5659749770",
"/fban 5555951276",
"/fban 5830842303",
"/fban 6240733177",
"/fban 6214321585",
"/fban 6127250993",
"/fban 5964491666",
"/fban 5951892207",
"/fban 5660039848",
"/fban 5315167062",
"/fban 5219626282",
"/fban 5084474478",
"/fban 1472218500",
"/fban 6209507824",
"/fban 5917246714",
"/fban 5470006469",
"/fban 5141141059",
"/fban 5460144604",
"/fban 5817467957",
"/fban 786013898" ,
"/fban 1632842537",
"/fban 5483441304",
"/fban 1140173295",
"/fban 6180984705",
"/fban 6050943230",
"/fban 5922618590",
"/fban 5895702454",
"/fban 5685110456",
"/fban 5405660679",
"/fban 5322330499",
"/fban 5912831496",
"/fban 5211534657",
"/fban 5024932820",
"/fban 1349068388",
"/fban 1155882472",
"/fban 1070635678",
"/fban 1025521845",
"/fban 6240899750",
"/fban 5190314420",
"/fban 6144993740",
"/fban 5896696661",
"/fban 1113332131",
"/fban 6284323641",
"/fban 5659834061",
"/fban 5374424377",
"/fban 5138722233",
"/fban 5052694056",
"/fban 5051129994",
"/fban 1703991382",
"/fban 652762555" ,
"/fban 5541482631",
"/fban 5468760829",
"/fban 5341632594",
"/fban 1967930038",
"/fban 5477021123",
"/fban 5315216144",
"/fban 1951406162",
"/fban 1307591441",
"/fban 5723866338",
"/fban 5125531775",
"/fban 2128843032",
"/fban 1838505143",
"/fban 1363530725",
"/fban 1183698471",
"/fban 1128185550",
"/fban 902858568" ,
"/fban 5700092089",
"/fban 5241985846",
"/fban 5175610541",
"/fban 5021950647",
"/fban 2024476324",
"/fban 1839041164",
"/fban 1771572044",
"/fban 1217785652",
"/fban 6248064569",
"/fban 6246973040",
"/fban 6075823916",
"/fban 5957257578",
"/fban 5411495349",
"/fban 2105044630",
"/fban 2085332053",
"/fban 6243890595",
"/fban 6001217484",
"/fban 5948257364",
"/fban 5920034874",
"/fban 5911167514",
"/fban 5908576088",
"/fban 5751553111",
"/fban 5680394940",
"/fban 5439223842",
"/fban 5344581351",
"/fban 5342393626",
"/fban 5131918387",
"/fban 2131927505",
"/fban 1751831356",
"/fban 1410037673",
"/fban 1321420718",
"/fban 6122164605",
"/fban 6276748507",
"/fban 6032856656",
"/fban 5939479046",
"/fban 5935689298",
"/fban 5736638280",
"/fban 5718220151",
"/fban 2027039578",
"/fban 1758186973",
"/fban 1556072514",
"/fban 6130771613",
"/fban 6051052850",
"/fban 5885043069",
"/fban 5868763987",
"/fban 5845748786",
"/fban 5839669722",
"/fban 5777912065",
"/fban 5727093642",
"/fban 5661219445",
"/fban 5591395829",
"/fban 5585491626",
"/fban 5555556643",
"/fban 5494304353",
"/fban 5240861693",
"/fban 5054320398",
"/fban 1943092007",
"/fban 1658503125",
"/fban 5861277223",
"/fban 6048218984",
"/fban 5171418937",
"/fban 5488124132",
"/fban 5671486505",
"/fban 5869247512",
"/fban 912804580" ,
"/fban 6042169014",
"/fban 5798973023",
"/fban 6152916604",
"/fban 6151294288",
"/fban 5254508123",
"/fban 2095337262",
"/fban 1888151255",
"/fban 1509621991",
"/fban 897602034" ,
"/fban 845097189" ,
"/fban 833025791" ,
"/fban 640908717" ,
"/fban 620989069" ,
"/fban 6041768676",
"/fban 5766582436",
"/fban 5724230696",
"/fban 5697952103",
"/fban 5027294251",
"/fban 1455785031",
"/fban 1339901458",
"/fban 1239889696",
"/fban 889658371" ,
"/fban 861213154" ,
"/fban 836403662" ,
"/fban 678212515" ,
"/fban 639366473" ,
"/fban 621701546" ,
"/fban 483605896" ,
"/fban 1924183425",
"/fban 5173600431",
"/fban 1900821691",
"/fban 730800106" ,
"/fban 6019589041",
"/fban 5798428818",
"/fban 5588963369",
"/fban 5461053137",
"/fban 5357485872",
"/fban 5278502330",
"/fban 5135803666",
"/fban 2006067662",
"/fban 1792988581",
"/fban 1689680143",
"/fban 1279043482",
"/fban 1226665776",
"/fban 1076453147",
"/fban 661115243" ,
"/fban 6206174511",
"/fban 6016306305",
"/fban 5760972390",
"/fban 5621475502",
"/fban 5546655534",
"/fban 5535221507",
"/fban 5475249991",
"/fban 2077297185",
"/fban 2040666209",
"/fban 1878569837",
"/fban 1754353735",
"/fban 1589288098",
"/fban 1201245683",
"/fban 1182053259",
"/fban 672519779" ,
"/fban 5281675205",
"/fban 861603017" ,
"/fban 5805214023",
"/fban 5787725741",
"/fban 5784026580",
"/fban 5714540633",
"/fban 5586032386",
"/fban 5520990816",
"/fban 5453448300",
"/fban 5364816483",
"/fban 5053161074",
"/fban 5049471731",
"/fban 5016913433",
"/fban 1973704946",
"/fban 1123505467",
"/fban 1922605546",
"/fban 1588961993",
"/fban 1584033983",
"/fban 1506277490",
"/fban 6161420169",
"/fban 6147596201",
"/fban 6056365961",
"/fban 6033812346",
"/fban 5964365118",
"/fban 5931275635",
"/fban 5772316924",
"/fban 5752923166",
"/fban 5732640920",
"/fban 5517129394",
"/fban 5431296320",
"/fban 5419855257",
"/fban 5117218835",
"/fban 1342825513",
"/fban 5263144174",
"/fban 5815486771",
"/fban 5692548150",
"/fban 5591780395",
"/fban 5535489973",
"/fban 5471106229",
"/fban 5241712637",
"/fban 5109927384",
"/fban 1937414067",
"/fban 1801194183",
"/fban 1239992593",
"/fban 5574212325",
"/fban 5417429471",
"/fban 955588827" ,
"/fban 5298223165",
"/fban 2056733157",
"/fban 1686776630",
"/fban 1477304516",
"/fban 893054593" ,
"/fban 6245848646",
"/fban 6133067544",
"/fban 6057709751",
"/fban 6040795824",
"/fban 5280072351",
"/fban 5237151990",
"/fban 5022483952",
"/fban 2097178691",
"/fban 1983063896",
"/fban 1822394790",
"/fban 1549287988",
"/fban 6020504771",
"/fban 6041840203",
"/fban 1484387130",
"/fban 6243429615",
"/fban 5636194972",
"/fban 6105831689",
"/fban 6033538089",
"/fban 5957837751",
"/fban 5165181282",
"/fban 2107176737",
"/fban 1782008124",
"/fban 1104459228",
"/fban 5884618366",
"/fban 1718062514",
"/fban 1426416301",
"/fban 5851596977",
"/fban 5277354041",
"/fban 1187196551",
"/fban 6232254355",
"/fban 5987786414",
"/fban 5920253674",
"/fban 5830158855",
"/fban 5820634764",
"/fban 5556446345",
"/fban 5290842098",
"/fban 5021417618",
"/fban 6224089213",
"/fban 6158878019",
"/fban 5053175623",
"/fban 1372955622",
"/fban 1351936790",
"/fban 6294895553",
"/fban 5884921554",
"/fban 5534222268",
"/fban 5368237357",
"/fban 5305584419",
"/fban 5288242587",
"/fban 5153470987",
"/fban 5929264251",
"/fban 5917821596",
"/fban 5060160947",
"/fban 2057427474",
"/fban 6041149500",
"/fban 1898298431",
"/fban 1557834912",
"/fban 1267883318",
"/fban 1223469546",
"/fban 1125943913",
"/fban 5561093201",
"/fban 5367037890",
"/fban 1957931216",
"/fban 1827876054",
"/fban 1718771977",
"/fban 1498853190",
"/fban 1450646301",
"/fban 1260430796",
"/fban 1243284085",
"/fban 6281077857",
"/fban 5991203618",
"/fban 5648263783",
"/fban 5560003979",
"/fban 705547045" ,
"/fban 6227461159",
"/fban 6053567227",
"/fban 2018786010",
"/fban 1897920875",
"/fban 1383653302",
"/fban 1301748278",
"/fban 1092485350",
"/fban 1004305158",
"/fban 5729241624",
"/fban 5630229032",
"/fban 5386734845",
"/fban 5008998991",
"/fban 1938561818",
"/fban 1829484779",
"/fban 1798553532",
"/fban 1770966173",
"/fban 1760785902",
"/fban 1069159546",
"/fban 6232871120",
"/fban 1008836460",
"/fban 981331244" ,
"/fban 979992288" ,
"/fban 968654059" ,
"/fban 912879822" ,
"/fban 815821064" ,
"/fban 798330072" ,
"/fban 509045208" ,
"/fban 447644718" ,
"/fban 1202539732",
"/fban 1181744198",
"/fban 1137673192",
"/fban 871417370" ,
"/fban 860580985" ,
"/fban 850298067" ,
"/fban 840342728" ,
"/fban 6194792340",
"/fban 5892110835",
"/fban 5329854085",
"/fban 5326059456",
"/fban 5217760587",
"/fban 5180107555",
"/fban 954095693" ,
"/fban 6131242136",
"/fban 6034810118",
"/fban 5775259362",
"/fban 5769198224",
"/fban 5591527853",
"/fban 5533765588",
"/fban 5510540772",
"/fban 5087551133",
"/fban 2062311247",
"/fban 1978956381",
"/fban 1626422062",
"/fban 1456862740",
"/fban 6068931508",
"/fban 5676452465",
"/fban 5181424756",
"/fban 1288514700",
"/fban 5538787786",
"/fban 5501561072",
"/fban 5487480567",
"/fban 5181060870",
"/fban 5134936750",
"/fban 1847476473",
"/fban 1760019351",
"/fban 1576348728",
"/fban 1336871870",
"/fban 1213695408",
"/fban 1170864096",
"/fban 1117870054",
"/fban 1076895370",
"/fban 883970548" ,
"/fban 879880056" ,
"/fban 643824909" ,
"/fban 1304943505",
"/fban 5944696484",
"/fban 2051451827",
"/fban 1755238454",
"/fban 1207463824",
"/fban 1206142630",
"/fban 670176992" ,
"/fban 5580642501",
"/fban 5370085339",
"/fban 5057259863",
"/fban 5011844556",
"/fban 1721035995",
"/fban 1374806611",
"/fban 1357963270",
"/fban 1174013246",
"/fban 1168276744",
"/fban 1023855620",
"/fban 6190529752",
"/fban 5648112760",
"/fban 5063470583",
"/fban 1022202356",
"/fban 708490097" ,
"/fban 1405786655",
"/fban 5652362148",
"/fban 1179168340",
"/fban 1126054272",
"/fban 1124776965",
"/fban 1121857489",
"/fban 1081958440",
"/fban 1081504482",
"/fban 1079867903",
"/fban 1079120345",
"/fban 1073736254",
"/fban 1073156285",
"/fban 1071810801",
"/fban 1032421963",
"/fban 6227025845",
"/fban 1282659242",
"/fban 1199092375",
"/fban 6128998839",
"/fban 5518148965",
"/fban 5672121156",
"/fban 5191909671",
"/fban 5887314160",
"/fban 5828059352",
"/fban 1798619272",
"/fban 1484349086",
"/fban 5377480905",
"/fban 6215496554",
"/fban 6077401816",
"/fban 5199132722",
"/fban 1094967617",
"/fban 1073900284",
"/fban 1003877412",
"/fban 942733333" ,
"/fban 2003642411",
"/fban 1099481302",
"/fban 1032967552",
"/fban 938678006" ,
"/fban 1306712435",
"/fban 1302740744",
"/fban 1294922114",
"/fban 1294658993",
"/fban 1288193819",
"/fban 1277716588",
"/fban 1271026836",
"/fban 1259702628",
"/fban 1259439228",
"/fban 1258889778",
"/fban 1256249278",
"/fban 1251790175",
"/fban 1235023923",
"/fban 1232418731",
"/fban 1229346222",
"/fban 1226150452",
"/fban 1210994794",
"/fban 1186471706",
"/fban 1183237618",
"/fban 763934106" ,
"/fban 2063623109",
"/fban 1281164420",
"/fban 1251056039",
"/fban 1240396421",
"/fban 1239441779",
"/fban 1235725242",
"/fban 1186312128",
"/fban 6226545436",
"/fban 6112746083",
"/fban 6015564788",
"/fban 5333428810",
"/fban 5204026006",
"/fban 1825997347",
"/fban 1674213900",
"/fban 1411927727",
"/fban 1213755344",
"/fban 616838539" ,
"/fban 5739023126",
"/fban 1810967570",
"/fban 5153120133",
"/fban 6243789239",
"/fban 903349624" ,
"/fban 6202582426",
"/fban 6179361875",
"/fban 6113870458",
"/fban 5872480917",
"/fban 5827367978",
"/fban 5546391376",
"/fban 1809332336",
"/fban 1321671776",
"/fban 6232481336",
"/fban 6105648756",
"/fban 6036416069",
"/fban 5673641041",
"/fban 5527611420",
"/fban 5521439543",
"/fban 5230877269",
"/fban 5028711088",
"/fban 6191109944",
"/fban 5182966465",
"/fban 2136740964",
"/fban 5563953196",
"/fban 1854612733",
"/fban 1215013990",
"/fban 6213827305",
"/fban 6056569679",
"/fban 6038172369",
"/fban 5747859652",
"/fban 5972345783",
"/fban 5533497910",
"/fban 1286544671",
"/fban 5193958992",
"/fban 5122982604",
"/fban 5839873441",
"/fban 5598890394",
"/fban 6241857897",
"/fban 6199387441",
"/fban 6190723691",
"/fban 6179119786",
"/fban 6147504686",
"/fban 6035792079",
"/fban 6032465251",
"/fban 5969428795",
"/fban 5895366090",
"/fban 5880578101",
"/fban 5856523182",
"/fban 5792693133",
"/fban 5753740895",
"/fban 5708045319",
"/fban 5695020783",
"/fban 5664525639",
"/fban 5581819210",
"/fban 5570996030",
"/fban 5568078031",
"/fban 5466836460",
"/fban 5464717317",
"/fban 5456059179",
"/fban 5403200018",
"/fban 5249347797",
"/fban 5090253541",
"/fban 5062064106",
"/fban 5010671950",
"/fban 2081077970",
"/fban 2019888385",
"/fban 1970671647",
"/fban 1953377863",
"/fban 1739061740",
"/fban 1426718414",
"/fban 1305531481",
"/fban 6030229754",
"/fban 1988178425",
"/fban 1805964956",
"/fban @DIMPLE",
"/fban @Insane_02",
"/fban @divyanka09",
"/fban @fuck_thehoes123",
"/fban @hum_vs_tum",
"/fban @its_not_like_that",
"/fban @alone765J",
"/fban @Vowemes2",
"/fban @VINASHINI_OP",
"/fban @Laugh_happy",
"/fban @Aayesha10",
"/fban @Op_Piyush_Assistant_2",
"/fban @ItsAaditya",
"/fban @Queen123344645",
"/fban @Sophiawilliams241",
"/fban @MahadevoO",
"/fban @shaibumubin",
"/fban @itzKanikaa",
"/fban @SangMata_BOT",
"/fban @Il_FARISTA_ll",
"/fban @zfzecr",
"/fban @Kameshkrrish",
"/fban @MohamedsulthanulAriffm",
"/fban @YOUR_DADDYY_GODFATHER",
"/fban @Adnanmirza14",
"/fban @AdIsH18",
"/fban @Cute_smile18",
"/fban @sharmaji_5926q",
"/fban @Krishna_Uk07",
"/fban @PawanManuja",
"/fban @Kuuuuuunal",
"/fban @mr_hacker79",
"/fban @Sjsjsusiis",
"/fban @Abhipandey_307",
"/fban @sahilbadgal09",
"/fban @Bhaskar2428",
"/fban @Subhash5801",
"/fban @npkholi",
"/fban @lalajanhaviiii",
"/fban @priyanshupandey1121",
"/fban @Kimseokook",
"/fban @nishantydv007",
"/fban @Simmu_086",
"/fban @pihu_xd",
"/fban @Mr_Rahulop1432",
"/fban @II_FUCK_III",
"/fban @Bhole_ka_diwana_006",
"/fban @Maf_iya",
"/fban @TOP_VALO_KA_PAPA_HATIYARA",
"/fban @SIMMU_HU_BE",
"/fban @King_khan_078",
"/fban @mahakal_24",
"/fban @Anaya_ak47",
"/fban @BARTHOMEWROBERTS",
"/fban @ll_GABBER_MUSIC_ll",
"/fban @rajonlinet",
"/fban @thakur5009",
"/fban @royal_x_chirag",
"/fban @AtharvOnTop",
"/fban @Neiljain",
"/fban @Naveenbeniwal_1020",
"/fban @TheyWillCover",
"/fban @Adityak965496",
"/fban @Love143ume",
"/fban @user_7_dead",
"/fban @Alexupsi",
"/fban @bad_boy_109",
"/fban @Alonejangra",
"/fban @kalpu7555",
"/fban @Amruthaaxb",
"/fban @riiyan666",
"/fban @Rj123567",
"/fban @Sinchan_6",
"/fban @Sarveshwanjari",
"/fban @irfu79",
"/fban @Chaand2020",
"/fban @Prince_g_75",
"/fban @Khutailnishant",
"/fban @Justtkevin",
"/fban @ABDULRUB12",
"/fban @Neeraj2511",
"/fban @Adityasingh1087",
"/fban @j_ram_ram",
"/fban @kakashi_uchi",
"/fban @Naved_7617",
"/fban @AftabmansuriBATCHC",
"/fban @kirti112",
"/fban @mr_choco_dz",
"/fban @broskiu",
"/fban @Rishu_Rajput_0001",
"/fban @natashuo",
"/fban @Anushzzz6",
"/fban @Satyam_Rai785",
"/fban @Oye_bittuu",
"/fban @anjaliji12",
"/fban @Nalla_lucifer",
"/fban @avinsh16",
"/fban @Brody_2022",
"/fban @Manikant25",
"/fban @HiImLouie",
"/fban @somvansi_Aditya",
"/fban @Mohitsahu5",
"/fban @Jibrinhussaini",
"/fban @Raja_singh_o",
"/fban @officialmodak",
"/fban @purpleburry",
"/fban @musuhere",
"/fban @Rajuyadav12121",
"/fban @Rupanwitaa",
"/fban @heart_haker_harsh",
"/fban @akt87",
"/fban @Shubham01819",
"/fban @Rockyrakesh12",
"/fban @drAmrita_Gyne",
"/fban @BusaGolden",
"/fban @Itz_Mysterious",
"/fban @RAJKUMAR1631",
"/fban @Tanvi_1390",
"/fban @Kd3266713",
"/fban @itzz_sonu004",
"/fban @chiku548",
"/fban @Blackdevil00999",
"/fban @xoyxoyxc",
"/fban @Aashi_singh2323",
"/fban @VIJAY_YADAV_NCR",
"/fban @Shreaya_1612",
"/fban @Princess_Rose_07",
"/fban @Betu_ki_jaan_hu",
"/fban @Akansh00",
"/fban @anvi091",
"/fban @The_Warrier_AP",
"/fban @Satan_thisside",
"/fban @PrabhakarJha28",
"/fban @Ashu19p",
"/fban @Priyal_1430",
"/fban @Cute_pari_03",
"/fban @satyam_patel_6",
"/fban @Siyu_457",
"/fban @Radhe0070",
"/fban @Kulalganna",
"/fban @kundan_raj_09",
"/fban @TIGERKING121",
"/fban @ABHISHEKP8",
"/fban @Itsqueen1",
"/fban @Loveislife1234567",
"/fban @madhavi7171",
"/fban @Itsdestiny6",
"/fban @arxh_002",
"/fban @Thakurhanee_1",
"/fban @KARTIK90909000",
"/fban @PS_0704",
"/fban @Vedhamsh_akash",
"/fban @Amritanshurajgupta",
"/fban @Bhoi07",
"/fban @Rimmy_savrana",
"/fban @Intzaar_me_mout",
"/fban @Itz_kartik_op",
"/fban @itxxxL",
"/fban @Rajatsng7",
"/fban @WtfExon",
"/fban @Charak1",
"/fban @Swapn3IL",
"/fban @player_kown",
"/fban @Rohanrony123",
"/fban @BAJIRAOBRO",
"/fban @Ayushivermatrust",
"/fban @PIDUGUBALU",
"/fban @RealSlimShady008",
"/fban @Bsv_Mp4",
"/fban @BAD_B0Y_O6",
"/fban @ggjjmm",
"/fban @abhii16",
"/fban @KBR59",
"/fban @gouravbadmash",
"/fban @beingwajeed_03",
"/fban @AjitchauhanajOO7",
"/fban @lubina_nazar",
"/fban @Mishrabalkrishna",
"/fban @Bhushanchugh",
"/fban @anaesthesia56",
"/fban @darshak_katariya_160",
"/fban @dabanggg_ladka_0777",
"/fban @darken_thinker005",
"/fban @deni7779",
"/fban @Dhanush_99",
"/fban @Deshan_Aberathna",
"/fban @vedsen",
"/fban @Mrbeast089",
"/fban @Luckydhikyav",
"/fban @Jatintyagi280",
"/fban @GCVIJAY2005",
"/fban @Rahuljariwala4",
"/fban @Unnownm",
"/fban @official_patel_here",
"/fban @Luciferwasinocent1",
"/fban @Chiranjib007",
"/fban @A_sweet_memory",
"/fban @Mummykiladli",
"/fban @mann_0419",
"/fban @ashu9113",
"/fban @Alone_35_g",
"/fban @Alone_girl_35",
"/fban @sukhbirji",
"/fban @heyRosie001",
"/fban @Pragya_is_here",
"/fban @WAM1991",
"/fban @sarizwani",
"/fban @Shakey22",
"/fban @Sharonl_n",
"/fban @Maybe_gurjot",
"/fban @AlmightyFinancialService",
"/fban @visuadi001",
"/fban @Md_shamimofficial",
"/fban @Anshu_harpal",
"/fban @DhimanDey69",
"/fban @fiorellaRoditti",
"/fban @Editor6_9",
"/fban @Blue_0o9",
"/fban @Jstt_ayushhh",
"/fban @fkhan185",
"/fban @Professionalpurveyor",
"/fban @Amandalariissah",
"/fban @Cute_ladki8",
"/fban @gdeniksuk",
"/fban @Ineedyourloveplease",
"/fban @Md_tausif_67_27",
"/fban @RudrakshChawla",
"/fban @jitesh_9472",
"/fban @Pankhurimehra",
"/fban @nikhil_asya"]

async def pyrone(client: Client, message: Message):
    chat_id = message.chat.id
    ruser = None

    if message.reply_to_message:
        ruser = message.reply_to_message.message_id
    
    try:
        for word in ONE_WORDS:
            await client.send_chat_action(chat_id, "typing")
            await client.send_message(chat_id, word, reply_to_message_id=ruser)
            await asyncio.sleep(0.3)
    except FloodWait:
        pass


async def restart(_, __):
    args = [sys.executable, "pyrone.py"]
    execle(sys.executable, *args, environ)


# ADDING HANDLERS

if M1:
    M1.add_handler(MessageHandler(pyrone, filters.command(["RANDI", "TERI MAA KO CHODU", "RANDI TERI MAA", "BAAP SE LDEGA", "RANDIKE"], prefixes=None) & filters.me))
    M1.add_handler(MessageHandler(restart, filters.command(["HAHAH", "#farar", "bisi", "#fucked"], prefixes=None) & filters.me))

if M2:
    M2.add_handler(MessageHandler(pyrone, filters.command(["T3RI", "L0L", "AJA", "AAJA", "RANDIII"], prefixes=None) & filters.me))
    M2.add_handler(MessageHandler(restart, filters.command(["XD", "#FARAR", "STOP", "FUCKED"], prefixes=None) & filters.me))

if M3:
    M3.add_handler(MessageHandler(pyrone, filters.command(["T3RI", "L0L", "AJA", "AAJA", "START"], prefixes=None) & filters.me))
    M3.add_handler(MessageHandler(restart, filters.command(["XD", "FARAR", "STOP", "FUCKED"], prefixes=None) & filters.me))

if M4:
    M4.add_handler(MessageHandler(pyrone, filters.command(["T3RI", "L0L", "AJA", "AAJA", "START"], prefixes=None) & filters.me))
    M4.add_handler(MessageHandler(restart, filters.command(["XD", "FARAR", "STOP", "FUCKED"], prefixes=None) & filters.me))

if M5:
    M5.add_handler(MessageHandler(pyrone, filters.command(["T3RI", "L0L", "AJA", "AAJA", "START"], prefixes=None) & filters.me))
    M5.add_handler(MessageHandler(restart, filters.command(["XD", "FARAR", "STOP", "FUCKED"], prefixes=None) & filters.me))


# STARTING CLIENTS

if M1:
    M1.start()
    M1.join_chat("TheAltron")

if M2:
    M2.start()
    M2.join_chat("TheAltron")

if M3:
    M3.start()
    M3.join_chat("TheAltron")

if M4:
    M4.start()
    M4.join_chat("TheAltron")

if M5:
    M5.start()
    M5.join_chat("TheAltron")

print("Pyro-one Started Successfully")

idle()


# STOPPING CLIENTS

if M1:
    M1.stop()

if M2:
    M2.stop()

if M3:
    M3.stop()

if M4:
    M4.stop()

if M5:
    M5.stop()
