# from TTS.api import TTS

# # Initialize TTS with an English model
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

# # Generate speech and save to a file
# text = (
#     "Global efforts to combat climate change are gaining momentum as countries around the world "
#     "pledge to reduce carbon emissions. The United Nations has called for urgent action to limit "
#     "global warming to 1.5 degrees Celsius above pre-industrial levels, and governments are responding "
#     "with ambitious plans. In the technology sector, major advancements in artificial intelligence are "
#     "continuing to shape the future of industries. From healthcare to finance, AI is transforming how "
#     "businesses operate, offering new opportunities for efficiency and innovation. Meanwhile, in the "
#     "world of sports, the upcoming Olympic Games are set to captivate audiences worldwide. Athletes are "
#     "preparing to compete on the global stage, showcasing their skills and determination. The event promises "
#     "to be a thrilling spectacle, with new records expected to be set. Finally, in entertainment, a highly "
#     "anticipated movie release is breaking box office records. The film, which features groundbreaking visual "
#     "effects and a star-studded cast, has garnered rave reviews from critics and audiences alike."
# )
# tts.tts_to_file(text=text, file_path="output_en1.wav")



# from TTS.api import TTS

# # Initialize TTS with a Hindi model
# tts = TTS(model_name="tts_models/hi/coqui/vits", progress_bar=False)

# # Generate speech and save to a file
# text = (
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

# # Save the output as a WAV file
# tts.tts_to_file(text=text, file_path="output_hi.wav")

# from TTS.api import TTS

# # Initialize TTS with a multilingual model
# tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False)

# # Generate speech and save to a file
# text = (
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

# # Save the output as a WAV file
# tts.tts_to_file(text=text, file_path="output_hi.wav")

# from TTS.api import TTS

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
# tts_hi.tts_to_file(text=text_hi, file_path="output_hi.wav")


from TTS.api import TTS

# Define the text to be converted to speech
text_hi = (
    "जलवायु परिवर्तन से निपटने के लिए वैश्विक प्रयास तेजी से बढ़ रहे हैं, "
    "क्योंकि दुनिया भर के देश कार्बन उत्सर्जन को कम करने का संकल्प ले रहे हैं। "
    "संयुक्त राष्ट्र ने औद्योगिक क्रांति से पहले के स्तरों की तुलना में वैश्विक तापमान वृद्धि "
    "को 1.5 डिग्री सेल्सियस तक सीमित करने के लिए त्वरित कार्यवाही की अपील की है, "
    "और सरकारें इस दिशा में महत्त्वाकांक्षी योजनाएं बना रही हैं। "
    "तकनीकी क्षेत्र में, कृत्रिम बुद्धिमत्ता (AI) के क्षेत्र में महत्वपूर्ण प्रगति हो रही है, "
    "जो विभिन्न उद्योगों के भविष्य का आकार दे रही है। स्वास्थ्य सेवा से लेकर वित्त तक, AI व्यवसाय "
    "के संचालन के तरीकों को बदल रहा है, जिससे नए अवसर और नवाचार की संभावनाएं सामने आ रही हैं। "
    "खेल जगत में, आगामी ओलंपिक खेलों का आयोजन दर्शकों के लिए बेहद रोमांचक होने वाला है। "
    "खिलाड़ी वैश्विक मंच पर प्रतिस्पर्धा के लिए तैयार हैं, अपनी क्षमता और दृढ़ संकल्प को प्रदर्शित "
    "करते हुए। यह आयोजन एक रोमांचक नजारा होगा, जिसमें नए रिकॉर्ड बनने की उम्मीद है। "
    "अंत में, मनोरंजन की दुनिया में, एक बहुप्रतीक्षित फिल्म ने बॉक्स ऑफिस पर रिकॉर्ड तोड़ दिया है। "
    "इस फिल्म में अत्याधुनिक विशेष प्रभाव और एक सितारों से सजी कास्ट है, जिसने समीक्षकों और दर्शकों दोनों "
    "से प्रशंसा प्राप्त की है।"
)

# Load a multilingual TTS model that supports Hindi
tts_hi = TTS('tts_models/multilingual/multi-dataset/xtts_v2', progress_bar=False)
# Assuming you have a list of available speakers; for example, 'speaker1'
speaker_id = 'speaker1'

# Modify the call to tts_to_file to include the speaker ID
tts_hi.tts_to_file(text=text_hi, file_path="output_hi.wav", speaker=speaker_id)

# Generate the Hindi speech and save it to a file
# tts_hi.tts_to_file(text=text_hi, file_path="output_hi.wav")
