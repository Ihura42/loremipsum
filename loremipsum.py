import random
import string
import os


#Function to generate random text with random letters
def random_generate():
    amount_articles = int(input("Write amount of articles: "))
    amount_sentence = int(input("Write a number of sentances: "))
    amount_words = int(input("Write a number of words: "))
    number_min = int(input("Write the minimum word length: "))
    number_max = int(input("Write the maximum word length: ")) 
    

    text = "" 
    for _ in range(amount_articles):
        sentance = "    "
        for _ in range(amount_sentence):
            word = ""
            number_length = random.randint(number_min,number_max)
            word += random.choice(string.ascii_uppercase)
            for _ in range(amount_words):
                for _ in range(number_length):
                    random_letter = random.choice(string.ascii_lowercase)
                    word += random_letter
                word += " "
            word = word[:-1]        
            word += ". "
            sentance += word   
        text += sentance
        text += "\n\n"
    output_text(text)       



# Function to generate czech or lorem ipsum text
def czech_generate(word_choice):
    num_paragraphs = int(input("Write amount of articles: "))
    num_sentences = int(input("Write a number of sentances in article: "))
    num_words = int(input("Write a number of words in sentence: "))
    number_minimum = int(input("Write the minimum word length: "))
    number_maximum = int(input("Write the maximum word length: "))

    if word_choice == 1:
        vocabulary = "zkaženějšími, rušená, kaligrafickým, sešikováno, těžknete, nezasvětil, doměříte, šibovat, převeze, bájemi, kresbou, nejpromyšlenějších, ochrnu, neinicializované, rozvaha, blahosklonné, jmenujícího, proutkaření, míníme, macešin, známkuje, plemenem, pokleknětou, skinovatelným, rozlousknutou, librové, ukončovacích, módním, otopnému, nevyplázla, vestibulům, mikropočítači, odladitelnými, rozkodrcaný, zvali, neumořitelný, nejzákladnějším, slýcháváme, syčivému, balkanských, odmapovanému, stonožkami, dotéká, magnetohydrodynamická, neposkytnu, vlezdoprdelismus, zaštiťovanými, přeběhnutí, nepřiměřených, soudružský, zkonvertoval, svářím, zlevňováním, řemínkovému, neodlákal, vzpružovat, autodestruktivní, stevardka, malečovskými, odstavováními, astrologou, poskákaný, zahalenějších, nematerializovala, límečkových, zbrocenou, hydratováno, měněná, shrnovala, světélkovalo, barbaře, třicáté, zákopový, nepronajmutí, zatímně, subdodavatelském, předvídaná, sílivýma, nevyčíslila, docentům, rebelovali, nevypravuj, elektrodě, bobtnaly, rákoskové, hostitele, revolucemi, slangové, připájenou, otoků, nakládán, zkonstatovat, uzamknutou, nesoudíš, nepovyšujme, fotolabech, nezavrtaly, nejovládanějšími, servismanům, devětačtyřicet, neskolí, křivděno, litvínovsku, přesvatého, přichomýtly, pilířovitými, zválcovala, titaničitýma, zrádcové, nepoposunuly, prostreku, vykydané, povztekanou, závisení, obehranější, soku, nevyvléknete, nezvali, pořekadly, grošovitými, roztírejte, dusnu, pružnějšího, znegována, neuvidíš, řepce, poblouzněnou, podřadící, sesazoval, ševelí, stříkaný, zasouvým, nasázenému, jedenáctá, vlezle, rezidentnost, jakartského, nerozpečetěnýma, povyhrnutí, holícími, nesaturovanými, zachutným, nesnídám, rafinovaný, přestylizovaném, vefoukávanýma, ventilátorem, symbolickému, nenejstydlivější, zmučeného, jezdecké, nekuňkalo, umravněný, vštěpili, výdobytkem, knihtiskárně, škvařenému, pátkovými, rosný, meruzalkovému, vozítkou, nejryzejší, probelhávat, vstřebávanými, vytápěcímu, paráděnému, vyčpělého, zpevněnou, zveřejnitelnému, přepouštěných, shrábnutých, připíchnutou, ověřovaným, namítlou, přelidněny, pětikorunou, odskakujícím, martínkovy, maleinový, přibijeme, nejprotáhlejší, nehladovým, snoubeneckým, tipoval, shlédnetou, míchali, vykrojili, škytavá, nesrovnanými, nechystými, aprílovou, pórovinového, nenařízneš, šéfuje, maltové, sežraní, obklíčenou, islamistického, obrývaných, rozplynuly, nadčasového, pažitka, doručovatelskou, přijmout, babrající, ošoupaného, optimalizovala, nehezky, neoplývými, genomový, doutnala, objektivními, různolistému, žaček, eutektické, klihovatýma, zasazujícímu, houfné, protimonopolními, zavinilo, adaptacích, setřena, vrátnicemi, vendulou, supího, příčná, ovívanými, zdemoralizovaným, cikorku, trestněprávních, předstírajících, nečerpej, ječmenářských, odosobněnými, blízce, zakolísaná, jodovými, ztrapníte, libreta, bité, racionálnějšími, spoluvlast, rozklikly, vytěsněn, lídin, nezmírňujte, zkrocena, obilnářská, nezamítnu, vyprodalo, přesvědčování, uhodíme, odezřenou, ikonového, svazkovýma, lamentujícímu, světobodů, vyprovázejících, kněževeských, nepodepisuje, patronance, cihlářské, zataraseno, komoleným, šedočerné, zatrpkli, využívaní, omrzlinám, kalkulačková, odchodům, antisemitova, lehlému, rozpochodovaným, chřupavou, pohupovanou, vypírat, měšťanovým, hověli, upřimná, zredigovaná, rovinové, odflinknutého, podplout, nevalných, oděn, nekladla, saskem, slavonická, zrcadlily, nepřikryl, narušovateli, rozfouknutý, aranžujícího, humanitárnímu, líha, řízkového, proklínaným, zobrazujte, spamům, praskými,vůl,buď,žár,čouh,řez,ňouc,plík,šup,šňou,žmouh,řep,žeň,ťouk,blýsk,mlž,klíč,vrah,pyr,ťouk,dřeň,říp,žluť,buň,pyr,žmouh,křep,klíč,šouk,plík,žluť,strom,dům,klíč,krabice,kočka,pes,škola,auto,stromek,skála,řeka,les,hora,lék,sklenice,pohár,čaj,stromovka,ryba,park,důmík,klíček,kniha,kostka,židle,okno,světlo,mléko,krabicek,kůň"
    elif word_choice == 2:
        vocabulary = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nam sed tellus id magna elementum tincidunt. Nullam sit amet magna in magna gravida vehicula. Duis viverra diam non justo. Proin pede metus, vulputate nec, fermentum fringilla, vehicula vitae, justo. Nullam rhoncus aliquam metus. Pellentesque sapien. Mauris metus. Etiam ligula pede, sagittis quis, interdum ultricies, scelerisque eu. Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? Vivamus ac leo pretium faucibus. Duis condimentum augue id magna semper rutrum. Nullam rhoncus aliquam metus. Integer pellentesque quam vel velit. Aliquam ante. Curabitur bibendum justo non orci.Vivamus luctus egestas leo. Integer lacinia. Aenean id metus id velit ullamcorper pulvinar. Pellentesque pretium lectus id turpis. Nullam sit amet magna in magna gravida vehicula. In sem justo, commodo ut, suscipit at, pharetra vitae, orci. Nam sed tellus id magna elementum tincidunt. Fusce wisi. Aliquam erat volutpat. Nulla est." 
    vocabulary = vocabulary.replace(",", "")
    vocabulary = vocabulary.replace(".", " ")
    words_list = vocabulary.split()
    filtred_words = []
    for word in words_list:
        if len(word) >= number_minimum and len(word) <= number_maximum:
            filtred_words.append(word)
    if not filtred_words:
        print("The dictionary doesn't have the right words")
        main()
    filtred_string = ' '.join(filtred_words)
    filtred_string = filtred_string.split()        


    text = ""
    for _ in range(num_paragraphs):
        paragraph = "   "
        for _ in range(num_sentences):
            sentence = ""
            for _ in range(num_words):
                rand_word = random.choice(filtred_string)
                sentence += " " + rand_word
            sentence = sentence[1:]    
            sentence = sentence[0].upper() + sentence[1:] + ". "
            paragraph += sentence
        text += paragraph + "\n\n"
    output_text(text)

# Function to output the generated text to console or file
def output_text(text):
    user_choice = input("Do you want to output a file? y/n ")
    if user_choice.lower() == 'y':
        file_name = "generated_text.txt"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)
        os.system(file_name)   
    elif user_choice.lower() == 'n':
        print(text)
    else: 
        print("You have a mistake")             
   
   
# Main function to drive the program
def main():
    word_choice = int(input("Select the generation method. 1.Czech dictionary / 2. Lorem dictionary / 3. Random letters ")) 
    if word_choice == 1 or word_choice == 2:
        czech_generate(word_choice)
    elif word_choice == 3:
        random_generate()
    else:
        print("You have a mistake")        
               
main()