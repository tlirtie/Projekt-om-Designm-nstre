**Projekt om designmønstre**

**Formål og målgruppe:**
Vi har valgt at udvikle et program, som skal hjælpe elever fra 0-3. klasse i grundskolen med basal matematik, såsom addition, subtraktion, multiplikation og division. Vores program skal helst forblive relativt simpelt og brugervenligt, og eleverne skal gerne kunne bruge programmet til at træne deres matematikfærdigheder.

**Valg af designmønstre:**
Vi har valgt at bruge designmønstret ”Strategy” til at håndtere de fire forskellige matematiske opgaver i vores program, nemlig addition, subtraktion, multiplikation og division. Vi vil oprette en overordnet klasse kaldet ”MatematikOperation”, som har fire underordnede objekter kaldet ”Addition”, ”Subtraktion”, ”Multiplikation” og ”Division”. Disse vil hver især være ansvarlige for at sammenligne brugerens svar, som input, med det korrekte svar. Vi kan derfor også lave et klassediagram som visualiserer dette.
![image](https://github.com/tlirtie/Projekt-om-Designm-nstre/assets/142231651/c0f90649-b2af-4918-b911-bdf980c6d47b)


**Programmering af designmønstre:**

Koden til vores Strategy-designmønster kan ses her: 
![image](https://github.com/tlirtie/Projekt-om-Designm-nstre/assets/142231651/b1d9cd97-ceda-4a6d-b5db-bb10ec8565d7)

Her er ”MatematikOperation” den overordnede klasse, og de specifikke matematiske operationer som f.eks. ”Addition” eller ”Multiplikation” er underordnede objekter til klassen ”MatematikOperation”. På den måde har vi overholdt Strategy-Designmønstret. Derudover kan vi også se at visse af de matematiske operationer har nogle krav som skal overholdes når der genereres et nyt spørgsmål. Et billede af dette er vedhæftet her:

 ![image](https://github.com/tlirtie/Projekt-om-Designm-nstre/assets/142231651/9eb6da01-cbc5-4d03-a8fb-5a455a4d3047)
![image](https://github.com/tlirtie/Projekt-om-Designm-nstre/assets/142231651/f4b60f0b-ae59-4dc5-979c-b8377e97c519)

Her kan vi se at hvis spørgsmålet ender ud med at være i ”Addition”, så genereres der 2 forskellige tal, altså num1 og num2 inden for intervallet [1:50]. Derefter kommer spørgsmålet ”Hvad er num1 + num2?”

I ”Subtraktion” kan vi se at num1 er et tilfældigt tal inden for intervallet [1:50] og num2 er et tal fra 1 til num2. Dette er for at vi ikke kommer ned i negative tal, da vores program jo primært er tiltænkt elever fra 0-3 klasse, så opgaverne skal ikke være alt for svære.

Indenfor ”Multiplikation” kan vi se at der genereres et tal fra 1 til 10. Dette er igen for at sørge for at opgaverne ikke bliver alt for svære, da gange med to cifre godt kan ende ud med at være ret kompliceret, især for yngre elever.
Og til sidst i ”Division” kan vi se at der genereres to tal indenfor intervallet [2:20], men de skal dog overholde visse krav. Krav 1 er at num2 ikke må være num1. Dette er fordi at ellers ender vi ud med spørgsmål som f.eks. 17 divideret med 17, hvilket jo selvfølgelig er alt for nemt. Derudover må num2 ikke være 1 eller 0, da det vil lave rigtig nemme spørgsmål som f.eks. 18 divideret med 0 eller 27 divideret med 1. Når de to tal divideres, skal resultatet også være et helt tal, så vi ikke ender ud med at resultatet er i kommatal, hvilket vil være for svært for vores målgruppe, som jo er elever i de mindre klassetrin i folkeskolen.

**Udviklingsproces:**

Til at starte med i udviklingen af programmet, gik vi udelukkende op i at få overholdt vores designmønster, som vi valgte skulle være Strategy. Derfor var vores første opgave at få implementeret vores Strategy-designmønster som skulle være de forskellige matematiske operationer. Det gøres i den kode som er under den overordnede klasse der hedder MatematikOperation (Kan ses under ”Programmering af designmønstre-delen af denne opgave) Efter vi havde lavet denne del af koden, gik vi i gang med en basal brugergrænseflade. Vi havde på forhånd tænkt at vi ville have en form for slider eller dropdown menu som kunne bruges til at skifte imellem opgaver inden for de forskellige matematiske operationer, så derfor lavede vi det til at starte med. Derefter lavede vi nogle knapper som endnu ikke var funktionelle. Disse var en ”Indsend svar” knap og en ”Generér spørgsmål” knap. På dette tidspunkt havde vi fået lavet en basal brugergrænseflade, som kan ses for neden:

![image](https://github.com/tlirtie/Projekt-om-Designm-nstre/assets/142231651/86fb382a-9ddf-4d56-aadc-58aa84b515c5)

Den her brugergrænseflade indeholder de vigtigste elementer i vores program, dog er den ret lille, hvilket er noget vi ender ud med at ændre på efter vores andre knapper har fået funktionalitet. Vi gik straks i gang med at arbejde på de resterende knapper. Det gjorde vi ved at gøre brug af de klasser som vi har lavet tidligere ved brug af Strategy-designmønstret. Vi koblede dem på de forskellige knapper, og ved tryk på knappen ”Indsend svar” blev brugerens input sammenlignet med det rigtige svar som er en midlertidig værdi der opbevares i baggrunden af programmet. Nu opdagede vi dog at der var nogle problemer. Vores opgaver indenfor division var alt for svære, og resultaterne endte ofte i lange kommatal, så vi var nødt til at arbejde på nogle restriktioner for at opgaverne vil kunne løses af vores målgruppe. Et billede af den gennemsnitlige division-opgave på det tidspunkt kan ses forneden. (Svaret er 1.28571428571, hvilket selvfølgelig er for svært da vores opgaver helst gerne skulle kunne løses i hovedet eller simpelt på papir)

 ![image](https://github.com/tlirtie/Projekt-om-Designm-nstre/assets/142231651/c5d0e26b-7fdf-4989-8f87-20f743528a1b)

Derfor blev vi nødt til at tilføje nogle restriktioner til de tilfældigt genererede tal. Det kan ses i vores kode her, og de specifikke restriktioner blev beskrevet grundigere i ”Programmering af designmønstre” delen af denne opgave:
 ![image](https://github.com/tlirtie/Projekt-om-Designm-nstre/assets/142231651/d89a7126-e72e-4f39-8955-4bf2be5ff646)

Efter dette var vores program pænt meget færdigt, og vi valgte at gøre programmets vindue større, så det ikke ligner en lille lommeregner i siden af skærmen. Til sidst endte vores brugergrænseflade med at se sådan her ud:
 ![image](https://github.com/tlirtie/Projekt-om-Designm-nstre/assets/142231651/8a52c226-33a6-4b6b-88a3-c558c1df72fc)

Titlen på programmet, ”Matematikeren” kunne være navnet på programmet hvis det endte ud med at blive udgivet.

**Brugergrænseflade:**

Vores brugergrænseflade er meget simpel og brugervenlig, hvilket selvfølgelig er en positiv ting nu da vores målgruppe primært er yngre elever fra ca. 3. klasse og under. Derfor vil vores brugere ikke have nogen problemer med at navigere rundt i vores UI. 

**Test og tilpasning af programmet:**

Til denne del har vi valgt at lave et testskema for at være sikre på at vores program virker som det skal. Det kan ses her forneden:
![image](https://github.com/tlirtie/Projekt-om-Designm-nstre/assets/142231651/88437405-610f-4e51-a644-42c0f0ac2f48)

**Refleksion over valg af designmønster:**
Vi mener at vores valg af Strategy-designmønstret faktisk endte ud med at bidrage positivt til udviklingen af vores program, og gjorde det meget nemmere at navigere rundt i koden. Alle vores matematiske operatorer er under samme klasse og er på en måde forbundet, hvilket gjorde det meget nemt at tilføje nye matematiske operatorer når vi havde fået lavet den første, og tilføje nye restriktioner og intervaller til de forskellige opgavetyper.
