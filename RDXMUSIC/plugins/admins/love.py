from RDXMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]
        ####
        
LOVETAG = LOVERAID = [
    "HATE ME I DONT CARE",
    "LEAVE ME I DONT CARE",
    "EK TU H TU H RHYGII",
    "TERE BIN MAR JAUNGA",
    "TU MERI H SMJI?",
    "KOI TERE MERE BEECH AYA MARDUNGA OSE",
    "TERE LIYE MAR B SKTA HU MAR B SKTA HU",
    "TERE SE JITNA MRJI GUSSA HO JAUN BUT I LOVE U YARR",
    "TERE LIE IS DUNIA SE LAD JAUNGA",
    "ANKO SE ANKHE MILAKE KHWAB CHURA LU TERE",
    "TERA ISHQ PANE LIE KITNE BETAN HU KESE BATAU TUJE",
    "ME JO JEE RHA HU WAJH TUM HO",
    "TU H TO M HU TUJSE M HU",
    "TUJE KITNA CHAHNE LAGE HAM KI SHBO M BYAN NA KAR PAYNGE",
    "CURRENT STATUS  I WANT TO HUG YOU AND WANAA CARRY LOUD",
    "I NEED YOU IN MY BAD IN MY GOOD",
    "HMESHA TERE SATH HU",
    "TERE SE KADM SE KDM MILAKE CHALNA CHHTA HU",
    "TUJE APNI SHOTI SI DUNIA KA EK BHT BADA HISA BANANA CHAHTA HU",
    "KYA JANE TU MERE IRADHE LE JAUNGA TERI SANSE CHURAKE",
    "DIL KHE RHA KI GUNHGAGAR BAN JA BADA SKOON H IN GUNAHO M",
    "MERI KHUSHNMA SUBH H TU",
    "MERI JAAN H TU",
    "EVEN TUJE IDEA B NHI H KI TERE EK SINGLE MESSAGE KA WAIT KRTE KRTE KITAN ROYA HU",
    "TUJE PANE LIE BHT TDFA HU",
    "KABI KABI LGTA H KI TUN MUJSE NHT DUR JA RHI H",
    "I DONT CARE ABOUT WORD BS I NEED YOU",
    "TUN BAS MERI H MERI RHNA",
    "BHT ROTA HU TERE LIE AKELA ME",
    "H YE NSHA YAN H JEHAR IS PYAR KO KYA NAM DU",
    "HMARE PYAR KI H YE ADHURI DASTA KI TUN PASS HOKE B BHT DOOR H",
    "PLZZ KABI MAT SHODNA MUJE I CANT LIVE WITHOUT YOU",
    "DO JISM H BUT EK JAAN H HAM DO",
    "MUJE BAS TU CHHIE NAHI PTA KYU BUT CHHIE TU H",
    "THERE ARE MANY PEOPLE IN WORLD BUT I ONLY NEED YOU",
    "WO TERA GUSSA HONA JHGDE KRNE I MISS YOU",
    "BHT PYAR KRTA HU TERE SE PLZZ DONT LEAVE ME",
    "Tere naalo challiye haseen koyi NA 😁😁",
    "Taare chann ambar zameen koyi nA",
    "Main Jado Tere Mode Utte Sir Rakheya🧐🧐",
    "Eh Ton Sachi Sama Vi Haseen Koi Na😖😖",
    "Sohniyan Vi Laggan Giyan Fer Walian😍😍",
    "Galan Nal Jado Takraiyan Waliyan🥰🥰",
    "Tare Dekhi Labh Labh Kiven Harde😁😁",
    "Tu Bala Ch Lakoiyan Jado Ratan Kaliyan😒😒",
    "Main Sab Kuj Har Tere Utton De’unga😌😌",
    "Sab Kuj War Tere Utton De’unga😉😉",
    "Akhir Ch Jan Tainu De’un Apni😎😎",
    "Chala Tainu Bhavein Pehli War De’unga😚😚",
    "Han Main Cheti Cheti Lawan😫😫",
    "Tere Nal Laini an😣😣",
    "Samay Da Tan Bhora Vi Yakeen Koi Na🥺🥺",
    "Tere Nalo Jhaliye Haseen Koi Na🥰🥰",
    "Tare Chann Ambar Zameen Koi Na😘😘",
    "Tere Nalo Jhaliye Haseen Koi Na😍😍",
    "Tare Chann Ambar Zameen Koi Na🥰🥰",
    "Main Jado Tere Mode Utte Sir Rakheya😁😁",
    "Eh Ton Sachi Sama Vi Haseen Koi Na😒😒",
    "Tu Yar Mera Tu Hi Ae Sahara AdiyE",
    "Main Pani Tera Mera Tu Kinara Adiye",
    "Phul Ban Jai Main Khushboo Bann Ju",
    "Deevan Bani Mera Teri Lau Ban Ju",
    "Haye Ujadiyan Thawan Te Banate Bag Ne",
    "Teriyan Ankhan Ne Kitte Jadu Yad Ne",
    "Jado Wang Kolon Phadi Vi Ni KassKe",
    "Totte Sambh Rakhe Tutte Hoye Kach De",
    "Han Ki Dil Yadan Rakhda Ae, Sambh Sambh Ke",
    "Hor Dil Sajjna Machine Koi Na",
    "Tere Nalo Jhaliye Haseen Koi Na",
    "Tare Chann Ambar Zameen Koi Na",
    "Tere Nalo Jhaliye Haseen Koi Na",
    "Tare Chann Ambar Zameen Koi Na",
    "Main Jado Tere Mode Utte Sir Rakheya",
    "Eh Ton Sachi Sama Vi Haseen Koi Na",
    "Kine Din Hogye Meri Akh Soi Na",
    "Tere Ton Bagair Mera Aithe Koi Na",
    "Tu Bhukh Vi Ae Tu Hi Ae Guzara Adiye",
    "Mannu Sab Kari Tu Ishara Adiye",
    "Ho Khaure Kinni War Seene Vich Khubiyan",
    "Surme De Vich Dovein Ankhan Dubbiyan",
    "Kini Sohni Lagge Jadon Chup Kar Je",
    "Jandi Jandi Shaman Nu Vi Dhup Kar Je",
    "Haye Main Paun Farmaishi Rang Tere Sohniye",
    "Unj Bahotan Gifty Shaukeen Koi Na",
    "Tere Nalo Jhaliye Haseen Koi Na😍😍",
    "Tare Chann Ambar Zameen Koi Na🥰🥰",
    "Tere Nalo Jhaliye Haseen Koi Na😍😍",
    "Tare Chann Ambar Zameen Koi Na🥰🥰",
    "Main Jado Tere Mode Utte Sir Rakheya😁😁",
    "Eh Ton Sachi Sama Vi Haseen Koi Na😒😒",
    "Kanna Wich Jhumka👀👀",
    "Akhan Wich Surma🙈🙈",
    "Ho Jaise Strawberry Candy😋😋",
    "Nakk Utte Koka🤨🤨",
    "Jeena Kare Aukha🤭🤭",
    "Haye Meri Jaan Kadd Laindi😌😌",
    "Tere Nakhre Haye Tauba Sanu Maarde🤫🤫",
    "Ho Gaya Hai Mera Baby Bura HaaL😊😊",
    "Sachi Lut Gaye Hum Tere Is Pyar Mein😏😏",
    "Jeeni Zindagi Hai Bas Tere Naal😚😚",
    "cause I Love You 😘😘",
    "I Love YoU SO MUCH 😍😍",
    "cause I Love You 😘😘",
    "I Love YoU SO MUCH 😍😍",
    "Sapno Mein Mere AayI😝😝",
    "Uff Oh Phir Neendein Hi Churayi😜😜",
    "Oh No! Tera Husan Nazara🥰🥰",
    "Baby! Lage Sohna Kitna PyarA😚😚",
    "Sapno Mein Mere Aayi😝😝",
    "Uff Oh Phir Neendein Hi Churayi😜😜",
    "Oh No! Tera Husan Nazara🥰🥰",
    "Baby! Lage Sohna Kitna PyarA😚😚",
    "Tainu Diamond Mundri Pehnawa😎😎",
    "Naale Duniya Sari Ghumawa🙈🙈",
    "Chhoti-Chhoti Gallan Utte Main Hasavaan💙💙",
    "Yaara Kade Vi Na Tainu Main Rulawaan🙊🙊",
    "cause I Love You  🙈🙈",
    "I Love You ❤️❤️",
    "cause I Love You🙈🙈",
    "I Love You ❤️❤️",
    "Yaari Laawan Sachi YaarI💫💫",
    "Tu Jaan Ton Vi Pyari😁😁",
    "Will Love You To The Moon And Back😆😆",
    "Hogi Saza Na Koyi Hogi😙😙",
    "Chahe Karun Chori Chaand Taare😉😉",
    "Imma Give You Them😅😅",
    "Yaari Laavan Sachi YaarI😘😘",
    "Tu Jaan Ton Vi PyarI😆😆",
    "Will Love You To The Moon And Back💕💕",
    "Hogee Sazaa Na Koyi Hogi💓💓",
    "Chahe Karun Chori Chaand Taare🥺🥺",
    "Imma Give You Them🥵🥵",
    "Puri Karunga Main Teri Sari Khahishein😁😁",
    "Tera Rakhanga Main Rajj Ke Khayal😘😘",
    "Kitni Khoobiyan Hai Tere Is Yaar Mein🥰🥰",
    "Aaja Bahon Mein Tu Bahein Bas Daal😂😂",
    "Aur Hota Nahi Ab Intezar🤩🤩",
    "Aur Hota Nahee Ab Intezaar😘😘",
    "cause I Love You 😍😍",
    "I Love YoU 😙😙",
    "cause I Love You",
    "I Love YoU SOOOOOOOOOOOOOOOOOO MUCHHHHHHHHHHHHHHHHHHHHH 😘😘",
    "WILL U BE MINE FOREVER??🤔🤔",
    "Je tu akh te main aan kaajal ve😌😌",
    "Tu baarish te main baadal ve🤫🤫",
    "Tu deewana main aan paagal ve🤪🤪",
    "Sohneya sohneya☺️☺️",
    "Je tu chann te main aan taara ve🤗🤗",
    "Main lehar te tu kinara ve😶😶",
    "Main aadha te tu saara ve🤗🤗",
    "Sohneya sohneya😗😗",
    "Tu jahan hai main wahan😘😘",
    "Tere bin main hoon hi kya🥲🥲",
    "Tere bin chehre se mere🤔🤔",
    "Udd jaaye rang ve😅😅",
    "Tujhko paane ke liye huM😁😁",
    "Roz mangein mannat ve🙈🙈",
    "Duniya to kya cheez hai yaara🙉🙉",
    "Thukra denge jannat ve😌😌",
    "Tujhko paane ke liye hum😌😌",
    "Roz mangein mannat ve🤫🤫",
    "Duniya to kya cheez hai yaara🤔🤔",
    "Thukra denge jannat ve😌😌",
    "Na parwah mainu apni aa😁😁",
    "Na parwah mainu duniya di👅👅",
    "Na parwah mainu apni aa😅😅",
    "Na parwah mainu duniya di👅👅",
    "Tere ton juda nahi kar sakdi🤬🤬",
    "Koyi taakat mainu duniya di😈😈",
    "Dooron aa jaave teri khushbu😎😎",
    "Akhan hun band taan vi vekh lawan😍😍",
    "Teri gali vich mera auna har roz😋😋",
    "Tera ghar jadon aave matha tek lawan😌😌",
    "Nirmaan tujhko dekh ke😏😏",
    "Aa jaave himmat ve😉😉",
    "Tujhko paane ke liye hum😊😊",
    "Roz mangein mannat ve😉😉",
    "Duniya to kya cheez hai yaara😌😌",
    "Thukra denge jannat ve😍😍",
    "Tujhko paane ke liye hum🤫🤫",
    "Roz mangein mannat ve😁😁",
    "Duniya to kya cheez hai yaara😏😏",
    "Thukra denge jannat ve😌😌",
    "SO MISS 😶😶",
    "KYA SOCHA APNE BAARE MAIN😆😆",
    "BADI MUSHKIL SE YEH SAB KARA H RE🥵🥵",
    "PAHLE PURA BOT HI KANG MAAR DIYA BUT🤫🤫",
    "WAHI ERROR AAYE JO AATE THE🥲🥲",
    "BUT TUMHARA HO CHUKA WALA BF😎😎",
    "AND FUTURE HUSBAND JO BANNE WALA THA WO BHOT SMART H RE😌😌",
    "ISS BAAR BOT BANAYA AND CHOTA SA EDIT KARA BAS😁😁",
    "AUR DEKO ABHI TUM USSI BOT SE YEH PADH PAA RHI😂😂",
    "HEHE BTW YEH CHORO MEKO NA TUMSE😶😶",
    "KUCH PUCHNA THA KI ME🤔🤔",
    "TUMHARE KABIL HU YA",
    "TUMHARE KABIL NHI😂💓",
    "AND EK AUR BAAT BOLNI THI KI😙😙",
    "I REALLY REALLY DEEPLY😙😙",
    "LOVE YOU FROM MY HEART TO YOUR HEAT AND MY SOUL ATTACHED BY YOUR SOUL CAN YOU BE MINE FOREVER😌😌❤️",
    "इश्क़ है या कुछ और ये पता नहीं, पर जो तुमसे है किसी और से नहीं 😁😁",
    "मै कैसे कहू की उसका साथ कैसा है, वो एक शख्स पुरे कायनात जैसा है ",
    " तेरा होना ही मेरे लिये खास है, तू दूर ही सही मगर मेरे दिल के पास है ",
    "मुझे तेरा साथ ज़िन्दगी भर नहीं चाहिये, बल्कि जब तक तू साथ है तबतक ज़िन्दगी चाहिए 😖😖",
    "तुझसे मोहब्बत कुछ अलग सी है मेरी, तुझे खयालो में नहीं दुआओ में याद करते है😍😍",
    "तू हज़ार बार भी रूठे तो मना लूँगा तुझे",
    "मगर देख मोहब्बत में शामिल कोई दूसरा ना हो😁😁",
    "किस्मत यह मेरा इम्तेहान ले रही है😒😒",
    "तड़प कर यह मुझे दर्द दे रही है😌😌",
    "दिल से कभी भी मैंने उसे दूर नहीं किया😉😉",
    "फिर क्यों बेवफाई का वह इलज़ाम दे रही है😎😎",
    "मरे तो लाखों होंगे तुझ पर😚😚",
    "मैं तो तेरे साथ जीना चाहता हूँ😫😫",
    "वापस लौट आया है हवाओं का रुख मोड़ने वाला😣😣",
    "दिल में फिर उतर रहा है दिल तोड़ने वाला🥺🥺",
    "अपनों के बीच बेगाने हो गए हैं🥰🥰",
    "प्यार के लम्हे अनजाने हो गए हैं😘😘",
    "जहाँ पर फूल खिलते थे कभी😍😍",
    "आज वहां पर वीरान हो गए हैं🥰🥰",
    "जो शख्स तेरे तसव्वुर से हे महक जाये😁😁",
    "सोचो तुम्हारे दीदार में उसका क्या होगा😒😒",
    "मोहब्बत का एहसास तो हम दोनों को हुआ था",
    "फर्क सिर्फ इतना था की उसने किया था और मुझे हुआ था",
    "सांसों की डोर छूटती जा रही है",
    "किस्मत भी हमे दर्द देती जा रही है",
    "मौत की तरफ हैं कदम हमारे",
    "मोहब्बत भी हम से छूटती जा रही है",
    "समझता ही नहीं वो मेरे अलफ़ाज़ की गहराई",
    "मैंने हर लफ्ज़ कह दिया जिसे मोहब्बत कहते है",
    "समंदर न सही पर एक नदी तो होनी चाहिए",
    "तेरे शहर में ज़िन्दगी कही तो होनी चाहिए",
    "नज़रों से देखो तोह आबाद हम हैं",
    "दिल से देखो तोह बर्बाद हम हैं",
    "जीवन का हर लम्हा दर्द से भर गया",
    "फिर कैसे कह दें आज़ाद हम हैं",
    "मुझे नहीं मालूम वो पहली बार कब अच्छा लगा",
    "मगर उसके बाद कभी बुरा भी नहीं",
    "सच्ची मोहब्बत कभी खत्म नहीं होती",
    "वक़्त के साथ खामोश हो जाती है",
    "ज़िन्दगी के सफ़र में आपका सहारा चाहिए",
    "आपके चरणों का बस आसरा चाहिए",
    "हर मुश्किलों का हँसते हुए सामना करेंगे",
    "बस ठाकुर जी आपका एक इशारा चाहिए",
    "जिस दिल में बसा था नाम तेरा हमने वो तोड़ दिया",
    "न होने दिया तुझे बदनाम बस तेरे नाम लेना छोड़ दिया",
    "प्यार वो नहीं जो हासिल करने के लिए कुछ भी करव दे",
    "प्यार वो है जो उसकी खुशी के लिए अपने अरमान चोर दे",
    "आशिक के नाम से सभी जानते हैं😍😍",
    "इतना बदनाम हो गए हम मयखाने में🥰🥰",
    "जब भी तेरी याद आती है बेदर्द मुझे😍😍",
    "तोह पीते हैं हम दर्द पैमाने में🥰🥰",
    "हम इश्क़ के वो मुकाम पर खड़े है😁😁",
    "जहाँ दिल किसी और को चाहे तो गुन्हा लगता है😒😒",
    "सच्चे प्यार वालों को हमेशा लोग गलत ही समझते है👀👀",
    "जबकि टाइम पास वालो से लोग खुश रहते है आज कल🙈🙈",
    "गिलास पर गिलास बहुत टूट रहे हैं😋😋",
    "खुसी के प्याले दर्द से भर रहे हैं🤨🤨",
    "मशालों की तरह दिल जल रहे हैं🤭🤭",
    "जैसे ज़िन्दगी में बदकिस्मती से मिल रहे हैं😌😌",
    "सिर्फ वक़्त गुजरना हो तो किसी और को अपना बना लेना🤫🤫",
    "हम दोस्ती भी करते है तो प्यार की तरह😊😊",
    "जरूरी नहीं इश्क़ में बनहूँ के सहारे ही मिले😏😏",
    "किसी को जी भर के महसूस करना भी मोहब्बत है😚😚",
    "नशे में भी तेरा नाम लब पर आता है😘😘",
    "चलते हुए मेरे पाँव लड़खड़ाते हैं😍😍",
    "दर्द सा दिल में उठता है मेरे😘😘",
    "हसीं चेहरे पर भी दाग नजर आता है😍😍",
    "हमने भी एक ऐसे शख्स को चाहा😝😝",
    "जिसको भुला न सके और वो किस्मत मैं भी नहीं😜😜",
    "सच्चा प्यार किसी भूत की तरह होता है🥰🥰",
    "बातें तो सब करते है देखा किसी ने नहीं😚😚",
    "मत पूछ ये की मैं तुझे भुला नहीं सकता😝😝",
    "तेरी यादों के पन्ने को मैं जला नहीं सकता😜😜",
    "संघर्ष यह है कि खुद को मारना होगा🥰🥰",
    "और अपने सुकून की खातिर तुझे रुला नहीं सकता😚😚",
    "दुनिया को आग लगाने की ज़रूरत नहीं😎😎",
    "Naale Duniya Sari Ghumawa🙈🙈",
    "तो मेरे साथ चसल आग खुद लग जाएगी💙💙",
    "तरस गये है हम तेरे मुंह से कुछ सुनने को हम🙊🙊",
    "प्यार की बात न सही कोई शिकायत ही कर दे  🙈🙈",
    "तुम नहीं हो पास मगर तन्हाँ रात वही है ❤️❤️",
    "वही है चाहत यादों की बरसात वही है🙈🙈",
    "हर खुशी भी दूर है मेरे आशियाने से ❤️❤️",
    "खामोश लम्हों में दर्द-ए-हालात वही है💫💫",
    "करने लगे जब शिकवा उससे उसकी बेवफाई का😁😁",
    "रख कर होंट को होंट से खामोश कर दिया😆😆",
    "राह में मिले थे हम, राहें नसीब बन गईं😙😙",
    "ना तू अपने घर गया, ना हम अपने घर गये😉😉",
    "तुम्हें नींद नहीं आती तो कोई और वजह होगी😅😅",
    "अब हर ऐब के लिए कसूरवार इश्क तो नहीं😘😘",
    "अना कहती है इल्तेजा क्या करनी😆😆",
    "वो मोहब्बत ही क्या जो मिन्नतों से मिले💕💕",
    "न जाहिर हुई तुमसे और न ही बयान हुई हमसे💓💓",
    "बस सुलझी हुई आँखो में उलझी रही मोहब्बत🥺🥺",
    "गुफ्तगू बंद न हो बात से बात चले🥵🥵",
    "नजरों में रहो कैद दिल से दिल मिले😁😁",
    "है इश्क़ की मंज़िल में हाल कि जैसे😘😘",
    "लुट जाए कहीं राह में सामान किसी का🥰",
    "मुकम्मल ना सही अधूरा ही रहने दो😂😂",
    "ये इश्क़ है कोई मक़सद तो नहीं है🤩🤩",
    "वजह नफरतों की तलाशी जाती है😘😘",
    "मोहब्बत तो बिन वजह ही हो जाती है 😍😍",
    "सिर्फ मरी हुई मछली को ही पानी का बहाव चलाती है 😙😙",
    "जिस मछली में जान होती है वो अपना रास्ता खुद तय करती है",
    "कामयाब लोगों के चेहरों पर दो चीजें होती है 😘😘",
    "एक साइलेंस और दूसरा स्माइल🤔🤔",
    "मेरी चाहत देखनी है तो मेरे दिल पर अपना दिल रखकर देखe😌😌",
    "तेरी धड़कन ना भड्जाये तो मेरी मोहब्बत ठुकरा देना🤫🤫",
    "गलतफहमी की गुंजाईश नहीं सच्ची मोहब्बत में🤪🤪",
    "जहाँ किरदार हल्का हो कहानी डूब जाती है☺️☺️",
    "होने दो मुख़ातिब मुझे आज इन होंटो से अब्बास🤗🤗",
    "बात न तो ये समझ रहे है पर गुफ़्तगू जारी है😶😶",
    "उदासियाँ इश्क़ की पहचान है🤗🤗",
    "मुस्कुरा दिए तो इश्क़ बुरा मान जायेगा😗😗",
    "कुछ इस अदा से हाल सुनाना हमारे दिल😘😘",
    "वो खुद ही कह दे किदी भूल जाना बुरी बात है🥲",
    "माना की उससे बिछड़कर हम उमर भर रोते रहे🤔🤔",
    "पर मेरे मार जाने के बाद उमर भर रोएगा वो😅😅",
    "दिल में तुम्हारी अपनी कभी चोर जायेंगे😁😁",
    "आँखों में इंतज़ार की लकीर छोड़ जायेंगे🙈🙈",
    "किसी मासूम लम्हे मैं किसी मासूम चेहरे से🙉🙉",
    "मोहब्बत की नहीं जाती मोहब्बत हो जाती है😌😌",
    "करीब आओ तो शायद हम समझ लोगे😌😌",
    "ये दूरिया तो केवल फसले बढ़ती है🤫🤫",
    "तेरे इश्क़ में इस तरह मैं नीलाम हो जाओ🤔🤔",
    "आखरी हो मेरी बोली और मैं तेरे नाम हो जाऊ😌😌",
    "आप जब तक रहेंगे आंखों में नजारा बनकर😁😁",
    "रोज आएंगे मेरी दुनिया में उजाला बनकर👅👅",
    "उसे जब से बेवफाई की है मैं प्यार की राह में चल ना सका😅😅",
    "उसे तो किसी और का हाथ थाम लियाबस फिर कभी सम्भल नहीं सका👅👅",
    "एक ही ख़्वाब देखा है कई बार मैंने🤬🤬",
    "तेरी शादी में उलझी है चाहिए मेरे घर की😈😈",
    "तुम्हे मेरी मोहब्बत की कसम सच बताना😎😎",
    "गले में डाल कर बाहें किससे सीखाया है😍😍",
    "नहीं पता की वो कभी मेरी थी भी या नहीं😋😋",
    "मुझे ये पता है बस की माई तो था उमर बस उसी का रहा😌😌",
    "तुमने देखा कभी चाँद से पानी गिरते हुएe😏😏",
    "मैंने देखा ये मंज़र तू में चेहरा धोते हुए😉😉",
    "ठुकरा दे कोई चाहत को तू हस के सह लेना😊😊",
    "प्यार की तबियत में ज़बर जस्ती नहीं होती😉😉",
    "तेरा पता नहीं पर मेरा दिल कभी तैयार नहीं होगा😌😌",
    "मुझे तेरे अलावा कभी किसी और से प्यार नहीं होगा😍😍",
    "दिल में आहट सी हुई रूह में दस्तक गूँजी🤫🤫",
    "किस की खुशबू ये मुझे मेरे सिरहाने आई😁😁",
    "उम्र भर लिखते रहे फिर भी वारक सदा रहा😏😏",
    "जाने किया लफ्ज़ थे जो हम लिख नहीं पाये😌😌",
    "लगा के फूल हाथों से उसने कहा चुपके से😶😶",
    "अगर यहाँ कोई नहीं होता तो फूल की जगह तुम होते😆😆",
    "जान जब प्यारी थी मरने का शौक था🥵🥵",
    "अब मरने का शौक है तो कातिल नहीं मिल रहा🤫🤫",
    "सिर्फ याद बनकर न रह जाये प्यार मेरा🥲🥲",
    "कभी कभी कुछ वक़्त के लिए आया करो😎😎",
    "मुझ को समझाया ना करो अब तो हो चुकी हूँ मुझ मैं😌😌",
    "मोहब्बत मशवरा होती तो तुम से पूछ लेता😁😁",
    "उन्हों ने कहा बहुत बोलते हो अब क्या बरस जाओगे😂😂",
    "हमने कहा जिस दिन चुप हो गया तुम तरस जाओ गए😶😶",
    "कुछ ऐसे हस्दे ज़िन्दगी मैं होते है🤔🤔",
    "के इंसान तो बच जाता है मगर ज़िंदा नहीं रहता😂💓",
]



# Command
    


@app.on_message(filters.command(["lovetag" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 . ")

    if message.reply_to_message and message.text:
        return await message.reply("/lovetag  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/lovetag  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ...")
    else:
        return await message.reply("/lovetag  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ..")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(LOVETAG)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


#

@app.on_message(filters.command(["cancelshayari", "shayarioff"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 ..")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦ OFFFFFFFFF♦")
