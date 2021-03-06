#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Me-page redovisning, texts from each course moment.
As cgi.

"""


# To write pagecontent to sys.stdout as bytes instead of string
import sys
import codecs


#Enable debugging of cgi-.scripts
import cgitb
cgitb.enable()


# Send the HTTP header
print("Content-Type: text/plain;charset=utf-8")
#print("Content-Type: text/html;charset=utf-8")
print("")


# Here comes the content of the webpage
content = """
Min Redovisnings-sida

==============================================================================
Kmom05:
------------------------------------------------------------------------------
- Hur kändes det med datastrukturerna dictionaries och tupler? Har du sett något liknande förut?

Datastrukturena kändes okej, och jag tyckte att dictionaries liknade listor i python. Dock har jag inte sett något som liknar tupler tidigare. Videon om dictionaries uppskattade jag mycket. Den var enkel men kändes inte lika redundant som de andra videorna sedan innan.

- Känns det som du fick ordning på listor, dictionaries och tupler? När man skall använda respektive och hur de kan användas?

Det känns som att jag fick ordning på skilnaderna mellan listor och dictionaries men tupler har jag lite svårt med. Dictionaries kan användas som bokstavligen en ordbok där det finns en key och dess value. Det finns ingen riktig ordning i dictionaries. Däremot är listor en lista med index.

- Använde du något av listor, dictionaries eller tupler när du gjorde uppgifterna, på vilket sätt?

Jag använde mig av dictionaries och listor lika mycket för att köra marvins textanalys. Jag ville hålla mig till dictionaries för att det var nytt för mig, men ibland behöver man använda sig av indexerade listor för att få ordning över datan. Angående tupler så är jag inte helt 100% säker på vilka användningsområden det handlar om.

- Hur gick det att utföra uppgifterna, vilken tog mest tid och vilken var mest lärorik?

Labben gick bra men det tog alldeles för mycket tid med marvin där jag hade problem med att kopiera en dictionary. Oavsett var jag gjorde det så blev dictionaryn inte som den skulle. Efter en stund så kom jag äntligen på vad som var fel, jag hade försökt kopiera en annan dictionary i en felaktig rad. Efter jag upptäckte detta så kunde jag lösa det och forsätta med arbetet. Det tog mer än en vecka.

- Gjorde du extrauppgiften?

Nej, eftersom jag redan ligger efter i tidsplaneringen behövde jag hoppa över den.

- Övrigt

Labben var som vanligt mycket kul och lärorik.


==============================================================================
Kmom04:
------------------------------------------------------------------------------
- Var det svårt att bekanta sig med datastrukturen för listor eller flöt det på bra?

Förutom den sista funktionen "inventory" flöde det bra på i detta moment.

Mitt problem var att det alltid fanns en tom element " " (white space) i listan när det skulle vara tom. Det löste sig med if-satsen som separerade strängerna för att skapa en lista när det fanns flera elementer, men inte gjorde något när filen var tom.
Text-fil var lite svår när man skulle öppna den i flera olika lager eftersom den är stängd i lägre lager.

Tyckte slice är jätteknepigt, gjorde massa försök och misslyckades. I alla fall känns listor mycket användbara.

- Hur kändes det att skriva grafiskt program i terminalen, kan du se något behov av den typen av program?
Det var väldigt svårt och inte alls roligt...(Ordet "Curses" påminde mig om det engelska ordet "curse" hela tiden)
Det tog mer än en hel vecka innan jag var klar. Jag förstår inte heller hur och i vilka situationer man kan dra nytta av det.

- Hur gick det att utföra uppgifterna, vilken tog mest tid och vilken var mest lärorik?
Som sagt var Curses var trist. Däremot var Labb-uppgifterna som alltid roliga. Dock blev Marvins 16:e funktionen alldeles för lång och tjatig med många indenter. Jag försökte skriva kortare kod, men det gick tyvärr inte i min nivå.

Tycker att det är väldigt intressant att det finns hur många sätt som helst att koda samma funktion.


==============================================================================
Kmom03:
------------------------------------------------------------------------------
- Har du programmerat med filhantering tidigare, känns det lätt eller svårt?

Nej, jag har aldrig gjort det tidigare, om man räknar bort "include"-functionen i php. Hade lite svårt med att välja en funktion mellan t ex "with open(file, "r") as f:" och "f = open(file, "r").read()". Det tog också lite tid innan jag lyckades med att ta fram endast det jag ville från filen, men ändå kändes det okej.

- Vad tycker du om video som läromedel, tycker du att de tillför något som läromedel?

Det är bra när man inte har kvar någon energi att googla och läsa. Däremot så känns det ganska långsamt och redundant när man inte har tid och känner sig stressad. Tycker inte att videorna innehåller särskillt mycket information med tanke på längden av dem. Vore kanske bättre med fler korta videor? Jag känner inte för att titta på något som är 10 min långt när jag inte är helt säker på om det innehåller exakt det jag vill veta. I alla fall så blir det en hel del googlande innan jag börjar titta på en video.

- Du har gjort din första modul i Python, känns strukturen bra?

Ja, hittills tycker jag att det går okej. Övningarna är lagom svåra men jag har lyckats klarat av dem. Tycker också att de är väldigt givande, lärorika och roliga.

- Vad tyckte du om de olika uppgifterna? Hur tänkte du när du utförde dem? Var de utmanande eller lätta?

Jag fann uppgifterna lagom utmanande. Jag blir fast i felhanteringarna då och då men det känns ändå mycket roligt.Beskrivningen av den tredje Marvin-uppgiften med dagens datum m.m. känndes dock lite oklar. Jag var inte säker på om hur en ny textfil skulle skapas, om strängerna t ex skulle vara i en lista eller i en lång mening. Jag tog den enklaste metoden att sätta varje sträng i lines med ingen annan data.


==============================================================================
Kmom02:
------------------------------------------------------------------------------
Detta moment var väldigt kul. Jag tyckte verkligen om att lösa många små problem. Det var mycket roligare än att jobba med miljön eller ladda upp och ner något hela tiden (dock vet jag att allt sånt är viktigt).

Syntaxen i Python kändes för petig först. Jag tyckte att det skulle vara för mycket jobb att se till att allt ska vara. Men det var faktiskt tvärtom, jag älskar syntaxen. Har läst lite PHP och JS med, men Python känns tydligast och enklast av alla tre. Tydliga syntaxen gör att man lätt kan förstå det andra  (eller t o m man själv) kodat. Det tycker jag är väldigt bra speciellt när man jobbar i ett stort team.

Valideringen gick okej. Jag fick flera felmeddelanden varje gång men de var så tydliga att jag i de flesta fall kunde fixa dem utan problem. Dock hade jag svårt med felmeddelandet om exception type eftersom jag inte kunde komma på en passande exception type som skulle innebära allt annat än "True". Men det gick ändå bra när jag fått ett tips om att använda "ValueError".

Det var mycket roligt att utföra uppgifterna, de var lagom svåra för mig. Tyckte att det var häftigt med hur man kan skapa, använda och kombinera funktioner.

Jag hade lite svårt med att förstå "while True" loopen, jag tänkte "While vad är true?". Men sedan lärde jag mig att det helt enkelt itererar så länge "expression" var true.

Det tog också lite längre tid för att sätta veriabler i rätta räckvidder.


==============================================================================
Kmom01:
------------------------------------------------------------------------------

Det var ett ganska jobbigt moment eftersom jag behövde väldigt mycket tid på många av delarna som bl.a. labbmiljön och validering etc, speciellt när jag behövde fixa "missing docstring"-felmeddelandet.

-Vilken utvecklingsmiljö använder du?
Windows 8.1 & cygwin eller Ubuntu 13.10 och Sublime Text2

-Är du bekant med Python sedan tidigare?
Lite grann. Gjorde väldigt enkla övningar för nybörjare 2014, men cgi är helt nytt för mig.

-Är du bekant med programmering och problemlösning sedan tidigare?
Nej, detta är helt nytt för mig.

-Är du bekant med terminalen och Unix-kommandon sedan tidigare?
Väldigt lite. En gång har har  jag använt terminalen och lekte med att flytta mig till kataloger i olika nivåer.

-Gick det bra att komma i gång med kursmomentet, var det lagom, för litet, för stort?
Det var vanligt att jag satt och jobbade vid datorn flera dagar för att lösa ett enda problem. Jag hoppas verkligen att jag kommer att bli bättre och smidigare. Tyckte ändå att mängden av uppgifterna var helt okej, men att förstå hur programmen fungerar med varandra och varför man använder dem var det svåraste för mig.

-Vilken del av kursmaterialet (böcker, artiklar, videor, etc) uppskattade du mest?
TheMokeyLords filmer tyckte jag var bra, för de hade tillräckligt mycket (men inte för mycket) information i korta avsnitt så att man kunde lätt hänga med.

Jag tillbringade flera dagar innan jag kunde komma igång med cgi. Jag förstod inte riktigt vad man skulle kunna göra med det först. I instruktionerna stod det att jag skulle skaffa två filer med samma innehåll, fast med olika filändelser som ".py" och ".cgi". Varför man skulle ha båda filerna kunde jag inte förstå. Efter många försök för att ta reda på kopplingen mellan filerna så bad jag äntligen läraren om hjälp. När jag fick det förklarat så förstår jag att det var ganska simpelt; py-filen var för att köra via terminalen och cgi-filen var anpassad för att köra via webben, helt enkelt.


"""


# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content)
