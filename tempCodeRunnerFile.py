from TTS.api import TTS

# # Define the text to be converted to speech
# text_hi = (
#     "जलवायु परिवर्तन से निपटने के लिए वैश्विक प्रयास तेजी से बढ़ रहे हैं, "
#     "क्योंकि दुनिया भर के देश कार्बन उत्सर्जन को कम करने का संकल्प ले रहे हैं। "
#     "संयुक्त राष्ट्र ने औद्योगिक क्रांति से पहले के स्तरों की तुलना में वैश्विक तापमान वृद्धि "
#     "को 1.5 डिग्री सेल्सियस तक सीमित करने के लिए त्वरित कार्यवाही की अपील की है, "
#     "और सरकारें इस दिशा में महत्त्वाकांक्षी योजनाएं बना रही हैं। "
#     "तकनीकी क्षेत्र में, कृत्रिम बुद्धिमत्ता (AI) के क्षेत्र में महत्वपूर्ण प्रगति हो रही है, "
#     "जो विभिन्न उद्योगों के भविष्य का आकार दे रही है। स्वास्थ्य सेवा से लेकर वित्त तक, AI व्यवसाय "
#     "के संचालन के तरीकों को बदल रहा है, जिससे नए अवसर और नवाचार की संभावनाएं सामने आ रही हैं। "
#     "खेल जगत में, आगामी ओलंपिक खेलों का आयोजन दर्शकों के लिए बेहद रोमांचक होने वाला है। "
#     "खिलाड़ी वैश्विक मंच पर प्रतिस्पर्धा के लिए तैयार हैं, अपनी क्षमता और दृढ़ संकल्प को प्रदर्शित "
#     "करते हुए। यह आयोजन एक रोमांचक नजारा होगा, जिसमें नए रिकॉर्ड बनने की उम्मीद है। "
#     "अंत में, मनोरंजन की दुनिया में, एक बहुप्रतीक्षित फिल्म ने बॉक्स ऑफिस पर रिकॉर्ड तोड़ दिया है। "
#     "इस फिल्म में अत्याधुनिक विशेष प्रभाव और एक सितारों से सजी कास्ट है, जिसने समीक्षकों और दर्शकों दोनों "
#     "से प्रशंसा प्राप्त की है।"
# )

# # Load the Hindi TTS model
# tts_hi = TTS('tts_models/hi/ekstep/tacotron2-DDC', progress_bar=False)

# # Generate the Hindi speech and save it to a file
# tts_hi.tts_to_file(text=text_hi, file_path="output_hi.wav"