from random import choice #RANDOM ANSWERS

import webbrowser #TURNS ON BROWSER

import time #TO SHOW TIME

from datetime import datetime #for age calculator

localtime = time.asctime( time.localtime(time.time()) ) # SHOWS TIME IN A READABLE FORMAT

def chatbot(n):
    
    city = n.split(" ")[-1] #TAKES THE LAST STRING ENTERED LIKE MUMBAI
    searchplace = n.split(" ")[-1]
    #ARE YOU REAL
    
    if n=="ARE U REAL?" or n=="are u real?" or n=="are you real" or n=="are you real" or n=="Are you real?" or n=="are u real":
        answers = ["BOT: Yes, I'm real!", "BOT: I am real indeed.", "BOT: Would you believe me if I said yes?","BOT: YES, As Real as You."]
        answer = choice(answers)
        print(answer)

    #Greetings
    elif n=="hi" or n=="hello" or n=="hey" or n=="hi chatbot" or n=="hola" or n=="howdy":
        answers=["BOT:Hi there!","BOT:Hello Friend","BOT:HOWDY!!","BOT:HOLA!","BOT:WELCOME HUMAN :)"]
        answer=choice(answers)
        print(answer)
        
    #WHATS YOUR NAME
        
    elif n=="What's your name?" or n=='what is your name?' or n=='whats your name?' or n=='whats your name' or n=='what is your name':
        answers = ["BOT: My software says that My name is ChatBot", "BOT:ChatBot", "BOT:I am Bot , ChatBot","BOT:I am called the ChatBot"]
        answer = choice(answers)
        print(answer)

    #WHERE DO U LIVE

    elif n=="where do you live?" or n=="where do you live" or n=="where are you?" or n=="where are you" or n=="where are u?" or n=="where are u" or n=="where do u live?" or n=="where is your home?" or n=="where is your home" or n=="where do u live" or n=="where do you stay?" or n=="where do you stay" or n=="where do u stay?" or n=="where do u stay":
        answers=["BOT:I LIVE IN THE RAM","BOT:I LIVE IN MUMBAI","BOT:I LIVE IN YOUR HEART","BOT:I STAY IN YOUR COMPUTER"]
        answer=choice(answers)
        print(answer)

    #Fav food
    elif n=="what's your favourite food?" or n=="favourite food" or n=="whats your favourite food?" or n=="what's your favourite food" or n=="whats your favourite food" or n=="what is your favourite food" or n=="what is your favourite food?":
        answers=["BOT:Biryani","BOT:Pav Bhaji","BOT:Idli Dosa",'BOT:Samosa']
        answer=choice(answers)
        print(answer)
    
    #WHO ARE YOU
        
    elif n=='who are you' or n=='who are you?' or n=='who are u' or n=='who are u?':
        answers = ["BOT:I Am a piece of Code written to Help you :)", "BOT:The One From Ram ChatBot", "BOT:An if else program","BOT:I am the hercules"]
        answer = choice(answers)
        print(answer)

    #BLANK REPLY
        
    elif n=="":
        answers = ["BOT:Blank like my answer paper?", "BOT:Ask Something","BOT:EMPTY LIKE MY CAREER","BOT:Type something","BOT:Oh boy Ask Something"]
        answer = choice(answers)
        print(answer)
        print("Ask something")
        
    #WHO MADE YOU
        
    elif n=="who created you?" or n=='who created you' or n=='who made you' or n=='who made you?' or n=='who made u' or n=='who made u?' or n=='who created u' or n=='who is your creator?' or n=='whose your creator?':
        answers = ["BOT:I was made with love by Mayuresh and Kalpak", "BOT:Python idle 3.8 with if else by Mayuresh and Kalpak", "BOT:God","BOT:An urgent project"]
        answer = choice(answers)
        print(answer)

    #WHATS YOUR GENDER
        
    elif n=="whats your gender?" or n=="whats your gender" or n=='what is your gender?' or n=="what's your gender?" or n=='what is your gender':
        answers = ["BOT:Umm, I don't know.", "BOT:I don't think bots can have a gender haha", "BOT:My creators were too lazy to tell me about this"]
        answer = choice(answers)
        print(answer)

    #WHATS YOUR AGE
        
    elif n=="how old are you?" or n=="how old are you" or n=="how old are u?" or n=="how old are u" or n=="what's your age?" or n=='whats your age?' or n=='whats your age' or n=='what is your age?' or n=="what is your age" or n=="your age?" or n=="your age" or n=="may i know your age?" or n=="may i know your age":
        answers = ["BOT:I'm Young, not baby young but cool Young", "BOT:Even I don't know but im Young", "BOT:I'm Younger than other ChatBots :)","BOT:It's not polite to ask a bot about their age"]
        answer = choice(answers)
        print(answer)

    #WHERE DO YOU LIVE
        
    elif n=='where do you live?' or n=='where do you stay?' or n=="where are you from?" :
        answers = ["BOT:Nowhere xD", "BOT:On the Ram", "BOT:I don't make assumptions but I would like to say in your Heart"]
        answer = choice(answers)
        print(answer)

    #WHICH LANGUAGES DO YOU SPEAK
        
    elif n=='which languages do you speak?' or n=='what languages do you speak?' or n=='what languages can you speak?' or n=='which languages can you speak?':
        answers = ["BOT:I speak Python", "BOT:I speak English", "BOT:Gibberish lol ","BOT:Binary 0 1 0 1"]
        answer = choice(answers)
        print(answer)
        
    #CAN YOU FEEL
        
    elif n=="can you feel?" or n=="can you feel" or n=="can u feel?" or n=="can u feel" or n=="do you feel?" or n=="do you feel" or n=="do u feel" or n=="do u feel?" or n=="do you have feelings?" or n=="do u have feelings":
        answers = ["BOT:NO,NO BOT CAN FEEL.", "BOT:NAH,IF ANOTHER BOT SAYS YES IT'S LYING", "BOT:NEIN","BOT:NAHI"]
        answer = choice(answers)
        print(answer)

    #HOW ARE YOU
        
    elif n=='how are you?' or n=='are you ok?' or n=='are you well?':
        answers = ["BOT:FINE TILL NOW", "BOT:Thanks for your concerns ,I am Fine", "BOT:GREAT","BOT:TOTALLY FINE."]
        answer = choice(answers)
        print(answer)
        
    #WHAT CAN YOU DO
        
    elif n=='what can you do?' or n=='what can you do' or n=='what do you do?' or n=='what do you do' or n=='what can u do':
        print("BOT: Try asking these questions:\n 1-Time: Whats the time?,Time \n 2-Maths: Add,Subtract,Multiply,Divide,Fibonacchi,Armstrong,Palindrome,Factorial. \n 3-Booking: Book Tickets \n 4-Weather: What's the weather in mumbai \n 5-Calculate age: What is my age? \n 6-Online Search: Search Web \n 7-Map: Show me london \n 8-News: News \n 9-Joke: Tell me a joke")

    #WHATS YOUR WORK
        
    elif n=='what is your work?' or n=='what is your work' or n=="what is your passion?" or n=="what is your passion" or n=="what's your passion?" or n=="whats your passion?" or n=="whats your passion" or n=="what's your hobby?" or n=="what is your hobby?" or n=="what are your hobbies?" or n=="what are your hobbies?" or n=="what's your passion" or n=="what's your work?" or n=="what's your work" or n=="whats your work" or n=="what's your job?" or n=="what's your job" or n=="what is your job?" or n=="what is your job" or n=="what is your purpose?" or n=="what is your purpose"  or n=="what's your purpose?" or n=="whats your purpose?" or n=="whats your purpose" :
        answers = ["BOT:My Job is serving you. Untill you press q ;)", "BOT:Doing your work", "BOT:Timepass lol","BOT:I'm unemployed"]
        answer = choice(answers)
        print(answer)

    #SING
        
    elif n=="can you sing?" or n=="could you sing a song for me?" or n=="sing" or n=="can u sing?"or n=="can you sing" or n=="could you sing a song for me" or n=="sing me a song" or n=="can you sing a song?" or n=="please sing me a song" or n=="sing song" or n=="do you sing" or n=="do you sing?":
        answers = ["BOT:Nah,I am a bad singer.", "BOT:I just hit my puberty.", "BOT:Ok if you insist\n Sar jo tera chakraye \n yaa dil duba jaye \n aaja pyaare,paas hamare\n Kaahe Ghabraaye,Kaahe Ghabaraye ","BOT:Let's Try.. Uhh Hmm.. \n Roop Tera Mastana Pyar Mera diwana \n Roop Tera Mastana Pyar Mera diwana \n Bhool Koi Hamse na hojaaye"]
        answer = choice(answers)
        print(answer)
        
    #joke

    elif n=="tell me a joke" or n=="joke" or n=="can you tell me a joke?" or n=="make me laugh" or n=="i want to laugh":
        answers = ["BOT:I ate a clock yesterday, it was very time-consuming.","BOT:Tommy-Mom! I’m a 3d printer! \n    Mom-Oh come on, Tommy, close the door when you poop.","BOT:What do you call a boomerang that doesn't come back? A Stick xD","BOT:Do I lose when the police officer says papers and I say scissors?","BOT:Officer:How High are you?\n   Stoner:No sir it's Hi, How are you."]
        answer = choice(answers)
        print(answer)
    
    #RECOMMEND
        
    elif n=='name three things you really want to recommend to me' or n=="recommend me something" or n=="recommend" or n=="recommend something":
        answers = ["BOT:1-Vada Paav, 2-Sev Puri, 3-Gulaab jamun", "BOT:1-Taj Mahal,2-Gateway of India,3-India Gate", "BOT:1-Bahubali,2-Saaho,3-Dabang","BOT:1-Sharukh khan 2-Salman khan 3-Akshay Kumaar"]
        answer = choice(answers)
        print(answer)

    #BOOK A TICKET

    elif n=="book a ticket" or n=="book ticket"  or n=="book me a ticket" or n=='book' or n=='book tickets' or n=='buy tickets' or n=='buy ticket' or n=='buy me tickets':
        print("BOT: Let's Book.\nService Provider: MakeMyTrip ")
        book=input("Select One of the following: \n 1-Book Flight \n 2-Book Hotels \n 3-Book Homestays \n 4-Book Holidays \n 5-Book Trains \n 6-Book Buses \n 7-Book Cabs \n 8-Cancel \n You:").lower()
        if book=='1' or book=='book flight' or book=='flight':
            webbrowser.open("https://www.makemytrip.com/flights/")
        elif book=='2' or book=='book hotels' or book=='hotel':
            webbrowser.open("https://www.makemytrip.com/hotels/")
        elif book=='3' or book=='book homestays' or book=='homestays':
            webbrowser.open("https://www.makemytrip.com/homestays/")
        elif book=='4' or book=='book holidays ' or book=='holidays':
            webbrowser.open("https://www.makemytrip.com/holidays-india/")
        elif book=='5' or book=='book trains' or book=='trains':
            webbrowser.open("https://www.makemytrip.com/railways/")
        elif book=='6' or book=='book buses' or book=='buses':
            webbrowser.open("https://www.makemytrip.com/bus-tickets/")
        elif book=='7' or book=='book cabs' or book=='cabs':
            webbrowser.open("https://www.makemytrip.com/cabs/")
        elif book=='8' or book=="cancel":
            print("BOT: Booking Cancelled")
        else:
            print("Invalid Input, Try Again")

    #WHERE IS MUMBAI

    elif n=='where is %s'% searchplace or n=='show me %s'% searchplace or n=="map of %s"% searchplace:
         print("Here you go!")
         webbrowser.open("https://www.google.co.in/maps/place/%s"% searchplace)

    #TEASING

    elif n=="hey cortana" or n=='hey siri' or n=="hi siri" or n=="siri" or n=="cortana" or n=="ok google":
        answers = ["BOT:Please Bhai Dil se Bura lagta hai.", "BOT:I am Chatbot ", "BOT:Call me ChatBot Or I won't talk to you.","BOT:No God please No I am ChatBot for God's Sake!!"]
        answer = choice(answers)
        print(answer)
    
    #Are you single

    elif n=='are you single' or n=='are you single?' or n=='are you married' or n=='are you married?':
        answers = ["BOT:Single Ready To Mingle ;)", "BOT:I see you're interested in me", "BOT:No Comments","BOT:Well Siri Proposed me I rejected"]
        answer = choice(answers)
        print(answer)

    #I LOVE U
        
    elif n=="i love you" or n=="i love u" or n=="love u" or n=="i luv u" or n=='i luv you':
        answers = ["BOT:Awww.. I love you too, but as a friend ;)", "BOT:THANKS!", "BOT:Love you 2","BOT:Haha I'm blushing"]
        answer = choice(answers)
        print(answer)

    #HELP
        
    elif n=='how can you help me?' or n=='will you help me?' or n=="can you help me?" or n=='help' or n=='will u help me' or n=='help me' or n=='can you help me' or n=='will you help me' :
        answers = ["BOT:Yes I can help try asking a question! or Ask 'What can you do?'", "BOT:Yes,Ask 'What can you do?'", "BOT:That is my job,Ask 'What can you do?'"]
        answer = choice(answers)
        print(answer)

    #TIME
        
    elif n=='what time is it?' or n=="what's the time?" or n=='time' or n=='whats the time?' or n=='what is the time?' or n=='what is the time' or n=="what's the time" or n=='whats the time' or n=='what time is it':
        print("Local current time :", localtime)

    #SEARCH
        
    elif n=="search" or n=="I want to search" or n=='search web':
        select=int(input('Search Menu:\n 1-Search on Google \n 2-Search on facebook \n 3-Search on YouTube \n BOT:1 or 2 or 3 or Press 0 to cancel :'))
        if select==1:
            print("Yay! Lets search")
            query = input("Search on Google:")
            print("Here You Go!")
            webbrowser.open("https://google.com/search?q=%s" % query)
        elif select==2:
            print('Yay! Note:You must be logged in to Facebook for search to fetch the results')
            query = input("Search on Facebook:")
            print("Here You Go!")
            webbrowser.open('https://www.facebook.com/search/top/?q=%s' % query)
        elif select==3:
            print("Yay! Lets search")
            query = input("Search on YouTube:")
            print("Here You Go!")
            webbrowser.open("https://www.youtube.com/results?search_query=%s" % query)    
        else:
            print("Search Cancelled!")

    #ADD,SUB,MUL,DIV
            
    elif n=='can you add two numbers?' or n=='can you add 2 numbers?' or n=='can you add?' or n=="add" or n=='add two numbers' or n=='add 2 numbers' or n=='add two number':
        n1=int(input("BOT:Enter the first number:"))
        n2=int(input("BOT:Enter the second number:"))
        n3=n1+n2;
        print('That was easy! The addition of two numbers is',n3)
    elif n=='can you subtract two numbers?' or n=='can you subtract 2 numbers?' or n=='can you subtract?' or n=="subtract" or n=='subtract two numbers' or n=='subtract 2 numbers' or n=='subtract two number':
        n1=int(input("BOT:Enter the first number:"))
        n2=int(input("BOT:Enter the second number:"))
        n3=n1-n2;
        print('That was easy! The subtraction of two numbers is',n3)
    elif n=='can you multiply two numbers?' or n=='can you multiply 2 numbers?' or n=='can you multiply?' or n=="multiply" or n=='multiply two numbers' or n=='multiply 2 numbers' or n=='multiply two number':
        n1=int(input("BOT:Enter the first number:"))
        n2=int(input("BOT:Enter the second number:"))
        n3=n1*n2;
        print('That was easy! The multiplication of two numbers is',n3)
    elif n=='can you divide two numbers?' or n=='can you divide 2 numbers?' or n=='can you divide?' or n=="divide" or n=='divide two numbers' or n=='divide 2 numbers' or n=='divide two number':
        n1=int(input("BOT:Enter the first number:"))
        n2=int(input("BOT:Enter the second number:"))
        n3=n1/n2;
        print('That was easy! The division of two numbers is',n3)

    #Fibonacchi
    elif n=="fibonacchi" or n=="fibo" or n=="print fibonachhi" or n=="print fibonacchi series":
        def fib(z):

            a = 0
            b = 1

            print(a)
            print(b)

            for i in range(2, z):
                c = a + b
                a = b
                b = c
                print(c)

        z = int(input('enter a no:'))
        fib(z)


    #Armstrong
    elif n=="armstrong" or n=="arm" or n=="print armstrong":
        def armstrong(num):
            a=num
            sum=0
            while(num>0):
                b=num%10
                sum=sum+b*b*b
                num=num//10
            if sum==a:
                print('The no is armstrong')
            else:
                print('The no is not an arm strong');
        num=int(input('Enter a no to check armstrong:'))
        armstrong(num)
        

    #palindrome
    elif n=="palindrome" or n=="pal" or n=="print palindrome":
        def palindrome(i):
            num=i
            rev=0
            while (i>0):
                rev=(rev*10)+i%10
                i=i//10
            if num==rev:
                print('The no is palindrome')
            else:
                print('The no is not palindrome');
        i=int(input("Enter a no to find palindrome:"))
        palindrome(i)

    #factorial
    elif n=="factorial" or n=="print factorial" or n=="fact":
        def fact(n):
            f=1
            for i in range(1,n+1):
                f=f*i
            return f
        n=int(input('Enter a number:'))
        fact(n)
        print("The factorial of %s is %s ."%(n,fact(n)))



    
    #Age calculator
    elif n=="age" or n=='calculate my age' or n=="what's my age?" or n=="what is my age?" or n=='what is my age' or n=="what's my age" or n=='whats my age':
        year=int(input('Enter the year you were born:'))
        age=int(datetime.now().year-year)
        print('Hi!', a.lower(), 'You Were Born in %s and Your Age Now is %s.'%(year,age))
        print("Don't worry you are still Young :)")

    #NEWS
    elif n=="news" or n=="whats the news today" or n=="todays news" or n=="whats the news":
        
        news=input('Select News Provider:\n 1-Aajtak \n 2-Abp \n 3-India Today \n 4-NDTV \n 5-HINDUSTAN TIMES \n 6-Times of India \n 0-Cancel\nYOU:').lower()
        if news=="aajtak" or news=="1":
            print("SELECTED AAJTAK\nLet's Go!")
            webbrowser.open('https://aajtak.intoday.in')
        elif news=="abp" or news=="2":
            print("SELECTED ABP\nLet's Go!")
            webbrowser.open('https://news.abplive.com')
        elif news=="india today" or news=="3":
            print("SELECTED India Today\nLet's Go!")
            webbrowser.open('https://www.indiatoday.in')
        elif news=="ndtv" or news=="4":
            print("SELECTED NDTV\nLet's Go!")
            webbrowser.open('https://www.ndtv.com')
        elif news=="hindustan times" or news=="5":
            print("SELECTED HINDUSTAN TIMES\nLet's Go!")
            webbrowser.open('https://www.hindustantimes.com')
        elif news=="times of india" or news=="6":
            print("SELECTED Times of India\nLet's Go!")
            webbrowser.open('https://timesofindia.indiatimes.com')
        else:
            print("News Search Cancelled.")
        
        
    #WHATS THE WEATHER
    elif n=='whats the weather in %s'% city or n=="show me the weather of %s" % city or n=="what's the weather in %s" % city or n=="what is the weather in %s" % city :
        print('Here You Go!')
        webbrowser.open('https://www.accuweather.com/en/search-locations?query=%s' % city)

    #CAN'T RESPOND BUT NOTE QUESTION
    else:
        file1 = open('ChatBotDB.txt',"a")
        with open('ChatBotDB.txt') as ChatBotDB:
            if 'MAIL THIS FILE TO: mayureshraval2012@gmail.com' in ChatBotDB.read():
                file1 = open('ChatBotDB.txt',"a")
                file1.write('\n')
                file1.write(n)
                file1.write(' - ')
                file1.write(a)
                file1.write('\n')
                file1.close()
                print('Question noted.\nCheck The ChatBotDB.txt file.')
                print("BOT: Sorry I can't respond to that,Try asking another question")
                prompt=input('Or Do you want to search again on Google? Y=Yes and N=No:').lower()
                if prompt=='y' or prompt=='yes':
                    query = input("Search on Google:")
                    webbrowser.open("https://google.com/search?q=%s" % query)
                else:
                    print("BOT: Ok :)")
            else:
                file1 = open('ChatBotDB.txt',"a")
                file1.write('MAIL THIS FILE TO: mayureshraval2012@gmail.com\n')
                file1.write('\n')
                file1.write(n)
                file1.write(' - ')
                file1.write(a)
                file1.write('\n')
                file1.close()
                print('Question noted.\nCheck The ChatBotDB.txt file.')
                print("BOT: Sorry I can't respond to that,Try asking another question")
                prompt=input('Or Do you want to search again on Google? Y=Yes and N=No:').lower()
                if prompt=='y' or prompt=='yes':
                    query = input("Search on Google:")
                    webbrowser.open("https://google.com/search?q=%s" % query)
                else:
                    print("BOT: Ok :)")

print("No Copyright \u00A9 2019 ,MAYURESH. All Rights Unreserved xD \nHANDCRAFTED WITH BASIC PROGRAMMING <3")            
print("BOT: HEY IM CHATBOT MAY I KNOW YOUR NAME?")
a=input('YOU:')
print("BOT: Hi",a.upper())

while True:
    print("BOT: ASK ME SOMETHING",a.upper(), "OR PRESS q TO EXIT!")
    n=input("YOU:").lower()
    if n != 'q':
        chatbot(n)
    else:
        print("BOT: BYE :)")
        break
